#test objects, please ignore...
def hammer(game):
     print("im a hammer")

def fist(game):
     print("why are you punching in space")
#you can start grading now 

def toolbox(game):
    from game import Game
    if game.playerAction == "look" and "toolbox" in game.inventory:
        print("A rather well apointed toolbox, with a deep supply of duct tape.")
        game.handleSkip = True
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
        else:
            print("there is nothing for the toolbox to be used on")
    else:
        print(f"you can't {game.playerAction} with this toolbox!")
    game.handleSkip = True
    
          
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
    elif "spacesuit" in game.inventory:
        print("The computer in your suit is getting confused.")
    game.handleSkip = True
    
def pass_handling():
    pass