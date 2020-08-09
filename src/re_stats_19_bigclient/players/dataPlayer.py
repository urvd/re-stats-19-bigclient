import requests
from bs4 import  BeautifulSoup


# recupere le nom du joueur
# chercher le nom du joueur
# en tirer des infos
from src.re_stats_19_bigclient.ApiManagement.requests_api import CallsApi


class Player:
    PLAYER_LINK = 'https://one-versus-one.com/fr/joueurs/'

    def __init__(self, player_name):
        self.player_name = player_name
        # self.dataPlayer

    def htmlRequestResult(self):
        strLink = self.PLAYER_LINK + self.player_name;
        print('link: ' + strLink)
        req = requests.get(strLink).text
        scrap = BeautifulSoup(req)
        return scrap.prettify()

class PlayerData:
    def __init__(self,club_data, seasons):
        self._playerList = CallsApi().playersListCalls()

    @property
    def playerList(self):
        return self._playerList


class PlayerResponseData:

    def __init__(self, buts=0, tir_cadre=0, passes_des=0, passes=0, tacles=0):
        # Offensive
        self._buts = buts
        self._tir_cadre = tir_cadre
        self._passes_des = passes_des
        self._passes = passes
        # DECISIVE
        #self.tir_bloque = None
        self._tacles = tacles
        #self.duel_aerien = None
        #self.interception = None

    @property
    def buts(self):
        return self._buts

    @property
    def passes(self):
        return self._passes

    @property
    def passes_des(self):
        return self._passes_des

    @property
    def tir_cadre(self):
        return self._tir_cadre

    @property
    def tacles(self):
        return self._tacles

    @buts.setter
    def buts(self, buts):
        self._buts = buts

    @passes.setter
    def passes(self, passes):
        self._passes = passes

    @passes_des.setter
    def passes_des(self, passes_des):
        self._passes_des = passes_des

    @tir_cadre.setter
    def tir_cadre(self, tir_cadre):
        self._tir_cadre = tir_cadre

    @tacles.setter
    def tacles(self, tacles):
        self._tacles = tacles

