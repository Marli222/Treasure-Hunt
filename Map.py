import sys
import os
import readchar

def Update(Map):
     os.system('clear')
     for row in Map:
        print(' '.join(map(str, row)))


Map1 = [["#","#","#","#","#"],
        ["#",".",".",".","#"],
        ["#",".",".",".","|"],
        ["#","#","#","#","#"]]

Map2 = [["#","#","#","#","#"],
        ["|",".",".",".","#"],
        ["#",".",".",".","#"],
        ["#","#","#","#","#"]]

x = 1
y = 1
Starter_Place = "."
Last = Starter_Place
last_y = 1
last_x = 1
Map1[y][x] = '@'
Update(Map1)
while True:
        key = readchar.readkey()
        Map1[last_y][last_x] = Last
        if key == "w":
            y -= 1
            if Map1[y][x] == "#":
                  y += 1
                  continue
            elif Map1[y][x] == "|":
                 break
            else:
                 Last = Map1[y][x]
                 last_y = y
                 last_x = x
                 Map1[y][x] = '@'
        elif key == "s":
              y += 1
              if Map1[y][x] == "#":
                  y -= 1
                  continue
              elif Map1[y][x] == "|":
                 break
              else:
                 Last = Map1[y][x]
                 last_y = y
                 last_x = x
                 Map1[y][x] = '@'
        elif key == "a":
              x -= 1
              if Map1[y][x] == "#":
                  x += 1
                  continue
              elif Map1[y][x] == "|":
                 break
              else:
                 Last = Map1[y][x]
                 last_y = y
                 last_x = x
                 Map1[y][x] = '@'               
        elif key == "d":
              x += 1
              if Map1[y][x] == "#":
                  x -= 1
                  continue
              elif Map1[y][x] == "|":
                 break
              else:
                 Last = Map1[y][x]
                 last_y = y
                 last_x = x
                 Map1[y][x] = '@'
        Update(Map1)

x = 1
y = 1
Starter_Place = "."
Last = Starter_Place
last_y = 1
last_x = 1
Map2[y][x] = '@'
Update(Map2)
while True:
        key = readchar.readkey()
        Map2[last_y][last_x] = Last
        if key == "w":
            y -= 1
            if Map2[y][x] == "#":
                  y += 1
                  continue
            elif Map2[y][x] == "|":
                 break
            else:
                 Last = Map2[y][x]
                 last_y = y
                 last_x = x
                 Map2[y][x] = '@'
        elif key == "s":
              y += 1
              if Map2[y][x] == "#":
                  y -= 1
                  continue
              elif Map2[y][x] == "|":
                 break
              else:
                 Last = Map2[y][x]
                 last_y = y
                 last_x = x
                 Map2[y][x] = '@'
        elif key == "a":
              x -= 1
              if Map2[y][x] == "#":
                  x += 1
                  continue
              elif Map2[y][x] == "|":
                 break
              else:
                 Last = Map2[y][x]
                 last_y = y
                 last_x = x
                 Map2[y][x] = '@'               
        elif key == "d":
              x += 1
              if Map2[y][x] == "#":
                  x -= 1
                  continue
              elif Map2[y][x] == "|":
                 break
              else:
                 Last = Map2[y][x]
                 last_y = y
                 last_x = x
                 Map2[y][x] = '@'
        Update(Map2)