import os
from scr.extract import download_data  
from scr.transform import transform_data
from scr.load import load_db

def extract():
    urls = [
        "https://www.ssp.sp.gov.br/assets/estatistica/transparencia/spDados/SPDadosCriminais_2022.xlsx",
        "https://www.ssp.sp.gov.br/assets/estatistica/transparencia/spDados/SPDadosCriminais_2023.xlsx"
    ]

    path_output = "./data/raw/"

    print("Starting data extraction...")
    for url in urls:
        file_name = os.path.basename(url)
        output_file = os.path.join(path_output, file_name)
        download_data(url, output_file)
    print("Extraction completed successfully")


def transform():
    path_data_raw = "./data/raw"
    city = "S.PAULO"
    years = [2021, 2022, 2023]  

    print("Starting data transformation...")
    transform_data(path_data_raw, city, years)
    print("Data transformation completed successfully")


def load():
    path_data_transformed = "./data/transformed/SPDadosCriminais_2021_2022_2023_clean.csv"
    
    print("Starting data loading...")
    load_db(path_data_transformed)
    print("Data loading completed successfully")


def main():
    print("ETL pipeline started...")
    extract()
    transform()
    load()
    print("ETL pipeline completed successfully")


if __name__ == "__main__":
    main()