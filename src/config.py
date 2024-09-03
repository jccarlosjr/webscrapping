import logging

logging.basicConfig(
    filename='logs/scraper.log',
    level=logging.INFO,         
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

AMAZON_URL = "https://www.amazon.com.br/"

CHROMEDRIVER_PATH = ".//drivers//chromedriver.exe"