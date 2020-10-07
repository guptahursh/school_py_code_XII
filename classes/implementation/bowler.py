class Bowler:
    def __init__(self,f_name,l_name):
        self.firstName = f_name
        self.lastName = l_name
        self.oversBowled = 0
        self.no_Maiden = 0
        self.lastOverRuns = 0
        self.runsGiven = 0
        self.wicketsTaken = 0

    def bowling(self):
        print("inputs:[Runs]/ W(wide)/ Wkt(wicket)/ N(no_ball)")
        Opt = {"Wkt":self.wicket,"W":self.wideOrNo,"N":self.wideOrNo}
        i = 1
        self.lastOverRuns = 0
        while i < 7:
            x = input(str(i)+" : ")
            if x in Opt:
                i += Opt[x]()
            else:
                try:
                    self.lastOverRuns += int(x)
                except:
                    print('invalid input: re-enter')
                    continue
            i += 1
        if self.lastOverRuns == 0:
            self.no_Maiden += 1
        self.runsGiven += self.lastOverRuns
        self.oversBowled += 1

    def wicket(self):
        self.wicketsTaken += 1
        return 0

    def wideOrNo(self):
        self.lastOverRuns += 1
        return -1

    def showInfo(self):
        print(f"""
        Name:\t\t {self.firstName} {self.lastName}
        Overs Bowled:\t\t {self.oversBowled}
        No. of Maidens:\t\t {self.no_Maiden}
        No. of runs given:\t {self.runsGiven}
        No. of wickets taken:\t {self.wicketsTaken}
        """)

Jack = Bowler("Jack","Smith")









