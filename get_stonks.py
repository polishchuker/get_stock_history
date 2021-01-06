import yfinance as yf



def get_portfolio():
    num_of_stocks = int(input('How many stocks do you have? '))

    portfolio = []
    for stock in range(num_of_stocks):
        stock = input('Enter Ticker Symbol of stock: ').upper()
        stock_data = yf.Ticker(stock)
        stock_history = stock_data.history(start="2009-01-01", end="2020-01-01")

        #checks to see if ticker is valid, if not raise exception
        if stock_history.empty:
            print('This ticker does not exist,please enter a valid ticker')
            raise Exception
        else:
            portfolio.append(stock_history)

    return portfolio,num_of_stocks

#test
#print(get_portfolio())
