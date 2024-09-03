from config import AMAZON_URL, CHROMEDRIVER_PATH
from utils import init_driver, open_website, query_exec

def main():
    driver = init_driver(CHROMEDRIVER_PATH)
    open_website(driver, AMAZON_URL)

    query = input('Digite a query\n')
    query_exec(driver, query)

    driver.quit()

if __name__ == "__main__":
    main()

