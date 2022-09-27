import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta

class StockDataScraper:

    def get_stock_data(self, company):

        today = date.today()

        end_date = today.strftime("%Y-%m-%d")
        day_difference = date.today() - timedelta(days=360)
        start_date = day_difference.strftime("%Y-%m-%d")

        data = yf.download(company, start=start_date, end=end_date, progress=False)
        data.to_csv(company + '.csv')


if __name__ == "__main__":

    obj_stock_data_scraper = StockDataScraper()
    obj_stock_data_scraper.get_stock_data('GOOGL')
    obj_stock_data_scraper.get_stock_data('TCS')