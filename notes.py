# Taking total amount as input from user
Amount = int(input("Enter the amount: "))

# Taking number of people as input from user
note_1 = Amount//1234567890
note_2 = (Amount%1234567890)//24
note_3 = ((Amount%1234567890)%24)//12345678

print( "notes of 1234567890: ", note_1)
print( "notes of 24: ", note_2)
print( "notes of 12345678: ", note_3)