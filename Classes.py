import os 
import readchar
import sys
import time
import json
import random

dollar_count = 0
def Check_Full(player,item):
    if player.inv == 30:
        Type(f"[Tutorial]: Your inventory is full. Would you like to replace {item.name} with another item? (y/n)")
        if 'Help3' not in player.cuts:
                    Type("[Tutorial]: Be careful if you drop an item you can never get it back.")
                    Type("[Tutorial]: You can sell random items to Marina instead?")
                    player.cuts.append("Help3")
        key = readchar.readkey()
        if key == 'y':
            for i,x in enumerate(player.inv):
                print(f"{i} - {x}")
            run = True
            while run == True:
                a = input("Enter the number > ")
                try:
                    player.inv.remove(player.inv[int(a)])
                    player.inv.append(item)
                except:
                    print("That is not a valid number.")
    else:
        player.inv.append(item)

def convert(astr):
    return json.loads(astr)

def MaxHp(player):
    if player.lvl == 1:
        player.maxhp = 10
    elif player.lvl == 2:
        player.maxhp = 30
    elif player.lvl == 3:
        player.maxhp = 50
    elif player.lvl == 4:
        player.maxhp = 70
    elif player.lvl == 5:
        player.maxhp = 100
    elif player.lvl == 6:
        player.maxhp = 200
    elif player.lvl == 7:
        player.maxhp = 300
    elif player.lvl == 8:
        player.maxhp = 400
    elif player.lvl == 9:
        player.maxhp = 500
    elif player.lvl == 10:
        player.maxhp = 600
    if player.hp > player.maxhp:
        if player.lvl == 1:
            player.hp = 10
        elif player.lvl == 2:
            player.hp = 30
        elif player.lvl == 3:
            player.hp = 50
        elif player.lvl == 4:
            player.hp = 70
        elif player.lvl == 5:
            player.hp = 100
        elif player.lvl == 6:
            player.hp = 200
        elif player.lvl == 7:
            player.hp = 300
        elif player.lvl == 8:
            player.hp = 400
        elif player.lvl == 9:
            player.hp = 500
        elif player.lvl == 10:
            player.hp = 600

def Exp(player):
    lastlvl = player.lvl
    if player.exp < 50:
        player.lvl = 1
        player.Rexp = 50 - player.exp
    elif player.exp > 50 and player.exp < 300:
        player.lvl = 2
        player.Rexp = 300 - player.exp
    elif player.exp > 300 and player.exp < 700:
        player.lvl = 3
        player.Rexp = 700 - player.exp
    elif player.exp > 700 and player.exp < 1200:
        player.lvl = 4
        player.Rexp = 1200 - player.exp
    elif player.exp > 1200 and player.exp < 2000:
        player.lvl = 5
        player.Rexp = 2000 - player.exp
    elif player.exp > 2000 and player.exp < 3000:
        player.lvl = 6
        player.Rexp = 3000 - player.exp
    elif player.exp > 3000 and player.exp < 4100:
        player.lvl = 7
        player.Rexp = 4100 - player.exp
    elif player.exp > 4100 and player.exp < 5400:
        player.lvl = 8
        player.Rexp = 5400 - player.exp
    elif player.exp > 5400 and player.exp < 7000:
        player.lvl = 9
        player.Rexp = 7000 - player.exp
    elif player.exp > 7000:
        player.lvl = 10
        player.Rexp = 0
    if lastlvl != player.lvl:
        if player.lvl == 10:
            Type("You have reached the highest level - Well done!")
        Type("You have leveled up!")
        Type("You regain full health!!!")
        MaxHp(player)
        player.hp = player.maxhp

def Save(player1):
    save = open("Savefile.txt",'w')
    if player1.location == Tut:
        player1.location = 'Tut'
    elif player1.location == MainCity:
        player1.location = 'MainCity'
    elif player1.location == TenjaPath:
        player1.location = 'TenjaPath'
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
    schar = open("Savechar.txt",'w')
    schar.write(f"{Fire.char}¬{Ice.char}¬{Cool.char}¬{Hot.char}")
    schar.close()
    Type("Saved!")

def LoadGame():
    load = open("Savefile.txt","r")
    loc = (load.readline()).split("¬")
    if loc[0] == 'MainCity':
        loc[0] = MainCity
    elif loc[0] == 'Tut':
        loc[0] = Tut
    elif loc[0] == 'TenjaPath':
        loc[0] = TenjaPath
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
    load3 = open("Savechar.txt",'r')
    loc3 = (load3.readline()).split("¬")
    Fire.char = int(loc3[0])
    Ice.char = int(loc3[1])
    Cool.char = int(loc3[2])
    Hot.char = int(loc3[3])
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
        if player.beat.name == 'Fire Amulet' or player.beat.name == 'Ice Amulet' or player.beat.name == 'Cool Amulet' or player.beat.name == 'Hot Amulet':
            if player.beat.char <= 0:
                Type("There are no more charges left...")
                if 'Help1' not in player.cuts:
                    Type("[Tutorial]: There are no more charges of this weapon.")
                    Type("[Tutorial]: Click q to use your fists, they never run out of charge...")
                    Type("[Tutorial]: You can also go to Harley to recharge or even craft a new amulet.")
                    player.cuts.append("Help1")
                a = 0
            else:
                Type(f"You used 1 charge of {player.beat.name}.")
                a = player.beat.atk * a + player.atk
                print(f"{target.name} is about to meet a magical demise! {player.name} dealt {a} damage!")
                player.beat.char -= 1
        if player.beat.name == 'Fist':
            a += player.atk + player.wpatk
            print(f"You punched {target.name}! {player.name} dealt {a} damage!")
        elif player.beat.name == 'Tiny Knife' or player.beat.name == 'Sword' or player.beat.name == 'Enhanced Sword' or player.beat.name == 'Dagger' or player.beat.name == 'Enhanced Dagger':
            a += player.atk + player.wpatk
            print(f"You stabbed {target.name}! {player.name} dealt {a} damage!")
        elif player.beat.name == 'Axe' or player.beat.name == 'Enhanced Axe':
            a += player.atk + player.wpatk
            print(f"You punched {target.name}! {player.name} dealt {a} damage!")
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
    player.location.Last1 = '.'
    if player.location == MainCity:
        a = random.randint(1,10)
        if a > 0 and a < 6: #Cheap Item
            b = random.randint(1,10)
            if b > 0 and b < 4:
                Type("You found a Frying Pan!")
                Check_Full(player,"Frying Pan")
            elif b >= 4 and b < 7:
                Type("You found Worn Boots!")
                Check_Full(player,"Worn Boots")
            elif b >= 7 and b < 10:
                Type("You found a Clear Gem!")
                Check_Full(player,"Clear Gem")
            elif b == 10:
                Type("You found a half drunk potion!")
                Check_Full(player,"Half Drunk Potion")
        elif a >= 6 and a < 9: #Ambush
            global last_loc
            last_loc = MainCity
            b = random.randint(1,2)
            if b == 1:
                Type("A Goblin Ambushed you!")
                player.Combat(['Goblin1'],{'Goblin1':'$','$':Fight},{'$':'Goblin1'})
            elif b == 2:
                Type("Two summons have ambushed you!")
                player.Combat(['Goblin1','Goblin2'],{'Goblin1':'$','Goblin2':'#','$':Fight},{'$':'Goblin1','#':'Goblin2'})
        elif a >= 9: #Rare
            Type("You found something rare!")
            b = random.randint(1,10)
            if b > 0 and b < 4:
                Type("You found a Clear Gem & Gold!")
                Check_Full(player,"Clear Gem")
                player.gold += 5
            elif b >= 4 and b < 7:
                Type("You found Refined Clear Gem!")
                Check_Full(player,"Refined Clear Gem")
            elif b >= 7 and b < 10:
                Type("You found a Fire Gem Ore!")
                Check_Full(player,"Fire Gem Ore")
            elif b == 10:
                Type("You found a simple potion!")
                Check_Full(player,"Simple Potion")
    elif player.location == TenjaPath:
        a = random.randint(1,10)
        if a > 0 and a < 6: #Cheap Item
            b = random.randint(1,10)
            if b > 0 and b < 4:
                Type("You found a Frying Pan!")
                Check_Full(player,"Frying Pan")
            elif b >= 4 and b < 7:
                Type("You found Worn Boots!")
                Check_Full(player,"Worn Boots")
            elif b >= 7 and b < 10:
                Type("You found a Clear Gem!")
                Check_Full(player,"Clear Gem")
            elif b == 10:
                Type("You found a half drunk potion!")
                Check_Full(player,"Half Drunk Potion")
        elif a >= 6 and a < 9: #Ambush
            last_loc = TenjaPath
            b = random.randint(1,4)
            if b == 1:
                Type("A Goblin Ambushed you!")
                player.Combat(['Goblin1'],{'Goblin1':'$','$':Fight},{'$':'Goblin1'})
            elif b == 2:
                Type("A Slime Ambushed you!")
                player.Combat(['Slime1'],{'Slime1':'$','$':Fight},{'$':'Slime1'})
            elif b == 3:
                Type("A couple of summons ambushed you!")
                c = random.randint(1,2)
                if c == 2:
                    player.Combat(['Slime1','Slime2','Goblin3'],{'Slime1':'$','Slime2':'#','Goblin3':'%','$':Fight},{'$':'Slime1','#':'Slime2','%':'Goblin3'})
                elif c == 1:
                    player.Combat(['Slime1','Goblin2','Goblin3'],{'Slime1':'$','Goblin2':'#','Goblin3':'%','$':Fight},{'$':'Slime1','#':'Goblin2','%':'Goblin3'})
            elif b == 4:
                Type("Two summons have ambushed you!")
                player.Combat(['Goblin1','Slime2'],{'Goblin1':'$','Slime2':'#','$':Fight},{'$':'Goblin1','#':'Slime2'})
        elif a >= 9: #Rare
            Type("You found something rare!")
            b = random.randint(1,10)
            if b > 0 and b < 4:
                Type("You found a Clear Gem!")
                Check_Full(player,"Clear Gem")
            elif b >= 4 and b < 7:
                Type("You found Refined Clear Gem!")
                Check_Full(player,"Refined Clear Gem")
            elif b >= 7 and b < 10:
                Type("You found a Fire Gem Ore!")
                Check_Full(player,"Fire Gem Ore")
            elif b == 10:
                Type("You found a simple potion!")
                Check_Full(player,"Simple Potion")
