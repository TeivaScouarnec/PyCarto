# BotPicarto

A small software to get the last five followers of his Picarto channel.

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

To use the software, you will need to:
1. unzip the folder
2. open the folder and open the executable BotPicarto.exe
3. Drag and drop your permissions that you copied and pasted earlier (DO NOT touch the api server)
4. Choose the delay (in seconds) for the software to recover your followers (Be careful, the shorter the delay, the more it can slow down your computer. Increase the delay if you experience slowdowns after you are connected)
5. Press "Connect"

Below you can see your last five followers.

## What are the libraries used?
[PIP-installer](https://pypi.org/project/pip/)
[PySimpleGui](https://github.com/PySimpleGUI/PySimpleGUI)
[Urllib3](https://urllib3.readthedocs.io/en/stable/)
