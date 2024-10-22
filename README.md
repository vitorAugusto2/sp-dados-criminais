# ETL para Dados Criminais de São Paulo (2021-2023)

## Introdução
Este projeto implementa um pipeline de ETL (Extração, Transformação e Carga) para processar dados criminais da cidade de São Paulo, abrangendo os anos de 2021 a 2023. O objetivo é facilitar a análise desses dados, organizando-os em um formato limpo e padronizado e inserindo-os em um banco de dados relacional para futuras consultas e análises.

O pipeline é dividido em três etapas principais:
1. **Extração**: Carrega os arquivos Excel por WebScraping
2. **Transformação**: Realiza a filtragem, limpeza e normalização dos dados.
3. **Carga**: Carrega os dados transformados em um banco de dados PostgreSQL.

## Estrutura do Projeto
```python
sp-dados-criminais/
│
├── config/
│   └── db_config.py          # Arquivo de configuração do banco de dados
│
├── data/
│   ├── raw/                  # Arquivos brutos (Excel)
│   └── transformed/          # Arquivos transformados e prontos para carga
│
├── scr/
│   ├── extract.py            # Script de extração
│   ├── load.py               # Script de carga no banco de dados
│   └── transform.py          # Script de transformação
│
├── main.py                   # Script principal do pipeline
├── requirements.txt          # Arquivo de dependências
└── README.md                 # Documentação do projeto
```

## Execução do Projeto ETL

### 1. Instalar as dependências
Instale as dependências listadas no arquivo `requirements.txt`:

```python
# Instalar as dependências
pip install -r requirements.txt
```

### 2. Configuração do Banco de Dados
Atualize o arquivo de configuração `db_config` com suas credenciais do banco de dados PostgreSQL.

```python
conn = psycopg2.connect(
    dbname="*****",           # Nome do banco de dados
    user="*****",             # Usuário do banco de dados
    password="*****",         # Senha do banco de dados
    host="*****",             # Endereço do servidor 
    port="*****"              # Porta do PostgreSQL 
)
```

### 3. Executar o código com Logs e Resultados
Execute o pipeline ETL com o comando abaixo para iniciar o processo de extração, transformação e carga dos dados:

```python
python main.py
``` 

Os logs de execução serão exibidos no terminal, indicando o progresso de cada etapa (extração, transformação e carga).