class Shop:
    def __init__(shop,stock,stockmapper):
        shop.stock = stock
        shop.mapper = stockmapper
class Weapons:
    def __init__(item, name, atk,charges):
        item.name = name
        item.atk = atk
        item.char = charges
# Magic Weapons
Fire = Weapons('Fire Amulet',3,2)
Ice = Weapons('Ice Amulet',5,0)
Cool = Weapons('Cool Amulet',10,0)
Hot = Weapons('Hot Amulet',15,0)

class Goblin:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 7
        mob.atk = 1
        mob.exp = 5
        mob.gold = 2
        mob.ran = [1,2]
        mob.drops = 'Goblin Ear'

class Slime:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 15
        mob.atk = 1
        mob.exp = 7
        mob.gold = 3
        mob.ran = [1,3]
        mob.drops = 'Slime Goo'

class Sprite:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 30
        mob.atk = 2
        mob.exp = 10
        mob.gold = 3
        mob.ran = [1,5]
        mob.drops = 'Sprite Essence'

class Troll:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 50
        mob.atk = 5
        mob.exp = 20
        mob.gold = 3
        mob.ran = [1,7]
        mob.drops = 'Troll Nail'

class Lich:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 60
        mob.atk = 5
        mob.exp = 20
        mob.gold = 3
        mob.ran = [1,9]
        mob.drops = 'Glowing Skull'

class TFollower:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 60
        mob.atk = 5
        mob.exp = 20
        mob.gold = 3
        mob.ran = [1,9]
        mob.drops = 'Half Drunk Potion'

class TGuardian:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 60
        mob.atk = 5
        mob.exp = 20
        mob.gold = 3
        mob.ran = [1,9]
        mob.drops = 'Fire Gem'

class MFollower:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 60
        mob.atk = 5
        mob.exp = 20
        mob.gold = 3
        mob.ran = [1,9]
        mob.drops = 'Simple Potion'

class MGuardian:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 60
        mob.atk = 5
        mob.exp = 20
        mob.gold = 3
        mob.ran = [1,9]
        mob.drops = 'Ice Gem'

class XFollower:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 60
        mob.atk = 5
        mob.exp = 20
        mob.gold = 3
        mob.ran = [1,9]
        mob.drops = 'Spicy Potion'

class XGuardian:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 60
        mob.atk = 5
        mob.exp = 20
        mob.gold = 3
        mob.ran = [1,9]
        mob.drops = 'Cool Gem'

