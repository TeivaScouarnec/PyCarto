# PyCarto

A small software to get the last follower of his Picarto channel.

[Download PyCarto](https://github.com/TeivaScouarnec/BotPicarto/releases/download/Release/PicartoFollower_1-0-0.zip)

## How to get my permissions ?

First of all, to use the software, you will need to authorize your account to access the Picarto server.
To do this:

1. Go to the [API](https://api.picarto.tv/) tab in the "setting" page of your Picarto account. 
![](https://i.imgur.com/NDnBv70.png) ![](https://i.imgur.com/kUNlHPx.png)

2. when you are on the API page, click on the Authorization option.
![](https://i.imgur.com/pqPdmTA.png)

3. Select all the options and click on authorize.
![](https://i.imgur.com/MpwYl9R.png)

4. Follow the instructions from Picarto.

5. After your account is authorized, scroll down and access the /categories tab.
![](https://i.imgur.com/97RrRX8.png)

6. Click on "Try it out" then "Execute".

![](https://i.imgur.com/6oUbjLS.png) ![](https://i.imgur.com/6TB8ZSU.png)

7. retrieve only the token in the line of code from the beginning to the end (make sure there are no quotation marks 
![](https://i.imgur.com/hbShzoE.png)

That's it you have your token.

## How to use the software?

1. Download the application and place it in a folder where you want.
2. Launch the application once, it will create two files.
3. Place your authentication token in "config.yaml" (optional: if you want, you can add a small sound in WAV to alert you of new followers)
4. Run "LastFollowerPicarto.exe" again, if you have set everything correctly, the application works and updates the file "lastfollower.txt".
5. In OBS, when you create a text, you can get the text inside the text file.

## What are the libraries used?
[PIP-installer](https://pypi.org/project/pip/)
[Pygame](https://pypi.org/project/pygame/)
[Urllib3](https://urllib3.readthedocs.io/en/stable/)
