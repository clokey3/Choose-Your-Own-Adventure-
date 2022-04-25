name = input ("Type Your name: ")
print ("Welcome", name, "to this adventure" )
error = 'Please use a proper answer'

While true:
q1 =input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?" ).lower()

if q1.lower() == "left":
    q11 = input("You come to a river, you can walk around it or swim across it. Type walk to walk around  and swim to swim across:")

    if q11.lower() == "swim":
        q12 = ("You see an alligator swimming directly at you. Do you fight or keep swimminng?")
            if q12.lower() == 'fight':
                print('You manage to fend off the alligator, but not without taking some damage."
    elif q2.lower() == "walk":
        print("You walk for many miles, ran out of water and you lost the game")
    else:
        print(error)
elif q1.lower() == "right":
    answer = input()
else:
    print(error)