class GuardE:
    def __init__(mob,name):
        mob.name = name
        mob.hp = 100
        mob.atk = 10
        mob.exp = 30
        mob.gold = 40
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
            elif i == 'Slime1':
                Slime1 = Slime('Slime1')
                At.append(Slime1)
            elif i == 'Slime2':
                Slime2 = Slime('Slime2')
                At.append(Slime2)
            elif i == 'Slime3':
                Slime3 = Slime('Slime3')
                At.append(Slime3)
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
                    elif wp == "Ice Amulet":
                        Type(f"You have equipped the Ice Amulet! It has {Ice.char} charges left.")
                        self.beat = Ice
                        self.wpatk = Ice.atk
                        time.sleep(1)
                    elif wp == "Cool Amulet":
                        Type(f"You have equipped the Cool Amulet! It has {Cool.char} charges left.")
                        self.beat = Cool
                        self.wpatk = Cool.atk
                        time.sleep(1)
                    elif wp == "Hot Amulet":
                        Type(f"You have equipped the Hot Amulet! It has {Hot.char} charges left.")
                        self.beat = Hot
                        self.wpatk = Hot.atk
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
                    elif wp == "Dagger":
                        Dagger = Weapons('Dagger',2,'')
                        Type("You unseathed your dagger.")
                        self.beat = Dagger
                        self.wpatk = Dagger.atk
                        time.sleep(1)
                    elif wp == "Enhanced Dagger":
                        Enhanced_Dagger = Weapons('Enhanced Dagger',4,'')
                        Type("You unseathed your dagger. It shimmers with magic.")
                        self.beat = Enhanced_Dagger
                        self.wpatk = Enhanced_Dagger.atk
                        time.sleep(1)
                    elif wp == "Sword":
                        Sword = Weapons('Sword',3,'')
                        Type("You unseathed your sword.")
                        self.beat = Sword
                        self.wpatk = Sword.atk
                        time.sleep(1)
                    elif wp == "Enhanced Sword":
                        Enhanced_Sword = Weapons('Enhanced Sword',5,'')
                        Type("You unseathed your sword. It shimmers with magic.")
                        self.beat = Enhanced_Sword
                        self.wpatk = Enhanced_Sword.atk
                        time.sleep(1)
                    elif wp == "Axe":
                        Axe = Weapons('Axe',5,'')
                        Type("You gripped your axe.")
                        self.beat = Axe
                        self.wpatk = Axe.atk
                        time.sleep(1)
                    elif wp == "Enhanced Axe":
                        Enhanced_Axe = Weapons('Enhanced Axe',6,'')
                        Type("You gripped your axe. It shimmers with magic.")
                        self.beat = Enhanced_Axe
                        self.wpatk = Enhanced_Axe.atk
                        time.sleep(1)
                    elif wp == 'Half Drunk Potion':
                        self.hp += random.randint(5,10)
                        MaxHp(self)
                        Type(f"The potion restored your health! You have {self.hp} hp.")
                        self.inv.remove('Half Drunk Potion')
                    elif wp == 'Simple Potion':
                        self.hp += random.randint(15,20)
                        MaxHp(self)
                        Type(f"The potion restored your health! You have {self.hp} hp.")
                        self.inv.remove('Simple Potion')
                    elif wp == 'Spicy Potion':
                        self.hp += random.randint(20,40)
                        MaxHp(self)
                        Type(f"The potion restored your health! You have {self.hp} hp.")
                        self.inv.remove('Spicy Potion')
                    elif wp == 'Nasty Potion':
                        self.hp += random.randint(50,70)
                        MaxHp(self)
                        Type(f"The potion restored your health! You have {self.hp} hp.")
                        self.inv.remove('Spicy Potion')
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
                        elif self.location.fmap['$'] == 'Slime1':
                            info(self.location.py_y,self.location.py_x,self,Slime1,Enemies)
                            Attack(self,Slime1)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                        if self.location.fmap['#'] == 'Goblin2':
                            info(self.location.py_y,self.location.py_x,self,Gob2,Enemies)
                            Attack(self,Gob2)
                        elif self.location.fmap['#'] == 'Slime2':
                            info(self.location.py_y,self.location.py_x,self,Slime2,Enemies)
                            Attack(self,Slime2)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "%":
                        if self.location.fmap['%'] == 'Goblin3':
                            info(self.location.py_y,self.location.py_x,self,Gob3,Enemies)
                            Attack(self,Gob3)
                        elif self.location.fmap['%'] == 'Slime3':
                            info(self.location.py_y,self.location.py_x,self,Slime3,Enemies)
                            Attack(self,Slime3)
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
                        elif self.location.fmap['$'] == 'Slime1':
                            info(self.location.py_y,self.location.py_x,self,Slime1,Enemies)
                            Attack(self,Slime1)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                        if self.location.fmap['#'] == 'Goblin2':
                            info(self.location.py_y,self.location.py_x,self,Gob2,Enemies)
                            Attack(self,Gob2)
                        elif self.location.fmap['#'] == 'Slime2':
                            info(self.location.py_y,self.location.py_x,self,Slime2,Enemies)
                            Attack(self,Slime2)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "%":
                        if self.location.fmap['%'] == 'Goblin3':
                            info(self.location.py_y,self.location.py_x,self,Gob3,Enemies)
                            Attack(self,Gob3)
                        elif self.location.fmap['%'] == 'Slime3':
                            info(self.location.py_y,self.location.py_x,self,Slime3,Enemies)
                            Attack(self,Slime3)
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
                        elif self.location.fmap['$'] == 'Slime1':
                            info(self.location.py_y,self.location.py_x,self,Slime1,Enemies)
                            Attack(self,Slime1)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                        if self.location.fmap['#'] == 'Goblin2':
                            info(self.location.py_y,self.location.py_x,self,Gob2,Enemies)
                            Attack(self,Gob2)
                        elif self.location.fmap['#'] == 'Slime2':
                            info(self.location.py_y,self.location.py_x,self,Slime2,Enemies)
                            Attack(self,Slime2)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "%":
                        if self.location.fmap['%'] == 'Goblin3':
                            info(self.location.py_y,self.location.py_x,self,Gob3,Enemies)
                            Attack(self,Gob3)
                        elif self.location.fmap['%'] == 'Slime3':
                            info(self.location.py_y,self.location.py_x,self,Slime3,Enemies)
                            Attack(self,Slime3)
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
                        elif self.location.fmap['$'] == 'Slime1':
                            info(self.location.py_y,self.location.py_x,self,Slime1,Enemies)
                            Attack(self,Slime1)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "#":
                        if self.location.fmap['#'] == 'Goblin2':
                            info(self.location.py_y,self.location.py_x,self,Gob2,Enemies)
                            Attack(self,Gob2)
                        elif self.location.fmap['#'] == 'Slime2':
                            info(self.location.py_y,self.location.py_x,self,Slime2,Enemies)
                            Attack(self,Slime2)
                    elif self.location.mapper[self.location.py_y][self.location.py_x] == "%":
                        if self.location.fmap['%'] == 'Goblin3':
                            info(self.location.py_y,self.location.py_x,self,Gob3,Enemies)
                            Attack(self,Gob3)
                        elif self.location.fmap['%'] == 'Slime3':
                            info(self.location.py_y,self.location.py_x,self,Slime3,Enemies)
                            Attack(self,Slime3)
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
            if random.randint(x.ran[0],x.ran[1]) == x.ran[1]:
                Check_Full(self,x.drops)
                Type(f"The {x.name} dropped a {x.drops}.")
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
                Check_Full(self,"Tiny Knife")
        if 'Defeated Guard' in self.cuts:
            Type(f"[Guard]: You? Defeated me? May you have mercy on our small island of Javara.")
            Type(f"[Guard]: We did not intend to fall onto your magicless land. Alas one of our own sabatagoted us.")
            MainCity.mapper[5][6] = '.'
            global last_loc
            last_loc = MainCity
        self.gold += gold
        self.exp += exp
        self.location = last_loc
        Exp(self)
        MaxHp(self)

    def Actions(self):
        while True:
            key = readchar.readkey()
            self.location.mapper[self.location.l_y][self.location.l_x] = self.location.Last1
            if key == 'x':
                Type("What item would you like to drop?")
                if 'Help3' not in self.cuts:
                    Type("[Tutorial]: Be careful if you drop an item you can never get it back.")
                    Type("[Tutorial]: You can sell random items to Marina instead?")
                    self.cuts.append("Help3")
                for o,i in enumerate(self.inv):
                    print(f"{o} - {i}")
                items = dict(enumerate(self.inv))
                item = input("Enter the number. > ")
                try: 
                    self.inv.remove(items[int(item)])
                except:
                    print("You don't have that item.")
            if key == 'e':
                if self.location.Last1 == '~':
                    Randomise(self)
                else:
                    Type("There is nothing to see here...")
            if key == 'o':
                a = input("Hp - int > ")
                b = input("Inv - list > ").split(',')
                c = input("Gold - int > ")
                d = input("Lvl - int > ")
                self.SetStats(int(a),b,int(c),int(d))
            if key == 'z':
                Exp(self)
                MaxHp(self)
                Type(f"{self.name} - at the {self.location.name}")
                Type(f"Hp: {self.hp}/{self.maxhp}")
                Type(f"Lvl: {self.lvl}")
                Type(f"{self.Rexp} exp is required to level up!")
                Type(f"Gold: {self.gold}")
                Type(f"Back Capacity: {len(self.inv)}/30")
                print("Currently has these items:")
                print(self.inv)
                if self.curq == '':
                    Type(f"{self.name} is currently not doing any quests.")
                else:
                    Type(f"{self.name} is currently doing {self.curq} quest.")
                print("Would you like to see all actions? (y/n)")
                key = readchar.readkey()
                if key == 'y':
                    print("'z' - Check player Status")  #Finish this list 
                    print("'x' - Remove an Item from Inventory")
                    print("'e' - Investigate the area")
                    print("'q' - Use an item")
                    print("'p' - Save & Quit")        
                input("Click enter to continue...")
            if key == 'q':
                Type("What item would you like to use?")
                for o,i in enumerate(self.inv):
                    print(f"{o} - {i}")
                items = dict(enumerate(self.inv))
                item = input("Enter the number. > ")
                try: 
                    a = items[int(item)]
                    if a == 'Half Drunk Potion':
                        self.hp += random.randint(5,10)
                        MaxHp(self)
                        Type(f"The potion restored your health! You have {self.hp} hp.")
                        self.inv.remove('Half Drunk Potion')
                    elif a == 'Simple Potion':
                        self.hp += random.randint(15,20)
                        MaxHp(self)
                        Type(f"The potion restored your health! You have {self.hp} hp.")
                        self.inv.remove('Simple Potion')
                    elif a == 'Spicy Potion':
                        self.hp += random.randint(5,10)
                        MaxHp(self)
                        Type(f"The potion restored your health! You have {self.hp} hp.")
                        self.inv.remove('Spicy Potion')
                    else:
                        Type("You can't use that item.")
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
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "£": 
                    info = self.location.emap['£']
                    info(self)
                    self.location.py_y += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "$": 
                    info = self.location.emap['$']
                    info(self)
                    self.location.py_y += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "%": 
                    info = self.location.emap['%']
                    info(self)
                    self.location.py_y += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "?": 
                    info = self.location.emap['?']
                    info(self)
                    self.location.py_y += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "!": 
                    info = self.location.emap['!']
                    info(self)
                    self.location.py_y += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "^": 
                    info = self.location.emap['^']
                    self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "_":
                    if 'Kai' not in self.cuts:
                        Looting_Tutorial(self)
                        self.location.py_y += 1
                        continue
                    else:
                        info = self.location.emap['_']
                        self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "-": 
                    info = self.location.emap['-']
                    self.location = info
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
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "£": 
                    info = self.location.emap['£']
                    info(self)
                    self.location.py_y -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "$": 
                    info = self.location.emap['$']
                    info(self)
                    self.location.py_y -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "%": 
                    info = self.location.emap['%']
                    info(self)
                    self.location.py_y -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "?": 
                    info = self.location.emap['?']
                    info(self)
                    self.location.py_y -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "!": 
                    info = self.location.emap['!']
                    info(self)
                    self.location.py_y -= 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "^": 
                    info = self.location.emap['^']
                    self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "_": 
                    info = self.location.emap['_']
                    self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "-": 
                    info = self.location.emap['-']
                    self.location = info
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
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "£": 
                    info = self.location.emap['£']
                    info(self)
                    self.location.py_x += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "$": 
                    info = self.location.emap['$']
                    info(self)
                    self.location.py_x += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "%": 
                    info = self.location.emap['%']
                    info(self)
                    self.location.py_x += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "?": 
                    info = self.location.emap['?']
                    info(self)
                    self.location.py_x += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "!": 
                    info = self.location.emap['!']
                    info(self)
                    self.location.py_x += 1
                    continue
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "^": 
                    info = self.location.emap['^']
                    self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "_": 
                    info = self.location.emap['_']
                    self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "-": 
                    info = self.location.emap['-']
                    self.location = info
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
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "?": 
                    info = self.location.emap['?']
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
                    self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "_": 
                    info = self.location.emap['_']
                    self.location = info
                elif self.location.mapper[self.location.py_y][self.location.py_x] == "-": 
                    info = self.location.emap['-']
                    self.location = info
                else:
                    self.location.Last1 = self.location.mapper[self.location.py_y][self.location.py_x]
                    self.location.l_y = self.location.py_y
                    self.location.l_x = self.location.py_x
                    self.location.mapper[self.location.py_y][self.location.py_x] = '@'
            self.location.Update()
    def SetStats(self,hp,inv,gold,lvl):
        self.hp = hp
        self.inv = inv
        self.gold = gold
        self.lvl = lvl

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
        print(f'HP: {player.hp}/{player.maxhp}\nEQUIPPED WEAPON: {v}\nITEMS: {x}')

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
    Check_Full(player,"Fire Amulet")
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
            Type("NEW QUEST!\n>>>The Disguised Ruin Hunter<<<")
            time.sleep(1)
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

