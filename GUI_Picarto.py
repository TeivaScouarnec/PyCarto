from pydoc import text
from unicodedata import name
import API_Picarto as picarto
import PySimpleGUI as sg
import yaml

##------------------------------------------------------------------------------------------------------##
##---------------------------------------Définitions----------------------------------------------------##
##------------------------------------------------------------------------------------------------------##

def getTokenUser():
    f = open('config.yaml','r')
    content = f.read()
    content_yaml = yaml.load(content,yaml.BaseLoader)
    return str(content_yaml['Token'])

def getAPI():
    f = open('config.yaml','r')
    content = f.read()
    content_yaml = yaml.load(content,yaml.BaseLoader)
    return str(content_yaml['API'])

def connectAPI(token,server):
    f = open('config.yaml','w')
    
    content = """
        Token : ""
        API : ""
    """

    contentYaml = yaml.load(content,yaml.BaseLoader)
    contentYaml['Token'] = token
    contentYaml['API'] = server
    f.write(yaml.dump(contentYaml))
    f.close()

##------------------------------------------------------------------------------------------------------##
##-------------------------------------------------GUI--------------------------------------------------##
##------------------------------------------------------------------------------------------------------##

def initFollowText():
    listFollow = picarto.initFollowers()
    text = ""

    for follow in listFollow:
        text += follow['time'] + " " + follow['name']+"\n"
    
    return text

def setFollowText(token,api):
    listFollow = picarto.UpdateFollowers(token,api)
    text = ""
    i = 0
    for follow in listFollow:
        if i > 5:
            text += follow['time'] + " " + follow['name']+"\n"
    return text

textFollow = initFollowText()

layout1 = [
    [[sg.Text("Your authorization:")],[sg.InputText(getTokenUser(),key='Token')]],
    [[sg.Text("API's Picarto:")],[sg.InputText(getAPI(),key='API')]],
    [sg.Button('Connect')],
    [sg.Text('Your Followers')],
    [sg.Text(initFollowText(),key='followers',)]
]

window = sg.Window(title="BotPicarto", layout=layout1 ,margins=(200,40) )

##------------------------------------------------------------------------------------------------------##
##-----------------------------------------Lancement du programme---------------------------------------##
##------------------------------------------------------------------------------------------------------##

while True:
    event, values = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Connect':
        connectAPI(values['Token'],values['API'])
        textFollow += setFollowText(values['Token'],values['API'])
        window['followers'].update(textFollow)