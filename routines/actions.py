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
    inFlightResponses = ["The earth grows further away.", "The sky grows more and more black through the window", "It is almost a dream."]

    if game.currentArea.names[0] == "capsule":
        match game.gameState:
            case "inFlight":
                if game.waitAmounts == 2 and not game.currentArea.flags["orbitCorrectionsDone"]:
                    game.add_radio_notification(radioContent="You need to enter the correct orbit calculations into the nav computer. Press buttons kj22 and mo11")
                    game.waitAmounts = 0
                elif game.waitAmounts < 2:    
                    print(inFlightResponses[game.waitAmounts])
                    game.waitAmounts += 1
            case "apporachingEarthOrbit":
                print("You are moving across the earth's surface with speed. Hurricanes, Oceans, and Continents float by.")
                game.gameState = "inEarthOrbit"
                game.currentArea.description = "You are now in orbit"

 