Harley = Shop(['Sword','Dagger','Axe'],{'Sword':40,'Dagger':15,'Axe':70})

def Weapons_Shop(player): # Harley
    if 'Wep' not in player.cuts:
        Type(f"[???]: Oh! Welcome vistor, its nice to see a new face around here.")
        Type(f"[Harley]: My name is Harley, and you are?")
        Type(f"[{player.name}]: I'm {player.name}.")
        Type(f"[Harley]: Well, {player.name} if you need anything to protect yourself, I've got weapons!")
        Type("[Harley]: I'm even developing a gun-styled magic weapon, inspired by your land!") 
        Type("[Harley]: It's not finished yet unfortunately...")
        Type("Ask about magic weapons? (y/n)")
        key = readchar.readkey()
        if key == 'y':
            Type(f"[{player.name}]: You make magic weapons?")
            Type("[Harley]: Yep! I even recharge them too - but you'll need to get the materials yourself.")
            Type("[Harley]: I need to run the shop after all...")
            Type("Ask about materials? (y/n)")
            key = readchar.readkey()
            if key == 'y':
                Type(f"[{player.name}]: Can't you buy the materials?")
                Type(f"[Harley]: Well usually I would buy materials from Dhara, but ever since the Fall. I don't trust him...")
                player.cuts.append("Wep2")
                Type("Ask about the Fall? (y/n)")
                key = readchar.readkey()
                if key == 'y':
                    Type(f"[{player.name}]: What's the Fall?")
                    Type("[Harley]: You don't know? I thought a vistor like you would be caught up on recent news in your land?")
                    Type("[Harley]: This Island used to float in the sky above your land's ocean. Now it doesn't. That was the Fall.")
                    Type("Ask for a better explaination. (y/n)")
                    key = readchar.readkey()
                    if key == 'y':
                        Type(f"[{player.name}]: Could I have a better explaination? Like what exactly caused you to fall?")
                        Type("[Harley]: ...")
                        time.sleep(2)
                        Type("[Harley]: Are you buying something or not?")


        player.cuts.append('Wep')
    if 'Solve' not in player.curq and player.lvl > 2 and 'Solve' not in player.cuts:
        Type(f"[Harley]: Hello, {player.name}. The Guardian of the Mylva temple has set an interesting puzzle at the entrance of the temple!")
        Type(f"[Harley]: Apparently, the puzzle is based on the Tenja Temple and it is SO HARD to solve. Could you solve it?")
        Type("[Harley]: Mind, you have to go to the temple to confirm you are correct.")
        Type("Accept? (y/n)")
        key = readchar.readkey()
        if key == 'y':
            Type(f"[Harley]: Great! Come back and tell me once you've solved it. I just want to the know the solution!")
            player.curq.append("Solve")
            Type("NEW QUEST!")
            Type(">>>The Puzzle of the Mylva Temple<<<")
        else:
            Type(f"[Harley]: That's ok, it is a very difficult puzzle after all.")
        player.cuts.append('Solve')
    if 'Solved' in player.compq and 'Solved' not in player.cuts:
        Type(f"[{player.name}]: So the solution was actually this...")
        Type(f"[Harley]: Interesting well thank you.")
        player.cuts.apppend('Solved')
        Type("QUEST COMPLETED!")
    Type("[Harley]: So do you want to look at my assortment of weapons? Or do you need some magic? (w/r/c)")
    key = readchar.readkey()
    if key == 'w':
        Type("[Harley]: These is all my weapons!")
        for x,i in enumerate(Harley.stock):
            print(f"{x} - {i} costs {Harley.mapper[i]} Gold")
        Type("[Harley]: Which would you like?")
        try:
            num = int(input("Enter the Number. > "))
            a = player.gold - Harley.mapper[Harley.stock[num]]
            if a < 0:
                Type("[Harley]: You're short. Come back when you have enough gold.")
            else:
                player.gold = a
                Check_Full(player,Harley.stock[num])
                Harley.stock.remove(Harley.stock[num])
                Type("[Harley]: Hope you like it!")
        except:
            Type("[Harley]: That item is not for sale...")
    elif key == 'r':
        Type("[Harley]: You want a recharge? I'll need the gem of the amulet and some Gold to do it.")
        Type("[Harley]: Show me the one you want to recharge.")
        list = ['Fire Amulet','Ice Amulet','Cool Amulet','Hot Amulet']
        for i,x in enumerate(list):
            print(f"{i} - {x}")
        try:
            num = int(input("Enter the Number. > "))
            a = list[num]
            if a == 'Fire Amulet':
                if 'Fire Amulet' not in player.inv or 'Fire Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: How many recharges? They cost 10 Gold each.")
                    num = int(input("Enter the Number. > ")) * 10
                    if num > player.gold:
                        Type("[Harley]: You're short. Come back when you have enough gold.")
                    else:
                        Fire.char += num//10
                        player.inv.remove("Fire Gem")
                        player.gold -= num
                        Type(f"[Harley]: I'm Done! You now have {Fire.char} charges.")
            elif a == 'Ice Amulet':
                if 'Ice Amulet' not in player.inv or 'Ice Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: How many recharges? They cost 15 Gold each.")
                    num = int(input("Enter the Number. > ")) * 15
                    if num > player.gold:
                        Type("[Harley]: You're short. Come back when you have enough gold.")
                    else:
                        Ice.char += num//15
                        player.inv.remove("Ice Gem")
                        player.gold -= num
                        Type(f"[Harley]: I'm Done! You now have {Ice.char} charges.")
            elif a == 'Cool Amulet':
                if 'Cool Amulet' not in player.inv or 'Cool Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: How many recharges? They cost 20 Gold each.")
                    num = int(input("Enter the Number. > ")) * 20
                    if num > player.gold:
                        Type("[Harley]: You're short. Come back when you have enough gold.")
                    else:
                        player.gold -= num
                        Cool.char += num//20
                        player.inv.remove("Cool Gem")
                        Type(f"[Harley]: I'm Done! You now have {Cool.char} charges.")
            elif a == 'Hot Amulet':
                if 'Hot Amulet' not in player.inv or 'Refined Clear Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: How many recharges? They cost 25 Gold each.")
                    num = int(input("Enter the Number. > ")) * 25
                    if num > player.gold:
                        Type("[Harley]: You're short. Come back when you have enough gold.")
                    else:
                        player.gold -= num
                        Hot.char += num//25
                        player.inv.remove("Refined Clear Gem")
                        Type(f"[Harley]: I'm Done! You now have {Hot.char} charges.")
        except:
            Type("[Harley]: Hahahaha. That's not an amulet.")
    elif key == 'c':
        Type(f"[Harley]: So you want me to craft something, {player.name}? What base material have you brought for me?")
        list = ['Sword','Dagger','Axe','Fire Gem','Ice Gem','Cool Gem','Clear Gem','Refined Clear Gem']
        for i,x in enumerate(list):
            print(f"{i} - {x}")
        try:
            num = int(input("Enter the Number. > "))
            a = list[num]
            if a == 'Sword':
                if 'Sword' not in player.inv or 'Clear Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: I've got an idea! I could enhance this sword with a gem! I require 5 Gold. (y/n)")
                    key = readchar.readkey()
                    if key == 'y':
                        num = 5
                        Type("[Harley]: Let me cook.")
                        if num > player.gold:
                            Type("[Harley]: You're short. Come back when you have enough gold.")
                        else:
                            Check_Full(player,"Enhanced Sword")
                            player.inv.remove('Sword')
                            player.inv.remove("Clear Gem")
                            player.gold -= num
                            Type(f"[Harley]: I'm Done! You now have a Enhanced Sword!")
                    else:
                        Type("[Harley]: You are missing out. Oh well.")
            elif a == 'Dagger':
                if 'Dagger' not in player.inv or 'Clear Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: I've got an idea! I could enhance this dagger with a gem! I require 5 Gold. (y/n)")
                    key = readchar.readkey()
                    if key == 'y':
                        num = 5
                        Type("[Harley]: Let me cook.")
                        if num > player.gold:
                            Type("[Harley]: You're short. Come back when you have enough gold.")
                        else:
                            Check_Full(player,"Enhanced Dagger")
                            player.inv.remove('Dagger')
                            player.inv.remove("Clear Gem")
                            player.gold -= num
                            Type(f"[Harley]: I'm Done! You now have a Enhanced Dagger!")
                    else:
                        Type("[Harley]: You are missing out. Oh well.")                   
            elif a == 'Axe':
                if 'Axe' not in player.inv or 'Clear Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: I've got an idea! I could enhance this axe with a gem! I require 10 Gold. (y/n)")
                    key = readchar.readkey()
                    if key == 'y':
                        num = 5
                        Type("[Harley]: Let me cook.")
                        if num > player.gold:
                            Type("[Harley]: You're short. Come back when you have enough gold.")
                        else:
                            Check_Full(player,"Enhanced Axe")
                            player.inv.remove('Axe')
                            player.inv.remove("Clear Gem")
                            player.gold -= num
                            Type(f"[Harley]: I'm Done! You now have a Enhanced Axe!")
                    else:
                        Type("[Harley]: You are missing out. Oh well.")                  
            elif a == 'Fire Gem':
                if 'Fire Gem' not in player.inv or 'Clear Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: Boring... I have to make another fire amulet? It costs 5 gold by the way. (y/n)")
                    key = readchar.readkey()
                    if key == 'y':
                        num = 5
                        Type("[Harley]: This is too easy.")
                        if num > player.gold:
                            Type("[Harley]: You're short. Come back when you have enough gold.")
                        else:
                            player.inv.append('Fire Amulet')
                            player.inv.remove('Fire Gem')
                            player.inv.remove("Clear Gem")
                            player.gold -= num
                            Type(f"[Harley]: Here you go. Another Amulet.")
                    else:
                        Type("[Harley]: Oh! You want me to make something else?")     
            elif a == 'Ice Gem':
                if 'Ice Gem' not in player.inv or 'Clear Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: Boring... I have to make another ice amulet? It cost five gold by the way. (y/n)")
                    key = readchar.readkey()
                    if key == 'y':
                        num = 5
                        Type("[Harley]: This is too easy.")
                        if num > player.gold:
                            Type("[Harley]: You're short. Come back when you have enough gold.")
                        else:
                            player.inv.append('Ice Amulet')
                            player.inv.remove('Ice Gem')
                            player.inv.remove("Clear Gem")
                            player.gold -= num
                            Type(f"[Harley]: Here you go. Another Amulet.")
                    else:
                        Type("[Harley]: Oh! You want me to make something else?")
            elif a == 'Cool Gem':
                if 'Cool Gem' not in player.inv or 'Clear Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: Boring... I have to make another cool amulet? It cost 5 gold by the way (y/n)")
                    key = readchar.readkey()
                    if key == 'y':
                        num = 5
                        Type("[Harley]: This is too easy.")
                        if num > player.gold:
                            Type("[Harley]: You're short. Come back when you have enough gold.")
                        else:
                            player.inv.append('Cool Amulet')
                            player.inv.remove('Cool Gem')
                            player.inv.remove("Clear Gem")
                            player.gold -= num
                            Type(f"[Harley]: Here you go. Another Amulet.")
                    else:
                        Type("[Harley]: Oh! You want me to make something else?")
            elif a == 'Clear Gem':
                if 'Clear Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: Hmm I has never thought as using this a base material... I'll see what I can do. For 5 gold though. (y/n)")
                    key = readchar.readkey()
                    if key == 'y':
                        num = 5
                        Type("[Harley]: I'm excited to try this out!")
                        if num > player.gold:
                            Type("[Harley]: You're short. Come back when you have enough gold.")
                        else:
                            player.inv.remove("Clear Gem")
                            player.gold -= num
                            Type(f"[Harley]: Sorry it didn't work. Maybe if the Clear Gem was more pure? And I had a fiery addtion.")
                    else:
                        Type("[Harley]: Really? Don't worry I'll try it in my own time.")
            elif a == 'Refined Clear Gem':
                if 'Refined Clear Gem' not in player.inv or 'Fire Gem' not in player.inv:
                    Type("[Harley]: You don't have the required materials.")
                else:
                    Type("[Harley]: Nice! You've got just what I needed! If this works I'll give you a charge free of charge! Hahaha! (y/n)")
                    Type("[Harley]: Still costs 5 gold though...")
                    key = readchar.readkey()
                    if key == 'y':
                        num = 5
                        Type("[Harley]: I've got this! It should work now.")
                        if num > player.gold:
                            Type("[Harley]: You're short. Come back when you have enough gold.")
                        else:
                            player.inv.append('Hot Amulet')
                            player.inv.remove('Fire Gem')
                            player.inv.remove("Refined Clear Gem")
                            player.gold -= num
                            Type(f"[Harley]: I did it! And the power radiating off this Amulet... It's simlar to the levitation gem...")
                            Type(f"Ask about Leviation Gem? (y/n)")
                            key = readchar.readkey()
                            if key == 'y':
                                Type(f"[{player.name}]: Levitation gem? Is that what caused this island to float?")
                                Type(f"[Harley]: You heard nothing. Vistors should not know about that...")
                    else:
                        Type("[Harley]: I even said I would give you a free charge?")
        except:
            Type("[Harley]: I can't craft anything with that.")
            
