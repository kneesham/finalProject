'''
Created on Nov 1, 2017

@author: tednesham
'''

from tkinter import *
from tkinter import ttk
from program.players import Player
from program.game import Game
from program.fileCabinet import FileCabinet

playerDetails = Player()
game = Game()
root = Tk()

def launchGame(*args):
    
    playerDetails.playerName = username.get()
    #assings the player name in the player class.
    print(playerDetails.playerName)
    
    if gametime60.get() == True:
        timer = 60
        
    elif gametime120.get() == True:
        timer = 120
        
    elif gametime180.get() == True:
        timer = 180
    else:
        timer = 0
    
    root.destroy()
    #closes the window where the user entered their username.
    
    game.start(timer)

root.title("Typing Test")

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
mainframe.columnconfigure(6, weight = 1)
mainframe.rowconfigure(6, weight = 1)

username = StringVar()
welcomeMessage = StringVar()
#lets tkinter know it's a string input
gametime60 = BooleanVar()
gametime120 = BooleanVar()
gametime180 = BooleanVar()

ttk.Label(mainframe, text="Welcome to my typing test!").grid( column= 1, columnspan = 2, row = 0, sticky = E)
ttk.Label(mainframe, text="plese enter a username:").grid(column = 0, columnspan= 2, row = 2, sticky = (W,E))
#outputs the

usernameEntry = ttk.Entry(mainframe, width = 30, textvariable = username)
usernameEntry.grid(column= 2, columnspan = 2, row=2, sticky=(W, E))

ttk.Radiobutton(mainframe, text = "1 Minute", variable = gametime60).grid(column = 0, row = 3, sticky = (W,E))
ttk.Radiobutton(mainframe, text = "2 Minutes", variable = gametime120).grid(column = 1,  row = 3, sticky = (W,E))
ttk.Radiobutton(mainframe, text = "3 Minutes", variable = gametime180).grid(column = 2, row = 3, sticky = (W,E))

ttk.Button(mainframe, width = 10, text="Take the Test!", command =launchGame).grid(column = 3, row = 3, sticky = (W,E))


root.bind('<Return>', launchGame)



root.mainloop()



