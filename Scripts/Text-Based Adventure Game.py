name=input("Enter your name: ")
print("Welcome to the adventure game, "+name+".")
print('''You find yourself waking up inside a deep maze. You find an envelope besides you which contains the following: "Find the exit before daybreak, else the maze will collapse on its own." You then decide to look around and find a forked path.
How do you proceed?
1.Go right
2.Go left''')
a=int(input("Enter your choice: "))
if a==1:
    print('''You proceed on the right path and find a cat.
What do you do now?
1.Pick it up
2.Ignore it
3.Harm it''')
    b=int(input("Enter your choice: "))
    if b==1:
        print('''You pick up the cat and find a key in its collar. You decide to take the key and proceed forward.
You now find three rooms with a lion, a red panda and a beehive in each. Which room do you enter?
1.The room with the lion
2.The room with the red panda
3.The room with the beehive''')
        c=int(input("Enter your choice: "))
        if c==1:
            print('''Well, that was a dumb move. The lion eats you and you die.
THE END''')
        elif c==2:
            print('''Well done! I wonder if you knew that a red panda, despite its name is not an actual panda. It is in fact a cute raccoon like creature which is red in colour and is extremely friendly and harmless.
The red panda plays with you for a while and then you notice that there is a door. You try using the key which you found on the cat's collar and to your surprise it unlocks the door! 
On the other side of this door you find a room with another door. You find a note on the door which says "Solve the riddle to open the door". The riddle is as follows "What is so fragile that saying its name breaks it?"''')
            g=input("Enter your answer to the riddle: ")
            answer=['silence','Silence','quiteness','Quiteness']
            if g in answer:
                print('''Well done! The answer is silence. The door automatically opens. You are finally free from the maze. You win!!
THE END.''')
            else:
                print('''Too bad, the answer was silence. You lose!
THE END.''')
        elif c==3:
            print('''Well, that was a not so smart move. The bees swarm around you and continuously sting you. You writhe in pain and agony. You lose!
THE END.''')
        else:
            print("Enter a valid choice! Either 1,2 or 3.")
            c=int(input("Enter your choice: "))
    elif b==2:
        print('''You decide to ignore the cat and proceed forward. You now find three rooms with a lion, a red panda and a beehive in each. Which room do you enter?
1.The room with the lion
2.The room with the red panda
3.The room with the beehive''')
        c=int(input("Enter your choice: "))
        if c==1:
            print('''Well, that was a dumb move. The lion eats you and you die.
THE END''')
        elif c==2:
            print('''Well done! I wonder if you knew that a red panda, despite its name is not an actual panda. It is in fact a cute raccoon like creature which is red in colour and is extremely friendly and harmless.
The red panda plays with you for a while and then you notice that there is a door. You move closer and find that there is a mechanical bot and a coin in front of the door. The bot tells you to toss the coin and if you get a Tails on it, the bot will open the door for you.
What do you do?
1.Toss the coin
2.Ignore the bot''')
            d=int(input("Enter your choice:"))
            if d==1:
                import random
                num=random.randint(1,2)
                if num==2:
                    print('''Woohoo! You got Tails! The bot opens the door for you. You are finally free from the maze! You win!
THE END.''')
                else:
                    print("Too bad, you got a Heads. Better luck next time.")
                    print("THE END.")
            elif d==2:
                print('''Well, you can't proceed if you choose to ignore the bot can you? You lose!
THE END.''')
            else:
                print("Enter a valid choice! Either 1 or 2.")
                d=int(input("Enter your choice:"))
        elif c==3:
            print('''Well, that was a not so smart move. The bees swarm around you and continuously sting you. You writhe in pain and agony. You lose!
THE END.''')
        else:
            print("Enter a valid choice! Either 1,2 or 3.")
            c=int(input("Enter your choice: "))
    elif b==3:
        print("Why would you harm an innocent cat?! You are banned from playing this game! YOU LOSE!!")
        print("THE END.")
    else:
        print("Enter a valid choice! Either 1,2 or 3.")
        b=int(input("Enter your choice: "))
elif a==2:
    print('''You proceed on the left path. You now find a door in front of which is a mechanical bot. The bot asks you to play a game of Rock Paper Scissors and if you win the bot will open the door for you. The bot also specifies that it will only use Scissors.
What do you use?
1.Rock
2.Paper
3.Scissors''')
    e=int(input("Enter your choice: "))
    if e==1:
        print('''Too bad, the bot uses Paper. Your trust in the bot has led to your defeat. You lose!
THE END.''')
    elif e==2:
        print('''The bot uses Paper too! Its a tie. But the condition was that the bot opens the door only if you win. So you can't proceed forward. You lose!
THE END.''')
    elif e==3:
        print('''Well done! You've outsmarted the bot! It never intended to use Scissors and in fact used Paper. Your distrust in people, or well... bots, has led to your victory. The bot congratulates you and opens the door.
On the other side of this door you find a room with another door. You find a note on the door which says "Solve the riddle to open the door". The riddle is as follows "What can't talk but will reply when spoken to?"''')
        f=input("Enter your answer to the riddle: ")
        ans=['echo','an echo','Echo','ECHO','An echo']
        if f in ans:
            print('''Well done! The answer is echo. The door automatically opens. You are finally free from the maze! You win!!
THE END.''')
        else:
            print('''Too bad, the answer was echo. You lose.
THE END.''')
    else:
        print("Enter a valid choice! Either 1,2 or 3.")
else:
    print("Enter a valid choice! Either 1,2 or 3.")
        
    
  

 

