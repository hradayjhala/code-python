human_year = int(input("How many human years?"))

if human_year in  range(0,3):
     dog_year = human_year * 10.5
     print(dog_year)

elif human_year >= 2:
     human_year = human_year - 2
     dog_year = human_year * 4
     dog_year = dog_year + 21
     print(dog_year)

else:
     print("Error")
 
