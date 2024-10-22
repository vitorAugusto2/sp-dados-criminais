# ETL para Dados Criminais de São Paulo (2021-2023)

## Introdução
Este relatório documenta a implementação de um pipeline ETL (Extração, Transformação e Carga) aplicado aos dados criminais da cidade de São Paulo, cobrindo os anos de 2021 a 2023. O projeto foi desenvolvido para organizar e processar os dados criminais, visando sua inserção em um banco de dados relacional (PostgreSQL), permitindo consultas e análises futuras.

## Objetivo
O objetivo deste projeto foi criar um processo automatizado que:

* **Extrair** os dados criminais brutos, provenientes de arquivos Excel.
* **Transformar** os dados, padronizando-os e tratando-os para remover inconsistências.
* **Carregar** os dados transformados em um banco de dados PostgreSQL.

## Descrição do Projeto
O pipeline ETL foi implementado em três etapas distintas: extração, transformação e carga. Abaixo estão descritas as especificações de cada etapa.

### **Extração**
A etapa de extração consistiu em carregar os dados brutos a partir de arquivos Excel contendo informações de criminalidade. Estes arquivos foram obtidos através de scraping de sites públicos da Secretaria de Segurança Pública de São Paulo.

### **Transformação**
Na etapa de transformação, foi realizado o tratamento dos dados extraídos. As operações de transformação incluíram: 

* Conversão de tipos de dados: Correção de formatação e tipagem incorreta de colunas, como datas e valores numéricos.
* Preenchimento de valores nulos: Aplicação de regras de negócios para preenchimento de valores ausentes.
* Remoção de duplicatas: Eliminação de registros duplicados para garantir a integridade dos dados.
* Filtragem de dados relevantes: Seleção de colunas e registros que seriam carregados no banco de dados.
* Normalização: Ajustes na padronização de nomes de colunas e categorias, garantindo consistência.

### **Carregar**
Por fim, na etapa de carga, os dados transformados foram carregados em um banco de dados PostgreSQL. Para isso, foram criadas tabelas normalizadas que armazenam as informações de forma organizada, possibilitando consultas rápidas e precisas.
  
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
├── src/
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

## Resultados
Após a implementação do pipeline ETL, foi possível gerar uma base de dados consistente e padronizada com os dados criminais de São Paulo de 2021 a 2023. Este repositório de dados agora pode ser utilizado para análises exploratórias, criação de relatórios e dashboards interativos, além de servir como fonte para estudos mais avançados.

-> colocar gif de execucao <-

## Trabalhos Futuros
Algumas melhorias futuras que podem ser implementadas incluem:

* Adição de scripts de monitoramento automático para verificar a disponibilidade de novos dados no site de origem.
* Implementação de visualizações gráficas com bibliotecas como Matplotlib e Seaborn para facilitar a análise exploratória dos dados.
* Criação de dashboards interativos com Power BI ou Tableau conectados diretamente ao banco de dados PostgreSQL.
* Aplicação de modelos de previsão: Utilização de técnicas de Machine Learning para prever tendências criminais futuras, identificando padrões temporais e espaciais que podem auxiliar nas políticas públicas de segurança.
