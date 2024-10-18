# i am making this out of spite
#import routines.accessories
#import routines.actions
import routines.targets
from game import Game
from area import Area
VERSION = "Early Alpha"


#basic start menu
def start_menu():
    print("1.about\n2.instructions\n3.play game")
    match input("input: "):
        case "1":
            print("SELENE is a moon mission over text. \nIt is created by Vicky Yang, Jade Lukken, and David Foster for CS 1612 at the University of Minnesota Duluth")
            start_menu()
        case "2":
            print("When prompted, type commands into the console and press ENTER. \nThese commands include:\nmove {location name}\npush {button name}\nand fix {object}")
            print("The \"map\" command draws a map in the turtle window. NOTE: Map window cannot be closed by player using window close button. \nTo exit the game, player must hit ctrl-c and then enter.")
            print("Try and experiment with potential commands to see if they work in potential situtations!")
            print("Paper and pencil is recommended to have on hand.")
            start_menu()
        case "3":
            return
        case _:
            print("input a correct input")
            start_menu()



        
   
#driver code
from routines.targets import button
oxygenTubeFixed = False
launchReady = False

BUTTON_DICT = {"jdry" : button, "uo13" : button, "vk88" : button, "jn34" : button, "wz81" : button, "vo29" : button, "fk73" : button, "kj22" : button, "mo11" : button, "we64" : button, "lq12" : button, "ii43" : button, "js01" : button, "cf04" : button, "sz24" : button, "ez59" : button, "n57x" : button, "msy4" : button, "aym1" : button, "0frz" : button, "dyjj" : button, "jv71" : button, "4lhm" : button, "fdcx" : button, "ut9c" : button, "8rsl" : button, "ra78" : button, "jmn8" : button, "rwb5" : button, "xuu6" : button, "sgub" : button, "awpz" : button, "rrdz" : button, "mdna" : button, "wa03" : button, "ut13" : button, "zo51" : button, "ef57" : button, "uj34" : button, "su33" : button}

#start sequence
mainassembly = Area(["main room", "main assembly", "start"], "This is the main assembly room. You need to get you ID Passes before you can do anything. They are on the table at the far end of the hall.", [], mapPath="savedshapes/capemap.json")
spacesuits = Area(["spacesuit", "suit"], "This is the spacesuit room. People are gathered to help you put on your space suit.",  [], mapPath="savedshapes/capemap.json")

#pad sequence
tower = Area(["tower", "pad"], "this is tower", [], mapPath="savedshapes/towermap.json")
outsidePad = Area(["outside", "outside pad"], "You are outside the main pad. It's time to the [elevator bay] in order to head up the tower and get in the capsule!", [], mapPath="savedshapes/towermap.json")
elevatorBay = Area(["bay"], "You are in the elevator bay. Time to head up and move into the [capsule]!", [], mapPath="savedshapes/towermap.json")

#moon burn sequence
capsule = Area(["capsule", "inside"], "this is the space capsule", [], {"launchReady" : launchReady}, mapPath="savedshapes/capsulemap.json")
dockingPort = Area(["docking port", "dock"], "you are next to the [docking port], out in space. the broken oxygen tube is right in front of you.", [], {"fixed" : Game.oxygenTubeFixed}, mapPath="savedshapes/capsulemap.json")
outsideCapsuleDoor = Area(["outside capsule door", "outside", "spacewalk", "space", "capsule door"], "you are out in space next to the [capsule door]. the broken oxygen tube is right next to the [docking port]", [], mapPath="savedshapes/capsulemap.json")
 
capsule.avaliable_targets = BUTTON_DICT 
dockingPort.avaliable_targets = {}
# capsule.gates = outsideCapsuleDoor.names + mainassembly.names + tower.names
# dockingPort.gates = outsideCapsuleDoor.names
# outsideCapsuleDoor.gates = capsule.names + dockingPort.names
# # cape stuff
# mainassembly.gates = capsule.names + tower.names + spacesuits.names
# spacesuits.gates = mainassembly.names + tower.names
# tower.gates = capsule.names + spacesuits.names

capsule.gates = [outsideCapsuleDoor,mainassembly]
dockingPort.gates = [outsideCapsuleDoor]
outsideCapsuleDoor.gates = [capsule,dockingPort]
# cape stuff
mainassembly.gates = [capsule, spacesuits]
spacesuits.gates = [mainassembly, outsidePad]
outsidePad.gates = [spacesuits, elevatorBay]
#tower.gates = [capsule, spacesuits]


game = Game(capsule) #TO ACCESS MONSTER FIGHT CHANGE "mainassembly" to "capsule!"




print("SELENE " + str(VERSION))

start_menu()

#basic starting senario
if game.currentArea == capsule:
    game.inventory.extend(["spacesuit", "toolbox", "id"])
    print("you are just about to your moon burn calculations that will put you in the moons orbit!")
    game.add_radio_notification("you see the \"incomming message\" light fire on your dashboard", "HOUSTON: we've detected a leak in one of the oxygen tubes out by the dock. please go out and fix it before you get ready for launch!")
    while not Game.gameOver:
        game.player_input()
        if Game.incorrectButtonPresses >= 2:
            print("your engines suddenly misfire and blow up your capsule. it's a sad day for spaceflight. :(")
            print("game over...")
            Game.gameOver = True
else:
    print(mainassembly.description)
    while not Game.gameOver:
        game.player_input()

