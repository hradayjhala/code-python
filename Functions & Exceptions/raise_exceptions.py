def process_file():
    try:
        f = open("C:\\Users\hrada\Documents\Hraday blogs & stuff\\funny.txt") #open any file you want with any address
        x=1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print()
        print("Cleaning up file")
        f.close()

process_file()
