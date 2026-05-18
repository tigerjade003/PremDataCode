import pandas as pd

years = [1996, 2019, 2023]

class Team:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.GF = 0
        self.GA = 0
        self.points = 0
        self.position = 0
    def __str__(self):
        return f"{self.name} - {self.points} points - Position: {self.position}"
    
def generate_teams(year, data):
    teams = {}
    
    for _, row in data.iterrows():
        HomeTeam = row['HomeTeam']
        AwayTeam = row['AwayTeam']
        
        if HomeTeam not in teams:
            teams[HomeTeam] = Team(HomeTeam, year)
        if AwayTeam not in teams:        
            teams[AwayTeam] = Team(AwayTeam, year)
    return teams

def rank_teams(teams):
    sorted_teams = sorted(
        teams.values(),
        key=lambda t: (-t.points, -(t.GF - t.GA), t.name)
    )
    for i, team in enumerate(sorted_teams):
        team.position = i + 1

def generatetable(teams, data):
    higherupwin = 0
    drawcount = 0
    lowerwin = 0
    for idx, row in data.iterrows():
        HomeTeam = row['HomeTeam']
        AwayTeam = row['AwayTeam']
        HG = row['FTHG']
        AG = row['FTAG']  
        Result = row['FTR']
        rank_teams(teams)
        HomeRank = teams[HomeTeam].position
        AwayRank = teams[AwayTeam].position
        """
        print(HomeRank)
        print(AwayRank)
        print(Result)
        """
        teams[HomeTeam].GF += HG
        teams[HomeTeam].GA += AG
        teams[AwayTeam].GF += AG
        teams[AwayTeam].GA += HG  
        if Result == 'H':
            teams[HomeTeam].points += 3
            if HomeRank < AwayRank:
                higherupwin += 1
            else:
                lowerwin += 1
        elif Result == 'A':
            teams[AwayTeam].points += 3
            if AwayRank < HomeRank:
                higherupwin += 1
            else:
                lowerwin += 1
        else:
            teams[HomeTeam].points += 1
            teams[AwayTeam].points += 1
            drawcount += 1
    print(higherupwin)
    print(drawcount)
    print(lowerwin)

data1997 = pd.read_csv('prem1997.csv')
data2019 = pd.read_csv('prem2019.csv')
data2023 = pd.read_csv('prem2023.csv')
teams1997 = generate_teams(1997, data1997)
teams2019 = generate_teams(2019, data2019)
teams2023 = generate_teams(2023, data2023)
print("1997:")
generatetable(teams1997, data1997)
print("2019:")
generatetable(teams2019, data2019)
print("2023:")
generatetable(teams2023, data2023)
