# Amazon Price Scraper

This project is a web scraper that uses Selenium to search for products on Amazon, extract prices, and save the results to an Excel file.

## Project Structure

- `scraper.py`: Main script to run the scraper.
- `utils.py`: Contains helper functions such as driver initialization, URL opening, search, and data extraction.
- `config.py`: Configuration file that stores the Amazon URL, ChromeDriver path, and logging settings.
- `requirements.txt`: List of dependencies required to run the project.

## Features

- **Product Search**: The scraper allows you to search for products on Amazon using a user-provided query.
- **Promotion Filtering**: After the search, the scraper applies a filter to display only products on sale.
- **Data Extraction**: Extracts product titles and prices from the search results page.
- **Excel Export**: The extracted data is saved in an Excel file located in the `data/raw/` folder.
- **Log Recording**: Logs the scraper’s execution in `logs/scraper.log`.

## Requirements

- Python 3.x  
- Google Chrome  
- ChromeDriver

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/jccarlosjr/webscrapping.git
   cd webscrapping
