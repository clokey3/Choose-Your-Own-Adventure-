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
                Break
            elif q12.lower() == 'swim':
                print('You try to swim faster but the alligator is too fast for you in the water. he takes a big bite out of your leg before you reach the other side.')
                break
            else:
                print(error)
    elif q11.lower() == "walk":
        q13 = input("A badger growls at you and looks prone to fight. Do you fight or runaway?")
            if q13.lower() == 'fight':
                print('You take some nasty hits from a ferocious beast, but eventually it retreats back to its lair')
                break
            elif q13.lower() == 'run':
                print('Good choice! fighting an animal like that would be suicide!')
                break
            else:
                print(error)
    else:
        print(error)
elif q1.lower() == "right":
    q14 = input('You come across a large mountain. Do you go over or around?)
        if q14.lower() == 'over':
            q15 = input('As you climb, you encounter apon a bunch of goats that inhabit this mountain. Do you want to pet the goat?')
                if q15.lower() == 'yes':
                    print('You have made a new friend! You are very careful when aproaching and the goat decides not to buck you off the mountain. It has such soft fur!')
                    break
                elif q15.lower() == 'no':
                    print('taking a long climb over the mountain to get away from the goats has made the expedition harder. You notice you are quite exhausted because of it. But you must move on.')
                    break
                else:
                    print(error)
                    break
       elif q14.lower() == 'around':
           q16 = input('Oh my god! It's a grizzly bear! Do you try to intimidate it or do you want to fight?')
                if q16.lower() = 'intimidate':
                       print('You get as big as possible and try to roar back at it. Turns out, the bear was just a mom concerned for her kids, so she walks away.')
                       break
                elif q16.lower() = 'fight':
                       print('big mistake. The bear swipes at you twice before you manage to run away.')
                       break
       else:
            print(error)
else:
    print(error)
