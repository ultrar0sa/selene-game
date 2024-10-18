def pull(game):
    print("pull")

def push(game):
    print("push")
    
def take(game):
    print("taking")

def look(game):
    print("You look around wildly, like a maniac.")
    
def radio(game):
    from game import Game
    if game.radioContent != "":
        print(game.radioContent)
    
def fix(game):
    print("fixing")

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
        print(Game.moveDisabledText)
        
            
   #Game.currentArea
    #print("moving")
    
def launch(game):
    from game import Game
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
