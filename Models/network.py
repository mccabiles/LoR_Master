import random
import urllib.request

# ios product development
API_KEY1 = '?api_key=' + 'RGAPI-693e34b0-9890-4591-a22d-36df07ccde53'
# ios new github release
API_KEY2 = '?api_key=' + 'RGAPI-5cfa0b1c-8d06-4d65-b9f7-3738e745fc7b'
# product github release
API_KEY3 = '?api_key=' + 'RGAPI-3dd1641a-6d80-458d-9fb5-357253d7674b'
# personal qq release
API_KEY4 = '?api_key=' + 'RGAPI-3b5bde16-66b4-4943-b8fa-241d27b29344'
# database release
API_KEY5 = '?api_key=' + 'RGAPI-3c0be235-cb0a-46de-8df8-d2381a330f94'

MATCH_KEY = '.api.riotgames.com/lor/match/v1/matches/by-puuid/'
DETAILS_KEY = '.api.riotgames.com/lor/match/v1/matches/'
NAME_KEY = '.api.riotgames.com/riot/account/v1/accounts/by-puuid/'
PUUID_KEY = '.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'

allKeys = [API_KEY1, API_KEY2, API_KEY3, API_KEY4, API_KEY5]
random.shuffle(allKeys)
API_KEY = allKeys[0]
aviliableKeys = []

def switchAPI():
    global aviliableKeys
    if not aviliableKeys:
        aviliableKeys = allKeys.copy()
    global API_KEY
    random.shuffle(aviliableKeys)
    API_KEY = aviliableKeys.pop()
    print('API CHANGED!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', API_KEY)

def getProxy():
    return urllib.request.getproxies()

class Network():
    def __init__(self, setting) -> None:
        self.setting = setting
        self.key = API_KEY
        return

    def getHeadLink(self):
        return 'https://' + self.setting.riotServer

    def getMatchesLink(self, ppid):
        return self.getHeadLink() + MATCH_KEY + ppid + '/ids' + API_KEY

    def getDetailsLink(self, matchId):
        return self.getHeadLink() + DETAILS_KEY + matchId + API_KEY

    def getNameLink(self, ppid):
        return self.getHeadLink() + NAME_KEY + ppid + API_KEY

    def getPUUID(self, name, tag):
        return self.getHeadLink() + PUUID_KEY + name + '/' + tag + API_KEY
