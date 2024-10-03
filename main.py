# i am making this out of spite
#import routines.accessories
#import routines.actions
import routines.targets
from game import Game
from area import Area
VERSION = "Early Alpha"

#VALID_PLAYER_ACTIONS = {"push" : push(), "pull" : pull(), "lie" : lie(), "cheat" : cheat(), "kill" : kill(), "look" : look()}
#VALID_NO_TARGET_COMMANDS = ["look"]
#VALID_TARGET_OBJECTS = ["button", "keypad"]
#VALID_ACCESSORY_OBJECTS = ["hammer", "fist"]
#playerAction = "" #may need to refactor this into a class later
#playerTargetObject = ""
#playerAccessoryObject = ""




        
   
#driver code
from routines.targets import button
oxygenTubeFixed = False
launchReady = False
BUTTON_DICT = {"jdry" : button, "uo13" : button, "vk88" : button, "jn34" : button, "wz81" : button, "vo29" : button, "fk73" : button, "kj22" : button, "mo11" : button, "we64" : button, "lq12" : button, "ii43" : button, "js01" : button, "cf04" : button, "sz24" : button, "ez59" : button, "n57x" : button, "msy4" : button, "aym1" : button, "0frz" : button, "dyjj" : button, "jv71" : button, "4lhm" : button, "fdcx" : button, "ut9c" : button, "8rsl" : button, "ra78" : button, "jmn8" : button, "rwb5" : button, "xuu6" : button, "sgub" : button, "awpz" : button, "rrdz" : button, "mdna" : button, "wa03" : button, "ut13" : button, "zo51" : button, "ef57" : button, "uj34" : button, "su33" : button}
cape = Area(["cape", "mission control"], "this is cape canveral", [], mapPath="savedshapes/capemap.json")
tower = Area(["tower"], "this is tower", [], mapPath="savedshapes/towermap.json")
capsule = Area(["capsule", "inside"], "this is the space capsule", [], {"launchReady" : launchReady}, "savedshapes/capsulemap.json")
dockingPort = Area(["docking port", "dock"], "you are next to the [docking port], out in space. the broken oxygen tube is right in front of you.", [], {"fixed" : oxygenTubeFixed})
outsideCapsuleDoor = Area(["outside capsule door", "outside", "spacewalk", "space", "capsule door"], "you are out in space next to the [capsule door]. the broken oxygen tube is right next to the [docking port]", [])
capsule.avaliable_targets = BUTTON_DICT
dockingPort.avaliable_targets = {}
capsule.gates = outsideCapsuleDoor.names + cape.names + tower.names
dockingPort.gates = outsideCapsuleDoor.names
outsideCapsuleDoor.gates = capsule.names + dockingPort.names
cape.gates = capsule.names + tower.names
tower.gates = capsule.names + cape.names



AREA_DICT = {"capsule" : capsule, "inside" : capsule, 
             "outside" : outsideCapsuleDoor, "spacewalk" : outsideCapsuleDoor, "space" : outsideCapsuleDoor, "capsule door" : outsideCapsuleDoor,
             "docking port" : dockingPort, "dock" : dockingPort,
             "cape" : cape, "mission control" : cape,
             "tower" : tower}
MAP_DICT = {"capsule" : "savedshapes/capsulemap.json", "cape" : "savedshapes/capemap.json", "tower" : "savedshapes/towermap.json"}
game = Game(capsule)
Game.AREA_DICT = AREA_DICT
Game.MAP_DICT = MAP_DICT

print(capsule.names[0])
print("SELENE " + str(VERSION))

print("you are just about to your moon burn calculations that will put you in the moons orbit!")
game.add_radio_notification("you see the \"incomming message\" light fire on your dashboard", "HOUSTON: we've detected a leak in one of the oxygen tubes out by the dock. please go out and fix it before you get ready for launch!")
while not Game.gameOver:
    game.player_input()
    if Game.incorrectButtonPresses >= 2:
        print("your engines suddenly misfire and blow up your capsule. it's a sad day for spaceflight. :(")
        print("game over...")
        Game.gameOver = True
