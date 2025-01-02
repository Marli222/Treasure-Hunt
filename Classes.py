import os 
import readchar
import sys
import time
import json
import random

def convert(astr):
    return json.loads(astr)

def MaxHp(player):
    if player.hp > player.maxhp:
        if player.lvl == 1:
            player.hp = 10
        elif player.lvl == 2:
            player.hp = 20
        elif player.lvl == 3:
            player.hp = 35
        elif player.lvl == 4:
            player.hp = 50
        elif player.lvl == 5:
            player.hp = 70
        elif player.lvl == 6:
            player.hp = 175
        elif player.lvl == 7:
            player.hp = 200
        elif player.lvl == 8:
            player.hp = 250
        elif player.lvl == 9:
            player.hp = 300
        elif player.lvl == 10:
            player.hp = 400

def Exp(player):
    if player.exp < 100:
        player.lvl = 1
        player.Rexp = 100 - player.exp
    elif player.exp > 100 and player.exp < 500:
        player.lvl = 2
        player.Rexp = 500 - player.exp
    elif player.exp > 500 and player.exp < 1000:
        player.lvl = 3
        player.Rexp = 1000 - player.exp

def Save(player1):
    save = open("Savefile.txt",'w')
    if player1.location == Tut:
        player1.location = 'Tut'
    elif player1.location == MainCity:
        player1.location = 'MainCity'
    list1 = json.dumps(player1.inv) 
    list2 = json.dumps(player1.compq)
    list3 = json.dumps(player1.cuts)
    list4 = json.dumps(player1.curq)
    save.write(f"{player1.location}¬{player1.hp}¬{player1.lvl}¬{player1.exp}¬{player1.Rexp}¬{player1.atk}¬{player1.name}¬{list1}¬{player1.gold}¬{player1.wpatk}¬{player1.beat}¬{player1.target}¬{list2}¬{list4}¬{list3}¬{player1.maxhp}")
    save.readline
    save.close()
    smap = open("Savemap,txt",'w')
    Map1 = json.dumps(Tut.mapper)
    Map2 = json.dumps(MainCity.mapper)
    smap.write(f"{Map1}¬{Map2}")
    smap.close()
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
    if loc[13] == '[]':
        loc[13] = []
    else:
        loc[13] = convert(loc[13])
    if loc[14] == '[]':
        loc[14] = []
    else:
        loc[14] = convert(loc[14])
        
    player1 = Stats(loc[0],int(loc[1]),int(loc[2]),int(loc[3]),int(loc[4]),int(loc[5]),loc[6],loc[7],int(loc[8]),loc[9],loc[10],loc[11],loc[12],loc[13],loc[14],int(loc[15]))
    load.close()
    load2 = open("Savemap,txt",'r')
    loc2 = (load2.readline()).split("¬")
    Tut.mapper = convert(loc2[0])
    MainCity.mapper = convert(loc2[1])
    player1.location.Update()
    player1.Actions()

def Type(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)
    print('')

def Fight(y,x,player,target,all):
    a = random.randint(0,6)
    if a > 0:
        if player.beat == '':
            Type("[Tutorial]: You need to equip a weapon to fight. Click q..")
            return
        if player.beat.name == 'Fire Amulet': #All magic items will be here.
            if player.beat.char <= 0:
                Type("There are no more charges left...")
                if 'Help1' not in player.cuts:
                    Type("[Tutorial]: There are no more charges of this weapon.")
                    Type("[Tutorial]: Click q to use your fists, they never run out of charge...")
                    player.cuts.append("Help1")
                a = 0
            else:
                Type(f"You used 1 charge of {player.beat.name}.")
                a = player.beat.atk * a + player.atk
                print(f"{target.name} is about to meet a magical demise! {player.name} dealt {a} damage!")
                player.beat.char -= 1
        if player.beat.name == 'Fist':
            a = player.atk + player.wpatk
            print(f"You punched {target.name}! {player.name} dealt {a} damage!")
        elif player.beat.name == 'Tiny Knife':
            a = player.atk + player.wpatk
            print(f"You stabbed {target.name}! {player.name} dealt {a} damage!")
    else:
        print(f"{target.name} dodged your attack.")
    target.hp -= a
    if target.hp <= 0:
        print(f"{player.name} has defeated {target.name}!")
        all.remove(target.name)
        player.location.mapper[y][x] = '.'

