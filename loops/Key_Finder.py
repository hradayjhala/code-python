key_location = "chair" # Location could be changed
locations = ["garage", "living room", "closet", "chair"] # You can add locations 
Start = input("Input Password to start program : ")
if Start == "Start": # Start is the password to access the location
    for i in locations:
        if i == key_location:
            print("Key is found in : ", i)
            break
        else:
            print("")
else:
    print("Access Denied")
