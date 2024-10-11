# ETL_SPDadosCriminais

### Argumentos

#### extract.py

**Args**:
* arquivos_excel (list): Lista de caminhos para arquivos Excel a serem processados.
* pasta_destino (str): Caminho da pasta onde o arquivo filtrado combinado será salvo.
* cidade (str): Nome da cidade para aplicar o filtro na coluna "CIDADE" (padrão: "S.PAULO").
* anos (list): Lista de anos para filtrar a coluna "ANO_BO" (padrão: [2021, 2022, 2023]).
* dados_filtrados (list): Lista de DataFrames resultantes da aplicação dos filtros em cada planilha.
* caminho_arquivo (str): Caminho completo onde o arquivo CSV combinado será salvo.
* arquivo_excel (str): Caminho para o arquivo Excel que contém as planilhas a serem processadas.
* nome_sheet (str): Nome da planilha específica dentro do arquivo Excel a ser processada.

#### transform.py
**Args**:

#### load.py
**Args**:
