import json


class ClubData:
    def __init__(self, leagueData):
        self.leagueType = leagueData
        result = json.loads(open(self.leagueType['file']).read())
        self.data = result['api']

    def getListTeams(self):
        return self.data["teams"]


    def getTeam(self, teamsCode):
        teams = self.data["teams"]
        for team in teams:
            if(teamsCode == team['id']):
                return team

        return None


    def getTeamsByName(self, teamsName):
        teams = self.data["teams"]
        for team in teams:
            if (teamsName == team['name']):
                return team

        return None