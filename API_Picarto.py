from ast import Str
import json
from logging import error
import os
from pydoc import text
from webbrowser import get
from pygame import mixer
import certifi
import pygame
import urllib3

hasSound = False

#---||| Rajoutes les derniers followers sur le fichier texte |||---#
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
    
    #---| Récupère les valeurs avec l'API Picarto |---#
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

    #---| Génère un nouveau fichier followers.json |---#
    try:
        fileJson = open("followers.json","r")
    except OSError:
        fileJson = open("followers.json","w")
        fileJson.write(getData)

    if (fileJson.read()=="" or fileJson.read()==None):
        fileJson = open("followers.json","w")
        fileJson.write(getData)
        fileJson.close()

    
    #---| Récupère les derniers followers |---#
    fileJson = open("followers.json","r")
    
    currentFollowers : list = Data
    oldFollowers = json.loads(fileJson.read())
    newFollowers : list = []

    for follower in currentFollowers:
        if (follower in oldFollowers):
            pass
        else:
            newFollowers.append(follower)
    fileJson.close()

    #---| Vérifies si c'est un nouveau follower|---#
    if (len(newFollowers) > 1):
        playerSound = mixer
        playerSound.init()
        try:
            playerSound.music.load(sound)
        except pygame.error:
            pass
        else:
            playerSound.music.play()

        #---| Mets à jour les fichiers et retourne les nouveaux followers |---#
        text1 : str = ""

        for follower in newFollowers:
            text1 += follower['name']
            text1 += ", "
        SetLastFollower(text1)

        fileJson = open("followers.json","w")
        fileJson.write(getData)
        fileJson.close()
        return (text1)

