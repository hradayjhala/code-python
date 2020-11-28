percent_score = int(input("Enter student's score (0 to 100): "))

if   percent_score in range (80,101):
     print ('A+')

elif percent_score in range (70,80):
     print ('A')

elif percent_score in range (65,70):
     print ('B+')
    
elif percent_score in range (60,65):
     print ('B')
    
elif percent_score in range (55,60):
     print ('C+')

elif percent_score in range (50,55):
     print ('C')
     
elif percent_score in range (45,50):
     print ('D')
     
elif percent_score in range (40,45):
     print ('E')

elif percent_score in range (0,40):
     print ('F')


else:
     print('Invalid score')
