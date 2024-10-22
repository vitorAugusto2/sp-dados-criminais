from config import db_config

def create_table(cursor):
    create_table = """
    CREATE TABLE SPDadosCriminais_2021_2022_2023_clean (
        NOME_DEPARTAMENTO            VARCHAR(255),
        NOME_SECCIONAL               VARCHAR(255),
        NOME_DELEGACIA               VARCHAR(255),
        CIDADE                       VARCHAR(255),
        NUM_BO                       VARCHAR(255),
        ANO_BO                       INT,
        DATA_COMUNICACAO_BO          DATE,
        DATA_OCORRENCIA_BO           DATE,
        HORA_OCORRENCIA_BO           TIME,
        DESCR_TIPOLOCAL              VARCHAR(255),
        BAIRRO                       VARCHAR(255),
        LOGRADOURO                   VARCHAR(255),
        NUMERO_LOGRADOURO            VARCHAR(50),
        LATITUDE                     FLOAT,
        LONGITUDE                    FLOAT,
        RUBRICA                      VARCHAR(255),
        DESCR_CONDUTA                VARCHAR(255),
        DATA_COMUNICACAO             DATE
    );
    """
    
    cursor.execute(create_table)


def load_db(path_data_transformed: str) -> None:
    conn = db_config.get_db_config()
    cursor = conn.cursor()
    
    create_table(cursor)

    copy_sql = """ 
    COPY SPDadosCriminais_2021_2022_2023_clean FROM STDIN 
    WITH CSV HEADER 
    DELIMITER AS ',' 
    """
        
    with open(path_data_transformed, "r", encoding="utf-8") as f:
        cursor.copy_expert(sql=copy_sql, file=f)
        
    conn.commit()
    cursor.close()
    conn.close()
