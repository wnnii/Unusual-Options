# Unusual-Options
Implements the Yahoo Finance API to gather and analyze live options chain data. Compares the current Volume to Open Interest to determine call/put options that demonstrate significant unusual activity.

## APIs 
Uses the Yahoo Finance API. This can be installed by running ```pip install yahoo_fin```<br/>
In order to update to the latest version please run the command  ```pip install yahoo_fin --Upgrade```

## How It Works
Through the options module of the Yahoo Finance API the script takes in the user input of a stock ticker and first views the expiration dates for that ticker's option chain. Looping through each date, the code stores data of both call and put options as lists and compares the Volume to Open Interest to determine if a contract is unusual or not. Generally, contracts that demonstrate Volume that is x 2.5 that of the Open Interest are marked as unusual and outputted.

## More to Come
1) Additional file(s) to implement this code as a discord bot (users can utilize the command $TICKER_NAME and the bot will return any respective unusual activity)
2) Auto repeat — set the bot to continuously scan for a specific ticker and be notified when changes occur
3) Auto search — allows the bot to automatically search tickers (may be limited at first to i.e just the SP500) and their corresponding data. 

### Example Image of Correct Usage of the Script: 
![image](https://user-images.githubusercontent.com/64718908/174224474-dc6c845a-1ac0-4212-8e14-fc667d75d1e9.png)
