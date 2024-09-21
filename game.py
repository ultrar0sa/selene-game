import routines.accessories
import routines.actions
import routines.targets
import re

class Game:
    correctButtonPresses = 0
    incorrectButtonPresses = 0
    gameOver = False
    VALID_PLAYER_ACTIONS = {"push" : routines.actions.push, "pull" : routines.actions.pull, "look" : routines.actions.look, "move" : routines.actions.move, "launch" : routines.actions.launch}
    VALID_TARGET_OBJECTS = {}
    VALID_ACCESSORY_OBJECTS = {"hammer" : routines.accessories.hammer, "fist" : routines.accessories.fist}
    AREA_DICT = {}
    
    
    def __init__(self, currentArea):
        self.currentArea = currentArea
        self.reset_input()
      
    def reset_input(self):
        self.playerAction = ""
        self.playerAccessoryObject = ""
        self.playerTargetObject = "" 
        self.desiredArea = "" 
        self.handleSkip = False
    
    def player_input(self, descriptionString):
        while True:
            self.reset_input()
            print(descriptionString)
            #cleaning up the input string
            inputString = input("enter command: ")
            inputString = inputString.lower()
            inputList = inputString.split()
            if len(inputList) == 0:
                print("try again.")
                continue
        
            useOldParser = False
            #main input parser, runs through each word in the command with each list of commands to see if it matches any of the valid words.
            if useOldParser:
                for word in inputList:
                    print("parsing: " +  word)# i hate this, horrible. 
                    for index in Game.VALID_PLAYER_ACTIONS: 
                        if index == word and self.playerAction == "":
                            self.playerAction = word
                    for index in Game.VALID_TARGET_OBJECTS:
                        if index == word and self.playerTargetObject == "":
                            print("found: " + index)
                            self.playerTargetObject = word
                    for index in Game.VALID_ACCESSORY_OBJECTS:
                        if index == word and self.playerAccessoryObject == "":
                            self.playerAccessoryObject = word    
            else:
                for index in Game.VALID_PLAYER_ACTIONS:
                    #print("parsing: " +  index)
                    p = re.compile(index)
                    m = p.search(inputString)
                    print(index + " " + str(m))
                    if m:  
                        self.playerAction = index
                for index in Game.VALID_TARGET_OBJECTS:
                    #print("parsing: " +  index)
                    p = re.compile(index)
                    m = p.search(inputString)
                    #print(index + " " + str(m))
                    if m:  
                        self.playerTargetObject = index
                        print("found target object: " + index)
                for index in Game.VALID_ACCESSORY_OBJECTS:
                    #print("parsing: " +  index)
                    p = re.compile(index)
                    m = p.search(inputString)
                    if m:  
                        self.playerAccessoryObject = index
                for index in Game.AREA_DICT:
                    p = re.compile(index)
                    m = p.search(inputString)
                    print(index + " " + str(m))
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