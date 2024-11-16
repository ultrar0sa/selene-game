

def button(game): #TODO: prob needs massive rewrite
    from game import Game
    #print("running button")
    game.handleSkip = True
    if game.playerAction == "push":
        match game.gameState:
            case "inFlight":
                if game.playerTargetObject == "kj22":
                    game.orbitButton1 = True
                    print("Correct button pushed!")
                elif game.playerTargetObject == "mo11":
                    game.orbitButton2 = True
                    print("Correct button pushed!")
                else:
                    print("you press the wrong button and rocket into the ground. :( \ngame over...")
                    Game.gameOver = True
                if game.orbitButton1 and game.orbitButton2:
                    game.currentArea.flags["orbitCorrectionsDone"] == True
                    game.add_radio_notification(radioContent="We can see that you've selected the correct buttons! The orbit should be coming up soon")
                    game.gameState = "apporachingEarthOrbit"
            case "earthMoonTransfer":
                firstCorrectPress = "vk88"
                secondCorrectPress = "wz81"
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
                            game.add_radio_notification(radioContent="bad news, we've detected a leak out in one of the oxygen tubes out by the dock. please go fix it.")
                            Game.correctButtonPresses += 1
                        else:
                            print("oops")
                            Game.incorrectButtonPresses += 1
                    case _:
                        game.add_radio_notification(radioContent="bad news, we've detected a leak out in one of the oxygen tubes out by the dock. please go fix it.")
                if Game.incorrectButtonPresses >= 2:
                    print("your engines suddenly misfire and blow up your capsule. it's a sad day for spaceflight. :(")
                    print("game over...")
                    Game.gameOver = True
    else:
        print("you cant " + game.playerAction + " a button!")

#BUTTON_DICT = {"jdry" : button, "uo13" : button, "vk88" : button, "jn34" : button, "wz81" : button, "vo29" : button, "fk73" : button, "kj22" : button, "mo11" : button, "we64" : button, "lq12" : button, "ii43" : button, "js01" : button, "cf04" : button, "sz24" : button, "ez59" : button, "n57x" : button, "msy4" : button, "aym1" : button, "0frz" : button, "dyjj" : button, "jv71" : button, "4lhm" : button, "fdcx" : button, "ut9c" : button, "8rsl" : button, "ra78" : button, "jmn8" : button, "rwb5" : button, "xuu6" : button, "sgub" : button, "awpz" : button, "rrdz" : button, "mdna" : button, "wa03" : button, "ut13" : button, "zo51" : button, "ef57" : button, "uj34" : button, "su33" : button}

def keypad(game):
    print("im keypad")

def pass_handling():
    pass