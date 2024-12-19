import os 
import readchar
import sys
import time
import json
import random

def convert(astr):
    return json.loads(astr)

def Save(player1):
    save = open("Savefile.txt",'w')
    if player1.location == Tut:
        player1.location = 'Tut'
    elif player1.location == MainCity:
        player1.location = 'MainCity'
    save.write(f"{player1.location}¬{player1.hp}¬{player1.lvl}¬{player1.exp}¬{player1.Rexp}¬{player1.atk}¬{player1.name}¬{player1.inv}¬{player1.gold}¬{player1.wpatk}¬{player1.beat}¬{player1.target}¬{player1.compq}¬{player1.curq}¬{player1.cuts}¬{player1.maxhp}")
    save.readline
    Type("Saved!")

def LoadGame():
    load = open("Savefile.txt","r")
    loc = (load.readline()).split("¬")
    print(loc)
    if loc[0] == 'MainCity':
        loc[0] = MainCity
    elif loc[0] == 'Tut':
        loc[0] = Tut
    if loc[7] == '[]':
        loc[7] = []
    else:
        loc[7] = convert(loc[7])
    if loc[12] == '[]':
        loc[12] = []
    else:
        loc[12] = convert(loc[12])
    if loc[14] == '[]':
        loc[14] = []
    else:
        loc[14] = convert(loc[14])
        
    player1 = Stats(loc[0],int(loc[1]),int(loc[2]),int(loc[3]),int(loc[4]),int(loc[5]),loc[6],loc[7],int(loc[8]),loc[9],loc[10],loc[11],loc[12],loc[13],loc[14],int(loc[15]))
    player1.location.Update()
    player1.Actions()

def Type(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)
    print('')

class Weapons:
    def __init__(item, name, atk, ob):
        item.name = name
        item.atk = atk

class Goblin:
    def __init__(mob):
        mob.name = 'Goblin'
        mob.hp = 15
        mob.atk = 1
        mob.exp = 5
        mob.gold = 2

class Slime:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 30
        mob.atk = 1
        mob.exp = 7
        mob.gold = 3

class Stats:
    def __init__(self, location, hp, lvl, exp, Rexp, atk, name, inv, gold, wp, beat, target, compq, curq, cuts, maxhp): #compq is completed quests and curq is current quest.
     self.name = name 
     self.hp = hp
     self.lvl = lvl
     self.exp = exp
     self.Rexp = Rexp
     self.atk = atk
     self.location = location
     self.inv = inv
     self.gold = gold
     self.wpatk = wp
     self.beat = beat
     self.target = target
     self.compq = compq
     self.curq = curq
     self.cuts = cuts #List of cutscenes the player has seen
     self.maxhp = maxhp
                  
    def Combat(self,Enemies):
        Combat = Combat_Area('Combat',[["~","~","~","~","~","~","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~","~","~","~","~","~","~"]],'.',1,3,{'Goblin1':'$','Goblin2':'$','Goblin3':'$','Fire Slime':'*'})
        for i in Enemies:
            y = 1
            x = 5
            Combat.mapper[y+1][x-1] = Combat.emap[i]
            if i == 'Goblin1':
                Gob1 = Goblin()
            elif i == 'Goblin2':
                Gob2 = Goblin()
            elif i == 'Goblin3':
                Gob3 = Goblin()
            elif i == 'Fire Slime':
                Fire_Slime = Slime(i)
        Combat.Update(self)
        while Enemies != []:
            key = readchar.readkey()
            if key == 'w':
                print("This works")

    def Actions(self):
        while True:
            key = readchar.readkey()
            self.location.mapper[self.location.l_y][self.location.l_x] = self.location.Last1
            if key == "p":
                os.system('clear')
                Type("Saving....")
                Save(self)
                quit()
            elif key == "w":
                self.location.py_y -= 1
                if self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                    self.location.py_y += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "|":
                    info = self.location.emap['|']
                    if 'Gob' in self.cuts:
                        self.location = info
                    else:
                        Tut_Fight(self)
                        self.location.py_y += 1
                        break
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "&": 
                    info = self.location.emap['&']
                    info(self.location,self)
                    self.location.py_y += 1
                    continue
                else:
                    self.location.Last1 = self.location.mapper[self.location.py_y][self.location.py_x]
                    self.location.l_y = self.location.py_y
                    self.location.l_x = self.location.py_x
                    self.location.mapper[self.location.py_y][self.location.py_x] = '@'
            elif key == "s":
                self.location.py_y += 1
                if self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                    self.location.py_y -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "|":
                    info = self.location.emap['|']
                    if 'Gob' in self.cuts:
                        self.location = info
                    else:
                        Tut_Fight(self)
                        self.location.py_y -= 1
                        break
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "&": 
                    info = self.location.emap['&']
                    info(self.location,self)
                    self.location.py_y -= 1
                    continue
                else:
                    self.location.Last1 = self.location.mapper[self.location.py_y][self.location.py_x]
                    self.location.l_y = self.location.py_y
                    self.location.l_x = self.location.py_x
                    self.location.mapper[self.location.py_y][self.location.py_x] = '@'
            elif key == "a":
                self.location.py_x -= 1
                if self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                    self.location.py_x += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "|": 
                    info = self.location.emap['|']
                    if 'Gob' in self.cuts:
                        self.location = info
                    else:
                        Tut_Fight(self)
                        self.location.py_x += 1
                        break
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "&": 
                    info = self.location.emap['&']
                    info(self.location,self)
                    self.location.py_x += 1
                    continue
                else:
                    self.location.Last1 = self.location.mapper[self.location.py_y][self.location.py_x]
                    self.location.l_y = self.location.py_y
                    self.location.l_x = self.location.py_x
                    self.location.mapper[self.location.py_y][self.location.py_x] = '@'              
            elif key == "d":
                self.location.py_x += 1
                if self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                    self.location.py_x -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "|":
                    info = self.location.emap['|']
                    if 'Gob' in self.cuts:
                        self.location = info
                    else:
                        Tut_Fight(self)
                        self.location.py_x -= 1
                        break
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "&": 
                    info = self.location.emap['&']
                    info(self.location,self)
                    self.location.py_x -= 1
                    continue
                else:
                    self.location.Last1 = self.location.mapper[self.location.py_y][self.location.py_x]
                    self.location.l_y = self.location.py_y
                    self.location.l_x = self.location.py_x
                    self.location.mapper[self.location.py_y][self.location.py_x] = '@'
            self.location.Update()