Dhara = Shop(['Fire Amulet','Ice Amulet','Cool Amulet','Hot Amulet','Clear Gem','Refined Clear Gem','Fire Gem','Ice Gem','Cool Gem','Gold'],{'Fire Amulet':30,'Ice Amulet':50,'Cool Amulet':70,'Hot Amulet':100,'Clear Gem':1,'Refined Clear Gem':5,'Fire Gem':10,'Ice Gem':15,'Cool Gem':20,'Gold':1})
def Conversion(player): #Dhara
    if 'Con' not in player.cuts:
        Type(f"[???]: Great! A new customer - Welcome {player.name} to Javara!")
        Type(f"[{player.name}]: How do you know my name?")
        Type(f"[???]: Well, I'm the one who helps to organise who comes into Javara from your land.")
        Type(f"[Dhara]: My name is Dhara - the assistant ambassador for Javara.")
        Type("[Dhara]: I'm your contact to your land whilst you are here. And I'll even exchange things you aquire here for dollars.") 
        Type("[Dhara]: Lots of Dollars.")
        Type("Ask about the exchange? (y/n)")
        key = readchar.readkey()
        if key == 'y':
            Type(f"[{player.name}]: What kind of things do you exchange?")
            Type("[Dhara]: Amulets, Gems, Gold. Anything valuable - I don't exchange useless items.")
            Type("[Dhara]: Stuff like that you can sell to Marina instead.")
        if 'Wep2' in player.cuts:   
            Type("Ask about Harley distrusting him? (y/n)")
            key = readchar.readkey()
            if key == 'y':
                Type(f"[{player.name}]: How come Harley thinks you're responsible for the Fall?")
                Type(f"[Dhara]: Wow. You are quite... Blunt. Alas, you are a potential customer so I'll answer your question.")
                Type("[Dhara]: I was one of the first to make contact with your people and I stand to profit from all of you vistors.")
                Type("[Dhara]: Objectively, I seem like the most likely subject. I may be a business man but I do have standards.")
                Type("Ask who Dhara thinks caused the Fall? (y/n)")
                key = readchar.readkey()
                if key == 'y':
                    Type(f"[{player.name}]: Who do you think caused it then.")
                    Type("[Dhara]: I don't think my opinon on this matter is necessary.")
                    Type("[Dhara]]: Yet. The Ruin Hunters have grown in number and power after the Fall.")
                    Type("[Dhara]: Just a little tip for my future customer.")
        player.cuts.append('Con')
    Type("[Dhara]: So do you want to convert your items? The exchange rate is 1 Gold to $1,000 (y/n)")
    key = readchar.readkey()
    if key == 'y':
        Type("[Dhara]: Select an item! The prices are set as seen, no-one else here does exchanges.")
        for x,i in enumerate(Dhara.stock):
            print(f"{x} - {i} for {Dhara.mapper[i]} Gold")
        try:
            num = int(input("Enter the Number. > "))
            if Dhara.stock[num] == 'Gold':
                Type("[Dhara]: How much gold do you want to exchange?")
                num = int(input("Enter the Number. > "))
                if num <= player.gold:
                    player.gold -= num
                    global dollar_count
                    dollar_count += num * 1000
                    Type(f"[Dhara]: Here, I've transferred the money. In total I've given you ${dollar_count}.")
                else:
                    Type("[Dhara]: Don't try and cheat me. It's a waste of time.")
            else:
                dollar_count += Dhara.mapper[Dhara.stock[num]]*1000
                Type(f"[Dhara]: Ah, a {Dhara.stock[num]}. I'll transfer {Dhara.mapper[Dhara.stock[num]]*1000} for this.")
                Type(f"[Dhara]: In total I have transferred ${dollar_count} to you. It was a pleasure doing business with you.")
        except:
            Type("[Dhara]: I don't exchange those types of items...")

