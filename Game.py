name=input("Enter your name:")
print('''You find yourself waking up in the midst of a deep and dark forest. You find an envelope beside you that contains the following "Solve the puzzle before daybreak if you want to get out alive". You decide to look around and you find a forked road.
      Which path do you take?
      1.Go left
      2.Go right''')
a=int(input("Enter your choice:"))
if a==1:
    print('''You proceed on the left path and find a haunted house. You decide to enter inside but you are asked for a password in order to open the door.
          What do you do?
          1.Break the door
          2.Look around
          3.Try out random combinations''')
    b=int(input("Enter your choice:"))
    if b==1:
        print('''You successfully break the door. The moment you enter inside you find a corpse lying on the floor amidst a pool of blood. You find three people in front of you''')
