import routines.accessories
import routines.actions
import routines.targets
import re

class Game:
    correctButtonPresses = 0
    incorrectButtonPresses = 0
    gameOver = False
    VALID_PLAYER_ACTIONS = {"push" : routines.actions.push, "pull" : routines.actions.pull, "look" : routines.actions.look, "radio" : routines.actions.radio, "fix" : routines.actions.fix, "move" : routines.actions.move, "launch" : routines.actions.launch, "map"  : routines.actions.map}
    VALID_TARGET_OBJECTS = {}
    VALID_ACCESSORY_OBJECTS = {"hammer" : routines.accessories.hammer, "fist" : routines.accessories.fist, "toolbox" : routines.accessories.toolbox, "tools" : routines.accessories.toolbox}
    AREA_DICT = {}
    MAP_DICT = {}
    from maps import Maps
    map = Maps()

    
    
    def __init__(self, currentArea):

        self.currentArea = currentArea
        self.radioNotification = ""
        self.radioContent = ""
        self.reset_input()
    
    def add_radio_notification(self, radioNotification, radioContent):
        self.radioNotification = radioNotification
        self.radioContent = radioContent
        print(radioNotification)
    
    def reset_input(self):
        self.playerAction = ""
        self.playerAccessoryObject = ""
        self.playerTargetObject = "" 
        self.desiredArea = "" 
        self.handleSkip = False
    def check_flags(self):
        try:
            if self.currentArea.flags["needFixed"] == True:
                self.add_radio_notification("the radio light fires on your spacesuit", "ok, now you are ready to start entering the proper details. the first button is vk88 and the second is wz81. then you should be ready to fire engines")
        except KeyError:
            pass
        
    def player_input(self, descriptionString=""):
        while True:
            self.check_flags()
            self.reset_input()
            if descriptionString != "":
                print(descriptionString)
            #cleaning up the input string
            inputString = input("enter command: ")
            inputString = inputString.lower()
            inputList = inputString.split()
            if len(inputList) == 0:
                print("try again.")
                continue
        
            Game.VALID_TARGET_OBJECTS = self.currentArea.avaliable_targets
            #main input parser, runs through each word in the command with each list of commands to see if it matches any of the valid words.
            for index in Game.VALID_PLAYER_ACTIONS:
                #print("parsing: " +  index)
                p = re.compile(index)
                m = p.search(inputString)
                #print(index + " " + str(m))
                if m:  
                    self.playerAction = index
            for index in Game.VALID_TARGET_OBJECTS:
                #print("parsing: " +  index)
                p = re.compile(index)
                m = p.search(inputString)
                #print(index + " " + str(m))
                if m:  
                    self.playerTargetObject = index
                    #print("found target object: " + index)
            for index in Game.VALID_ACCESSORY_OBJECTS:
                #print("parsing: " +  index)
                p = re.compile(index)
                m = p.search(inputString)
                if m:  
                    self.playerAccessoryObject = index
            for index in Game.AREA_DICT:
                p = re.compile(index)
                m = p.search(inputString)
                #print(index + " " + str(m))
                if m:
                    self.desiredArea = index
                     
            #if no action taken player is reprompted
            if self.playerAction == "":
                print("try again.")
                self.reset_input()
                continue
            
            if self.playerTargetObject == "":
                self.playerTargetObject = False
            if self.playerAccessoryObject == "":
                self.playerAccessoryObject = False
            if self.playerAccessoryObject != False:
                Game.VALID_ACCESSORY_OBJECTS[self.playerAccessoryObject](self)
            if not self.handleSkip and self.playerTargetObject != False:
                Game.VALID_TARGET_OBJECTS[self.playerTargetObject](self)
            if not self.handleSkip:
                Game.VALID_PLAYER_ACTIONS[self.playerAction](self)
            break
   