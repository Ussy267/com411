# prompt user's to pick a direction
print("pick a direction to move the paint brush")

# read user's response
direction = (input())

# check if user's response is a direction
if direction == "up":
    print("I am painting in the upward direction!")
elif  direction == "down":
    print("I am painting in the downward direction!")
elif direction == "left":
    print("i am painting in the left direction")
elif direction == "right":
    print("I am painting in the right direction")