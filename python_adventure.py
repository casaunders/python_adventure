# Project needs functions, if/else statements and logging.
# Create functions to process events to work through game, generate ASCII art etc.
# Story will progress by selecting the appropriate choices.
# Bring in ASCII art from separate files.
# from playsound import playsound

def print_ascii(fn):
    f= open(fn,"r")
    print("".join([line for line in f]))

print_ascii("banner.txt")
print_ascii("station.txt")
def game_start():
  print_ascii("station.txt")
print("|--------------------------------------------------------------------------------------|")
print("|  Hello Traveler. I see your ticket location. But what if I told you that you can be  |")
print("|    and have all you ever wished for? I have here a ticket for a special location     |")
print("|  which can grant you all you ever desired. But you will have to navigate some real   |")
print("|  treacherous terrain for this one-of-a-kind item. So, traveler... what do you say?   |")
print("|   Can you navigate the tough trek ahead and return more powerful then ever before?   |")
print("|--------------------------------------------------------------------------------------|")

def accept():
    traveler = input(">How courageous... adventurous. What's your name traveler? \n>")
    print(f">Enjoy the ride {traveler}...")
    print("|--------------------------------------------------------------------------------------|")
    print("| You accept the ticket and board the train. You feel a mysterious aura as you enter.  |")
    print("|  As the train begins to pick up speed you hear thunderous claps as you notice your   |")
    print("|  surroundings begin to morph into unintelligible space to your eye! Your eyes are    |")
    print("| then blinded by a massive light! Once you adjust you notice a large hole set before  |")
    print("| you - like the landscape was ripped from reality as is if it was paper. It was a new |")
    print("|  location a new dimension perhaps. The train moved quicker and quicker to the void!  |")
    print("|  Your heart beats as fast as the train it seems, as suddenly you fall unconscious!   |")
    print("|--------------------------------------------------------------------------------------|")

def reject():
    print_ascii("sign.txt")
    print("|------------------------------------------------------------------------------------|")
    print("|                                                                                    |")
    print("| That's too bad. Fortune favors the brave. It's good to know when you can't cut it. |")
    print("|                                     GAME OVER                                      |")
    print("|------------------------------------------------------------------------------------|")
    exit(0)

def stay():
    print_ascii("death.txt")
    print("|---------------------------------------------------------------------------------------|")
    print("|   You spend days on end trying to restart the train and desperately try to find a way |")
    print("|    back home. You look through all you can to no avail. Too scared to move away from  |")
    print("|   your current surroundings you slowly dive into the depths of madness until one day  |")
    print("|   you broke completely. You live out your fantasies in a trance while in reality you  |")
    print("| are cornered in a feeble state rocking back and forth murmuring to yourself inaudibly.|")
    print("|                                    GAME OVER                                          |")
    print("|---------------------------------------------------------------------------------------|")
    exit(0)

def go():
    print_ascii("desert.txt")
    print("|---------------------------------------------------------------------------------------|")
    print("|  You step out hesitantly, looking around. You realize you are in a vast desert. You   |")
    print("|  see many things and really wonder what you can find that's so powerful in a barren   |")
    print("|    wasteland. You see an odd sight. A mule executed by hanging. You notice a gleam    |")
    print("| emanating from the mule's belly. You wonder if this is the item you were told about.  |")
    print("|      You have a decision to make. Do you search the body, or turn tail and run?       |")
    print("|---------------------------------------------------------------------------------------|")

def search():
    print_ascii("key.txt")
    print("|---------------------------------------------------------------------------------------|")
    print("|      You stick your hand in the gutted stomach of the executed animal, searching.     |")
    print("|  You find a key and wonder what it may go to. Maybe all this searching was worth it.  |")
    print("|      You hear a rumble from behind and then feel a violent shaking at your feet!      |")
    print("| You turn to see a large door rising from the sand! It is not attached to a thing! You |")
    print("|  see a small padlock on the handle locking it tight. This must be what the key is to! |")
    print("|---------------------------------------------------------------------------------------|")

