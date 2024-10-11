from scr.extract import processar_arquivos  

def extract_data():
    """
    Realiza a extração dos dados a partir de arquivos Excel.
    """
    
    arquivos_excel = [
        "./data/raw/SPDadosCriminais_2022.xlsx",
        "./data/raw/SPDadosCriminais_2023.xlsx"
    ]
    pasta_destino = "./data/filtered"
    cidade = "S.PAULO"
    anos = [2021, 2022, 2023]

    processar_arquivos(arquivos_excel, pasta_destino, cidade, anos)

def transform_data():
    """
    Placeholder para a etapa de transformação dos dados.
    """
    
    print("Transformação dos dados ainda não implementada.")

def load_data():
    """
    Placeholder para a etapa de carga dos dados em um banco ou sistema de destino.
    """
    
    print("Carga dos dados ainda não implementada.")


def main():
    """
    Função principal que executa as etapas de extração, transformação e carga (ETL).
    """
    
    extract_data()
    transform_data()
    load_data()

if __name__ == "__main__":
    main()