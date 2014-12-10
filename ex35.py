from sys import exit

def gold_room():
    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    how_much = int(choice)

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

    choice = raw_input("> ")

    if choice == "yes" or choice == "go in":
        print "As you reach for the gracefully curved, stone handle, someone opens it from the inside -- a mermaid."
        print '"Visitor?" the mermaid asks in a soft, echoey voice. "Please do come in." She gives you a warm smile.'
        print "Do you trust her?"

        trust = raw_input("> ")

        if trust == "yes":
            print "You hesitantly take the mermaid's outstretched hand, and let her lead you inside."
            print '''It's very warm and cozy here, unlike the merciless cold outside this strange castle.
            You glance uncertainly at the mermaid, who sits you down at a wooden table engraved with fancy patterns.
            She offers you the milk and cookies (wait, wut?) on the table.'''
            print " "
            print "1. Who are you?"
            print "2. What is this place?"
            print "3. How do I get out of here?"

            ask = raw_input("> ")

            if ask == "1":
                print 'The mermaid smiles slyly. "The keeper of this underwater castle."'
            elif ask == "2":
                print 'The mermaid smiles slyly. "The underwater castle in the middle of this dark underwater realm.'
            elif ask == "3":
                print 'The mermaid gazes at you intently with her aquamarine eyes. "The answer you seek, you will find within."'
                print "Was there a hint of sadness in her voice just now?"
            else:
                print "The mermaid blinks at you, confused."
                print '"Let me try again," you stammer.'

        elif trust == "no":
            print "You stare at the mermaid's outstretched hand, and the mermaid averts her eyes and withdraws her hand."
            print '"If you do not wish to accept my welcome, you will have to survive out there in the dark and face the Risk," she says. "I will leave you to your game then."'
            print "She falls silent, glances at you somewhat worriedly, then slowly closes the door shut. You're on your own now. You feel the pressure of the darkness behind you."
            print "You begin to think that wasn't exactly the best choice you've made so far."
        else:
            print 'The mermaid looks at you with curious eyes. I don\'t think she understands that," you think to yourself.'

    elif choice == "no" or choice == "don't go in":
        print '''You feel somewhat scared as you look behind you and see only cold darkness, but you decide to leave the door untouched. 
        You force yourself to turn from the tempting warmth and swim out into the unknown, ready to face any dangers to come.'''
    else:
        print "You can make a better choice than that, come on."
        print '"Let me try that again," you say."'



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