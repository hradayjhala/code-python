indian = ["samosa", "dal", "naan", "sabji", "pav bhaji"]
italian = ["pizza", "pasta", "brooch", "macaroni"]
american = ["burger", "coke", "wrap", "frankie"]
middle_eastern  = ["meze", "hummus", "falafal", "feta"]
dish = input("Enter a dish : ")
if dish in indian :
    print("Indian")
elif dish in italian :
    print("Italian")
elif dish in american :
    print("American")
elif dish in middle_eastern :
    print("Middle Eastern")
else :
    print("I don't know which dish it is based on my little knowledge")
