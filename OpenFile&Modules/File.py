f = open("C:\\Users\hrada\Documents\Hraday blogs & stuff\\funny.txt", "r") # Change Address and file name 
for line in f :
    tokens = line.split(' ')
    print(len(tokens))
