from yahoo_fin import options
from yahoo_fin import stock_info as si
from yahoo_fin import news

user_input = input("Enter a ticker to get options data: ") 
user_input = user_input.upper()

stock_news = news.get_yf_rss(user_input)
current_price = si.get_live_price(user_input)

dates = options.get_expiration_dates(user_input)

for date in dates:
    options_chain = options.get_options_chain(user_input, date)

    call_options_OI = options_chain['calls']['Open Interest']
    call_options_volume = options_chain['calls']['Volume']

    put_options_OI = options_chain['puts']['Open Interest']
    put_options_volume = options_chain['puts']['Volume']  

    list_call_options_OI = list(call_options_OI)
    list_call_options_volume = list(call_options_volume)

    list_put_options_OI = list(put_options_OI)
    list_put_options_volume = list(put_options_volume)

    for a in range(len(list_call_options_volume)):
        if list_call_options_volume[a] == '-':
            list_call_options_volume[a] = 0
        if list_call_options_OI[a] == '-':
            list_call_options_OI[a] = 0

    for y in range(len(list_put_options_volume)):
        if list_put_options_volume[y] == '-':
            list_put_options_volume[y] = 0
        if list_put_options_OI[y] == '-':
            list_put_options_OI[y] = 0
    
    ind_arr = []
    for i in range(len(list_call_options_OI)):
        if (int(list_call_options_volume[i]) > int(list_call_options_OI[i]) * 2.5) and \
        int(list_call_options_OI[i]) != 0 and int(list_call_options_volume[i]) > 1000: 
            ind_arr.append(i) 

    ind_arr2 = []
    for w in range(len(list_put_options_OI)):
        if (int(list_put_options_volume[w]) > int(list_put_options_OI[w]) * 2.5) and \
        int(list_put_options_OI[w]) != 0 and int(list_put_options_volume[w]) > 1000: 
            ind_arr2.append(w) 

    if not ind_arr:
        break
    else: 
        for j in ind_arr:
            print(user_input.upper() + str(options_chain['calls']['Strike'][j]) + "C" 
            + " expires on " + date + " it currently has a bid/ask spread of " + str(options_chain['calls']['Bid'][j])
            + " : " + str(options_chain['calls']['Ask'][j]) + "." + " The current change is: " + str(options_chain['calls']['Change'][j])
            + " (" + str(options_chain['calls']['% Change'][j]) + ")." +  " OI: " + str(options_chain['calls']['Open Interest'][j])
            + ", Vol: " + str(options_chain['calls']['Volume'][j]) + ", IV: " + str(options_chain['calls']['Implied Volatility'][j]) + ".")

    if not ind_arr2:
        break
    else:
        for t in ind_arr2:
            print(user_input.upper() + str(options_chain['puts']['Strike'][t]) + "P" 
            + " expires on " + date + " it currently has a bid/ask spread of " + str(options_chain['puts']['Bid'][t])
            + " : " + str(options_chain['puts']['Ask'][t]) + "." + " The current change is: " + str(options_chain['puts']['Change'][t])
            + " (" + str(options_chain['puts']['% Change'][t]) + ")." +  " OI: " + str(options_chain['puts']['Open Interest'][t])
            + ", Vol: " + str(options_chain['puts']['Volume'][t]) + ", IV: " + str(options_chain['puts']['Implied Volatility'][t]) + ".")

print("")
print("The current stock price for " + user_input.upper()  + " is " + str(round(current_price, 2)))
print("")