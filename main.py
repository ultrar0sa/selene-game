# i am making this out of spite
#import routines.accessories
#import routines.actions
import routines.actions
import routines.targets
from game import Game
from area import Area
VERSION = "1.0"


#basic start menu
def start_menu(game):
    print("1.about\n2.instructions\n3.play game\n4.load game\n5.exit")
    match input("input: "):
        case "1":
            print("SELENE is a moon mission over text. \nIt is created by Vicky Yang, Jade Lukken, and David Foster for CS 1612 at the University of Minnesota Duluth")
            start_menu(game)
        case "2":
            print("When prompted, type commands into the console and press ENTER.")
            print("here's a list of all of the commands and roughly what they do:\npush (used to push buttons)\npress (used to push buttons)\npull (used to pull things)\nradio (used to respond to base (make sure to use it whenever you radio light goes off))\nfix (used to fix things, most commonly with tools)\nmove (used to move to different locations)\nlaunch (launches various phases of the mission (liftoff, burn for the moon))\nmap (prints of the area in the map window, if you are confused on where to go, try this!)\ntake (used to add things to your inventory)\ninventory (used to view your inventory)\nget (used to add things to your inventory)\ndrive (used to get and then move the rover on the moon)\ninfo (gives you info on the current area)\nwait (used to wait for a period of time. if nothing is happening in the capsule, try waiting!)\nlook (look at various things in your inventory)\nsave (used to save the game)\nload (used to load the game)\nexit (used to exit the game)")
            print("further instructions can be found at https://github.com/ultrar0sa/selene-game")
            start_menu(game)
        case "3":
            return
        case "4":
            routines.actions.load(game)
            return
        case "5":
            Game.gameOver = True
            return
        case _:
            print("input a correct input")
            start_menu(game)



        
   
#driver code
from routines.targets import button
oxygenTubeFixed = False
launchReady = False
orbitCorrectionsDone = False

#BUTTON_DICT = {"jdry" : button, "uo13" : button, "vk88" : button, "jn34" : button, "wz81" : button, "vo29" : button, "fk73" : button, "kj22" : button, "mo11" : button, "we64" : button, "lq12" : button, "ii43" : button, "js01" : button, "cf04" : button, "sz24" : button, "ez59" : button, "n57x" : button, "msy4" : button, "aym1" : button, "0frz" : button, "dyjj" : button, "jv71" : button, "4lhm" : button, "fdcx" : button, "ut9c" : button, "8rsl" : button, "ra78" : button, "jmn8" : button, "rwb5" : button, "xuu6" : button, "sgub" : button, "awpz" : button, "rrdz" : button, "mdna" : button, "wa03" : button, "ut13" : button, "zo51" : button, "ef57" : button, "uj34" : button, "su33" : button}
BUTTON_DICT = {"button" : button}
#start sequence
mainassembly = Area(["main room", "main assembly", "start"], "This is the main assembly room. You need to get you ID Passes before you can do anything. They are on the table at the far end of the hall.", [], mapPath="savedshapes/capemap.json")
spacesuits = Area(["spacesuit", "suit"], "This is the spacesuit room. People are gathered to help you put on your space suit.",  [], mapPath="savedshapes/capemap.json")

#pad sequence
tower = Area(["tower", "pad"], "this is tower", [], mapPath="savedshapes/towermap.json")
outsidePad = Area(["outside", "outside pad"], "You are outside the main pad. It's time to the [elevator bay] in order to head up the tower and get in the capsule!", [], mapPath="savedshapes/towermap.json")
elevatorBay = Area(["bay"], "You are in the elevator bay. Time to head up and move into the [capsule]!", [], mapPath="savedshapes/towermap.json")

