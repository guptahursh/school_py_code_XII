from datetime import datetime
import random
class Match:
    def __init__(self,team1,team2,**kwargs):
        self.location = kwargs[loc]
        self.time = datetime.now().strftime("%D|%H:%M:%S")
        self.innings = 0
        self.overs = kwargs['overs'] # 
        self.inning_running = 0
        self.over_running = 0
        if 'innings' in kwargs:
            self.no_of_innings = kwargs['innings']
        else:
            self.no_of_innings = 2
        self.teams = (team1,team2) # objects of teams

    def start(self):
        self.inning_running += 1
        x = self.toss()
        if self.teams[x].choice() == 'bat':
            y = [teams[x],teams[x-1]]
        else:
            y = [teams[x-1],teams[x]]
        while self.inning_running <= self.no_of_innings:
            self.start_innings(y) # batting and bowling
            y[0],y[1] = y[1],y[0]
            self.inning_running += 1

    def toss(self):
        return random.choice([0,1])

    def start_innings(self,batting_team,bowling_team):
        pass









