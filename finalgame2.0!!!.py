import time #Imports a module to add a pause

#Defining user response
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

required = ("\nUse only A, B, or C\n") #Cutting down on duplication

#The story is broken into sections, starting with "intro"
def intro():
  print ("After a long four years at Magnet High School, you have finally graduated! Your grades were good enough to get you into the prestigious college you have been dying to go to. Your first week of college goes by, and you are beginning to feel more comfortable. You meet a guy named Chad in your first period class. Chad suggests that you two should hang out after school, and you could not agree more, you need to start meeting new people. Chad lets you decide what you guys will do. :")
  time.sleep(1)
  print ("""  A. Play video games in his dorm room
  B. Study at a coffee shop
  C. Frat party""")
  choice = input(">>> ") #Here is your first choice.
  if choice in answer_A:
    option_videogames()
  elif choice in answer_B:
    print ("\nYour response has left Chad in awe. He says he has changed his mind and calls you boring. "
    "\n\nYou lost your shot at a friend! You are a failure.")
  elif choice in answer_C:
    option_fratparty()
  else:
    print (required)
    intro()

def option_videogames(): 
  print ("\nYou meet Chad in the quad and walk over to his dorm room. You open the door and are hit in the face with a stench that reeks so bad it is undescribable. You shake it off and play some Playstation with Chad. Out of the corner of your eye, "
  "you notice a MAGA flag. Your family hates Donald Trump. Do you:")
  time.sleep(1)
  print ("""  A. Call Chad a mean word
  B. Ignore the flag""")
  choice = input(">>> ")
  if choice in answer_A:
    option_brawl()
  elif choice in answer_B:
    print ("\nYou and Chad continue to game, but slowly realize that you guys have nothing in common. "
    "\n\nChad is a very straight forward guy. He tells you that you are NOT cool enough for him. He kicks you out of his room.")

def option_brawl():
  print("Chad is stunned. He says he wants to fight you, bro. He squares up and you are left with no choice but to attack him. You:")
  time.sleep(1)
  print ("""  A. Suckerpunch him
  B. Try to give him a mean backhand
  C. Attempt a low class move and aim at his privates""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("Did you seriously think you could take out Chad? Chad eats punches for days. He laughs at your pathetic attempt. You close your eyes and cry for your mommy. "
    "\n\nChad didn't even need to hit you. You made a fool out of yourself. Better luck next time.")
  elif choice in answer_B:
    print ("\Chad is stunned at the hit he has absorbed. The only person to ever slap Chad is his mother. The slap triggers some sort of PTSD and Chad breaks down into tears. "
    "You failed at making a new friend, but you succeeded at preserving your health.")
  elif choice in answer_C:
    print ("\nYou have made Chad angry. Sure, the kick hurts, but Chad is overcome by emotions of pure rage. Why would you pull off such a low class move? You know better than that."
    "\n\nWhen you wake up from your blackout, you are in the campus hospital. At least Chad had the decency to check you in after beating you up.")

  print("You have failed to make a new friend.")

def option_fratparty():
  print ("\nChad comes by your room later to take you to your first frat party. You are a bit nervous but excited to meet new people. You arrive at the frat house and see lots of people already there. Chad takes you inside and introduces you to his friends. They stand together in a mixed group of guys and girls. Suddenly, you feel your body tremble and you feel what you think is a fart creeping its way down your intestines. It hurts, bad. Do you: ")
  print ("""  A. Hold it in\nB. Let it rip""")
  choice = input(">>> ")
  if choice in answer_A:
    option_socializing()
  elif choice in answer_B:
    print ("\nIt was not a quiet one, as you had hoped for. The roar of the gas leaving your rear end horrifies Chad and his friends. The music at the party turns off. Everyone points at you and laughs. Chad sighs and shakes his head. \n\nYou were kicked out of the frat party for stinking up the already stinky frat house even more.")

def option_socializing(): 
  print ("\nAfter talking to Chad and his friends, you all seem to be getting along, and Chad pulls you aside. He tells you that he is going leave for a bit, but he does not want you to be alone, so he gives you some options of what to do while he is gone. You can: ")
  time.sleep(1)
  print ("""  A. Drink with Chad's bros
  B. Hang out with Chad's girlfriend, Britney""")
  choice = input(">>> ")
  if choice in answer_A:
    print ("\nAfter processing what you had just agreed to do, you realize that you are a good kid and you do not participate in illegal activities such as under age drinking. "
    "\n\nYou sprint out the door of the frat house and head back to your room, finding solace in your textbooks.")
  if choice in answer_B:
    option_britney()

def option_britney():
  print ("\n You and Britney talk for a bit. She seems to genuinely like you as a person. You two decide to leave the party and get some ice cream, and tell Chad to meet you at the ice cream place. However, you have no money on you, and Britney claims that she forgot her wallet in her room. She tells you to come with her. Do you: ")
  time.sleep(1)
  print ("""  A. Go with her
  B. Be a weirdo and say no""")
  choice = input(">>> ")
  if choice in answer_A:
    option_britneyroom()
  if choice in answer_B:
    print ("\nThere was absolutely no reason for you to not go with Britney. You should never leave a girl alone at an hour like that walking around campus. "
    "\n\nBritney tells Chad that you abandoned her, and he is not mad at you, but he is disappointed. You made Chad sad.")

def option_britneyroom():
  print ("\n You make it to Britney's room and she looks for her wallet. After a few minutes, she still has not found it. Britney asks you to look around for her wallet while she changes her top. You hesitate, because the dorm room is a one bedroom setup, but agree to what she says. Suddenly, someone bursts through the doors of Britney's room. It's Chad, and he is mad... You can't blame him. You know that the scenario looks bad from a third person point of view. You sigh and mentally prepare yourself for what is about to happen. What do you say to Chad?: ")
  print ("""  A. It isn't what it looks like!
  B. What's up bro?
  C. What took you so long?""")
  choice = input(">>> ")
  if choice in answer_A:
    option_brawl()
  if choice in answer_B:
    option_brawl()
  if choice in answer_C:
    option_brawl()

def option_failure():
  print("You failed to make a new friend. You lose.")

intro()


