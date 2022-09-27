import pandas as pd
import plotly.graph_objects as go
from csv import writer

class CandlestickCreator:

    def get_candlestick(self, company):

        data = pd.read_csv(company + ".csv")

        figure = go.Figure(data=[go.Candlestick(x=data["Date"], 
            open=data["Open"], high=data["High"], low=data["Low"], close=data["Close"])])

        figure.update_layout(title = company + " Stock Price Analysis", xaxis_rangeslider_visible=False)
        # figure.show()

        figure.write_image(company + '.jpg')


if __name__ == "__main__":

    obj_candlestick_creator = CandlestickCreator()
    obj_candlestick_creator.get_candlestick('GOOGL')
    obj_candlestick_creator.get_candlestick('TCS')