less = int(input("How many containers of your containers are 1 litre or less?"))

more = int(input("How many containers of your containers are more than 1 litre?"))

depositForless = 0.10

Totalmoneyforless = depositForless * less

depositFormore = 0.25

Totalmoneyformore = depositFormore * more

Totalmoney = Totalmoneyformore + Totalmoneyforless

print(Totalmoney)