def Attack(player,mob):
    if mob.hp > 0:
        a = random.randint(mob.ran[0],mob.ran[1])
        if a > 1:
            b = random.randint(0,6) * mob.atk
            print(f"{mob.name} attacked you for {b} points.")
            player.hp -= b
        else:
            print(f"{player.name} dodged the attack!")
        if player.hp < 0:
            print(f"You have been defeated....")
            quit()
    else:
        pass

def Randomise(player):
    Type("your mother")

class Weapons:
    def __init__(item, name, atk,charges):
        item.name = name
        item.atk = atk
        item.char = charges
# Magic Weapons
Fire = Weapons('Fire Amulet',3,2)

class Goblin:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 15
        mob.atk = 1
        mob.exp = 5
        mob.gold = 2
        mob.ran = [1,3]

class Slime:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 30
        mob.atk = 1
        mob.exp = 7
        mob.gold = 3
        mob.ran = [1,4]

class GuardE: #Change stats for game balancing later
    def __init__(mob,name):
        mob.name = name
        mob.hp = 100
        mob.atk = 10
        mob.exp = 7
        mob.gold = 3
        mob.ran = [1,10]

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
                  
    def Combat(self,Enemies,emap,fmap):
        Combat = Combat_Area('Combat',[['~','~','~','~','~'],
        ['~','.','.','.','~'],
        ['~','.','.','.','~'],
        ['~','.','.','.','~'],
        ['~','~','~','~','~']],'.',1,3,emap,fmap) 
        #for emap and fmap - $ mob1 ; # mob2 ; % mob3 
        self.location = Combat
        y = 0
        x = 3
        At = []
        gold = 0
        exp = 0
        for q,i in enumerate(Enemies):
            if q < 4:
                y += 1
                Combat.mapper[y][x] = Combat.emap[i]
            elif q >= 4:
                y -= 1
                x = 2
                Combat.mapper[y][x] = Combat.emap[i]
            if i == 'Goblin1':
                Gob1 = Goblin('Goblin1')
                At.append(Gob1)
            elif i == 'Goblin2':
                Gob2 = Goblin('Goblin2')
                At.append(Gob2)
            elif i == 'Goblin3':
                Gob3 = Goblin('Goblin3')
                At.append(Gob3)
            elif i == 'Guard':
                Guard1 = GuardE('Guard')
                At.append(Guard1)
        Combat.Update(self)
        while Enemies != []:
            self.location.mapper[self.location.l_y][self.location.l_x] = self.location.Last1
            key = readchar.readkey()
            if key == 'q':
                Type("What item would you like to use?")
                for o,i in enumerate(self.inv):
                    print(f"{o} - {i}")
                items = dict(enumerate(self.inv,0))
                item = input("Enter the number. > ")
                try: 
                    wp = items[int(item)]
                    if wp == "Fire Amulet":
                        Type(f"You have equipped the Fire Amulet! It has {Fire.char} charges left.")
                        self.beat = Fire
                        self.wpatk = Fire.atk
                        time.sleep(1)
                    elif wp == "Fist":
                        Fist = Weapons('Fist',self.atk,'')
                        Type(f"You've clenched your fists!")
                        self.beat = Fist
                        self.wpatk = Fist.atk
                        time.sleep(1)
                    elif wp == "Tiny Knife":
                        Knife = Weapons('Tiny Knife',2,'')
                        Type("You unseathed the small knife.")
                        self.beat = Knife
                        self.wpatk = Knife.atk
                        time.sleep(1)
                except:
                    print("You don't have that item.")
            elif key == "w":
                self.location.py_y -= 1
                if self.location.mapper[self.location.py_y][self.location.py_x] == "~":
                    self.location.py_y += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "$" or self.location.mapper[self.location.py_y][self.location.py_x] == "#" or self.location.mapper[self.location.py_y][self.location.py_x] == "%": 
                    info = self.location.emap['$']
                    if self.location.mapper[self.location.py_y][self.location.py_x] == "$":
                        if self.location.fmap['$'] == 'Goblin1': #Add more elif statements for different mobs mapped to $ smbyol
                            info(self.location.py_y,self.location.py_x,self,Gob1,Enemies)
                            Attack(self,Gob1)
                        elif self.location.fmap['$'] == 'Guard':
                            info(self.location.py_y,self.location.py_x,self,Guard1,Enemies)
                            Attack(self,Guard1)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                        if self.location.fmap['#'] == 'Goblin2':
                            info(self.location.py_y,self.location.py_x,self,Gob2,Enemies)
                            Attack(self,Gob2)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "%":
                        if self.location.fmap['%'] == 'Goblin3':
                            info(self.location.py_y,self.location.py_x,self,Gob3,Enemies)
                            Attack(self,Gob3)
                    self.location.py_y += 1
                    continue
                else:
                    self.location.Last1 = self.location.mapper[self.location.py_y][self.location.py_x]
                    self.location.l_y = self.location.py_y
                    self.location.l_x = self.location.py_x
                    self.location.mapper[self.location.py_y][self.location.py_x] = '@'
            elif key == "s":
                self.location.py_y += 1
                if self.location.mapper[self.location.py_y][self.location.py_x] == "~":
                    self.location.py_y -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "$" or self.location.mapper[self.location.py_y][self.location.py_x] == "#" or self.location.mapper[self.location.py_y][self.location.py_x] == "%": 
                    info = self.location.emap['$']
                    if self.location.mapper[self.location.py_y][self.location.py_x] == "$":
                        if self.location.fmap['$'] == 'Goblin1': #Add more elif statements for different mobs mapped to $ smbyol
                            info(self.location.py_y,self.location.py_x,self,Gob1,Enemies)
                            Attack(self,Gob1)
                        elif self.location.fmap['$'] == 'Guard':
                            info(self.location.py_y,self.location.py_x,self,Guard1,Enemies)
                            Attack(self,Guard1)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                        if self.location.fmap['#'] == 'Goblin2':
                            info(self.location.py_y,self.location.py_x,self,Gob2,Enemies)
                            Attack(self,Gob2)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "%":
                        if self.location.fmap['%'] == 'Goblin3':
                            info(self.location.py_y,self.location.py_x,self,Gob3,Enemies)
                            Attack(self,Gob3)
                    self.location.py_y -= 1
                    continue
                else:
                    self.location.Last1 = self.location.mapper[self.location.py_y][self.location.py_x]
                    self.location.l_y = self.location.py_y
                    self.location.l_x = self.location.py_x
                    self.location.mapper[self.location.py_y][self.location.py_x] = '@'
            elif key == "a":
                self.location.py_x -= 1
                if self.location.mapper[self.location.py_y][self.location.py_x] == "~":
                    self.location.py_x += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "$" or self.location.mapper[self.location.py_y][self.location.py_x] == "#" or self.location.mapper[self.location.py_y][self.location.py_x] == "%": 
                    info = self.location.emap['$']
                    if self.location.mapper[self.location.py_y][self.location.py_x] == "$":
                        if self.location.fmap['$'] == 'Goblin1': #Add more elif statements for different mobs mapped to $ smbyol
                            info(self.location.py_y,self.location.py_x,self,Gob1,Enemies)
                            Attack(self,Gob1)
                        elif self.location.fmap['$'] == 'Guard':
                            info(self.location.py_y,self.location.py_x,self,Guard1,Enemies)
                            Attack(self,Guard1)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                        if self.location.fmap['#'] == 'Goblin2':
                            info(self.location.py_y,self.location.py_x,self,Gob2,Enemies)
                            Attack(self,Gob2)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "%":
                        if self.location.fmap['%'] == 'Goblin3':
                            info(self.location.py_y,self.location.py_x,self,Gob3,Enemies)
                            Attack(self,Gob3)
                    self.location.py_x += 1
                    continue
                else:
                    self.location.Last1 = self.location.mapper[self.location.py_y][self.location.py_x]
                    self.location.l_y = self.location.py_y
                    self.location.l_x = self.location.py_x
                    self.location.mapper[self.location.py_y][self.location.py_x] = '@'              
            elif key == "d":
                self.location.py_x += 1
                if self.location.mapper[self.location.py_y][self.location.py_x] == "~":
                    self.location.py_x -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "$" or self.location.mapper[self.location.py_y][self.location.py_x] == "#" or self.location.mapper[self.location.py_y][self.location.py_x] == "%": 
                    info = self.location.emap['$']
                    if self.location.mapper[self.location.py_y][self.location.py_x] == "$":
                        if self.location.fmap['$'] == 'Goblin1': #Add more elif statements for different mobs mapped to $ smbyol
                            info(self.location.py_y,self.location.py_x,self,Gob1,Enemies)
                            Attack(self,Gob1)
                        elif self.location.fmap['$'] == 'Guard':
                            info(self.location.py_y,self.location.py_x,self,Guard1,Enemies)
                            Attack(self,Guard1)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                        if self.location.fmap['#'] == 'Goblin2':
                            info(self.location.py_y,self.location.py_x,self,Gob2,Enemies)
                            Attack(self,Gob2)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "%":
                        if self.location.fmap['%'] == 'Goblin3':
                            info(self.location.py_y,self.location.py_x,self,Gob3,Enemies)
                            Attack(self,Gob3)
                    self.location.py_x -= 1
                    continue
                else:
                    self.location.Last1 = self.location.mapper[self.location.py_y][self.location.py_x]
                    self.location.l_y = self.location.py_y
                    self.location.l_x = self.location.py_x
                    self.location.mapper[self.location.py_y][self.location.py_x] = '@'
            self.location.Update(self)  
        for x in At:
            gold += x.gold * random.randint(x.ran[0],x.ran[1])
            exp += x.exp * random.randint(x.ran[0],x.ran[1])
        Type(f"You have gained {gold} gold pieces and {exp} exprience points!")
        self.beat = ''
        # Cutscenes after combat:
        if 'Help2' not in self.cuts:
            Type(f"[Tutorial]: Press z to check your status and inventory!")
            Type(f"[Tutorial]: This is especially useful to see how much exp you need to level up!")
            self.cuts.append("Help2")
        if 'Gob' not in self.cuts:
            Type(f"You see the Goblin had dropped a small knife.")
            Type(f"Take it? (y/n)")
            key = readchar.readkey()
            if key == 'y':
                Type("You have obtained the tiny knife...")
                self.inv.append("Tiny Knife")
        if 'Defeated Guard' in self.cuts:
            Type(f"[Guard]: You? Defeated me? May you have mercy on our small island of Javara.")
            Type(f"[Guard]: We did not intend to fall onto your magicless land. Alas one of our own sabatagoted us.")
            MainCity.mapper[5][6] = '.'
        self.gold += gold   
        self.exp += exp
        self.location = last_loc
        Exp(self)
        MaxHp(self)

    def Actions(self):
        while True:
            key = readchar.readkey()
            self.location.mapper[self.location.l_y][self.location.l_x] = self.location.Last1
            if key == 'e':
                if self.location.Last1 == '~':
                    Randomise(self)
                else:
                    Type("There is nothing to see here...")
            if key == 'z':
                MaxHp(self)
                Exp(self)
                Type(f"{self.name} - at the {self.location.name}")
                Type(f"Hp: {self.hp}")
                Type(f"Lvl: {self.lvl}")
                Type(f"{self.Rexp} exp is required to level up!")
                Type(f"Gold: {self.gold}")
                if self.curq == '':
                    Type(f"{self.name} is currently not doing any quests.")
                else:
                    Type(f"{self.name} is currently doing {self.curq} quest.")
                input("Click enter to continue...")
            if key == 'q':
                Type("What item would you like to use?")
                for o,i in enumerate(self.inv):
                    print(f"{o} - {i}")
                items = dict(enumerate(self.inv))
                item = input("Enter the number. > ")
                try: 
                    print(items[int(item)])
                except:
                    print("You don't have that item.")
            if key == "p":
                os.system('cls')
                Type("Saving....")
                Save(self)
                quit()
            if key == "w":
                self.location.py_y -= 1
                if self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                    self.location.py_y += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "|":
                    info = self.location.emap['|']
                    if 'Gob' not in self.cuts:
                        Tut_Fight(self)
                        self.location.py_y += 1
                        break
                    elif 'Amb2' not in self.cuts:
                        Amb2(self)
                    else:
                        self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "&": 
                    info = self.location.emap['&']
                    info(self)
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
                    if 'Gob' not in self.cuts:
                        Tut_Fight(self)
                        self.location.py_y -= 1
                        break
                    elif 'Amb2' not in self.cuts:
                        Amb2(self)
                    else:
                        self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "&": 
                    info = self.location.emap['&']
                    info(self)
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
                    if 'Gob' not in self.cuts:
                        Tut_Fight(self)
                        self.location.py_x += 1
                        break
                    elif 'Amb2' not in self.cuts:
                        Amb2(self)
                    else:
                        self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "&": 
                    info = self.location.emap['&']
                    info(self)
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
                    if 'Gob' not in self.cuts:
                        Tut_Fight(self)
                        self.location.py_x -= 1
                        break
                    elif 'Amb2' not in self.cuts:
                        Amb2(self)
                    else:
                        self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "&": 
                    info = self.location.emap['&']
                    info(self)
                    self.location.py_x -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "£": 
                    info = self.location.emap['£']
                    info(self)
                    self.location.py_x -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "$": 
                    info = self.location.emap['$']
                    info(self)
                    self.location.py_x -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "%": 
                    info = self.location.emap['%']
                    info(self)
                    self.location.py_x -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "!": 
                    info = self.location.emap['!']
                    info(self)
                    self.location.py_x -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "^": 
                    info = self.location.emap['^']
                    info(self)
                    self.location.py_x -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "_": 
                    info = self.location.emap['_']
                    info(self)
                    self.location.py_x -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "-": 
                    info = self.location.emap['-']
                    info(self)
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
        os.system('cls')
        for row in zone.mapper:
            print(' '.join(map(str, row)))