def Shady_Merchant(player):# Taylor the Ruin Hunter
    if 'Shad' not in player.cuts:
        if 'Ruin Hunter' in player.curq:
            Type(f"[{player.name}]: You're the ruin hunter I was talking to online correct? Taylor?")
            Type(f"[Taylor]: Yes, you are {player.name} I believe. I'm happy you made it.")
            Type(f"[{player.name}]: Passing the test to get to Javara wasn't very difficult when I have an inside man.")
            Type(f"[{player.name}]: A stray summon even attacked me and I got a free amulet.")
            Type("[Taylor]: Which one?")
            Type(f"[{player.name}]: A fire amulet. It seems quite powerful.")
            Type("[Taylor]: Yes it is. But you need to recharge or it will lose its power. I'll recharge it for you.")
            Type("[Taylor]: Well, I can see how compentent you are already. I've got a hunting spot for you. Yet, I fear it may be too easy for you.")
            Type("QUEST COMPLETED!")
            Type(">>>RUIN HUNTER<<<")
            Type("Reward: 20 Exp!")
            player.cuts.append("Joined")
            player.curq.remove('Ruin Hunter')
            player.compq.append("Ruin Hunter")
            player.exp += 20
            Exp(player)
            MaxHp(player)
        else:
            Type("[???]: Get lost.")
            Type("Leave? (y/n)")
            key = readchar.readkey()
            if key == 'n':
                Type(f"[{player.name}]: Why should I? I'm just a vistor - if you didn't want vistors to bother you...")
                Type(f"[{player.name}]: You should've said at home.")
                Type(f"[Taylor]: Confident. I like you. The name's Taylor.")
                Type(f"[Taylor]: How about you assist some of your vistor friends by joining my crew - The Ruin Hunters.")
                Type(f"[{player.name}]: Ruin Hunters? What do you do?")
                Type(f"[Taylor]: We loot the ruins of this land and sell the spoils to your land.")
                Type(f"[Taylor]: Join us, any spoils you get you can sell to Dhara - so long as you hunt where the boss tells you.")
                Type("Join? (y/n)")
                key = readchar.readkey()
                if key == 'y':
                    Type(f"[Taylor]: Wonderful. I've got your first hunting spot ready.")
                    player.cuts.append("Joined")
                else:
                    Type(f"[Taylor]: No? I've never had a vistor refuse before... You know too much.")
                    Type(f"[Taylor]: You are lucky that guard in the corner is watching over the square.")
                    Type(f"[Taylor]: Watch your back. It's not only summons that will attack you now...")
                    MainCity.mapper[3][5] = '.'
        player.cuts.append('Shad')
    if 'Joined' in player.cuts:
        if 'Tenja' not in player.cuts:
            Type(f"[Taylor]: The first hunting spot I have for you is the Tenja Temple.")
            Type(f"[Taylor]: It's at the end of the Tenja Path, it looks like this '_' from here.")
            Type(f"[Taylor]: There are only simple summons on that path and in the temple.")
            Type(f"[Taylor]: The Guardian is quite weak - you so find it easy.")
            Type(f"[Taylor]: Bring back the staff of Tenja to prove you killed the Guardian.")
            Type(f"[Taylor]: Don't worry you can keep it.")
            Type("NEW QUEST!\n>>>Defeat the Tenja Guardian<<<")
            player.curq.append("Defeat Tenja")
            player.cuts.append('Tenja')
        elif 'Defeat Tenja' not in player.cuts:
            if 'The Tenja Staff' not in player.inv:
                Type(f"[Taylor]: Come back when you have proof you killed the Tenja Guardian.")
                Type(f"[Taylor]: {player.name}, I thought you would find this hunt easy?")
            else:
                Type("[Taylor]: Amazing. The staff looks even better in person!")
                Type("QUEST COMPLETED!\n>>>Defeat the Tenja Guardian<<<")
                player.cuts.append("Defeat Tenja")
                player.compq.append('Defeat Tenja')
        if 'Mylva' not in player.cuts and "Defeat Tenja" in player.compq:
            Type(f"[Taylor]: The second hunting spot I have for you is the Mylva Temple.")
            Type(f"[Taylor]: It's at the end of the Mylva Path, it looks like this '^' from here.")
            Type(f"[Taylor]: It's a trouble to get in as the Guardian recently made a puzzle you must solve for entry.")
            Type(f"[Taylor]: I've got one of the native Ruin hunters to help you out - Arden.")
            Type(f"[Taylor]: He should solve that puzzle and all you need to do is kill the Guardian.")
            Type(f"[Taylor]: Make sure to bring the shield here.")
            Type("NEW QUEST!\n>>>Defeat the Mylva Guardian<<<")
            player.curq.append("Defeat Mylva")
            player.cuts.append('Mylva')
        elif 'Defeat Mylva' not in player.cuts and "Defeat Tenja" in player.compq:
            if 'The Mylva Shield' not in player.inv:
                Type("[Taylor]: Solve the puzzle, kill the guardian, bring the shield.")
                Type("[Taylor]: Simple. Now do it.")
            else:
                Type("[Taylor]: Good job. Now there is only one relic left for you to obtain.")
                Type("QUEST COMPLETED!\n>>>Defeat the Mylva Guardian<<<")
                player.compq.append("Defeat Mylva")
                player.cuts.append('Defeat Mylva')
        if 'Defeat Xira' not in player.cuts and "Defeat Mylva" in player.compq:
            if 'The Xira Crown' not in player.inv:
                Type("[Taylor]: Not even you can aquire the crown?")
                Type("[Taylor]: Try again... If we aquire all three relics, we could bring magic to your land!")
            else:
                Type("[Taylor]: I think it's time you met the Boss. He has requested that you show him the relics.")
                Type("[Taylor]: Go to the Great Temple. The Guard may try to stop you but you are strong. The Boss will meet you there.")
            player.compq.append("Defeat Xira")
            player.cuts.append('Defeat Xira')
            Type("NEW QUEST!\n>>>Meet the Boss of the Ruin Hunters<<<")
            player.curq.append("Meet")
            player.cuts.append('Xira')
        elif 'Xira' not in player.cuts and "Defeat Mylva" in player.compq:
            Type(f"[Taylor]: This time you need to go to the Xira Temple. It's very dangerous so be careful.")
            Type(f"[Taylor]: It's at the end of the Xira Path, it looks like this '-' from here.")
            Type(f"[Taylor]:The Guardian is very strong so make sure to focus your attacks on weaker followers first.")
            Type(f"[Taylor]: And make sure to get a lot of potions. I'll give you two to assist you.")
            Check_Full(player,'Simple Potion')
            Check_Full(player,'Simple Potion')
            Type(f"[Taylor]: Unfortunately, I can't get any other Ruin Hunters to assist you.")
            Type(f"[Taylor]: They are working hard to cover up the deaths of the other Guardians.\n[Taylor]: Make sure to bring the crown back here.")
            Type("NEW QUEST!\n>>>Defeat the Xira Guardian<<<")
            player.curq.append("Defeat Xira")
            player.cuts.append('Xira')  
    else:
        Type("[???]: Didn't I tell you to get lost? Beat it.")

