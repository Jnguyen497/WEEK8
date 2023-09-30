def main():
  # Display the Intro Screen
  intro()
  
  # Get the Ticker Symbol
  try:
    ticker = input('Please enter ticker symbol: ')
    stocks = { 'AAPL': 189.70, 'AMZN': 137.27, 'ATVI': 92.03, 'GOOGL': 135.77, 'HSY': 212.10, 'META': 300.15, 'NFLX': 523.45, 'RBLX': 29.13, 'TSLA': 256.49, 'ZM': 73.28 }
    
    print(f"The current price of {ticker} is ${stocks[ticker]:.2f}") 
  #update  
  # No Search Found
  except:
    print()
    print("Not found, try again!")
    print()
    print()
    main()

  # The Intro Function Re-displays
def intro():
  print('Welcome to the Stock Dictionary!')
  print()
  print('Please use all caps for ticker symbol')

main()
