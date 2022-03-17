from fileinput import close
from importlib.abc import Loader
import os
from time import sleep
import API_Picarto as picarto
import yaml

##------------------------------------------------------------------------------------------------------##
##---------------------------------------Définitions----------------------------------------------------##
##------------------------------------------------------------------------------------------------------##

def getTokenUser():
    f = open('config.yaml','r')
    content = f.read()
    content_yaml = yaml.load(content,yaml.BaseLoader)
    Token = content_yaml['Token']
    return str(Token)

def getAPI():
    f = open('config.yaml','r')
    content = f.read()
    content_yaml = yaml.load(content,yaml.BaseLoader)
    APIID = content_yaml['API']
    return str(APIID)

def getDelay():
    f = open('config.yaml','r')
    content = f.read()
    content_yaml = yaml.load(content,yaml.BaseLoader)
    DELAYtime = content_yaml['Delay']
    return str(DELAYtime)

def getSound():
    f = open('config.yaml','r')
    content = f.read()
    content_yaml = yaml.load(content,yaml.BaseLoader)
    sound = content_yaml['Sound']
    return str(sound)

def init():
    if (os.path.exists("config.yaml") == False):
        f = open('config.yaml',"x")
        document = {
            'API' : 'https://api.picarto.tv/api/v1/user/followers',
            'Token' : '',
            'Delay' : '60',
            'Sound' : ''
        }
        yaml.dump(document,f)
        f.close()

    if (os.path.exists("lastFollower.txt") == False):
        f = open("lastFollower.txt",'x')
        f.close()

##------------------------------------------------------------------------------------------------------##
##-----------------------------------------Lancement du programme---------------------------------------##
##------------------------------------------------------------------------------------------------------##

def start():
    init()
    API : str = getAPI()
    Token : str = getTokenUser()
    DELAY = getDelay()
    Sound : str = getSound()

    if (DELAY.isnumeric() == False) or (DELAY.isnumeric() == "") or (DELAY.isnumeric() == None):
        print("[Script] Error! Please, check your delay in the config.yaml file.\n")
        input("Press enter to exit the program.")
        exit()
    elif getAPI() == None or getAPI() =="":
        print("[Script] Error! Please, check the URL of your API in the config.yaml file.\n")
        input("Press enter to exit the program.")
        exit()
    elif getTokenUser() == None or getTokenUser() =="":
        print("[Script] Error! Please, check your authorization's token in the config.yaml file.\n")
        input("Press enter to exit the program.")
        exit()
    else:
        run(API,Token,int(DELAY),Sound)

def run(API,Token,Delay,Sound):
    fileSound = Sound

    if picarto.UpdateSound(Sound) == False:
        fileSound = ''

    while True:
        clear = lambda: os.system('cls')
        clear()
        print(picarto.UpdateFollowers(Token,API,fileSound))
        sleep(Delay)
start()