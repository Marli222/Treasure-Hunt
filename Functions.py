import sys
import time
from Classes import *
import readchar

def Save(player1):
    save = open("Savefile",'w')
    save.write(f"{player1.name}\n{player1.hp}\n{player1.lvl}\n{player1.exp}") #Finish writing this...
def NewGame():
    player1 = Stats('',10,1,0,100,1,Tut,[],0,'','','',[],'',[],10)
    Tutorial(player1,Tut)
def LoadGame():
    player1 = Stats()
    GameLoop()

def Tutorial(player,Tut):
    Type("[???]: Welcome! Hopefully you're not too dizzy?")
    Type("[???]: I know the teleportation can feel a bit weird, especially when you first experience it.")
    Type("[???]: What's your name again??")
    player.name = input("[Tutorial]: Enter your name... > ")
    Tut.Update()
    Type(f"[???]: You're awake {player.name}! Good, I thought I was talking to myself...")
    Type("[???]: OK, now try and move about! I won't judge you if you bump into the force field!")
    print("[Tutorial]: Press wasd to move.")
    while True:
        key = readchar.readkey()
        if key in 'wasd':
            Type(f"[???]: Oh. Sorry I forgot to break the paralysis spell... Haha - My bad, {player.name}.")
            break
    player.Actions()

    
def Main():
    Type("NEW GAME - 1")
    Type("LOAD GAME - 2")
    Type("EXIT GAME - 3")
    while True:
        ene = input("Enter number based on your command. > ")
        if ene == '1':
            NewGame()
            break
        elif ene == '2':
            LoadGame()
            break
        elif ene == '3':
            quit()
        else:
            Type("That was not a valid number, try again.")

def GameLoop():
    run = True
    while run:
        pass

Main()