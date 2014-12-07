from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print ("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            print ("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def underwater_castle():
    print "You open the door, and immediately you're engulfed in deep blue water that gushes out."
    print "You're floating in the dark water, and you open your eyes against the freezing cold."
    print "You see lights in the distance, and you start swimming towards it."
    print "As you get closer you feel warmth coming from the light source."
    print "Soon you're staring astonishedly at an enormous underwater castle towering over you."
    print "There is a door in front of you, adorned with a small window with light glowing through."
    print "Do you dare go in?"

    choice == raw_input("> ")

    if choice == "yes" or choice == "go in":
        print "As you reach for the gracefully curved, stone handle, someone opens it from the inside -- a mermaid."
        print '"Visitor?" the mermaid asks in a soft, echoey voice. "Please come in." She gives you a warm smile.'
        


def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your front, right and left."
    print "Which one do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "front":
        underwater_castle()
    else:
        dead("You stumble around the room until you starve.")


start()