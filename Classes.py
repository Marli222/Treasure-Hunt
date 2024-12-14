import os 
import readchar

class Weapons:
    def __init__(item, name, atk, ob):
        item.name = name
        item.atk = atk

class Stats:
    def __init__(self, name, hp, lvl, exp, Rexp, atk, location, inv, gold, wp, beat, target, compq, curq, maxhp): #compq is completed quests and curq is current quest.
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
     self.maxhp = maxhp

    def Actions(self,area):
        while True:
            key = readchar.readkey()
            area.mapper[area.l_y][area.l_x] = area.Last1
            if key == "w":
                area.py_y -= 1
                if area.mapper[area.py_y][area.py_x] == "#":
                    area.py_y += 1
                    continue
                elif area.mapper[area.py_y][area.py_x] == "|":
                    break
                else:
                    area.Last1 = area.mapper[area.py_y][area.py_x]
                    area.l_y = area.py_y
                    area.l_x = area.py_x
                    area.mapper[area.py_y][area.py_x] = '@'
            elif key == "s":
                area.py_y += 1
                if area.mapper[area.py_y][area.py_x] == "#":
                    area.py_y -= 1
                    continue
                elif area.mapper[area.py_y][area.py_x] == "|":
                    break
                else:
                    area.Last1 = area.mapper[area.py_y][area.py_x]
                    area.l_y = area.py_y
                    area.l_x = area.py_x
                    area.mapper[area.py_y][area.py_x] = '@'
            elif key == "a":
                area.py_x -= 1
                if area.mapper[area.py_y][area.py_x] == "#":
                    area.py_x += 1
                    continue
                elif area.mapper[area.py_y][area.py_x] == "|":
                    break
                else:
                    area.Last1 = area.mapper[area.py_y][area.py_x]
                    area.l_y = area.py_y
                    area.l_x = area.py_x
                    area.mapper[area.py_y][area.py_x] = '@'              
            elif key == "d":
                area.py_x += 1
                if area.mapper[area.py_y][area.py_x] == "#":
                    area.py_x -= 1
                    continue
                elif area.mapper[area.py_y][area.py_x] == "|":
                    break
                else:
                    area.Last1 = area.mapper[area.py_y][area.py_x]
                    area.l_y = area.py_y
                    area.l_x = area.py_x
                    area.mapper[area.py_y][area.py_x] = '@'
            area.Update()

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
        zone.emapper = emap

    def Update(zone):
        os.system('clear')
        for row in zone.mapper:
            print(' '.join(map(str, row)))


Tutorial = Area("Dock",[["#","#","#","#","#"],
        ["#",".",".",".","#"],
        ["#",".",".",".","|"],
        ["#","#","#","#","#"]],'.',1,1,{'&':lambda : print()})

player1 = Stats('',10,1,0,100,1,'Tutorial',[],0,'','','',[],'',10)
Tutorial.Update()

player1.Actions(Tutorial)
