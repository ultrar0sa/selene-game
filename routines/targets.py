

def button(game):
    #print("running button")
    game.handleSkip = True
    firstCorrectPress = "vk88"
    secondCorrectPress = "wz81"
    if game.playerAction == "push":
        from game import Game
        match Game.correctButtonPresses:
            case 0:
                if game.playerTargetObject == firstCorrectPress:
                    print("you pressed the first button correctly")
                    Game.correctButtonPresses += 1
                else:
                    print("oops")
                    Game.incorrectButtonPresses += 1
            case 1:
                if game.playerTargetObject == secondCorrectPress:
                    print("you pressed the second button correctly, you can now burn")
                    Game.correctButtonPresses += 1
                else:
                    print("oops")
                    Game.incorrectButtonPresses += 1
            case _:
                print("you can now burn for the moon!")
    else:
        print("you cant " + game.playerAction + " a button!")

#BUTTON_DICT = {"jdry" : button, "uo13" : button, "vk88" : button, "jn34" : button, "wz81" : button, "vo29" : button, "fk73" : button, "kj22" : button, "mo11" : button, "we64" : button, "lq12" : button, "ii43" : button, "js01" : button, "cf04" : button, "sz24" : button, "ez59" : button, "n57x" : button, "msy4" : button, "aym1" : button, "0frz" : button, "dyjj" : button, "jv71" : button, "4lhm" : button, "fdcx" : button, "ut9c" : button, "8rsl" : button, "ra78" : button, "jmn8" : button, "rwb5" : button, "xuu6" : button, "sgub" : button, "awpz" : button, "rrdz" : button, "mdna" : button, "wa03" : button, "ut13" : button, "zo51" : button, "ef57" : button, "uj34" : button, "su33" : button}

def keypad(game):
    print("im keypad")

def pass_handling():
    pass