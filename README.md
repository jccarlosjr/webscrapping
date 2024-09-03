# Amazon Price Scraper

Este projeto é um web scraper que utiliza o Selenium para buscar produtos na Amazon, extrair os preços e salvar os resultados em um arquivo Excel.

## Estrutura do Projeto

- `scraper.py`: Script principal para execução do scraper.
- `utils.py`: Contém funções auxiliares, como inicialização do driver, abertura de URL, pesquisa e extração de dados.
- `config.py`: Arquivo de configuração onde estão armazenados a URL da Amazon, o caminho do ChromeDriver e as configurações de logging.
- `requirements.txt`: Lista das dependências necessárias para executar o projeto.

## Funcionalidades

- **Pesquisa de Produtos**: O scraper permite buscar produtos na Amazon utilizando uma query fornecida pelo usuário.
- **Filtragem de Promoções**: Após a pesquisa, o scraper aplica um filtro para exibir apenas produtos em promoção.
- **Extração de Dados**: Extrai os títulos e preços dos produtos exibidos na página de resultados.
- **Exportação para Excel**: Os dados extraídos são salvos em um arquivo Excel localizado na pasta `data/raw/`.
- **Registro de Logs**: Registra logs da execução do scraper em `logs/scraper.log`.

## Requisitos

- Python 3.x
- Google Chrome
- ChromeDriver

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/jccarlosjr/webscrapping.git
   cd webscrapping
