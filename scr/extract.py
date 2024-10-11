import os
from typing import List
import pandas as pd


def carregar_e_filtrar_planilha(arquivo_excel: str, nome_sheet: str, cidade: str, anos: List[int]) -> pd.DataFrame:
    """
    Carrega uma planilha de um arquivo Excel e aplica o filtro com base na cidade e anos especificados.
    """
    
    df = pd.read_excel(arquivo_excel, sheet_name=nome_sheet, nrows=200) # amostra: add 'nrows=value' 
    
    if "CIDADE" in df.columns and "ANO_BO" in df.columns:
        df_filtrado = df[(df["CIDADE"] == cidade) & (df["ANO_BO"].isin(anos))]
        return df_filtrado
    else:
        print(f"A planilha '{nome_sheet}' no arquivo '{arquivo_excel}' não contém as colunas necessárias.")
        return pd.DataFrame()  

def processar_arquivo_excel(arquivo_excel: str, cidade: str, anos: List[int]) -> List[pd.DataFrame]:
    """
    Processa um arquivo Excel, filtrando todas as planilhas de acordo com os parâmetros fornecidos.
    """
    
    dados_filtrados = []

    sheet_names = pd.ExcelFile(arquivo_excel).sheet_names
    
    for nome_sheet in sheet_names:
        df_filtrado = carregar_e_filtrar_planilha(arquivo_excel, nome_sheet, cidade, anos)
        if not df_filtrado.empty:
            dados_filtrados.append(df_filtrado)
    
    return dados_filtrados

def combinar_e_salvar_dados(dados_filtrados: List[pd.DataFrame], caminho_arquivo: str) -> None:
    """
    Combina uma lista de DataFrames filtrados e salva o resultado em um único arquivo CSV.
    """
    
    if dados_filtrados:
        df_combinado = pd.concat(dados_filtrados, ignore_index=True)
        df_combinado.to_csv(caminho_arquivo, index=False)
        print(f"Arquivo combinado salvo em: {caminho_arquivo}")
    else:
        print("Nenhum dado foi encontrado com os critérios de filtragem.")

def processar_arquivos(arquivos_excel: List[pd.DataFrame], pasta_destino: str, cidade: str, anos: List[int]) -> None:
    """
    Processa uma lista de arquivos Excel, aplicando o filtro para cada planilha e combinando os resultados.
    """
    
    caminho_arquivo_combinado = os.path.join(pasta_destino, "SPDadosCriminais_SP_2021_2023_filtrado.csv")
    
    todos_dados_filtrados = []

    for arquivo_excel in arquivos_excel:
        dados_filtrados = processar_arquivo_excel(arquivo_excel, cidade, anos)
        todos_dados_filtrados.extend(dados_filtrados)
    
    combinar_e_salvar_dados(todos_dados_filtrados, caminho_arquivo_combinado)