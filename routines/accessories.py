#test objects, please ignore...
def hammer(game):
     print("im a hammer")

def fist(game):
     print("why are you punching in space")
#you can start grading now 

def toolbox(game):
    from game import Game
    game.handleSkip = True
    if game.playerAction == "look" and "toolbox" in game.inventory:
        print("A rather well apointed toolbox, with a deep supply of duct tape.")
        return
    if "toolbox" not in game.inventory:
        if (game.playerAction == "take" or game.playerAction == "get"):
            if game.currentArea.names[0] == "capsule":
                print("you take the toolbox")
                game.inventory.append("toolbox")
                return #lmao
            else:
                print("there is no toolbox to take")
                return
        else:
            print("what toolbox?")
            return
        
    if game.playerAction == "fix":
        # print(game.currentArea.flags.keys())
        # print(game.currentArea.names)
        if "fixed" in game.currentArea.flags.keys():
            game.currentArea.flags["fixed"] = True
            match game.currentArea.names[0]:
                case "docking port":
                    Game.oxygenTubeFixed = True
                    print("the oxygen tube is fixed.")
                    return
        else:
            print("there is nothing for the toolbox to be used on")
            return
    print(f"you can't {game.playerAction} with this toolbox!")

def rover(game):
    from game import Game
    from routines import actions
    game.handleSkip = True
    if game.playerAction == "look" and "rover" in game.inventory:
        print("it's a mighty fine rover, if you don't say yourself")
        return
    if "rover" not in game.inventory:
        if game.playerAction == "drive":
            if game.currentArea.names[0] == "site":
                print("you hop on the rover. the seat is unconfortable, but you'll deal. you are on the moon, you know.")
                game.inventory.append("rover")
                Game.VALID_PLAYER_ACTIONS["drive"] = actions.move #might break
                return 
            else:
                print("the rover has not detached yet.")
                return
        else:
            print(f"you can't {game.playerAction} with the rover!")
            return
        

          
def id(game):
    from game import Game
    if game.playerAction == "look" and "id" in game.inventory:
        print("It's a basic identification card, fit for an astronaut.")
        game.handleSkip = True
        return
    if (game.playerAction == "take" or game.playerAction == "get") and "id" not in game.inventory:
        print("you pick up the id. ")
        game.inventory.append("id")
    else: 
        print("You play around with your ID like an idiot.")
    game.handleSkip = True

def spacesuit(game):
    from game import Game
    if game.playerAction == "look" and "spacesuit" in game.inventory:
        print("The thing that will keep you alive in space")
        game.handleSkip = True
        return
    if (game.playerAction == "take" or game.playerAction == "get") and "spacesuit" not in game.inventory:
        game.inventory.append("spacesuit")
        print("you put on your space suit")
    elif "spacesuit" in game.inventory:
        print("The computer in your suit is getting confused.")
    game.handleSkip = True
    
def pass_handling():
    pass