import os 
import readchar
import sys
import time
import random

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

class Stats:
    def __init__(self, name, hp, lvl, exp, Rexp, atk, location, inv, gold, wp, beat, target, compq, curq, cuts, maxhp): #compq is completed quests and curq is current quest.
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
     self.commap = [["~","~","~","~","~","~","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~",".",".",".",".",".","~"],
                  ["~","~","~","~","~","~","~"]]
     self.commapper = {'Goblin':'$','Fire Slime':'*'}
                  

    def Combat(self,Enemies):
        y = 0
        x = 6
        for i in Enemies:
            self.commap[y+1][x-1] = self.commapper[i]
            if i == 'Goblin':
                pass
            elif i == 'Fire Slime':
                print("Working!")
        self.Update_Commap()
    
    def Update_Commap(self):
        os.system('clear')
        for row in self.commap:
            print(' '.join(map(str, row)))
        print(f'HP: {self.hp} ITEMS: {self.inv}')

    def Actions(self):
        while True:
            key = readchar.readkey()
            self.location.mapper[self.location.l_y][self.location.l_x] = self.location.Last1
            if key == "w":
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
    player.inv.append('Fire Amulet')
    player.Combat(['Goblin','Fire Slime'])
    

def Amb(loc,player):
    if 'Amb1' not in player.cuts:
        Type(f'[Ambrosia]: Hi, My name is Ambrosia! I\'ll be your guide around Javara!')
        Type(f'[Ambrosia]: It\'s lovely to meet you {player.name}')
        Type(f'[Ambrosia]: I always love showing vistors around - especially when I get to see their fuh-o-ne?')
        Type(f'[Ambrosia]: Is that how you pronounce it? (Y/N)')
        Type(f'[Tutorial]: Click y or n to make your choice...')
        key = readchar.readkey()
        player.cuts.append('Amb1')
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
player1 = Stats('',10,1,0,100,1,Tutorial,[],0,'','','',[],'',10)
Tutorial.Update()

player1.Actions()
'''
