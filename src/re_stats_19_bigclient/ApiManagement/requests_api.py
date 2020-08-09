import requests


class CallsApi:
    API_FOOTBALL_CALL = "https://api-football-v1.p.rapidapi.com/v2/"
    API_FOOTBALL_HEADERS = {'x-rapidapi-host': 'api-football-v1.p.rapidapi.com',
                            'x-rapidapi-key': '35203f6d9dmshbd9b33f83d7343bp122468jsn3246bca289a7'}
    def playersListCalls(self, season, club_id):
        return requests.request(
            'GET',
            url=self.API_FOOTBALL_CALL + "/players/squad/" + club_id + "/" + season,
            headers=self.API_FOOTBALL_HEADERS).json()
