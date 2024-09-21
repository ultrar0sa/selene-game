class Area:
    # names = []
    # description = ""
    # gates = []  #list of avalible areas accessible from this area.
    # flags = []  #list of dictionaries with the key being the flag name and the value being a boolean or other value.
    def __init__(self, name, description, gates, flags):
        self.names = name
        self.description = description
        self.gates = gates #list of avalible areas accessible from this area.
        self.flags = flags #list of dictionaries with the key being the flag name and the value being a boolean or other value.
