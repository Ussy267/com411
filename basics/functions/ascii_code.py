print("Program Started!")

print( "Please enter a standard character:")
character = input()

if  len ( character ) == 1:
    ASCII = ord( character )
    print (f"The ASCII code for {character} is {ASCII}.")