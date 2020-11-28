x = input("Enter Number 1 : ")
y = input("Enter Number 2 : ")
try:
    z = int(x) / int(y)
except ZeroDivisionError as e:
    print("Divison by Zero Exception")
    z = None
except Exception as e:
    print("Exception type: ", type(e).__name__)
    z = None
print("Division is: ", z)
