import json
from logging import error
from pygame import mixer
import certifi
import pygame
import urllib3

hasSound = False

#---||| Ré-édite le fichier data.json |||---#
def SetLastFollower(text1):
    #---| Ouvre (ou créer) un nouveau fichier et le réécris |---#
    f = open("lastFollower.txt",'w')
    f.write(text1)
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

def UpdateSound(sound):
    if sound == "" or sound == None:
        print ("[Script] No sound found! please, check your path in the config.yaml")
        return False

    playerSound = mixer
    playerSound.init()

    try:
        playerSound.music.load(sound)
    except pygame.error:
        print ("[Script] No sound found! please, check your path in the config.yaml")
        return False
    else:
        return True

#---||| Mets à jour les "followers" grâce au data.json |||---#
def UpdateFollowers(token,API,sound):
    
    getData = getFollowers(token,API)

    #---| Charge la base de données depuis le serveur Picarto |---#
    try:
        Data = json.loads(getData)
    except ValueError:
        print("[Picarto] ValueError! Don't load file data")
        return
    except TypeError:
        print("[Picarto] TypeError! Don't load file data")
        return
    
    #---| Récupère le dernier follower |---#
    followers = []

    for follower in Data:
        followers.append(follower['name'])

    followers.reverse()

    #---| Vérifies si c'est un nouveau follower|---#
    LastFollower = str(followers[0])
    f = open("lastFollower.txt",'r')
    currentLastFollower = f.read()
    
    if currentLastFollower != LastFollower:
        playerSound = mixer
        playerSound.init()
        try:
            playerSound.music.load(sound)
        except pygame.error:
            pass
        else:
            playerSound.music.play()

    #---| Mets à jour le fichier et retourne les nouveaux followers |---#
    SetLastFollower(LastFollower)
    return LastFollower



