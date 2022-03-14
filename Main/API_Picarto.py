import json
import certifi
import urllib3

#---||| Ré-édite le fichier data.json |||---#
def SetFileData(jsonFile):
    if jsonFile == None:
        return

    #---| Ouvre (ou créer) un nouveau fichier et le réécris |---#
    f = open("Main\data.json",'w')
    f.write("")
    f.write(json.dumps(jsonFile))
    f.close()

#---||| Obtient les "followers" grâce à l'API de Picarto |||---#
def getFollowers(token,API):

    #---| Autoriser les certifications et les cookies pour le site Internet |---#
    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where()
    )

    #---| Envois une requête pour récuperer les données sous formats JSON |---#
    try:
       r = http.request('get', str(API), headers={
           'Accept' : 'application/json',
           'Authorization' : 'Bearer ' + str(token),
           })
    except urllib3.exceptions.HTTPError:
        print("[Picarto] HTTPError")
        return 
    except ValueError:
        print("[Picarto] ValueError")
        return 
    print("[Picarto] Statut request: "+ str(r.status))
    
    if (r.status == 200):
        return(str(r.data.decode('utf-8')))
    else:
        return

#---||| Mets à jour les "followers" grâce au data.json |||---#
def UpdateFollowers(token,API):
    
    followers = []

    #---| Ouvre le data.json |---#
    with open('Main\data.json') as json_file:
        try:
            data=json.load(json_file)
        except ValueError:
            data = []

    try:
        getData = getFollowers(token,API)
    except None:
        print ("[Picarto] None Data!")
        return

    #---| Charge la base de données depuis le serveur Picarto |---#
    try:
        newData = json.loads(getData)
    except ValueError:
        print("[Picarto] ValueError! Don't load file data")
        return
    except TypeError:
        print("[Picarto] TypeError! Don't load file data")
        return

    #---| Compare le fichier data et la BDD de Picarto |---#
    for follower in newData:
        followers.append(follower['name'])
    followers.reverse()
    #---| Mets à jour le fichier data.json et retourne les nouveaux followers |---#
    SetFileData(newData)
    return showFollowers(followers)

#---||| Montre les "followers" |||---#
def showFollowers(text):
    textFollowers = []
    
    for follower in text:
        textFollowers.append ({
                'name': follower,
                })
    print (textFollowers)
    return textFollowers

#---||| Initialise les "followers" |||---#
def initFollowers():
    with open('Main\data.json') as json_file:
        try:
            data=json.load(json_file)
        except ValueError:
            data=[]

    nbsfollow = 0
    textFollowers = []
    dataReverse = []

    for follower in data:
        dataReverse.append ({
            'name': str(follower['name']),
        })
    dataReverse.reverse()

    for follower in dataReverse:
            textFollowers.append(follower)

    return textFollowers
