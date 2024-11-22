import json

def pull(game):
    print("pull")

def push(game):
    print("push")
    
def take(game):
    print("taking")

def look(game):
    print("looking") #i fucked up

def radio(game):
    from game import Game
    if game.radioContent != "":
        print(game.radioContent)
    Game.radioNotifPresentButNotAnswered = False
    
def fix(game):
    print("What? With no tools?")

def move(game):
    from game import Game
    from area import Area
    #print(game.currentArea.gates)
    if not Game.disableMovement:
        if game.desiredArea != "":
        # for allowedArea in game.currentArea.gates:
        #      if game.desiredArea == allowedArea:
        #          if game.desiredArea
        #          game.currentArea = Game.AREA_DICT[allowedArea]
        #          print(game.currentArea.description)
            game.currentArea = game.desiredArea
            print(game.currentArea.description)
        else:
            print("You can't move there!")
    else:
        print(Game.moveDisabledText)
        
        
   #Game.currentArea
    #print("moving")
    
def launch(game):
    from game import Game
    if game.currentArea.names[0] == "capsule":
        match game.gameState:
            case "start":
                print("liftoff!")
                game.currentArea.description = "You are in flight and headed towards orbit."
                game.gameState = "inFlight"
                print("now the wait")
            case "earthMoonTransfer":
                print(Game.oxygenTubeFixed)
                if Game.correctButtonPresses >= 2 and Game.oxygenTubeFixed:
                    print("the engines fire successfully and you are on your way to the moon! :)")
                    game.gameState = "inTransfer"
                else:
                    print("the engines misfire, blowing up your capsule in space. it's a very sad day for space travel. :(")
                    print("game over...")
                    Game.gameOver = True

def map(game):
    from game import Game
    from maps import Maps
    from area import Area
    
    Game.map.load_file(game.currentArea.mapPath)
    print("printed map")

def info(game):
    from game import Game
    print(game.currentArea.description)

def wait(game):
    from game import Game
    inFlightResponses = ["the earth grows further away.", "the sky grows more and more black through the window", "it is almost a dream."]

    if game.currentArea.names[0] == "capsule":
        match game.gameState:
            case "inFlight":
                if game.waitAmounts == 2 and not game.currentArea.flags["orbitCorrectionsDone"]:
                    game.add_radio_notification(radioContent="you need to enter the correct orbit calculations into the nav computer. press buttons 1A and 3C")
                    game.waitAmounts = 0
                elif game.waitAmounts < 2:    
                    print(inFlightResponses[game.waitAmounts])
                    game.waitAmounts += 1
            case "apporachingEarthOrbit":
                print("you are moving across the earth's surface with speed. hurricanes, oceans, and continents float by.")
                game.gameState = "inEarthOrbit"
                game.currentArea.description = "You are now in orbit"
            case "inTransfer":
                print("this is a long wait, this one. the blue ball grows weaker and weaker into the void. everyone everywhere is getting smaller.") 
                print("you eat plenty of space snacks and listen to plenty of space music.")
                print("you even get put on tv.")
                print("but in the end it's time. it's time to land on the moon.")
                print("you take manual joystick control. your going to need it.")
                game.gameState = "landingTime"



def save(game):
    from game import Game
    gameDict = {"gameState" : game.gameState,
                "currentArea" : game.currentArea.names[0],
                "inventory" : game.inventory,
                "movementDisabled" : Game.disableMovement,
                "moveDisabledText" : Game.moveDisabledText,
                "oxygenTubeFixed" : Game.oxygenTubeFixed,
                "waitAmounts" : game.waitAmounts,
                "landingSite" : game.landingSite,
                "orbitButton1" : game.orbitButton1,
                "orbitButton2" : game.orbitButton2,
                "correctButtonPresses" : Game.correctButtonPresses,
                "incorrectButtonPresses" : Game.incorrectButtonPresses,
                "radioNotifPresentButNotAnswered" : Game.radioNotifPresentButNotAnswered,
                "radioNotification" : game.radioNotification,
                "radioContent" : game.radioContent}
    

    with open("save.json", mode="w") as file:
        file.write(json.dumps(gameDict, indent=4))
        file.close()
    
def load(game):
    from game import Game
    from area import Area
    with open("save.json", mode="r") as file:
        gameDict = json.load(file)
        game.gameState = gameDict["gameState"]
        for area in Game.AREA_LIST:
            if area.names[0] == gameDict["currentArea"]:
                game.currentArea = area
                break
        game.inventory = gameDict["inventory"]
        Game.disableMovement = gameDict["movementDisabled"]
        Game.moveDisabledText = gameDict["moveDisabledText"]
        Game.oxygenTubeFixed = gameDict["oxygenTubeFixed"]
        game.waitAmounts = gameDict["waitAmounts"]
        game.landingSite = gameDict["landingSite"]
        game.orbitButton1 = gameDict["orbitButton1"]
        game.orbitButton2 = gameDict["orbitButton2"]
        Game.correctButtonPresses = gameDict["correctButtonPresses"]
        Game.incorrectButtonPresses = gameDict["incorrectButtonPresses"]
        game.radioNotification = gameDict["radioNotification"]
        game.radioContent = gameDict["radioContent"]
        if gameDict["radioNotifPresentButNotAnswered"]:
            radio(game)

def exit(game):
    from game import Game
    Game.gameOver = True