class Area:
    def __init__(zone,name,map1,start,x,y,emap):
        zone.name = name
        zone.mapper = map1
        zone.start = start
        zone.Last1 = zone.start
        zone.py_x = x
        zone.py_y = y
        zone.l_x = x
        zone.l_y = y
        zone.mapper[zone.py_y][zone.py_x] = '@'
        zone.emap = emap

    def Update(zone):
        os.system('clear')
        for row in zone.mapper:
            print(' '.join(map(str, row)))

class Combat_Area(Area):
    def __init__(zone, name, map1, start, x, y, emap):
        super().__init__(name, map1, start, x, y, emap)

    def Update(self,player):
        os.system('clear')
        for row in self.mapper:
            print(' '.join(map(str, row)))
        x = ','.join(player.inv)
        print(f'HP: {player.hp} ITEMS: {x}')

def Tut_Fight(player):
    os.system('clear')
    commap = [["#","#","#","#","#"],
        ["#",".",".","&","#"],
        ["#",".","@","$","|"],
        ["#","#","#","#","#"]]
    for row in commap:
            print(' '.join(map(str, row)))
    Type(f'[Goblin]: KEKEKEKKEKEKKEKE - A defenceless vistor! Easy pickings!!')
    Type(f'[Ambrosia]: Is that a goblin? Quick use this!')
    Type('You obtained a Fire amulet!')
    player.inv.append("Fire Amulet")
    player.Combat(["Goblin1","Fire Slime"])
    

def Amb(loc,player):
    if "Amb1" not in player.cuts:
        Type(f'[Ambrosia]: Hi, My name is Ambrosia! I\'ll be your guide around Javara!')
        Type(f'[Ambrosia]: It\'s lovely to meet you {player.name}')
        Type(f'[Ambrosia]: I always love showing vistors around - especially when I get to see their fuh-o-ne?')
        Type(f'[Ambrosia]: Is that how you pronounce it? (Y/N)')
        Type(f'[Tutorial]: Click y or n to make your choice...')
        key = readchar.readkey()
        player.cuts.append("Amb1")
        if key == 'y':
            Type(f'[{player.name}]: Yep.')
            Type(f'[Ambrosia]: Lovely! I really do enjoy seeing people\'s wallpapers - it is always facinating...')
            Type(f'[Ambrosia]: Anyways, I\'ll take you to the main city! We\'re just waiting on another vistor.')
            Type(f'[Ambrosia]: If you want to start walking the pathway is down and to your right.')
            Type(f'[Tutorial]: Walk through the | to reach the city.')
            player.cuts.append('Fire')
        else:
            Type(f'[Ambrosia]: Oh. I must sound stupid...')
            Type(f'[Ambrosia]: Anyways, I\'ll take you to the main city. We\'re just waiting on another vistor.')
            Type(f'[Ambrosia]: If you want to start walking the pathway is down and to your right.')
            Type(f'[Tutorial]: Walk through the | to reach the city.')
    else:
        Type(f'[Ambrosia]: I am flattered you want to talk with me but I\'m going to be waiting here.\n[Ambrosia]: Start walking and I\'ll catch up with you later on.')
        Type(f'[Tutorial]: Walk through the | to reach the city.')
    
    #loc.mapper[1][3] = '.'
    #loc.Update()

MainCity = Area("Main City",[["#","#","#","#","#"],
        ["#",".",".",".","#"],
        ["|",".",".",".","#"],
        ["#","#","#","#","#"]],'.',1,1,{'|':'','&':'Ambrosia'})
Tut = Area("Dock",[["#","#","#","#","#"],
        ["#",".",".","&","#"],
        ["#",".",".",".","|"],
        ["#","#","#","#","#"]],'.',1,1,{'|':MainCity,'&':Amb})
MainCity.emap = {'|':Tut,'&':'Ambrosia'}

'''
player1 = Stats('',10,1,0,100,1,Tut,[],0,'','','',[],'',['Gob'],10)
Tut.Update()

player1.Actions()
'''