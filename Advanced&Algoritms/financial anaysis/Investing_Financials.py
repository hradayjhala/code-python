import time

 #Calculates Net Cash
company_cash = (input("Enter company cash (cash and cash equivalents + marketable securities) : "))
company_cash = float(company_cash)
debt = (input("Enter long term debt : "))
debt = float(debt)
net_cash = company_cash - debt
shares_outstanding = (input("Enter shares outstanding : "))
shares_outstanding = float(shares_outstanding)
print("Net cash per share : ", net_cash / shares_outstanding)
time.sleep(5)

#Calculates debt-equity
equity = (input("Enter company equity : "))
equity = float(equity)
total = debt + equity
print("Percent of Equity: ", (equity / total)*100)
time.sleep(5)

#calculates book value per share 
book_value = (input("Book Value : "))
book_value = float(book_value)
book_value = book_value / shares_outstanding
print("Book Value per share : ", book_value)
time.sleep(5)

#calculates free cash flow per share
free_cash_flow = (input("Enter Free Cash Flow : "))
free_cash_flow = float(free_cash_flow)
free_cash_flow = free_cash_flow / shares_outstanding
print("Free Cash Flow per share : ", free_cash_flow)
time.sleep(5)

#checks inventories 
inv_year1 = (input("Enter inventories for current year : "))
inv_year1 = float(inv_year1)
inv_year2 = (input("Enter inventories for previous year : "))
inv_year2 = float(inv_year2)
inv_year3 = (input("Enter inventories for year before previous year : "))
inv_year3 = float(inv_year3)
time.sleep(2)
if inv_year1 < inv_year2 < inv_year3:
    print("Company Inventory Decreasing - Good ")
else:
    print("Inventory stable or increasing - Not so Good")
time.sleep(5)

#checks ROE
ROE = input("Enter increase in ROE for company (decimal) : ")
ROE = float(ROE)
industry = input("Enter increase in ROE for industry (decimal) : ")
industry = float(industry)
time.sleep(2)
if ROE > industry:
    print("Very Good, it is better than industry by : ", (ROE - industry) * 100, "%")
else:
    print("Could be bad")
time.sleep(5)

#Calculates Current Ratio
current_assets = (input("Enter current assets : "))
current_assets = float(current_assets)
current_liabilities = int(input("Enter current liabilities : "))
current_liabilities = float(current_liabilities)
current_ratio = current_assets / current_liabilities
time.sleep(2)
if current_ratio > 2:
    print("Company May be undervalued as current ratio is ", current_ratio)
else:
    print("Company may be undervalued or fairvalued or overvalued as current ratio is ", current_ratio)
time.sleep(5)

#calculates pe/growth (keep pe as decimal lol)
growth_rate = input("Enter company growth rate in decimal : ")
growth_rate = float(growth_rate)
pe = input("Enter P/E ratio : ")
pe = float(pe)
if growth_rate / pe >= 2:
    print("Great as growth rate by pe is : ", growth_rate / pe)
elif growth_rate / pe >= 1.5:
    print("Okay as growth rate by pe is : ", growth_rate / pe)
else:
    print("Not so good as growth rate by pe is : ", growth_rate / pe)
time.sleep(5)

#PB*PE calculation
price = input("Enter stock price : ")
price = float(price)
pb = price / book_value
if pb * pe <= 22.5:
    print("PB * PE is ", pb * pe, " - Great")
else:
    print("Okay, it is PB*PE is ", pb * pe, " Not the best")
time.sleep(5)

#calculates graham number 
eps = input("Enter eps : ")
eps = float(eps)
if (eps * book_value * 22.5) **0.5 > price:
    print("GOOD, the Graham Number is ", (eps * book_value * 22.5) **0.5)
else:
    print("This may not be a value stock according to Graham's number - ", (eps * book_value * 22.5) **0.5)
time.sleep(5)

#calaculates net net value
inv_year1 = inv_year1 * 0.5
company_cash = float(company_cash)
accounts = input("Enter accounts receivable : ")
accounts = float(accounts)
accounts = accounts * 0.75
total_liabilities = input("Enter current liabilities : ")
total_liabilities = float(total_liabilities)
net_net = company_cash + accounts + inv_year1 - total_liabilities
net_net = net_net / shares_outstanding
print("Net Net per share value is : ", net_net)
time.sleep(5)

# calculates intrinsic value
round_1 = input("Enter growth rate of cash flow for first 3 years : ")
round_1 = float(round_1)
round_1 = round_1 + 1
discount = input("Enter discount rate : ")
discount = float(discount)
discount = discount + 1
free_cash_flow = free_cash_flow * shares_outstanding
year1 = (free_cash_flow * round_1) / discount
year2 = (year1 * round_1) / discount
year3 = (year2 * round_1) / discount
first_3 = year3 + year1 + year2
round_2 = input("Enter growth rate for next 3 years : ")
round_2 = float(round_2)
round_2 = round_2 + 1
year4 = (year3 * round_2) / discount
year5 = (year4 * round_2) / discount
year6 = (year5 * round_2) / discount
next_3 = year4 + year5 + year6
round_3 = input("Enter growth rate for last 3 years : ")
round_3 = float(round_3)
round_3 = round_3 + 1
year7 = (year6 * round_3) / discount
year8 = (year7 * round_3) / discount
year9 = (year8 * round_3) / discount
last_3 = year7 + year8 + year9
sell_of_value = year9 * 12
cash = input("Enter cash and cash equivalents : ")
cash = float(cash)
DCF = sell_of_value + free_cash_flow + first_3 + next_3 + last_3 + cash
IV = DCF / shares_outstanding
if IV > price:
    print("The company's intrinsic value per share is ", IV)
else:
    print("The company's intrinsic value is below stock price, it is ", IV)
time.sleep(5)

#calculates risk reward ratio
shares = int(input("Enter num of shares you may buy for risk reward calculation : "))
reward = IV - price
reward = reward * shares
print()
min_price = input("Enter minimum price of company if it falls for 1 year(must be below share price) : ")
min_price = float(min_price)
min_loss = price - min_price
min_loss = min_loss * shares
ratio = reward / min_loss
print("The risk-reward ratio is ", ratio, ":1")
time.sleep(5)

#calculates the kelly formula
profit = input("Enter percentage profit possible in 3 years (in decimal) : ")
profit = float(profit)
odds1 = input("Enter the odds of this profit (in decimal) : ")
odds1 = float(odds1)
break_even_odds = input("Enter odds of breaking even in 3 years (in decimal) : ")
break_even_odds = float(break_even_odds)
odds_of_loss = input("Enter odds of 15% or less return in 3 years (in decimal) : ")
odds_of_loss = float(odds_of_loss)
odds_of_total_loss = input("Enter odds of total loss in investment (in decimal) : ")
odds_of_total_loss = float(odds_of_total_loss)
edge = (odds1 * (profit + 1)) + (break_even_odds * 0) + (odds_of_loss * -0.015 + odds_of_total_loss * -1)
odds = odds1 * (profit + 1)
kelly = edge / odds
kelly = kelly * 100
time.sleep(5)
print("The percentage rate of success according to the kelly formula is : ", kelly, "%")
time.sleep(3)
print()
print()
print("Financials calculation finished! Yay! ")
