noOfPeople =  0
noOfPeople = int ( input ( " Enter noOfPeople " ) )
handshake  =  0
if noOfPeople <= 1 :
    print ( "0" )
else:
    while ( noOfPeople > 0 ) :
        handshake += noOfPeople-1
        noOfPeople -= 1
    print(handshake)
