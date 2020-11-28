dog_year = int(input("How many dog years?"))

if   dog_year in  range(0,2):
     human_year = dog_year * 10.5
     print(human_year)

elif dog_year == 2:
     dog_year = dog_year * 105
     human_year = int(dog_year /10 )
     print(human_year)

elif dog_year > 2:
     dog_year = dog_year - 2
     human_year = dog_year * 4
     human_year = human_year + 21
     print(human_year)

else:
     print("Error")
