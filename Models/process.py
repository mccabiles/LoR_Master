import psutil
import constants as c
import sentry_sdk
import locale
import requests
import datetime
import json

sysLanguage = locale.getdefaultlocale()[0]

def getLogPath():
    logFilePath = None
    for proc in psutil.process_iter():
        try:
            if proc.name() == u"LoR.exe":
                logFilePath = proc.cmdline()[4]
        except psutil.AccessDenied:
            print("Permission error or access denied on process")
            return None
        except Exception as e:
            print('getLogPath error: ', e)
            return None
    return logFilePath


def readLog(setting):
    path = getLogPath()
    if path is None:
        setting.isLorRunning = False
    else:
        setting.isLorRunning = True
        try:
            with open(path, 'r', encoding='utf-8') as lorLog:
                for line in lorLog.readlines():
                    line = line.strip()
                    if '[TrySetShardDnsLive] setting dns data by affinity' in line:
                        setting.riotServer = str(line).split().pop()
                    if 'Server opened successfully at port: ' in line:
                        setting.port = str(line).split().pop()
                    if 'Using user-preferred language CultureInfo of ' in line:
                        setting.language = str(line).split().pop()
                    if '[CheckingForUpdates] StartCheckingForUpdates for user ' in line:
                        playerId = str(line).split("[CheckingForUpdates] StartCheckingForUpdates for user ", 1)[1]
                        if playerId != setting.playerId:
                            setting.playerId = playerId
                            sentry_sdk.set_user({"id": playerId, "username": playerId + ' ' + setting.riotServer, "ip_address": "{{auto}}"})
                            sentry_sdk.set_context("info", {"version": c.VERSION_NUM, "riotLanguage": setting.language, "sysLanguage": sysLanguage})
                            sentry_sdk.capture_message(
                                playerId + ' ' + setting.riotServer)
                            try:
                                data = {}
                                data['riot_id'] = setting.playerId
                                data['server'] = setting.riotServer
                                data['riot_language'] = setting.language
                                data['sys_language'] = sysLanguage
                                url = "https://lmttest.herokuapp.com/login"
                                headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                                response = requests.post(url, data=json.dumps(data), headers=headers)
                                print(response.text)
                            except requests.exceptions.HTTPError as e:
                                print('post error', e.response.text)
        except IOError:
            print('log file not accessible: ', path)
        except Exception as e:
            print('readLog error', e)


def isSimulation():
    isPython = True
    try:
        for proc in psutil.process_iter():
            try:
                if proc.name() == u"LoRMasterTracker.exe":
                    isPython = False
                if proc.name() == u"python.exe":
                    isPython = True
            except psutil.AccessDenied:
                print("Permission error or access denied on process")
                return isPython
            except IndexError as e:
                print('runElectron IndexError: ', e)
                return isPython
    except Exception as e:
        print('runElectron error:', e)
        return isPython
    print('isSimulation: ', isPython)
    return isPython