class Combat_Area(Area):
    def __init__(zone, name, map1, start, x, y, emap,fmap):
        super().__init__(name, map1, start, x, y, emap)
        zone.fmap = fmap

    def Update(self,player):
        os.system('cls')
        for row in self.mapper:
            print(' '.join(map(str, row)))
        x = ', '.join(player.inv)
        if player.beat == '':
            v = 'None'
        else:
            v = player.beat.name
        print(f'HP: {player.hp}\nEQUIPPED WEAPON: {v}\nITEMS: {x}')

def Tut_Fight(player):
    os.system('cls')
    commap = [["#","#","#","#","#"],
        ["#",".",".","&","#"],
        ["#",".","@","$","|"],
        ["#","#","#","#","#"]]
    for row in commap:
            print(' '.join(map(str, row)))
    Type(f'[Goblin]: $£&£% $%&$!£%$& £$%@#')
    Type(f'[Ambrosia]: Is that a stray goblin? Quick use this!')
    Type('You obtained a Fire amulet!')
    player.inv.append("Fire Amulet")
    Type(f"[Tutorial]: {player.name}, click q to use the fire amulet.")
    global last_loc
    last_loc = Tut
    player.Combat(["Goblin1"],{'Goblin1':'$','$':Fight},{'$':'Goblin1'})
    player.cuts.append("Gob")
    player.location.Update()
    player.Actions()    

