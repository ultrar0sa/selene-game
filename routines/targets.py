#redoing buttons because fuck it
from tkinter import *
from tkinter import ttk

def handle_button(*args, row, column, game, root):
    from game import Game
    fuckit = ["A", "B", "C", "D"] #bodge
    print(f"{column+1}{fuckit[row]}")
    buttonText = f"{column+1}{fuckit[row]}"
    game.handleSkip = True
   
    match game.gameState:
        case "inFlight":
            if buttonText == "1A":
                game.orbitButton1 = True
                print("Correct button pushed!")
                root.quit()
                root.destroy()
            elif buttonText == "3C":
                game.orbitButton2 = True
                print("Correct button pushed!")
                root.quit()
                root.destroy()
            else:
                print("you press the wrong button and rocket into the ground. :( \ngame over...")
                Game.gameOver = True
                root.quit()
                root.destroy()
            if game.orbitButton1 and game.orbitButton2:
                game.currentArea.flags["orbitCorrectionsDone"] == True
                game.add_radio_notification(radioContent="We can see that you've selected the correct buttons! The orbit should be coming up soon")
                game.gameState = "apporachingEarthOrbit"
        case "earthMoonTransfer":
            firstCorrectPress = "2B"
            secondCorrectPress = "3D"
            match Game.correctButtonPresses:
                case 0:
                    if game.playerTargetObject == firstCorrectPress:
                        print("you pressed the first button correctly")
                        Game.correctButtonPresses += 1
                        root.destroy()
                    else:
                        print("oops")
                        Game.incorrectButtonPresses += 1
                        root.destroy()
                case 1:
                    if game.playerTargetObject == secondCorrectPress:
                        game.add_radio_notification(radioContent="bad news, we've detected a leak out in one of the oxygen tubes out by the dock. please go fix it.")
                        Game.correctButtonPresses += 1
                        root.destroy()
                    else:
                        print("oops")
                        Game.incorrectButtonPresses += 1
                        root.destroy()
                case _:
                    #game.add_radio_notification(radioContent="bad news, we've detected a leak out in one of the oxygen tubes out by the dock. please go fix it.")
                    root.destroy()
            if Game.incorrectButtonPresses >= 2:
                print("your engines suddenly misfire and blow up your capsule. it's a sad day for spaceflight. :(")
                print("game over...")
                Game.gameOver = True
                

def button(game):
    from game import Game
    if game.playerAction == "push" or game.playerAction == "press":
        buttonRoot = Tk()
        buttonRoot.title("Button Matrix")
        buttonRoot.resizable(False, False)
        buttonFrame = ttk.Frame(buttonRoot, padding="3 3 12 12")
        buttonFrame.grid(column=0, row=0, sticky="N S E W")
        buttonList = []
        fuckit = ["A", "B", "C", "D"] #made out of anger because i gave up on byte additon 
        for row in range(0,4):
            buttonList.append([])
            for column in range(0,3):
                text = f"{column+1}{fuckit[row]}"
                button = ttk.Button(buttonFrame, width=2, text=f"{column+1}{fuckit[row]}", command=lambda r = row, c = column: handle_button(row=r, column=c, game=game, root=buttonRoot)) #HAVING TWO BUTTONS DO THE SAME THING BUT WITH DIFFERENT ARGS SHOULDN'T BE THIS HARD ARE YOU SERIOUS TK
                buttonList[row].append(button)
        for row in range(0,4):
            for column in range(0, 3):
               buttonList[row][column].grid(column=column+1, row=row+1)
        # test = ttk.Label(buttonFrame, text="gamer")
        # test.grid(row=0,column=0)
        ttk.Label(buttonFrame, text="1", justify="center").grid(column=1,row=0)
        ttk.Label(buttonFrame, text="2", justify="center").grid(column=2,row=0)
        ttk.Label(buttonFrame, text="3", justify="center").grid(column=3,row=0)

        ttk.Label(buttonFrame, text="A", justify="center").grid(column=0,row=1)
        ttk.Label(buttonFrame, text="B", justify="center").grid(column=0,row=2)
        ttk.Label(buttonFrame, text="C", justify="center").grid(column=0,row=3)
        ttk.Label(buttonFrame, text="D", justify="center").grid(column=0,row=4)
        

        buttonRoot.mainloop()
    else:
        print(f"you can't {game.playerAction} a button!")






# def button(game): #TODO: prob needs massive rewrite
#     from game import Game
#     #print("running button")
#     game.handleSkip = True
#     if game.playerAction == "push":
#         match game.gameState:
#             case "inFlight":
#                 if game.playerTargetObject == "kj22":
#                     game.orbitButton1 = True
#                     print("Correct button pushed!")
#                 elif game.playerTargetObject == "mo11":
#                     game.orbitButton2 = True
#                     print("Correct button pushed!")
#                 else:
#                     print("you press the wrong button and rocket into the ground. :( \ngame over...")
#                     Game.gameOver = True
#                 if game.orbitButton1 and game.orbitButton2:
#                     game.currentArea.flags["orbitCorrectionsDone"] == True
#                     game.add_radio_notification(radioContent="We can see that you've selected the correct buttons! The orbit should be coming up soon")
#                     game.gameState = "apporachingEarthOrbit"
#             case "earthMoonTransfer":
#                 firstCorrectPress = "vk88"
#                 secondCorrectPress = "wz81"
#                 match Game.correctButtonPresses:
#                     case 0:
#                         if game.playerTargetObject == firstCorrectPress:
#                             print("you pressed the first button correctly")
#                             Game.correctButtonPresses += 1
#                         else:
#                             print("oops")
#                             Game.incorrectButtonPresses += 1
#                     case 1:
#                         if game.playerTargetObject == secondCorrectPress:
#                             game.add_radio_notification(radioContent="bad news, we've detected a leak out in one of the oxygen tubes out by the dock. please go fix it.")
#                             Game.correctButtonPresses += 1
#                         else:
#                             print("oops")
#                             Game.incorrectButtonPresses += 1
#                     case _:
#                         game.add_radio_notification(radioContent="bad news, we've detected a leak out in one of the oxygen tubes out by the dock. please go fix it.")
#                 if Game.incorrectButtonPresses >= 2:
#                     print("your engines suddenly misfire and blow up your capsule. it's a sad day for spaceflight. :(")
#                     print("game over...")
#                     Game.gameOver = True
#     else:
#         print("you cant " + game.playerAction + " a button!")

#BUTTON_DICT = {"jdry" : button, "uo13" : button, "vk88" : button, "jn34" : button, "wz81" : button, "vo29" : button, "fk73" : button, "kj22" : button, "mo11" : button, "we64" : button, "lq12" : button, "ii43" : button, "js01" : button, "cf04" : button, "sz24" : button, "ez59" : button, "n57x" : button, "msy4" : button, "aym1" : button, "0frz" : button, "dyjj" : button, "jv71" : button, "4lhm" : button, "fdcx" : button, "ut9c" : button, "8rsl" : button, "ra78" : button, "jmn8" : button, "rwb5" : button, "xuu6" : button, "sgub" : button, "awpz" : button, "rrdz" : button, "mdna" : button, "wa03" : button, "ut13" : button, "zo51" : button, "ef57" : button, "uj34" : button, "su33" : button}

def keypad(game):
    print("im keypad")

def pass_handling():
    pass