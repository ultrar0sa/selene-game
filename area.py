class Area:
    # names = []
    # description = ""
    # gates = []  #list of avalible areas accessible from this area.
    # flags = {}  dictionaries with the key being the flag name and the value being a boolean or other value.
    # avaliable_targets = {} dict, key the name of the target allowed, and the value being the target function needed to be run.
    def __init__(self, name, description, gates, flags = {}, avaliable_targets = {}, mapPath=""):
        self.mapPath = mapPath
        self.names = name
        self.description = description
        self.gates = gates #list of avalible area names accessible from this area.
        self.flags = flags #dictionary with the key being the flag name and the value being a boolean or other value.
        self.avaliable_targets = avaliable_targets
        # print(self.flags)
    
