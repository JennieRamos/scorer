class Score(object):
    def __init__(self ,team_name, score, new_score ):
        self.score = score
        self.team_name = team_name
        self.new_score = 0

class Team(object):
    def __init__(self):
        self.team1 = {}
        self.team2 = {}

    def  add_team1(self, team_name, score):
    	self.team1[team_name.team_name] = new_score

    def  add_team2(self, team_name, score):
        self.team2[team_name.team_name] = new_score
        
    def add_score(self, team_name, score):
        self.new_score = new_score + score
  
    def get_score(self, team_name):
    	return self.teams.get(team-name)
        