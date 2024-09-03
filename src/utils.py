from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from subprocess import CREATE_NO_WINDOW 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pandas as pd


def init_driver(chromedriver_path):
    """
    Inicializa o driver do Selenium.
    :param chromedriver_path: Caminho para o executável do chromedriver.
    :return: Instância do driver do Selenium.
    """
    chrome_service = Service(chromedriver_path)
    chrome_service.creation_flags = CREATE_NO_WINDOW
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver


def open_website(driver, url):
    """
    Abre a URL especificada no navegador.
    :param driver: Instância do driver do Selenium.
    :param url: URL do site a ser aberto.
    """
    driver.get(url)


def find_xpath(driver, xpath):
    """
    Depois de uma espera implícita, busca o elemento baseado no XPATH
    :param driver: A instância do webdriver em execução.
    :return: O elemento encontrado
    """
    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element = driver.find_element(By.XPATH, xpath)
    return element
    

def query_exec(driver, query):
    """
    Executa a pesquisa baseada na query passada e extrai os dados para excel

    :param driver: A instância do webdriver em execução.
    :param query: A query a usada para buscar os preços.
    """
    wait = WebDriverWait(driver, 5)
    search_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="twotabsearchtextbox"]')))
    search_input.send_keys(query, Keys.ENTER)
    find_xpath(driver, '//*[@id="p_n_deal_type/23565493011"]/span/a/span').click()
    extract_data(driver, query)


def extract_data(driver: webdriver.Chrome, query: str) -> dict:
    """
    Extrai todos os títulos e preços dos elementos filhos do div pai que possuem os atributos 
    data-cy="title-recipe" e data-cy="price-recipe", exporta para excel
    e retorna um dicionário com os dados encontrados.

    :param driver: A instância do webdriver em execução.
    :param query: A query a usada para buscar os preços.
    :return: Um dicionário com títulos e preços encontrados.
    """
    results = {}

    current_title = None

    cards = driver.find_elements(By.CLASS_NAME, 'puis-card-container')

    for card in cards:
        divs = card.find_elements(By.CSS_SELECTOR, 'div')
        for div in divs:
            data_cy = div.get_attribute('data-cy')
            if data_cy == 'title-recipe':
                name_span = div.find_element(By.CSS_SELECTOR, 'span.a-size-base-plus')
                current_title = name_span.text

            elif data_cy == 'price-recipe':
                price_span = div.find_element(By.CSS_SELECTOR, 'span.a-price')
                price_symbol = price_span.find_element(By.CSS_SELECTOR, 'span.a-price-symbol').text
                prince_int = price_span.find_element(By.CSS_SELECTOR, 'span.a-price-whole').text
                price_decimal = price_span.find_element(By.CSS_SELECTOR, 'span.a-price-decimal').text
                price_fraction = price_span.find_element(By.CSS_SELECTOR, 'span.a-price-fraction').text
                product_price = f"{price_symbol} {prince_int}.{price_decimal}{price_fraction}"
                results[current_title] = product_price
                current_title = None
            
    query = query.lower()
    query = query.replace(' ', '_')

    df = pd.DataFrame(list(results.items()), columns=['Nome', 'Preço'])
    df.to_excel(f'.//data//raw//{query}.xlsx', index=False)

    return results