import time
import Main.API_Picarto as picarto
import PySimpleGUI as sg
import yaml

##------------------------------------------------------------------------------------------------------##
##---------------------------------------Définitions----------------------------------------------------##
##------------------------------------------------------------------------------------------------------##

def getTokenUser():
    f = open('Main\config.yaml','r')
    content = f.read()
    content_yaml = yaml.load(content,yaml.BaseLoader)
    return str(content_yaml['Token'])

def getAPI():
    f = open('Main\config.yaml','r')
    content = f.read()
    content_yaml = yaml.load(content,yaml.BaseLoader)
    return str(content_yaml['API'])

def connectAPI(token,server):
    f = open('Main\config.yaml','w')
    
    content = """
        Token : ""
        API : ""
    """

    contentYaml = yaml.load(content,yaml.BaseLoader)
    contentYaml['Token'] = token
    contentYaml['API'] = server
    f.write(yaml.dump(contentYaml))
    f.close()

def getCurrentTime():
    ArrayTime = time.localtime()
    currentTime = str(ArrayTime[3])+ ":"+ str(ArrayTime[4])
    return currentTime


##------------------------------------------------------------------------------------------------------##
##-------------------------------------------------GUI--------------------------------------------------##
##------------------------------------------------------------------------------------------------------##

def initFollowText():
    listFollow = picarto.initFollowers()
    text = ""

    i = 0

    for follow in listFollow:
        if (i < 5):
            text += follow['name']+"\n"
            i+=1
    return text

def setFollowText(token,api):
    listFollow = picarto.UpdateFollowers(token,api)
    text = ""

    if listFollow == None:
        print("[Picarto] Don't get data in server!")
        return text
    
    i = 0

    for follow in listFollow:
        if i < 5:
            text += follow['name']+"\n"
            i+=1
    return text

textFollow = initFollowText()

layout1 = [
    [[sg.Text("Your authorization:")],[sg.InputText(getTokenUser(),key='Token')]],
    [[sg.Text("API's Picarto: (don't change but if you are sure)")],[sg.InputText(getAPI(),key='API')]],
    [sg.Button('Connect'),sg.Button('stop')],
    [sg.Text('_'*30)],
    [sg.Text('delay refresh: '),sg.Input('60',key='delay'),sg.Text('sec')],
    [sg.Text('_'*30)],
    [sg.Text('Your Followers')],
    [sg.Text("( Last update:"), sg.Text(getCurrentTime(),key='time'),sg.Text("Running: "),sg.Text('Off',key='running'),sg.Text(')')],
    [sg.Text(initFollowText(),key='followers',)]
]

window = sg.Window(title="PicartoFollowers", layout=layout1 ,margins=(200,40) )

##------------------------------------------------------------------------------------------------------##
##-----------------------------------------Lancement du programme---------------------------------------##
##------------------------------------------------------------------------------------------------------##

IsConnected = False
delay = 0

def ConnectToServer():
    connectAPI(values['Token'],values['API'])
    textFollow = setFollowText(values['Token'],values['API'])
    window['followers'].update(textFollow)
    window['time'].update(getCurrentTime())

while True:
    event, values = window.read(timeout=1000)

    if event == sg.WIN_CLOSED:
        IsConnected = False
        break
    
    elif event == 'stop':
        IsConnected = False
        window['running'].update('Off')

    elif event == 'Connect':
        if (values['Token'] == "") or (values['API'] == "") :
            sg.Popup("Please fill in all fields!")
        
        try:
            delay = int(values['delay']) * 1000
        except ValueError:
            sg.Popup("The delay is not a number!")

        IsConnected = True
        window['running'].update('On')

    if IsConnected:
        ConnectToServer()
        window.read(timeout=delay)
