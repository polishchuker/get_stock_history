# get_stock_history
This simple program asks you to enter the amount of stocks you wish to examine and their ticker symbol. It will then return a list of data frames containing the following information: **date, open price, high, low, close, volume, dividends, stock splits**



## More Detail

  First the method prompts you to enter the amount of stocks you wish to see.
  Next it will prompt you for the start and end date for which you are to recieve the data for. The data must be entered in the following format: year-month-day (example: 2009-04-20) 
  Then it asks for their ticker symbol.(It automaticly converts the letters to uppercase, if the ticker symbol is not valid it will raise an exception)
  Finaly it will return a list of dataframes containing the following information: date, open price, high, low, close, volume, dividends, stock splits. The funttion also returns the number of stocks you entered when first prompted. 
  