def Amb(player):
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
            player.cuts.append("Fire")
        else:
            Type(f'[Ambrosia]: Oh. I must sound stupid...')
            Type(f'[Ambrosia]: Anyways, I\'ll take you to the main city. We\'re just waiting on another vistor.')
            Type(f'[Ambrosia]: If you want to start walking the pathway is down and to your right.')
            Type(f'[Tutorial]: Walk through the | to reach the city.')
    else:
        Type(f'[Ambrosia]: I am flattered you want to talk with me but I\'m going to be waiting here.\n[Ambrosia]: Start walking and I\'ll catch up with you later on.')
        Type(f'[Tutorial]: Walk through the | to reach the city.')
    
def Amb2(player):
    Type(f'[Ambrosia]: Wow! I thought I might of needed to help you but you are a natural with that amulet!')
    Type(f'[Ambrosia]: I suggest that you write about that Goblin in your notes app.')
    Type(f"[Tutorial]: Make sure to click 'p' outside of combat to save your progress.")
    Type(f'[Ambrosia]: It\'s easier to defeat summons if you know what you are up against.')
    Type(f"Ask about summons? (y/n)")
    key = readchar.readkey()
    if key == 'y':
        Type(f"[{player.name}]: Summons? What are those?")
        Type(f'[Ambrosia]: My apologies, I assumed you knew what I meant.\n[Ambrosia]: Summons are creatures the Guardians bring to this plane to protect the ruins.')
        Type(f"Ask about ruins? (y/n)")
        key = readchar.readkey()
        if key == 'y':
            Type(f"[{player.name}]: The ruins? Ruins of what?")
            Type(f'[Ambrosia]: That my dear vistor is not something outsiders should know about.\n[Ambrosia]: However seeing as I did put you in harms way I\'ll let you choose.')
            Type(f"[Ambrosia]: I\'ll let you keep the Fire amulet and even recharge it. Or I can tell you a bit about the ruins?")
            Type(f"Ruins or Amulet? (r/a)")
            if key == 'r':
                Type(f"[Ambrosia]: Ok, {player.name} you seem to very interested in our history. More so then magic, haha!")
                Type("[Ambrosia]: I guess that why you were picked to come and visit our floating island. Or previously floating...")
                Type("[Ambrosia]: The ruins are the old temples bulit by my ancestors to worship our gods.\n[Ambrosia]: Now, they are used as storage for powerful magic items as they corrupt the land around them.")
                Type("[Ambrosia]: Interesting, right?")
            else:
                Type(f"[Ambrosia]: Ah, {player.name} you've got a taste for magic huh?")
                a = random.randint(2,5)
                Type(f"[Ambrosia]: I'll give you {a} more charges! I'm sure you can use those gold pieces you got from that Goblin to get more charges..")
                Fire.char += a
                Type(f"{Fire.name} now has {Fire.char} charges!")
                player.cuts.append("Recharge")
    if 'Recharge' not in player.cuts:
        Type(f"[Ambrosia]: Could I have my amulet back now?")
        Type(f"Give back Amulet? (y/n)")
        key = readchar.readkey()
        if key == 'y':
            Type(f"[{player.name}]: Sure, here.")
            Type(f"[Ambrosia]: No it's ok. That was a test - and you passed!")
            if 'Fire' in player.cuts:
                a = random.randint(2,5)
                Type(f"[Ambrosia]: Here, I'll give you {a} more charges! I'm happy, you're not one of those magic hungry, Ruin Hunters...")
                Fire.char += a
                Type(f"{Fire.name} now has {Fire.char} charges!")
            Type(f"[Ambrosia]: I think our other vistor may have not made it to the teleporting spot - I need to go assist them! I'll catch up later!")
        else:
            Type(f"[{player.name}]: No.")
            Type(f"[Ambrosia]: That's a joke right?")
            Type(f"[{player.name}]: ...")
            time.sleep(2)
            Type(f"[Ambrosia]: I see.")
            player.curq.append('Ruin Hunter')
            Type("New Quest Started!\n>>>The Disguised Ruin Hunter<<<")
    player.location.mapper[1][3] = '.'
    player.location.Update()
    player.cuts.append("Amb2")