def run():
    print_ascii("wolf.txt")
    print("|---------------------------------------------------------------------------------------|")
    print("|  Spooked and confused by the whole sight you feel that you need to run! Just as this  |")
    print("| thought crosses your mind you hear a low rumble and the a slight growl. You turn and  |")
    print("| find yourself face to face with a wolfpack! They quickly surround you. You pray they  |")
    print("|      finish you quick as they lunge toward you, ripping into their next feast!        |")
    print("|                                    GAME OVER                                          |")
    print("|---------------------------------------------------------------------------------------|")
    exit(0)

def use_key():
    print_ascii("lock.txt")
    print("|---------------------------------------------------------------------------------------|")
    print("|  You stick the key in and turn until you here a click. You wonder if you reached the  |")
    print("|    holy grail. Your hand trembles as you push the door handle down and cracked the    |")
    print("|  door open slightly. Do you finish the quest and force yourself through the gateway?  |")
    print("|---------------------------------------------------------------------------------------|")

def investigate():
    print_ascii("landscape.txt")
    print("|---------------------------------------------------------------------------------------|")
    print("|You decide that maybe this was all not worth it after all and that a floating door is a|")
    print("| too much right now. You begin to walk away looking for another soul hoping to find a  |")
    print("|      answer and a way back home... People to this day say you are still walking.      |")
    print("|           One thing is for sure. You were never seen or heard from again.             |")
    print("|                                    GAME OVER                                          |")
    print("|---------------------------------------------------------------------------------------|")
    exit(0)

def finish():
    print_ascii("win.txt")
    print('|---------------------------------------------------------------------------------------|')
    print('|   As you push through the door you feel your head become cloudy and start hearing a   |')
    print('|  distant ringing in the distance. The door becomes heavier as you think you come too  |')
    print('|  far to be stopped now! You feel you are losing strength as the ringing becomes much  |')
    print('|   louder and louder. You shut your eyes and push with all your might! You once again  |')
    print('|  open your eyes to new surroundings. Your room... you stop the alarm clocks intrusive |')
    print('|    sound as you think back to the dream and whisper to yuorself, "That was weird!"    |')
    print('|                                     GAME COMPLETE                                     |')
    print('|---------------------------------------------------------------------------------------|')

first_decision = input(">Traveler... Do you accept the ticket of a lifetime? \nAccept or Reject? \n>").lower()

if first_decision == "accept":
    accept()
elif first_decision == "reject":
    reject()
else:
    print('Not a valid input. Please type "Yes" or "No"')

print_ascii("door.txt")

print("|--------------------------------------------------------------------------------------|")
print("| You awake and realize the train has stopped. You collect yourself and pull the door  |")
print("|   open. You hesitate as you think of stepping out into the unknown land. You are     |")
print("|  beginning to second guess yourself as you wonder if this spontaneous vacation was   |")
print("|  worth it. But you are stuck now! Or are you? Can you go back...? Probably not. How  |")
print("|  would you pilot this train? Who drove it here? Doesn't matter. What do you do? You  |")
print("|   have to make a choice. Do you stay or do you step foot into the unknown outdoors?  |")
print("|                     Should you stay or should you go now?                            |")
print("|--------------------------------------------------------------------------------------|")

second_decision = input(">Traveler... Do you stay and try to jerry-rig the train to get back home? Or do you travel out into the unknown plateau? \nStay or Go? \n>").lower()

if second_decision == "stay":
    stay()
elif second_decision == "go":
    go()
else:
    print('Not a valid input. Please type "Stay" or "Go"')

third_decision = input(">Traveler... Do you search? Or do you run? \nSearch or Run? \n>").lower()

if third_decision == "search":
    search()
elif third_decision == "run":
    run()
else:
    print('Not a valid input. Please type "Search" or "Run"')

fourth_decision = input(">Traveler... Do you use the key? Or do you investigate eslewhere? \nUse Key or Investigate? \n>").lower()

if fourth_decision == "use key":
    use_key()
elif fourth_decision == "investigate":
    investigate()
else:
    print('Not a valid input. Please type "Search" or "Run"')

sixth_decision = input(">Traveler... Do you want to finish the quest? \nFinish\n>").lower()

if sixth_decision == "finish":
    finish()
else:
    print('Not a valid input. Please type "Finish"')
    