Marina = Shop(['Simple Potion','Spicy Potion','Nasty Potion'],{'Simple Potion':10,'Spicy Potion':20,'Nasty Potion':50})
Marina2 = Shop(['Glowing Skull','Troll Nail','Sprite Essence','Slime Goo','Goblin Ear','Frying Pan','Worn Boots','Simple Potion','Spicy Potion','Nasty Potion','Clear Gem','Refined Clear Gem','Fire Gem Ore','Fire Gem','Ice Gem Ore','Ice Gem','Cool Gem Ore','Cool Gem','Fire Amulet','Ice Amulet','Cool Amulet','Hot Amulet','Axe','Sword','Dagger','Tiny Knife','Enhanced Dagger','Enhanced Axe','Enhanced Sword'],{'Glowing Skull':50,'Troll Nail':35,'Sprite Essence':25,'Slime Goo':15,'Goblin Ear':5,'Frying Pan':1,'Worn Boots':1,'Simple Potion':10,'Spicy Potion':20,'Nasty Potion':30,'Clear Gem':1,'Refined Clear Gem':5,'Fire Gem Ore':5,'Fire Gem':10,'Ice Gem Ore':15,'Ice Gem':20,'Cool Gem Ore':30,'Cool Gem':40,'Fire Amulet':10,'Ice Amulet':20,'Cool Amulet':30,'Hot Amulet':50,'Axe':30,'Sword':20,'Dagger':10,'Tiny Knife':5,'Enhanced Dagger':20,'Enhanced Axe':60,'Enhanced Sword':40})
def Potion_Geek(player):# Marina
    if 'Pot' not in player.cuts:
        Type("[???]: Hello, you're a vistor aren't you? What's your name?")
        Type(f"[{player.name}]: I'm {player.name}.")
        Type("[Marina]: My name is Marina, would you like to try out my potions?")
        if player.hp < player.maxhp:
            Type("[Marina]: I can see you've taken some damage from some summons...")
            Type("[Marina]: I can sell you some potions - they heal wounds instantly!")
            Type("[Marina]: A far upgrade from the medicene in your land.")
        else:
            Type("[Marina]: Some how you're unscathed from our summons...")
            Type("[Marina]: Your luck won't last forever! I suggest you get some potions just in case.")
        player.cuts.append('Pot')
    Type("[Marina]: Wanna buy some potions? I brewed them today! Or are you here to sell something? (p/s)")
    key = readchar.readkey()
    if key == 'p':
        Type("[Marina]: These is all my potions!")
        for x,i in enumerate(Marina.stock):
            print(f"{x} - {i} costs {Marina.mapper[i]} Gold")
        Type("[Marina]: Which would you like?")
        try:
            num = int(input("Enter the Number. > "))
            a = player.gold - Marina.mapper[Marina.stock[num]]
            if a < 0:
                Type("[Marina]: Sell me some of your items, then maybe you'll have enough gold?")
            else:
                player.gold = a
                Check_Full(player,Marina.stock[num])
                Type("[Marina]: Hope you like it!")
        except:
            Type("[Marina]: I don't sell those types of potions...")
    elif key == 's':
        Type("[Marina]: Ooooooh! What have you brought for me? I'll buy anything you found here off you.")
        for x,i in enumerate(Marina2.stock):
            print(f"{x} - {Marina2.mapper[i]} Gold for {i}")
        try:
            num = int(input("Enter the Number. > "))
            if Marina2.stock[num] in player.inv:
                Type("[Marina]: Nice, I can add this to my collection! I'm sure I can make a potion from this.")
                player.inv.remove(Marina2.stock[num])
                player.gold += Marina2.mapper[Marina2.stock[num]]
            else:
                Type("[Marina]: If you don't have the item don't waste my time. And don't get my hopes up.")
        except:
            Type("[Marina]: That doesn't exist... Is that something useful from your land?")

