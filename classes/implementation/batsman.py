class Batsman:
    def __init__(self,f_name,l_name):
        self.firstName = f_name
        self.lastName = l_name
        self.runsMade = 0
        self.fours = 0
        self.sixers = 0

    def batting(self):
        # fill it in the future
        pass

    def hit(self,run):
        if run == 4:
            self.fours += 1
        elif run == 6:
            self.sixers += 1
        self.runsMade += run




