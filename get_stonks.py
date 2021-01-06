import yfinance as yf



def get_portfolio():
    num_of_stocks = int(input('How many stocks do you have? '))
    print('In the following format  in the following format "year-month-day" e.g: 2009-01-13  ')
    start_date = input('Enter start date of data: ')
    print()
    print('In the following format  in the following format "year-month-day" e.g: 2020-04-20  ')
    end_date= input('Enter the end date of data: ')
    print()
    portfolio = []
    for stock in range(num_of_stocks):
        stock = input('Enter Ticker Symbol of stock: ').upper()
        stock_data = yf.Ticker(stock)
        stock_history = stock_data.history(start=start_date, end=end_date)

        #checks to see if ticker is valid, if not raise exception
        if stock_history.empty:
            print('This ticker does not exist,please enter a valid ticker')
            raise Exception
        else:
            portfolio.append(stock_history)

    return portfolio,num_of_stocks

#test
#print(get_portfolio())