def Looting_Tutorial(player):
    os.system('cls')
    commap = [["#","_","#","^","#","-","#","#"],
        ["#","?",".",".",".",".",".","#"],
        ["#","@","£","~","~","%",".","#"],
        ["#",".","$","~","~","!",".","#"],
        ["|",".",".",".",".",".","&","}"],
        ["#","#","#","#","#","#","#","#"]]
    for row in commap:
            print(' '.join(map(str, row)))
    Type(f"[???]: Oh! Sorry, I didn't mean to bump into you. Are you ok? (y/n)")
    key = readchar.readkey()
    if key == 'y':
        Type(f"[{player.name}]: Yes, I'm fine. Are you?")
        Type("[Kai]: I am. My name is Kai by the way. I haven't seen you around so you must be a vistor too right? (y/n)")
        key = readchar.readkey()
        if key == 'y':
            Type(f"[{player.name}]: Yes, I just got here today. What were you doing past there?")
            Type("[Kai]: I was excavating and found some cool gems! They shimmer because of the magic they contain!")
            Type("[Kai]: Amazing right! I can see some here in the square but I won't mind if you investigate them instead?")
            Type(f"[{player.name}]: Investigate?")
            Type("[Kai]: Hunt, Loot... Just find small treasures to take back to Earth you know.")
        if key == 'n':
            Type(f"[{player.name}]: No? I've lived here my whole life.")
            Type("[Kai]: Really? I had a feeling you were... Nevermind. Still indulge me in some conversation.")
            Type("[Kai]: I haven't looked around the City Square, maybe there is something rare to be found?")
    else:
        Type(f"[{player.name}]: No! That hurt...")
        Type(f"[???]: I'm really sorry then! Here have something interesting I found in the wildlife.")
        Type(f"[???]: I know it doesn't make up for it but I've collected a lot of these already.")
        Type(f"You obtained a Clear Gem!")
        Check_Full(player,"Clear Gem")
        Type("[Kai]: If you couldn't tell I'm a vistor... I was investigating the area above.")
        Type("[Kai]: I was going to loot here as well but I'll leave that to you.")
    Type("[Kai]: I'll tell you what. Meet me up here once you've investigated the City Square. I'll have something for you!")
    Type("NEW QUEST!\n>>>Loot the Main City<<<")
    Type("[Tutorial]: Click 'e' when on a '~' tile to investigate the area.")
    player.curq.append('Invest Tutorial')
    player.cuts.append("Kai")

def Other_Vistor(player):
    if '~' in MainCity.mapper[3] or '~' in MainCity.mapper[4]:
        Type("[Kai]: Oh, did you really investigate the City Square or did you walk back here behind me?")
    else:
        if 'Invest Tutorial' not in player.compq:
            Type("[Kai]: Hey! You came to meet me - nice!\n[Kai]: And you even loot- I mean investigated the City Square!\n[Kai]: As promised I have something for you...")
            Type("QUEST COMPLETED!")
            Type(">>>Loot the City Square<<<")
            Type("Reward: 20 exp, Half Full Potion")
            player.curq.remove('Invest Tutorial')
            player.compq.append("Invest Tutorial")
            player.exp += 20
            Check_Full(player,"Half Drunk Potion")
            Exp(player)
            MaxHp(player)
        if "Goblin Ear" not in player.curq:
            Type("[Kai]: You know, I've been struggling with a problem.")
            Type("[Kai]: Could you help? If you do I'll give you something else useful! (y/n)")
            key = readchar.readkey()
            if key == 'y':
                Type("[Kai]: Great! I've been trying to get a Goblin Ear to analyse but I'm finding it difficult to defeat those summons.")
                Type("[Kai]: Could you get me a Goblin Ear?")
                Type("[Kai]: I suggest you go to Harley to buy/craft a stronger weapon.")
                Type("Find out more? (y/n)")
                key = readchar.readkey()
                if key == 'y':
                    Type("[Tutorial]: Talk to Harley '£' in the Main City to buy a stronger weapon.")
                    Type("[Tutorial]: Click 'c' when talking to Harley to craft - which can increase weapon strength.")
                    Type("[Tutorial]: If you don't have Gold, sell useless items to Marina...")
                player.curq.append("Goblin Ear")
            else:
                Type("[Kai]: That's ok. If you change your mind I'll be here waiting!")
        if "Goblin Ear" not in player.inv and "Goblin Ear" in player.curq:
            Type("[Kai]: Do you have it? No? Oh, there are Goblins around here so you can find it!")
        if "Goblin Ear" in player.inv:
            Type("[Kai]: You got it for me! Thanks.")
            Type("[Kai]: As promised I have this for you...")
            Type("[Kai]: I'll see you around then!")
            TenjaPath.mapper[2][1] = '~'
            Type("QUEST COMPLETED!")
            Type(">>>Fetch Goblin Ear<<<")
            Type("Reward: 50 exp, Simple Potion")
            player.curq.remove('Goblin Ear')
            player.inv.remove('Goblin Ear')
            player.compq.append("Goblin Ear")
            player.exp += 50
            Check_Full(player,"Simple Potion")
            Exp(player)
            MaxHp(player)

        

def Pre_Boss_Fight(player):
    pass

TenjaPath = Area("Tenja Path",[['#','#','#','#','#','#','#','#','#','#','#','#','#'],
 ['#','.','.','~','.','.','~','.','.','~','.','%','|'], #%; four slimes
 ['#','?','~','.','~','.','.','~','.','.','~','.','#'], #?; Kai
 ['#','.','.','.','.','~','.','.','~','.','.','~','#'],
 ['#','_','#','#','#','#','#','#','#','#','#','#','#']],'.',1,3,{'|':''})
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
MainCity.emap = {'|':Tut,'&':Guard,'£':Weapons_Shop,'$':Conversion,'!':Shady_Merchant,'%':Potion_Geek,'_':TenjaPath}
TenjaPath.emap = {'|':MainCity,'_':MainCity,'?':Other_Vistor,'%':Pre_Boss_Fight}

'''
player1 = Stats('',10,1,0,100,1,Tut,[],0,'','','',[],'',['Gob'],10)
Tut.Update()

player1.Actions()
'''