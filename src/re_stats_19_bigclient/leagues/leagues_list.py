#league type
PREMIER_LEAGUE = { 'API_FOOTBALL_ID': 524, 'code': "GB", 'file': 'ressources/premier-league.json'}
LIGUE_1 = {'API_FOOTBALL_ID': 525, 'code': "FR", 'file': 'ressources/ligue1.json'}
LIGA = {'API_FOOTBALL_ID': 525, 'code': "FR", 'file': 'ressources/liga.json'}
BUNDESLIGA = {'API_FOOTBALL_ID': 525, 'code': "FR", 'file': 'ressources/bundesliga1.json'}
SERIE_A= {'API_FOOTBALL_ID': 525, 'code': "FR", 'file': 'ressources/serieA.json'}


class LeagueData:

    def init(self, type):
        self._leagueData = type

    @property
    def leagueData(self):
        return  self._leagueData