#moon burn sequence
capsule = Area(["capsule", "inside"], "You're inside the capsule, and everything's ready. You just need to say [launch]. There's a toolbox hidden in some cabinet, along with plenty of space snacks.", [], {"launchReady" : launchReady, "orbitCorrectionsDone" : orbitCorrectionsDone}, mapPath="savedshapes/capsulemap.json")
dockingPort = Area(["docking port", "dock"], "you are next to the [docking port], out in space. the broken oxygen tube is right in front of you.", [], {"fixed" : Game.oxygenTubeFixed}, mapPath="savedshapes/capsulemap.json")
outsideCapsuleDoor = Area(["outside capsule door", "outside", "spacewalk", "space", "capsule door"], "you are out in space next to the [capsule door]. the broken oxygen tube is right next to the [docking port]", [], mapPath="savedshapes/capsulemap.json")
 
#moon crater
landingSite = Area(["outside","site"], "this where you landed. your [rover] has detached from your capsule and is ready to [ride]", [], mapPath="savedshapes/cratermap.json")
craterEdge = Area(["edge"], "this is the edge of the crater you landed in. your end goal is in sight, but is still across a vast and unknown plain.", [], mapPath="savedshapes/cratermap.json")
moonPlain = Area(["plain"], "you are in the land of unknowns now. tranquility awaits. [apollo] awaits", [], mapPath="savedshapes/moonmap.json")
apolloEnding = Area(["apollo", "tranqulity"], "one small step", [], mapPath="savedshapes/apollo.json")
capsule.avaliable_targets = BUTTON_DICT 
dockingPort.avaliable_targets = {}
# capsule.gates = outsideCapsuleDoor.names + mainassembly.names + tower.names
# dockingPort.gates = outsideCapsuleDoor.names
# outsideCapsuleDoor.gates = capsule.names + dockingPort.names
# # cape stuff
# mainassembly.gates = capsule.names + tower.names + spacesuits.names
# spacesuits.gates = mainassembly.names + tower.names
# tower.gates = capsule.names + spacesuits.names

capsule.gates = [outsideCapsuleDoor]
dockingPort.gates = [outsideCapsuleDoor]
outsideCapsuleDoor.gates = [capsule,dockingPort]
# cape stuff
mainassembly.gates = [capsule, spacesuits]
spacesuits.gates = [mainassembly, outsidePad]
outsidePad.gates = [spacesuits, elevatorBay]
elevatorBay.gates = [capsule]
#tower.gates = [capsule, spacesuits]
landingSite.gates = [craterEdge]
craterEdge.gates = [moonPlain]
moonPlain.gates = [apolloEnding]

AREA_LIST = [mainassembly, spacesuits, tower, outsidePad, elevatorBay, capsule, outsideCapsuleDoor, dockingPort, landingSite, craterEdge, moonPlain, apolloEnding]

game = Game(mainassembly) #TO ACCESS MONSTER FIGHT CHANGE "mainassembly" to "capsule!"

Game.AREA_LIST = AREA_LIST


print("SELENE " + str(VERSION))

start_menu(game)

#basic starting senario
# if game.currentArea == capsule:
#     game.inventory.extend(["spacesuit", "toolbox", "id"])
#     print("you are just about to your moon burn calculations that will put you in the moons orbit!")
#     game.add_radio_notification("you see the \"incomming message\" light fire on your dashboard", "HOUSTON: we've detected a leak in one of the oxygen tubes out by the dock. please go out and fix it before you get ready for launch!")
#     while not Game.gameOver:
#         game.player_input()
#         if Game.incorrectButtonPresses >= 2:
#             print("your engines suddenly misfire and blow up your capsule. it's a sad day for spaceflight. :(")
#             print("game over...")
#             Game.gameOver = True
routines.actions.info(game)
while not Game.gameOver: #bodges on top of bodges until the whole thing is made out of duck tape and hope. fuck the haters.
    if game.gameState == "landed" and landingSite not in capsule.gates:
        capsule.gates.remove(outsideCapsuleDoor)
        capsule.gates.append(landingSite)
    game.player_input()

if game.gameState == "victory":
    print("THANKS FOR PLAYING SELENE")

input("press enter to leave: ")