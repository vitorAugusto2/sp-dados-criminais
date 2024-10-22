import os
import pandas as pd
from typing import List


def read_and_filter_excel(file_path: str, city: str, years: List[int]) -> pd.DataFrame:
    xls = pd.ExcelFile(file_path)
    filtered_data = []
    
    for sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet, nrows=1000)
        df_filtered = df[(df["CIDADE"] == city) & (df["ANO_BO"].isin(years))]
        filtered_data.append(df_filtered)
    
    return pd.concat(filtered_data, ignore_index=True)


def transform_data(path_data_raw: str, city: str, years: List[int]) -> None:
    all_data = []

    for file in os.listdir(path_data_raw):
        if file.endswith(".xlsx"):
            file_path = os.path.join(path_data_raw, file)
            df_filtered = read_and_filter_excel(file_path, city, years)
            all_data.append(df_filtered)
    
    df_concat = pd.concat(all_data, ignore_index=True)

    df_concat.drop_duplicates(inplace=True)

    df_concat["DATA_COMUNICACAO_BO"] = df_concat["DATA_COMUNICACAO_BO"].fillna(df_concat["DATA_OCORRENCIA_BO"])
    df_concat["DATA_OCORRENCIA_BO"] = df_concat["DATA_OCORRENCIA_BO"].fillna("DESCONHECIDO")
    df_concat["HORA_OCORRENCIA_BO"] = df_concat["HORA_OCORRENCIA_BO"].fillna("00:00:00")
    df_concat["DESCR_TIPOLOCAL"] = df_concat["DESCR_TIPOLOCAL"].fillna("OUTROS")
    df_concat["BAIRRO"] = df_concat["BAIRRO"].fillna("DESCONHECIDO")
    df_concat["LOGRADOURO"] = df_concat["LOGRADOURO"].fillna("DESCONHECIDO")
    df_concat["NUMERO_LOGRADOURO"] = df_concat["NUMERO_LOGRADOURO"].fillna("DESCONHECIDO")
    df_concat["DESCR_CONDUTA"] = df_concat["DESCR_CONDUTA"].fillna("OUTROS")

    df_concat["LATITUDE"] = pd.to_numeric(df_concat["LATITUDE"], errors="coerce")
    df_concat["LONGITUDE"] = pd.to_numeric(df_concat["LONGITUDE"], errors="coerce")
    df_concat.dropna(subset=["LATITUDE", "LONGITUDE"], inplace=True)
    df_concat = df_concat[(df_concat["LATITUDE"].between(-90, 90)) & (df_concat["LONGITUDE"].between(-180, 180))]
    df_concat = df_concat[(df_concat["LATITUDE"] != 0) & (df_concat["LONGITUDE"] != 0)]
    
    df_concat.drop(columns=[
        "DESCR_PERIODO", 
        "DESC_PERIODO",
        "NOME_DELEGACIA_CIRCUNSCRIÇÃO", 
        "NOME_DEPARTAMENTO_CIRCUNSCRIÇÃO", 
        "NOME_SECCIONAL_CIRCUNSCRIÇÃO", 
        "NOME_MUNICIPIO_CIRCUNSCRIÇÃO", 
        "NATUREZA_APURADA", 
        "MES_ESTATISTICA", 
        "ANO_ESTATISTICA"
    ], inplace=True)

    df_concat = df_concat.apply(lambda col: col.str.upper() 
                                if col.dtype == "object" and col.apply(lambda x: isinstance(x, str)).all() 
                                else col)

    df_concat.sort_values(by="ANO_BO", ascending=False, inplace=True)
    
    path_output = "./data/transformed/"
    output_file = os.path.join(path_output, "SPDadosCriminais_2021_2022_2023_clean.csv")
    df_concat.to_csv(output_file, index=False)

    print(f"File saved in {path_output}")