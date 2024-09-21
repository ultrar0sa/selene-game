def pull(game):
    print("pull")

def push(game):
    print("push")
    

def look(game):
    print("look")
    
def radio(game):
    print("radio")
    

def move(game):
    from game import Game
    from area import Area
    #print(game.currentArea.gates)
    for allowedArea in game.currentArea.gates:
        if game.desiredArea == allowedArea:
            game.currentArea = Game.AREA_DICT[allowedArea]
            print(game.currentArea.description)
            
   #Game.currentArea
    #print("moving")
    
def launch(game):
    from game import Game
    if Game.correctButtonPresses >= 2:
        print("the engines fire successfully and you are on your way to the moon! :)")
    else:
        print("the engines misfire, blowing up your capsule in space. it's a very sad day for space travel. :(")
        print("game over...")
    Game.gameOver = True
    