def Guard(player):
    Type(f"[Guard]: Where do you think you are going? Vistors are not allowed past here.")
    Type("Attack the Guard? (y/n)")
    key = readchar.readkey()
    if key == 'y':
        player.cuts.append("Defeated Guard")
        Type(f"[{player.name}]: If you won't get out of my way, I'll guess I'll get past by force!")
        player.Combat(['Guard'],{'Guard':'$','$':Fight},{'$':'Guard'})
    else:
        Type(f"[{player.name}]: Oh. Sorry, I'll leave.")


def Weapons_Shop(player): #
    if 'Wep' not in player.cuts:
        pass

def Magic_Shop(player):
    pass

def Shady_Merchant(player):#
    pass

def Potion_Geek(player):#
    pass

MainCity = Area("Main City",[["#","_","#","^","#","-","#","#"],
        ["#",".",".",".",".",".",".","#"],
        ["#",".","£","~","~","%",".","#"],
        ["#",".","$","~","~","!",".","#"],
        ["|",".",".",".",".",".","&","}"],
        ["#","#","#","#","#","#","#","#"]],'.',1,4,{'|':'','&':'Ambrosia'}) #£ - Weapons Shop $ - Magic Shop ! - Scanveger merchant /Ruin Hunter in disigue (Ruin Hunter Quest or tells you to get lost) % - Loves potions and the how the herbs on this island have magical effects
Tut = Area("Dock",[["#","#","#","#","#"],
        ["#",".",".","&","#"],
        ["#",".",".",".","|"],
        ["#","#","#","#","#"]],'.',1,1,{'|':MainCity,'&':Amb})
MainCity.emap = {'|':Tut,'&':Guard,'£':Weapons_Shop,'$':Magic_Shop,'!':Shady_Merchant,'%':Potion_Geek}

'''
player1 = Stats('',10,1,0,100,1,Tut,[],0,'','','',[],'',['Gob'],10)
Tut.Update()

player1.Actions()
'''