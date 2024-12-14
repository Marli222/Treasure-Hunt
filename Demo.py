import winsound
jshard = 0
class Zonemap:
    def __init__(map,zname,zdescript,zsearch,zitems,zmobs,zoneunlocked,zsearched,zNPCs,zkey,Mup,Mdown,Mleft,Mright):
        map.zname = ''
        map.zdescript = ''
        map.zsearch = ''
        map.zitems = []
        map.zmobs = []
        map.zoneunlocked = True
        map.zsearched = False
        map.zNPCs = []
        map.zkey = []
        map.Mup = {}
        map.Mdown = {}
        map.Mleft = {}
        map.Mright = {}

#MAIN ROOMS
f100_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f100_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f100_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f99_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f99_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f99_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f98_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f98_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f98_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f97_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f97_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f97_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f96_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f96_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f96_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f95_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f95_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f95_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f94_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f94_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f94_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f93_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f93_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f93_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f92_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f92_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f92_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f91_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f91_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f91_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f90_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f89_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f89_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f89_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f88_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f88_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f88_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f87_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f87_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f87_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f86_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f86_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f86_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f85_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f85_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f85_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f84_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f84_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f84_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f83_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f83_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f83_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f82_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f82_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f82_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f81_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f81_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f81_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f80_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f79_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f79_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f79_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f78_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f78_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f78_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f77_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f77_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f77_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f76_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f76_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f76_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f75_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f75_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f75_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f74_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f74_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f74_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f73_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f73_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f73_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f72_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f72_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f72_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f71_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f71_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f71_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f70_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f69_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f69_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f69_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f68_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f68_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f68_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f67_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f67_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f67_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f66_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f66_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f66_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f65_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f65_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f65_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f64_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f64_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f64_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f63_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f63_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f63_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f62_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f62_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f62_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f61_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f61_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f61_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f60_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f59_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f59_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f59_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f58_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f58_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f58_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f57_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f57_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f57_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f56_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f56_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f56_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f55_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f55_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f55_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f54_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f54_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f54_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f53_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f53_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f53_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f52_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f52_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f52_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f51_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f51_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f51_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f50_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f49_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f49_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f49_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f48_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f48_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f48_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f47_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f47_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f47_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f46_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f46_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f46_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f45_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f45_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f45_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f44_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f44_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f44_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f43_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f43_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f43_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f42_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f42_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f42_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f41_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f41_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f41_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f40_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f39_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f39_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f39_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f38_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f38_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f38_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f37_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f37_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f37_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f36_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f36_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f36_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f35_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f35_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f35_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f34_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f34_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f34_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f33_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f33_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f33_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f32_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f32_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f32_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f31_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f31_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f31_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f30_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f29_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f29_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f29_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f28_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f28_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f28_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f27_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f27_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f27_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f26_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f26_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f26_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f25_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f25_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f25_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f24_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f24_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f24_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f23_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f23_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f23_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f22_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f22_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f22_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f21_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f21_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f21_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f20_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f19_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f19_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f19_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f18_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f18_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f18_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f17_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f17_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f17_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f16_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f16_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f16_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f15_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f15_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f15_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f14_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f14_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f14_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f13_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f13_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f13_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f12_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f12_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f12_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f11_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f11_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f11_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f10_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f9_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f9_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f9_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f8_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f8_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f8_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f7_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f7_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f7_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f6_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f6_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f6_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f5_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f5_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f5_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f4_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f4_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f4_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f3_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f3_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f3_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f2_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f2_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f2_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f1_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f1_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f1_3 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
f0_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
fG = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})



f100_1.zname = 'Floor 100, Room 1'
f100_1.zdescript = 'The room was infact your own office, and it looked pretty fancy.'
f100_1.zsearch = 'You open your desk pulling out a notebook, your wallet and a small green vial.'
f100_1.zitems = ['Notebook','Wallet','Miniscule Healing Potion']
f100_1.zmobs = []
f100_1.zoneunlocked = True
f100_1.zsearched = False
f100_1.zNPCs = []
f100_1.zkey = []
f100_1.Mup = {}
f100_1.Mdown = {}
f100_1.Mleft = {}
f100_1.Mright = f100_2


f100_2.zname = 'Floor 100, Room 2'
f100_2.zdescript = 'What would be the main hallway but seems to be another office. Weird...'
f100_2.zsearch = 'You go through your collegues\' desks, you find a key.'
f100_2.zitems = ['Floor-99 Key']
f100_2.zmobs = []
f100_2.zoneunlocked = True
f100_2.zsearched = False
f100_2.zNPCs = []
f100_2.zkey = []
f100_2.Mup = {}
f100_2.Mdown = {}
f100_2.Mleft = f100_1
f100_2.Mright = f100_3


f100_3.zname = 'Floor 100, Room 3'
f100_3.zdescript = 'It\'s the Main Hallway, usually their would be access to a lift but it has "out of order" written on it.'
f100_3.zsearch = 'You find a staircase which will take you downstairs.'
f100_3.zitems = []
f100_3.zmobs = ['Goblin']
f100_3.zoneunlocked = True
f100_3.zsearched = False
f100_3.zNPCs = []
f100_3.zkey = []
f100_3.Mup = {}
f100_3.Mdown = f99_1
f100_3.Mleft = f100_2
f100_3.Mright = {}

f99_1.zname = 'Floor 99, Room 1'
f99_1.zdescript = 'Just an empty hallway, a bit eerie...'
f99_1.zsearch = 'You couldn\'t find anything of use.'
f99_1.zitems = []
f99_1.zmobs = []
f99_1.zoneunlocked = False
f99_1.zsearched = False
f99_1.zNPCs = []
f99_1.zkey = 'Floor-99 Key'
f99_1.Mup = f100_3
f99_1.Mdown = {}
f99_1.Mleft = f99_2
f99_1.Mright = {}

f99_2.zname = 'Floor 99, Room 2'
f99_2.zdescript = 'The locker room, though all the names on the lockers were in some strange language.'
f99_2.zsearch = 'You try to open any of the lockers but all you could find was a small vial.'
f99_2.zitems = ['Miniscule Healing Potion']
f99_2.zmobs = []
f99_2.zoneunlocked = True
f99_2.zsearched = False
f99_2.zNPCs = []
f99_2.zkey = []
f99_2.Mup = {}
f99_2.Mdown = {}
f99_2.Mleft = f99_3
f99_2.Mright = f99_1

f99_3.zname = 'Floor 99, Room 3'
f99_3.zdescript = 'The Office\'s reception, although the receptionist is a Goblin!'
f99_3.zsearch = 'You searched through the Goblin\'s belongings and found a pearl sized orb.'
f99_3.zitems = ['Miniscule Exp Orb']
f99_3.zmobs = ['Goblin']
f99_3.zoneunlocked = True
f99_3.zsearched = False
f99_3.zNPCs = []
f99_3.zkey = []
f99_3.Mup = {}
f99_3.Mdown = f98_1
f99_3.Mleft = {}
f99_3.Mright = f99_2

f98_1.zname = 'Floor 98, Room 1'
f98_1.zdescript = 'A room with two doors, and a staircase.'
f98_1.zsearch = 'There\'s nothing here...'
f98_1.zitems = []
f98_1.zmobs = []
f98_1.zoneunlocked = True
f98_1.zsearched = False
f98_1.zNPCs = []
f98_1.zkey = []
f98_1.Mup = f99_3
f98_1.Mdown = f97_1
f98_1.Mleft = f98_3
f98_1.Mright = f98_2

f98_2.zname = 'Floor 98, Room 2'
f98_2.zdescript = 'An empty room with a Goblin sharpening it\'s dagger.'
f98_2.zsearch = 'You tried to take the Goblin\'s Dagger, it broke... Oof.'
f98_2.zitems = []
f98_2.zmobs = ['Goblin']
f98_2.zoneunlocked = True
f98_2.zsearched = False
f98_2.zNPCs = []
f98_2.zkey = []
f98_2.Mup = {}
f98_2.Mdown = {}
f98_2.Mleft = f98_1
f98_2.Mright = {}

f98_3.zname = 'Floor 98, Room 3'
f98_3.zdescript = 'An empty room with a slime absorbing what seems like... er, A KEY!'
f98_3.zsearch = 'You got your hands covered in gooey slime whilst getting the key from it\'s body.'
f98_3.zitems = ['Floor-97 Key']
f98_3.zmobs = ['Slime']
f98_3.zoneunlocked = True
f98_3.zsearched = False
f98_3.zNPCs = []
f98_3.zkey = []
f98_3.Mup = {}
f98_3.Mdown = {}
f98_3.Mleft = {}
f98_3.Mright = f98_1

f97_1.zname = 'Floor 97, Room 1'
f97_1.zdescript = 'Two doors, the one on the right reads "Weapons Storage" and the other "Golden Home Residency"'
f97_1.zsearch = 'You found some gold in the corner of the room, lucky...'
f97_1.zitems = ['Gold']
f97_1.zmobs = []
f97_1.zoneunlocked = False
f97_1.zsearched = False
f97_1.zNPCs = []
f97_1.zkey = 'Floor-97 Key'
f97_1.Mup = f98_1
f97_1.Mdown = f96_2
f97_1.Mleft = {}
f97_1.Mright = f97_2

f97_2.zname = 'Floor 97, Room 2'
f97_2.zdescript = 'The sign was a trap!'
f97_2.zsearch = 'After rummaging in the monsters stuff for a while you found a few vials.'
f97_2.zitems = ['Miniscule Healing Potion','Tiny Healing Potion']
f97_2.zmobs = ['Goblin','Goblin']
f97_2.zoneunlocked = True
f97_2.zsearched = False
f97_2.zNPCs = []
f97_2.zkey = []
f97_2.Mup = {}
f97_2.Mdown = f96_1
f97_2.Mleft = f97_1
f97_2.Mright = f97_3

f97_3.zname = 'Floor 97, Room 3'
f97_3.zdescript = 'Yeah all that\'s being stored here is monsters.'
f97_3.zsearch = 'You found a Key in the Goblin\'s pockets.'
f97_3.zitems = ['Floor-96 Key']
f97_3.zmobs = ['Goblin','Slime']
f97_3.zoneunlocked = True
f97_3.zsearched = False
f97_3.zNPCs = []
f97_3.zkey = []
f97_3.Mup = {}
f97_3.Mdown = {}
f97_3.Mleft = f97_2
f97_3.Mright = {}

f96_1.zname = 'Floor 96, Room 1'
f96_1.zdescript = 'It was a small and cozy home, though every thing was sized for Goblins.\nThis seemed to be the living room.'
f96_1.zsearch = 'You found a few gold pieces on sofa.'
f96_1.zitems = ['Gold']
f96_1.zmobs = []
f96_1.zoneunlocked = False
f96_1.zsearched = False
f96_1.zNPCs = []
f96_1.zkey = 'Floor-96 Key'
f96_1.Mup = f97_2
f96_1.Mdown = f95_1
f96_1.Mleft = f96_2
f96_1.Mright = f96_3

f96_2.zname = 'Floor 96, Room 2'
f96_2.zdescript = 'It was the main lobby for the different apartments, three mail boxes one for each home that resided here.'
f96_2.zsearch = 'You couldn\'t get your hand down the mail boxes...'
f96_2.zitems = []
f96_2.zmobs = []
f96_2.zoneunlocked = True
f96_2.zsearched = False
f96_2.zNPCs = []
f96_2.zkey = []
f96_2.Mup = f97_1
f96_2.Mdown = f95_3
f96_2.Mleft = {}
f96_2.Mright = f96_1

f96_3.zname = 'Floor 96, Room 3'
f96_3.zdescript = 'The Kitchen of the quaint home, a Slime and Goblin were making vial of that useful green liquid.'
f96_3.zsearch = 'You inspected the green liquid to make sure it was safe before pouring it into two small vials.'
f96_3.zitems = ['Miniscule Healing Potion','Miniscule Healing Potion']
f96_3.zmobs = ['Slime','Goblin']
f96_3.zoneunlocked = True
f96_3.zsearched = False
f96_3.zNPCs = []
f96_3.zkey = []
f96_3.Mup = {}
f96_3.Mdown = f95_2
f96_3.Mleft = f96_1
f96_3.Mright = {}

f95_1.zname = 'Floor 95, Room 1'
f95_1.zdescript = 'A quite messy room which might be someone\'s bedroom. It seemed they were not home.'
f95_1.zsearch = 'It was impossible to find anything in the mess.'
f95_1.zitems = []
f95_1.zmobs = []
f95_1.zoneunlocked = False
f95_1.zsearched = False
f95_1.zNPCs = []
f95_1.zkey = 'Floor-95 Key'
f95_1.Mup = f96_1
f95_1.Mdown = f94_2
f95_1.Mleft = {}
f95_1.Mright = f95_2

f95_2.zname = 'Floor 95, Room 2'
f95_2.zdescript = 'This room was extremely clean, yet every space was filled with either books or bookselves.'
f95_2.zsearch = 'All the books were in Elfish, unless you could read it they were useless...'
f95_2.zitems = ['esreveR','eht','sdrow','staht','hsiflE']
f95_2.zmobs = []
f95_2.zoneunlocked = True
f95_2.zsearched = False
f95_2.zNPCs = []
f95_2.zkey = []
f95_2.Mup = f96_3
f95_2.Mdown = f94_1
f95_2.Mleft = f95_1
f95_2.Mright = {}

f95_3.zname = 'Floor 95, Room 3'
f95_3.zdescript = 'A communal bathroom, lucky no-one was using it at the moment.'
f95_3.zsearch = 'You found a key in the bathroom cupboard.'
f95_3.zitems = ['Floor-95 Key']
f95_3.zmobs = []
f95_3.zoneunlocked = True
f95_3.zsearched = False
f95_3.zNPCs = []
f95_3.zkey = []
f95_3.Mup = f96_2
f95_3.Mdown = {}
f95_3.Mleft = {}
f95_3.Mright = {}

f94_1.zname = 'Floor 94, Room 1'
f94_1.zdescript = 'The biggest room you\'ve ever since for just clothes. And they looked expensive too.'
f94_1.zsearch = 'You found a key within a shoe box.'
f94_1.zitems = ['Floor-94 Key']
f94_1.zmobs = []
f94_1.zoneunlocked = True
f94_1.zsearched = False
f94_1.zNPCs = []
f94_1.zkey = []
f94_1.Mup = f95_2
f94_1.Mdown = {}
f94_1.Mleft = f94_2
f94_1.Mright = {}

f94_2.zname = 'Floor 94, Room 2'
f94_2.zdescript = 'A amazing bedroom, complete with lots of decorations and expensive looking furniture.'
f94_2.zsearch = 'A few gold pieces were left on person\'s desk.'
f94_2.zitems = ['Gold']
f94_2.zmobs = []
f94_2.zoneunlocked = False
f94_2.zsearched = False
f94_2.zNPCs = []
f94_2.zkey = 'Floor-94 Key'
f94_2.Mup = f95_1
f94_2.Mdown = {}
f94_2.Mleft = f94_3
f94_2.Mright = f94_1

f94_3.zname = 'Floor 94, Room 3'
f94_3.zdescript = 'A lab, in the middle of someone\'s apartment. Weird...'
f94_3.zsearch = 'You found a slightly glowing orb just resting in a petri disk.'
f94_3.zitems = ['Miniscule Exp Orb']
f94_3.zmobs = []
f94_3.zoneunlocked = True
f94_3.zsearched = False
f94_3.zNPCs = []
f94_3.zkey = []
f94_3.Mup = {}
f94_3.Mdown = f93_1
f94_3.Mleft = {}
f94_3.Mright = f94_2

f93_1.zname = 'Floor 93, Room 1'
f93_1.zdescript = 'Another communal lobby area with mail boxes for the two apartments you had just walked through.'
f93_1.zsearch = 'Stop trying to put your hand down mail boxes...'
f93_1.zitems = []
f93_1.zmobs = []
f93_1.zoneunlocked = True
f93_1.zsearched = False
f93_1.zNPCs = []
f93_1.zkey = []
f93_1.Mup = f94_3
f93_1.Mdown = {}
f93_1.Mleft = f93_2
f93_1.Mright = {}

f93_2.zname = 'Floor 93, Room 2'
f93_2.zdescript = 'This lobby area must be popular because three monsters decided to hangout here.'
f93_2.zsearch = 'You find the door to next lobby to the left.'
f93_2.zitems = []
f93_2.zmobs = ['Slime','Goblin','Goblin']
f93_2.zoneunlocked = True
f93_2.zsearched = False
f93_2.zNPCs = []
f93_2.zkey = []
f93_2.Mup = {}
f93_2.Mdown = f92_1
f93_2.Mleft = f93_3
f93_2.Mright = f93_1

f93_3.zname = 'Floor 93, Room 3'
f93_3.zdescript = 'The lobby had a person! They seemed to be human maybe you should talk to them?'
f93_3.zsearch = 'The person sitting in this lobby has a book in their hand called "tnemelE tiripS gnirednaW a gnieb ot ediuG"'
f93_3.zitems = []
f93_3.zmobs = []
f93_3.zoneunlocked = True
f93_3.zsearched = False
f93_3.zNPCs = []
f93_3.zkey = []
f93_3.Mup = {}
f93_3.Mdown = f92_2
f93_3.Mleft = {}
f93_3.Mright = f93_2

f92_1.zname = 'Floor 92, Room 1'
f92_1.zdescript = 'This was the first communal washing room, and even though washing was running. No-one was here.'
f92_1.zsearch = 'You saw a key resting on a washing machine.'
f92_1.zitems = ['Floor-92 Key']
f92_1.zmobs = []
f92_1.zoneunlocked = True
f92_1.zsearched = False
f92_1.zNPCs = []
f92_1.zkey = []
f92_1.Mup = f93_2
f92_1.Mdown = {}
f92_1.Mleft = f92_2
f92_1.Mright = {}

f92_2.zname = 'Floor 92, Room 2'
f92_2.zdescript = 'This was the second communal washing room, and it seemed to be someone doing their washing here.\nShould you talk to them?'
f92_2.zsearch = 'You couldn\'t find anything other than lost Goblin socks.'
f92_2.zitems = []
f92_2.zmobs = []
f92_2.zoneunlocked = True
f92_2.zsearched = False
f92_2.zNPCs = []
f92_2.zkey = []
f92_2.Mup = f93_3
f92_2.Mdown = {}
f92_2.Mleft = f92_3
f92_2.Mright = f92_1

f92_3.zname = 'Floor 92, Room 3'
f92_3.zdescript = 'This was the third communal washing room, no-one was here...'
f92_3.zsearch = 'You found some healing potions lying around with a note.'
f92_3.zitems = ['Medium Healing Potion','Tiny Healing Potion','Miniscule Healing Potion','Note1']
f92_3.zmobs = []
f92_3.zoneunlocked = False
f92_3.zsearched = False
f92_3.zNPCs = []
f92_3.zkey = 'Floor-92 Key'
f92_3.Mup = {}
f92_3.Mdown = f91_1
f92_3.Mleft = {}
f92_3.Mright = f92_2

f91_1.zname = 'Floor 91, Room 1'
f91_1.zdescript = 'A very interesting waiting room, everything seemed completed spotless as if someone had just cleaned up.'
f91_1.zsearch = 'There was nothing apart from lavish furniture (not even a speck of dust)\nWhy is there even a waiting room here?'
f91_1.zitems = []
f91_1.zmobs = []
f91_1.zoneunlocked = True
f91_1.zsearched = False
f91_1.zNPCs = []
f91_1.zkey = []
f91_1.Mup = f92_3
f91_1.Mdown = f90_1
f91_1.Mleft = f91_3
f91_1.Mright = f91_2

f91_2.zname = 'Floor 91, Room 2'
f91_2.zdescript = 'The room was an office of sorts, a name card with written the desk "Alice: First Assistant of the Goblin King".\nAh, Alice must be the Goblin about to attack you now.'
f91_2.zsearch = 'You noticed a Notebook on the desk, you couldn\'t open it but you had a feeling it was Adagios.'
f91_2.zitems = ['Sealed Notebook','Gold']
f91_2.zmobs = ['Goblin']
f91_2.zoneunlocked = True
f91_2.zsearched = False
f91_2.zNPCs = []
f91_2.zkey = []
f91_2.Mup = {}
f91_2.Mdown = {}
f91_2.Mleft = f91_1
f91_2.Mright = {}

f91_3.zname = 'Floor 91, Room 3'
f91_3.zdescript = 'A storage room full of cleaning items, no doubt to keep room 1 as clean as it is.n\And of course not complete without any monsters.'
f91_3.zsearch = 'You found another note in the dead Goblins pocket.'
f91_3.zitems = ['Note2','Tiny Healing Potion','Miniscule Healing Potion']
f91_3.zmobs = ['Goblin']
f91_3.zoneunlocked = True
f91_3.zsearched = False
f91_3.zNPCs = []
f91_3.zkey = []
f91_3.Mup = {}
f91_3.Mdown = {}
f91_3.Mleft = {}
f91_3.Mright = f91_1

f90_1.zname = 'Floor 90, Room 1'
f90_1.zdescript = 'A large throne room, the celling had to be at least 100 metres from the Ground, which logically didn\'t make any sense.\nThough the reason behind it was completly justified, the largest Goblin you\'ve ever seen sat at around 30 metres.\nWithout a word the Goblin King Swung his large club at you.'
f90_1.zsearch = 'The Goblin King dropped an Exp Orb and a large green vial.'
f90_1.zitems = ['Tiny Exp Orb','Medium Healing Potion']
f90_1.zmobs = ['Goblin King']
f90_1.zoneunlocked = False
f90_1.zsearched = False
f90_1.zNPCs = []
f90_1.zkey = 'Floor-90 Key'
f90_1.Mup = f91_1
f90_1.Mdown = f89_1
f90_1.Mleft = {}
f90_1.Mright = {}

f89_1.zname = 'Floor 89, Room 1'
f89_1.zdescript = 'A Entrance to the late Goblins King\'s throne room. It seemed to be heavily guarded.'
f89_1.zsearch = 'There was nothing here of value...'
f89_1.zitems = []
f89_1.zmobs = ['Goblin','Goblin','Goblin']
f89_1.zoneunlocked = True
f89_1.zsearched = False
f89_1.zNPCs = []
f89_1.zkey = []
f89_1.Mup = f90_1
f89_1.Mdown = {}
f89_1.Mleft = {}
f89_1.Mright = f89_2

f89_2.zname = 'Floor 89, Room 2'
f89_2.zdescript = 'Just an empty hallway. Nothing more or less. It basically just empty space.'
f89_2.zsearch = 'On the right end of the hallway was another room it seemed to be another housing complex or something similar.'
f89_2.zitems = []
f89_2.zmobs = []
f89_2.zoneunlocked = True
f89_2.zsearched = False
f89_2.zNPCs = []
f89_2.zkey = []
f89_2.Mup = {}
f89_2.Mdown = {}
f89_2.Mleft = f89_1
f89_2.Mright = f89_3

f89_3.zname = 'Floor 89, Room 3'
f89_3.zdescript = 'The entrance to another apartment complex, someone was in here looking a bit stressed. Maybe they need help?'
f89_3.zsearch = 'You were able get your hand down the mail box for these apartments. Wander what is in store for you.'
f89_3.zitems = ['Tiny Exp Orb','Tiny Exp Orb']
f89_3.zmobs = []
f89_3.zoneunlocked = True
f89_3.zsearched = False
f89_3.zNPCs = []
f89_3.zkey = []
f89_3.Mup = {}
f89_3.Mdown = f88_1
f89_3.Mleft = f89_2
f89_3.Mright = {}

f88_1.zname = 'Floor 88, Room 1'
f88_1.zdescript = 'Weird, there is a slime here but it seems to be sleeping... Try not to wake it up.'
f88_1.zsearch = 'Somehow you didn\'t wake up the slime looking around the empty apartment\'s front room.\nThere is nothing here.'
f88_1.zitems = []
f88_1.zmobs = []
f88_1.zoneunlocked = True
f88_1.zsearched = False
f88_1.zNPCs = []
f88_1.zkey = []
f88_1.Mup = f89_3
f88_1.Mdown = f87_3
f88_1.Mleft = {}
f88_1.Mright = f88_2

f88_2.zname = 'Floor 88, Room 2'
f88_2.zdescript = 'Even weirder, there is a Zombie and a Goblin here and they both seem to be sleeping...'
f88_2.zsearch = 'You barely searched in fear of waking up the monsters.'
f88_2.zitems = []
f88_2.zmobs = []
f88_2.zoneunlocked = True
f88_2.zsearched = False
f88_2.zNPCs = []
f88_2.zkey = []
f88_2.Mup = {}
f88_2.Mdown = f87_2
f88_2.Mleft = f88_1
f88_2.Mright = f88_3

f88_3.zname = 'Floor 88, Room 3'
f88_3.zdescript = 'The bedroom of the empty apartment, it seemed as though a Zombie lives here.'
f88_3.zsearch = 'You found a Key on the lying on the floor with some gold.'
f88_3.zitems = ['Floor-87 Key','Gold']
f88_3.zmobs = []
f88_3.zoneunlocked = False
f88_3.zsearched = False
f88_3.zNPCs = []
f88_3.zkey = 'Floor-88 Key'
f88_3.Mup = {}
f88_3.Mdown = f87_1
f88_3.Mleft = f88_2
f88_3.Mright = {}

f87_1.zname = 'Floor 87, Room 1'
f87_1.zdescript = 'Another person\'s apartment and it seems that person is home... Should you sneak away or talk to them?'
f87_1.zsearch = 'You couldn\'t find anything useful, just a few books lying around.'
f87_1.zitems = ['Floor-86 Key','Trapped']
f87_1.zmobs = []
f87_1.zoneunlocked = True
f87_1.zsearched = False
f87_1.zNPCs = []
f87_1.zkey = []
f87_1.Mup = f88_3
f87_1.Mdown = {}
f87_1.Mleft = f87_2
f87_1.Mright = {}

f87_2.zname = 'Floor 87, Room 2'
f87_2.zdescript = 'Holly\'s bedroom/bathroom. It was pretty nice if not for the Zombie *in* the toliet.'
f87_2.zsearch = 'You found a semi-large exp orb and a key on Holly\'s bed, she would\'t mind you if you took it? Right?'
f87_2.zitems = ['Floor-88 Key','Tiny Exp Orb']
f87_2.zmobs = ['Zombie']
f87_2.zoneunlocked = True
f87_2.zsearched = False
f87_2.zNPCs = []
f87_2.zkey = []
f87_2.Mup = f88_2
f87_2.Mdown = {}
f87_2.Mleft = f87_3
f87_2.Mright = f87_1

f87_3.zname = 'Floor 87, Room 3'
f87_3.zdescript = 'Holly\'s Kitchen and Dining room. She seemed to really like monsters because you just interuppted a Slime and a Zombie.'
f87_3.zsearch = 'You found a few healing potions and a dreaded note...'
f87_3.zitems = ['Tiny Healing Potion','Miniscule Healing Potion','Miniscule Healing Potion','Note3']
f87_3.zmobs = ['Zombie','Slime']
f87_3.zoneunlocked = False
f87_3.zsearched = False
f87_3.zNPCs = []
f87_3.zkey = 'Floor-87 Key'
f87_3.Mup = f88_1
f87_3.Mdown = f86_2
f87_3.Mleft = {}
f87_3.Mright = f87_2

f86_1.zname = 'Floor 86, Room 1'
f86_1.zdescript = 'It seemed to be someone else\'s apartment yet it was very quiet and no-one seemed to be around.\nMaybe that\'s why the door is locked?'
f86_1.zsearch = 'Nothing, to note except for the pile of gold coins on the dining table.'
f86_1.zitems = ['Gold','Gold']
f86_1.zmobs = []
f86_1.zoneunlocked = False
f86_1.zsearched = False
f86_1.zNPCs = []
f86_1.zkey = 'Floor-86 Key'
f86_1.Mup = f87_3
f86_1.Mdown = {}
f86_1.Mleft = f86_2
f86_1.Mright = {}

f86_2.zname = 'Floor 86, Room 2'
f86_2.zdescript = 'Oh, no... Someone was definitely here. They hadn\'t seemed to notice you yet, since they were facing away reading a book. Maybe you should talk to them?'
f86_2.zsearch = 'The person\'s room was very tidy, but felt empty. There wasn\'t anything good to take...'
f86_2.zitems = []
f86_2.zmobs = []
f86_2.zoneunlocked = True
f86_2.zsearched = False
f86_2.zNPCs = []
f86_2.zkey = []
f86_2.Mup = {}
f86_2.Mdown = f85_2
f86_2.Mleft = f86_3
f86_2.Mright = f86_1

f86_3.zname = 'Floor 86, Room 3'
f86_3.zdescript = 'Eli\'s apartment though he\'d forgotten to lock the door on this side and now Goblins were attacking. Again.'
f86_3.zsearch = 'You found a key in one of the Goblin\'s pockets.'
f86_3.zitems = ['Floor-84 Key']
f86_3.zmobs = ['Goblin','Goblin','Goblin']
f86_3.zoneunlocked = True
f86_3.zsearched = False
f86_3.zNPCs = []
f86_3.zkey = []
f86_3.Mup = {}
f86_3.Mdown = f85_1
f86_3.Mleft = {}
f86_3.Mright = f86_2

f85_1.zname = 'Floor 85, Room 1'
f85_1.zdescript = 'This looked to be a personal gym inside someone\'s apartment. The person who lives here is probably very strong.'
f85_1.zsearch = 'All the Gym equipment here was too heavy to carry.'
f85_1.zitems = []
f85_1.zmobs = []
f85_1.zoneunlocked = True
f85_1.zsearched = False
f85_1.zNPCs = []
f85_1.zkey = []
f85_1.Mup = f86_3
f85_1.Mdown = f84_2
f85_1.Mleft = f85_3
f85_1.Mright = f85_2

f85_2.zname = 'Floor 85, Room 2'
f85_2.zdescript = 'A training room, you could tell by the person practicing their swordmanship on a helpless dummy. Maybe you shouldn\'t talk to them, they look very strong...'
f85_2.zsearch = 'You couldn\'t search very much without alerting the person in the room. Maybe you should talk to them?'
f85_2.zitems = []
f85_2.zmobs = []
f85_2.zoneunlocked = True
f85_2.zsearched = False
f85_2.zNPCs = []
f85_2.zkey = []
f85_2.Mup = f86_2
f85_2.Mdown = {}
f85_2.Mleft = f85_1
f85_2.Mright = {}

f85_3.zname = 'Floor 85, Room 3'
f85_3.zdescript = 'Yonaite\'s bathroom, it had a large hot tub and an assortment of bath salts. The perfect place to relax after a good training session.'
f85_3.zsearch = 'You found a single large green vial in the drug cabinet.'
f85_3.zitems = ['Large Healing Potion']
f85_3.zmobs = []
f85_3.zoneunlocked = True
f85_3.zsearched = False
f85_3.zNPCs = []
f85_3.zkey = []
f85_3.Mup = {}
f85_3.Mdown = f84_1
f85_3.Mleft = {}
f85_3.Mright = f85_1

f84_1.zname = 'Floor 84, Room 1'
f84_1.zdescript = 'Still in Yonaite\'s apartment, this room being a meeting or party room of sorts.'
f84_1.zsearch = 'Eleri had a stand set-up selling Exp Orbs. Maybe you should buy some?\nUse \'talk\' and then \'eleri\' to access the Exp Shop.'
f84_1.zitems = []
f84_1.zmobs = []
f84_1.zoneunlocked = True
f84_1.zsearched = False
f84_1.zNPCs = ['eleri']
f84_1.zkey = []
f84_1.Mup = f85_3
f84_1.Mdown = {}
f84_1.Mleft = {}
f84_1.Mright = f84_2

f84_2.zname = 'Floor 84, Room 2'
f84_2.zdescript = 'Yonaite\'s Kitchen, it was quite large and had a variety of food. She won\'t mind if I took some?'
f84_2.zsearch = 'You found some orange-chocolate, a brownie and a burnt pizza.'
f84_2.zitems = ['Orange Chocolate','Brownie','Burnt Pizza']
f84_2.zmobs = []
f84_2.zoneunlocked = False
f84_2.zsearched = False
f84_2.zNPCs = []
f84_2.zkey = 'Floor-84 Key'
f84_2.Mup = f85_1
f84_2.Mdown = {}
f84_2.Mleft = f84_1
f84_2.Mright = f84_3

f84_3.zname = 'Floor 84, Room 3'
f84_3.zdescript = 'Yonaite\'s Bedroom, it seemed that Yonaite had a very large apartment...'
f84_3.zsearch = 'You spotted a ring on Yonaite\'s bedside table. It looked a lot like the one Holly described.'
f84_3.zitems = ['Ring']
f84_3.zmobs = []
f84_3.zoneunlocked = True
f84_3.zsearched = False
f84_3.zNPCs = []
f84_3.zkey = []
f84_3.Mup = {}
f84_3.Mdown = f83_1
f84_3.Mleft = f84_2
f84_3.Mright = {}

f83_1.zname = 'Floor 83, Room 1'
f83_1.zdescript = 'Yonaite\'s SECOND bathroom, how does she have three floors worth of apartment? Never mind that a Zombie decided they want to go to the loo.'
f83_1.zsearch = 'You found the a small green vial the Zombie dropped. Why would a Zombie need a Healing Potion?'
f83_1.zitems = ['Miniscule Healing Potion']
f83_1.zmobs = ['Zombie']
f83_1.zoneunlocked = True
f83_1.zsearched = False
f83_1.zNPCs = []
f83_1.zkey = []
f83_1.Mup = f84_3
f83_1.Mdown = {}
f83_1.Mleft = f83_2
f83_1.Mright = f83_3

f83_2.zname = 'Floor 83, Room 2'
f83_2.zdescript = 'This was Yonaite\'s walk-in wardrobe, she had A LOT of clothes.'
f83_2.zsearch = 'You found nothing in Yonaite\'s pockets.'
f83_2.zitems = []
f83_2.zmobs = []
f83_2.zoneunlocked = True
f83_2.zsearched = False
f83_2.zNPCs = []
f83_2.zkey = []
f83_2.Mup = {}
f83_2.Mdown = f82_3
f83_2.Mleft = {}
f83_2.Mright = f83_1

f83_3.zname = 'Floor 83, Room 3'
f83_3.zdescript = 'This was Yonaite\'s Guest Bedroom, it seemed like someone was staying here...'
f83_3.zsearch = 'You found a note on the bed. Hopefully it was nice.'
f83_3.zitems = ['Note4']
f83_3.zmobs = []
f83_3.zoneunlocked = False
f83_3.zsearched = False
f83_3.zNPCs = []
f83_3.zkey = 'Floor-83 Key'
f83_3.Mup = {}
f83_3.Mdown = f82_1
f83_3.Mleft = f83_1
f83_3.Mright = {}

f82_1.zname = 'Floor 82, Room 1'
f82_1.zdescript = 'Another Lobby area, probably meant there was another set of rooms coming up...'
f82_1.zsearch = 'You found a two hidden Exp Orbs. They weren\'t hidden very well.'
f82_1.zitems = ['Medium Exp Orb','Tiny Exp Orb']
f82_1.zmobs = []
f82_1.zoneunlocked = True
f82_1.zsearched = False
f82_1.zNPCs = []
f82_1.zkey = []
f82_1.Mup = f83_3
f82_1.Mdown = {}
f82_1.Mleft = {}
f82_1.Mright = f82_2

f82_2.zname = 'Floor 82, Room 2'
f82_2.zdescript = 'Just another Empty Hallway, though from here you could hear the squishing of slimes. It\'s usually not that loud...'
f82_2.zsearch = 'Nothing, this room is empty... ;-;'
f82_2.zitems = []
f82_2.zmobs = []
f82_2.zoneunlocked = True
f82_2.zsearched = False
f82_2.zNPCs = []
f82_2.zkey = []
f82_2.Mup = {}
f82_2.Mdown = f81_1
f82_2.Mleft = f82_1
f82_2.Mright = {}

f82_3.zname = 'Floor 82, Room 3'
f82_3.zdescript = 'Yonaite\'s Lab, though it seems Sone was occupying it at the moment. She seemed focused making more potions.'
f82_3.zsearch = 'You saw some potions on display, it looks like Sone is selling them. Maybe if you talk to her she\'ll give you some?'
f82_3.zitems = ['Floor-83 Key']
f82_3.zmobs = []
f82_3.zoneunlocked = True
f82_3.zsearched = False
f82_3.zNPCs = ['sone']
f82_3.zkey = []
f82_3.Mup = f83_2
f82_3.Mdown = {}
f82_3.Mleft = {}
f82_3.Mright = {}

f81_1.zname = 'Floor 81, Room 1'
f81_1.zdescript = 'No wonder you could hear slimes, there was one here in a empty room.\nBut a single slime would\'t make this much noise. Hmm...'
f81_1.zsearch = 'You found nothing of use.'
f81_1.zitems = []
f81_1.zmobs = ['Slime']
f81_1.zoneunlocked = True
f81_1.zsearched = False
f81_1.zNPCs = []
f81_1.zkey = []
f81_1.Mup = f82_2
f81_1.Mdown = {}
f81_1.Mleft = {}
f81_1.Mright = f81_2

f81_2.zname = 'Floor 81, Room 2'
f81_2.zdescript = 'The sound of slimes was just getting louder, even though there was two here. It didn\'t seem to be just from them.'
f81_2.zsearch = 'You found one of Sone\'s lovely potions for your troubles. A slime dropped it.'
f81_2.zitems = ['Tiny Healing Potion']
f81_2.zmobs = ['Slime','Slime']
f81_2.zoneunlocked = True
f81_2.zsearched = False
f81_2.zNPCs = []
f81_2.zkey = []
f81_2.Mup = {}
f81_2.Mdown = {}
f81_2.Mleft = f81_1
f81_2.Mright = f81_3

f81_3.zname = 'Floor 81, Room 3'
f81_3.zdescript = 'Ok, the sound of slimes was extremely loud... And you could tell it definitely was not coming from the three slimes infront of you.'
f81_3.zsearch = 'The slimes dropped two green vials, one small and one big.'
f81_3.zitems = ['Tiny Healing Potion','Medium Healing Potion']
f81_3.zmobs = ['Slime','Slime','Slime']
f81_3.zoneunlocked = True
f81_3.zsearched = False
f81_3.zNPCs = []
f81_3.zkey = []
f81_3.Mup = {}
f81_3.Mdown = f80_1
f81_3.Mleft = f81_2
f81_3.Mright = {}

f80_1.zname = 'Floor 80, Room 1'
f80_1.zdescript = 'The room was massive, with reason. How else was the MASSIVE slime here going to fit. This is going to be interesting.\nAnd maybe difficult.'
f80_1.zsearch = 'You found the biggest vial of potion you\'ve ever found. EVER. It should be called a bucket instead of a vial.'
f80_1.zitems = ['MASSIVE Healing Potion']
f80_1.zmobs = ['MASSIVE Slime']
f80_1.zoneunlocked = False
f80_1.zsearched = False
f80_1.zNPCs = []
f80_1.zkey = 'Floor-80 Key'
f80_1.Mup = f81_3
f80_1.Mdown = f79_1
f80_1.Mleft = {}
f80_1.Mright = {}

f79_1.zname = 'Floor 79, Room 1'
f79_1.zdescript = 'This room was weird, it was long hallway which seemed to connect to other \'rooms\'.\nYou could see Room 3 from here. Barely but still.\nIt was enough to know you had a lot of fighting to do.'
f79_1.zsearch = 'You found some Gold pieces leading to Floor 78, Room 1. Is this a trap or something?'
f79_1.zitems = ['Gold']
f79_1.zmobs = ['Wolf']
f79_1.zoneunlocked = True
f79_1.zsearched = False
f79_1.zNPCs = []
f79_1.zkey = []
f79_1.Mup = f80_1
f79_1.Mdown = {}
f79_1.Mleft = f79_2
f79_1.Mright = {}

f79_2.zname = 'Floor 79, Room 2'
f79_2.zdescript = 'The hallway continues, with even more monsters down here.'
f79_2.zsearch = 'You saw more Gold pieces leading to Floor 78, Room 1.'
f79_2.zitems = ['Gold']
f79_2.zmobs = ['Goblin','Wolf']
f79_2.zoneunlocked = True
f79_2.zsearched = False
f79_2.zNPCs = []
f79_2.zkey = []
f79_2.Mup = {}
f79_2.Mdown = {}
f79_2.Mleft = f79_3
f79_2.Mright = f79_1

f79_3.zname = 'Floor 79, Room 3'
f79_3.zdescript = 'The last part of the hallway, of course it has the most monsters.'
f79_3.zsearch = 'You found the last of the Gold pieces.'
f79_3.zitems = ['Gold']
f79_3.zmobs = []
f79_3.zoneunlocked = True
f79_3.zsearched = False
f79_3.zNPCs = []
f79_3.zkey = []
f79_3.Mup = {}
f79_3.Mdown = f78_1
f79_3.Mleft = {}
f79_3.Mright = f79_2

f78_1.zname = 'Floor 78, Room 1'
f78_1.zdescript = 'This room was interesting, one door on the right labelled shops, another on the left labelled resting zone.\nThe last door was to a staircase heading to Floor 77, which had even more gold pieces on it.\n Which way do you go?'
f78_1.zsearch = 'You peaked through the left door as you heard some strange noises. The things "resting" in their are two wolves.'
f78_1.zitems = []
f78_1.zmobs = []
f78_1.zoneunlocked = True
f78_1.zsearched = False
f78_1.zNPCs = []
f78_1.zkey = []
f78_1.Mup = f79_3
f78_1.Mdown = f79_1
f78_1.Mleft = f78_3
f78_1.Mright = f78_2

f78_2.zname = 'Floor 78, Room 2'
f78_2.zdescript = 'The sign do not lie, there were only two stores here though. Eleri\'s stand and Sone\'s Stall.'
f78_2.zsearch = 'Sone must\'ve cleared the area because there was not anything to take.'
f78_2.zitems = []
f78_2.zmobs = []
f78_2.zoneunlocked = True
f78_2.zsearched = False
f78_2.zNPCs = ['sone','eleri']
f78_2.zkey = []
f78_2.Mup = {}
f78_2.Mdown = {}
f78_2.Mleft = f78_1
f78_2.Mright = {}

f78_3.zname = 'Floor 78, Room 3'
f78_3.zdescript = 'The sign didn\'t lie persay. But the other things resting in here are wolves.'
f78_3.zsearch = 'You found a key!'
f78_3.zitems = ['Floor-77 Key']
f78_3.zmobs = []
f78_3.zoneunlocked = True
f78_3.zsearched = False
f78_3.zNPCs = []
f78_3.zkey = []
f78_3.Mup = {}
f78_3.Mdown = {}
f78_3.Mleft = {}
f78_3.Mright = f78_1

f77_1.zname = 'Floor 77, Room 1'
f77_1.zdescript = 'This room was built like a cave, very dark. The only light in the room was off.'
f77_1.zsearch = 'You found the lightswitch and realised that the room was empty. Oof-'
f77_1.zitems = []
f77_1.zmobs = []
f77_1.zoneunlocked = False
f77_1.zsearched = False
f77_1.zNPCs = []
f77_1.zkey = 'Floor-77 Key'
f77_1.Mup = f78_1
f77_1.Mdown = f76_2
f77_1.Mleft = {}
f77_1.Mright = f77_2

f77_2.zname = 'Floor 77, Room 2'
f77_2.zdescript = 'Another dark room, maybe if you find the light you\'ll be able to see.'
f77_2.zsearch = 'After turning on the light, you could see the room had been completely cleared out.\nLike someone had robbed, I mean searched the place before you...'
f77_2.zitems = []
f77_2.zmobs = []
f77_2.zoneunlocked = True
f77_2.zsearched = False
f77_2.zNPCs = []
f77_2.zkey = []
f77_2.Mup = {}
f77_2.Mdown = f76_1
f77_2.Mleft = f77_1
f77_2.Mright = f77_3

f77_3.zname = 'Floor 77, Room 3'
f77_3.zdescript = 'This room wasn\'t dark, thankfully but it did have a couple of Zombies.'
f77_3.zsearch = 'You found a Key in one of the Zombie\'s rotting flesh. Lovely!'
f77_3.zitems = ['Floor-76 Key']
f77_3.zmobs = []
f77_3.zoneunlocked = True
f77_3.zsearched = False
f77_3.zNPCs = []
f77_3.zkey = []
f77_3.Mup = {}
f77_3.Mdown = {}
f77_3.Mleft = f77_2
f77_3.Mright = {}

f76_1.zname = 'Floor 76, Room 1'
f76_1.zdescript = 'Someone must have purposefully switched off the lights in these rooms as this was another dark room.'
f76_1.zsearch = 'You found the light switch only to find the room completely empty...'
f76_1.zitems = []
f76_1.zmobs = []
f76_1.zoneunlocked = False
f76_1.zsearched = False
f76_1.zNPCs = []
f76_1.zkey = 'Floor-76 Key'
f76_1.Mup = f77_2
f76_1.Mdown = f75_1
f76_1.Mleft = f76_2
f76_1.Mright = f76_3

f76_2.zname = 'Floor 76, Room 2'
f76_2.zdescript = 'A lit room which had been cleared out like the rest of them.'
f76_2.zsearch = 'Wow, you found NOTHING.'
f76_2.zitems = []
f76_2.zmobs = []
f76_2.zoneunlocked = True
f76_2.zsearched = False
f76_2.zNPCs = []
f76_2.zkey = []
f76_2.Mup = f77_1
f76_2.Mdown = f75_3
f76_2.Mleft = {}
f76_2.Mright = f76_1

f76_3.zname = 'Floor 76, Room 3'
f76_3.zdescript = 'There was someone walking through this lit room, you should probably ask them about your mugger and Mochaii.'
f76_3.zsearch = 'Wow, you found NOTHING.'
f76_3.zitems = []
f76_3.zmobs = []
f76_3.zoneunlocked = True
f76_3.zsearched = False
f76_3.zNPCs = []
f76_3.zkey = []
f76_3.Mup = {}
f76_3.Mdown = f75_2
f76_3.Mleft = f76_1
f76_3.Mright = {}

f75_1.zname = 'Floor 75, Room 1'
f75_1.zdescript = 'Someone must have purposefully switched off the lights in these rooms as this was another dark room.'
f75_1.zsearch = 'You found the light switch only to find the room completely empty...'
f75_1.zitems = []
f75_1.zmobs = []
f75_1.zoneunlocked = False
f75_1.zsearched = False
f75_1.zNPCs = []
f75_1.zkey = 'Floor-75 Key'
f75_1.Mup = f76_1
f75_1.Mdown = f74_2
f75_1.Mleft = {}
f75_1.Mright = f75_2

f75_2.zname = 'Floor 75, Room 2'
f75_2.zdescript = 'Someone must have purposefully switched off the lights in these rooms as this was another dark room.'
f75_2.zsearch = 'You found the light switch only to find the room completly empty...'
f75_2.zitems = []
f75_2.zmobs = []
f75_2.zoneunlocked = True
f75_2.zsearched = False
f75_2.zNPCs = []
f75_2.zkey = []
f75_2.Mup = f76_3
f75_2.Mdown = f74_1
f75_2.Mleft = f75_1
f75_2.Mright = {}

f75_3.zname = 'Floor 75, Room 3'
f75_3.zdescript = 'This room wasn\'t dark, thankfully but it did have a couple of Slimes.'
f75_3.zsearch = 'You found a Key in one of the Slimes goo.'
f75_3.zitems = ['Floor-75 Key']
f75_3.zmobs = ['Slime','Slime','Slime']
f75_3.zoneunlocked = True
f75_3.zsearched = False
f75_3.zNPCs = []
f75_3.zkey = []
f75_3.Mup = f76_2
f75_3.Mdown = {}
f75_3.Mleft = {}
f75_3.Mright = {}

f74_1.zname = 'Floor 74, Room 1'
f74_1.zdescript = 'This room wasn\'t dark, thankfully but it did have a couple of Wolves and a Goblin.'
f74_1.zsearch = 'You found a Key in the Goblin\'s pocket.'
f74_1.zitems = ['Floor-74 Key']
f74_1.zmobs = ['Wolf','Wolf','Goblin']
f74_1.zoneunlocked = True
f74_1.zsearched = False
f74_1.zNPCs = []
f74_1.zkey = []
f74_1.Mup = f75_2
f74_1.Mdown = {}
f74_1.Mleft = f74_2
f74_1.Mright = {}

f74_2.zname = 'Floor 74, Room 2'
f74_2.zdescript = 'Someone must have purposefully switched off the lights in these rooms as this was another dark room.'
f74_2.zsearch = 'You found the light switch only to find the room completely empty...'
f74_2.zitems = []
f74_2.zmobs = []
f74_2.zoneunlocked = False
f74_2.zsearched = False
f74_2.zNPCs = []
f74_2.zkey = 'Floor-74 Key'
f74_2.Mup = f75_1
f74_2.Mdown = {}
f74_2.Mleft = f74_3
f74_2.Mright = f74_1

f74_3.zname = 'Floor 74, Room 3'
f74_3.zdescript = 'There was someone walking through this lit room, you should probably ask them about your mugger and Mochaii.'
f74_3.zsearch = 'Wow, you found NOTHING.'
f74_3.zitems = []
f74_3.zmobs = []
f74_3.zoneunlocked = True
f74_3.zsearched = False
f74_3.zNPCs = []
f74_3.zkey = []
f74_3.Mup = {}
f74_3.Mdown = f73_1
f74_3.Mleft = {}
f74_3.Mright = f74_2

f73_1.zname = 'Floor 73, Room 1'
f73_1.zdescript = 'This room wasn\'t dark, thankfully but it did have a couple of Slimes and a Zombie.'
f73_1.zsearch = 'Wow, you found NOTHING.'
f73_1.zitems = []
f73_1.zmobs = ['Slime','Zombie','Slime']
f73_1.zoneunlocked = True
f73_1.zsearched = False
f73_1.zNPCs = []
f73_1.zkey = []
f73_1.Mup = f74_3
f73_1.Mdown = {}
f73_1.Mleft = f73_2
f73_1.Mright = {}

f73_2.zname = 'Floor 73, Room 2'
f73_2.zdescript = 'This room wasn\'t dark, thankfully but it did have a couple of Wolves and a Zombie.'
f73_2.zsearch = 'Wow, you found a health potion. Possibly the one item that hasn\'t been stolen yet.'
f73_2.zitems = ['Tiny Healing Potion']
f73_2.zmobs = ['Wolf','Wolf','Zombie']
f73_2.zoneunlocked = True
f73_2.zsearched = False
f73_2.zNPCs = []
f73_2.zkey = []
f73_2.Mup = {}
f73_2.Mdown = f72_1
f73_2.Mleft = f73_3
f73_2.Mright = f73_1

f73_3.zname = 'Floor 73, Room 3'
f73_3.zdescript = 'There was someone walking through this lit room, you should probably ask them about your mugger and Mochaii.'
f73_3.zsearch = 'Wow, you found NOTHING.'
f73_3.zitems = []
f73_3.zmobs = []
f73_3.zoneunlocked = True
f73_3.zsearched = False
f73_3.zNPCs = []
f73_3.zkey = []
f73_3.Mup = {}
f73_3.Mdown = f72_2
f73_3.Mleft = {}
f73_3.Mright = f73_2

f72_1.zname = 'Floor 72, Room 1'
f73_1.zdescript = 'This room wasn\'t dark and there wasn\'t any monsters!!'
f73_1.zsearch = 'Wow, you found two health potions AND a key.'
f72_1.zitems = ['Floor-72 Key']
f72_1.zmobs = []
f72_1.zoneunlocked = True
f72_1.zsearched = False
f72_1.zNPCs = []
f72_1.zkey = []
f72_1.Mup = f73_2
f72_1.Mdown = {}
f72_1.Mleft = f72_2
f72_1.Mright = {}

f72_2.zname = 'Floor 72, Room 2'
f72_2.zdescript = 'There was someone walking through this lit room, you should probably ask them about your mugger and Mochaii.'
f72_2.zsearch = 'Wow, you found NOTHING.'
f72_2.zitems = []
f72_2.zmobs = []
f72_2.zoneunlocked = True
f72_2.zsearched = False
f72_2.zNPCs = []
f72_2.zkey = []
f72_2.Mup = f73_3
f72_2.Mdown = {}
f72_2.Mleft = f72_3
f72_2.Mright = f72_1

f72_3.zname = 'Floor 72, Room 3'
f72_3.zdescript = 'Someone must have purposefully switched off the lights in these rooms as this was another dark room.'
f72_3.zsearch = 'You found the light switch only to find the room completely empty...'
f72_3.zitems = []
f72_3.zmobs = []
f72_3.zoneunlocked = False
f72_3.zsearched = False
f72_3.zNPCs = []
f72_3.zkey = 'Floor-72 Key'
f72_3.Mup = {}
f72_3.Mdown = f71_1
f72_3.Mleft = {}
f72_3.Mright = f72_2

f71_1.zname = 'Floor 71, Room 1'
f71_1.zdescript = 'This room wasn\'t dark, thankfully but it did have a couple of Zombies.'
f71_1.zsearch = 'Wow, you found a health potion. The items being stolen is slowly get better.'
f71_1.zitems = ['Tiny Healing Potion']
f71_1.zmobs = ['Zombie','Zombie','Zombie']
f71_1.zoneunlocked = True
f71_1.zsearched = False
f71_1.zNPCs = []
f71_1.zkey = []
f71_1.Mup = f72_3
f71_1.Mdown = f70_1
f71_1.Mleft = f71_3
f71_1.Mright = f71_2

f71_2.zname = 'Floor 71, Room 2'
f71_2.zdescript = 'This room was so cramped. It was filled to the brim with anything that could of possibly been in a room.\nAll the stolen items were in this singular room. Or at least it looked like they were.'
f71_2.zsearch = 'You found five Exp Orbs and three green vials. That was only because you couldn\'t get to the rest of the stuff in this room.'
f71_2.zitems = ['MASSIVE Exp Orb','Large Exp Orb','Medium Exp Orb','Tiny Exp Orb','Miniscule Exp Orb','Medium Healing Potion','Tiny Healing Potion','Miniscule Healing Potion']
f71_2.zmobs = []
f71_2.zoneunlocked = True
f71_2.zsearched = False
f71_2.zNPCs = []
f71_2.zkey = []
f71_2.Mup = {}
f71_2.Mdown = {}
f71_2.Mleft = f71_1
f71_2.Mright = {}

f71_3.zname = 'Floor 71, Room 3'
f71_3.zdescript = 'This was the room Minx said her friend Taylor was heading to. She is not here yet...'
f71_3.zsearch = 'Wow, Nothing. Yes, just nothing.'
f71_3.zitems = []
f71_3.zmobs = []
f71_3.zoneunlocked = True
f71_3.zsearched = False
f71_3.zNPCs = []
f71_3.zkey = []
f71_3.Mup = {}
f71_3.Mdown = {}
f71_3.Mleft = {}
f71_3.Mright = f71_1

f70_1.zname = 'Floor 70, Room 1'
f70_1.zdescript = 'Yet another dark room, but this time it doesn\'t seem very empty...'
f70_1.zsearch = 'The Zombie dropped a lot of Healing Potions. Sone is most definitely pissed.'
f70_1.zitems = ['Large Healing Potion','Large Healing Potion','Large Healing Potion']
f70_1.zmobs = ['Undecayed Zombie']
f70_1.zoneunlocked = False
f70_1.zsearched = False
f70_1.zNPCs = []
f70_1.zkey = 'Floor-70 Key'
f70_1.Mup = f71_1
f70_1.Mdown = f69_1
f70_1.Mleft = {}
f70_1.Mright = {}

f69_1.zname = 'Floor 69, Room 1'
f69_1.zdescript = ''
f69_1.zsearch = ''
f69_1.zitems = []
f69_1.zmobs = []
f69_1.zoneunlocked = True
f69_1.zsearched = False
f69_1.zNPCs = []
f69_1.zkey = []
f69_1.Mup = f70_1
f69_1.Mdown = {}
f69_1.Mleft = {}
f69_1.Mright = f69_2

f69_2.zname = 'Floor 69, Room 2'
f69_2.zdescript = ''
f69_2.zsearch = ''
f69_2.zitems = []
f69_2.zmobs = []
f69_2.zoneunlocked = True
f69_2.zsearched = False
f69_2.zNPCs = []
f69_2.zkey = []
f69_2.Mup = {}
f69_2.Mdown = {}
f69_2.Mleft = f69_1
f69_2.Mright = f69_3

f69_3.zname = 'Floor 69, Room 3'
f69_3.zdescript = ''
f69_3.zsearch = ''
f69_3.zitems = []
f69_3.zmobs = []
f69_3.zoneunlocked = True
f69_3.zsearched = False
f69_3.zNPCs = []
f69_3.zkey = []
f69_3.Mup = {}
f69_3.Mdown = f68_1
f69_3.Mleft = f69_2
f69_3.Mright = {}

f68_1.zname = 'Floor 68, Room 1'
f68_1.zdescript = ''
f68_1.zsearch = ''
f68_1.zitems = []
f68_1.zmobs = []
f68_1.zoneunlocked = True
f68_1.zsearched = False
f68_1.zNPCs = []
f68_1.zkey = []
f68_1.Mup = f69_3
f68_1.Mdown = f67_3
f68_1.Mleft = {}
f68_1.Mright = f68_2

f68_2.zname = 'Floor 68, Room 2'
f68_2.zdescript = ''
f68_2.zsearch = ''
f68_2.zitems = []
f68_2.zmobs = []
f68_2.zoneunlocked = True
f68_2.zsearched = False
f68_2.zNPCs = []
f68_2.zkey = []
f68_2.Mup = {}
f68_2.Mdown = f67_2
f68_2.Mleft = f68_1
f68_2.Mright = f68_3

f68_3.zname = 'Floor 68, Room 3'
f68_3.zdescript = ''
f68_3.zsearch = ''
f68_3.zitems = ['Floor-67 Key']
f68_3.zmobs = []
f68_3.zoneunlocked = False
f68_3.zsearched = False
f68_3.zNPCs = []
f68_3.zkey = 'Floor-68 Key'
f68_3.Mup = {}
f68_3.Mdown = f67_1
f68_3.Mleft = f68_2
f68_3.Mright = {}

f67_1.zname = 'Floor 67, Room 1'
f67_1.zdescript = ''
f67_1.zsearch = ''
f67_1.zitems = ['Floor-66 Key']
f67_1.zmobs = []
f67_1.zoneunlocked = True
f67_1.zsearched = False
f67_1.zNPCs = []
f67_1.zkey = []
f67_1.Mup = f68_3
f67_1.Mdown = {}
f67_1.Mleft = f67_2
f67_1.Mright = {}

f67_2.zname = 'Floor 67, Room 2'
f67_2.zdescript = ''
f67_2.zsearch = ''
f67_2.zitems = ['Floor-68 Key']
f67_2.zmobs = []
f67_2.zoneunlocked = True
f67_2.zsearched = False
f67_2.zNPCs = []
f67_2.zkey = []
f67_2.Mup = f68_2
f67_2.Mdown = {}
f67_2.Mleft = f67_3
f67_2.Mright = f67_1

f67_3.zname = 'Floor 67, Room 3'
f67_3.zdescript = ''
f67_3.zsearch = ''
f67_3.zitems = []
f67_3.zmobs = []
f67_3.zoneunlocked = True
f67_3.zsearched = False
f67_3.zNPCs = []
f67_3.zkey = 'Floor-67 Key'
f67_3.Mup = f68_1
f67_3.Mdown = f66_2
f67_3.Mleft = {}
f67_3.Mright = f67_2

f66_1.zname = 'Floor 66, Room 1'
f66_1.zdescript = ''
f66_1.zsearch = ''
f66_1.zitems = []
f66_1.zmobs = []
f66_1.zoneunlocked = True
f66_1.zsearched = False
f66_1.zNPCs = []
f66_1.zkey = 'Floor-66 Key'
f66_1.Mup = f67_3
f66_1.Mdown = {}
f66_1.Mleft = f66_2
f66_1.Mright = {}

f66_2.zname = 'Floor 66, Room 2'
f66_2.zdescript = ''
f66_2.zsearch = ''
f66_2.zitems = []
f66_2.zmobs = []
f66_2.zoneunlocked = True
f66_2.zsearched = False
f66_2.zNPCs = []
f66_2.zkey = []
f66_2.Mup = {}
f66_2.Mdown = f65_2
f66_2.Mleft = f66_3
f66_2.Mright = f66_1

f66_3.zname = 'Floor 66, Room 3'
f66_3.zdescript = ''
f66_3.zsearch = ''
f66_3.zitems = ['Floor-64 Key']
f66_3.zmobs = []
f66_3.zoneunlocked = True
f66_3.zsearched = False
f66_3.zNPCs = []
f66_3.zkey = []
f66_3.Mup = {}
f66_3.Mdown = f65_1
f66_3.Mleft = {}
f66_3.Mright = f66_2

f65_1.zname = 'Floor 65, Room 1'
f65_1.zdescript = ''
f65_1.zsearch = ''
f65_1.zitems = []
f65_1.zmobs = []
f65_1.zoneunlocked = True
f65_1.zsearched = False
f65_1.zNPCs = []
f65_1.zkey = []
f65_1.Mup = f66_3
f65_1.Mdown = f64_2
f65_1.Mleft = f65_3
f65_1.Mright = f65_2

f65_2.zname = 'Floor 65, Room 2'
f65_2.zdescript = ''
f65_2.zsearch = ''
f65_2.zitems = []
f65_2.zmobs = []
f65_2.zoneunlocked = True
f65_2.zsearched = False
f65_2.zNPCs = []
f65_2.zkey = []
f65_2.Mup = f66_2
f65_2.Mdown = {}
f65_2.Mleft = f65_1
f65_2.Mright = {}

f65_3.zname = 'Floor 65, Room 3'
f65_3.zdescript = ''
f65_3.zsearch = ''
f65_3.zitems = []
f65_3.zmobs = []
f65_3.zoneunlocked = True
f65_3.zsearched = False
f65_3.zNPCs = []
f65_3.zkey = []
f65_3.Mup = {}
f65_3.Mdown = f64_1
f65_3.Mleft = {}
f65_3.Mright = f65_1

f64_1.zname = 'Floor 64, Room 1'
f64_1.zdescript = ''
f64_1.zsearch = ''
f64_1.zitems = []
f64_1.zmobs = []
f64_1.zoneunlocked = True
f64_1.zsearched = False
f64_1.zNPCs = []
f64_1.zkey = []
f64_1.Mup = f65_3
f64_1.Mdown = {}
f64_1.Mleft = {}
f64_1.Mright = f64_2

f64_2.zname = 'Floor 64, Room 2'
f64_2.zdescript = ''
f64_2.zsearch = ''
f64_2.zitems = []
f64_2.zmobs = []
f64_2.zoneunlocked = False
f64_2.zsearched = False
f64_2.zNPCs = []
f64_2.zkey = 'Floor-64 Key'
f64_2.Mup = f65_1
f64_2.Mdown = {}
f64_2.Mleft = f64_1
f64_2.Mright = f64_3

f64_3.zname = 'Floor 64, Room 3'
f64_3.zdescript = ''
f64_3.zsearch = ''
f64_3.zitems = []
f64_3.zmobs = []
f64_3.zoneunlocked = True
f64_3.zsearched = False
f64_3.zNPCs = []
f64_3.zkey = []
f64_3.Mup = {}
f64_3.Mdown = f63_1
f64_3.Mleft = f64_2
f64_3.Mright = {}

f63_1.zname = 'Floor 63, Room 1'
f63_1.zdescript = ''
f63_1.zsearch = ''
f63_1.zitems = []
f63_1.zmobs = []
f63_1.zoneunlocked = True
f63_1.zsearched = False
f63_1.zNPCs = []
f63_1.zkey = []
f63_1.Mup = f64_3
f63_1.Mdown = {}
f63_1.Mleft = f63_2
f63_1.Mright = f63_3

f63_2.zname = 'Floor 63, Room 2'
f63_2.zdescript = ''
f63_2.zsearch = ''
f63_2.zitems = []
f63_2.zmobs = []
f63_2.zoneunlocked = True
f63_2.zsearched = False
f63_2.zNPCs = []
f63_2.zkey = []
f63_2.Mup = {}
f63_2.Mdown = f62_3
f63_2.Mleft = {}
f63_2.Mright = f63_1

f63_3.zname = 'Floor 63, Room 3'
f63_3.zdescript = ''
f63_3.zsearch = ''
f63_3.zitems = []
f63_3.zmobs = []
f63_3.zoneunlocked = False
f63_3.zsearched = False
f63_3.zNPCs = []
f63_3.zkey = 'Floor-63 Key'
f63_3.Mup = {}
f63_3.Mdown = f62_1
f63_3.Mleft = f63_1
f63_3.Mright = {}

f62_1.zname = 'Floor 62, Room 1'
f62_1.zdescript = ''
f62_1.zsearch = ''
f62_1.zitems = []
f62_1.zmobs = []
f62_1.zoneunlocked = True
f62_1.zsearched = False
f62_1.zNPCs = []
f62_1.zkey = []
f62_1.Mup = f63_3
f62_1.Mdown = {}
f62_1.Mleft = {}
f62_1.Mright = f62_2

f62_2.zname = 'Floor 62, Room 2'
f62_2.zdescript = ''
f62_2.zsearch = ''
f62_2.zitems = []
f62_2.zmobs = []
f62_2.zoneunlocked = True
f62_2.zsearched = False
f62_2.zNPCs = []
f62_2.zkey = []
f62_2.Mup = {}
f62_2.Mdown = f61_1
f62_2.Mleft = f62_1
f62_2.Mright = {}

f62_3.zname = 'Floor 62, Room 3'
f62_3.zdescript = ''
f62_3.zsearch = ''
f62_3.zitems = ['Floor-63 Key']
f62_3.zmobs = []
f62_3.zoneunlocked = True
f62_3.zsearched = False
f62_3.zNPCs = []
f62_3.zkey = []
f62_3.Mup = f63_2
f62_3.Mdown = {}
f62_3.Mleft = {}
f62_3.Mright = {}

f61_1.zname = 'Floor 61, Room 1'
f61_1.zdescript = ''
f61_1.zsearch = ''
f61_1.zitems = []
f61_1.zmobs = []
f61_1.zoneunlocked = True
f61_1.zsearched = False
f61_1.zNPCs = []
f61_1.zkey = []
f61_1.Mup = f62_2
f61_1.Mdown = {}
f61_1.Mleft = {}
f61_1.Mright = f61_2

f61_2.zname = 'Floor 61, Room 2'
f61_2.zdescript = ''
f61_2.zsearch = ''
f61_2.zitems = ['Floor-60 Key']
f61_2.zmobs = []
f61_2.zoneunlocked = True
f61_2.zsearched = False
f61_2.zNPCs = []
f61_2.zkey = []
f61_2.Mup = {}
f61_2.Mdown = {}
f61_2.Mleft = f61_1
f61_2.Mright = f61_3

f61_3.zname = 'Floor 61, Room 3'
f61_3.zdescript = ''
f61_3.zsearch = ''
f61_3.zitems = []
f61_3.zmobs = []
f61_3.zoneunlocked = True
f61_3.zsearched = False
f61_3.zNPCs = []
f61_3.zkey = []
f61_3.Mup = {}
f61_3.Mdown = f60_1
f61_3.Mleft = f61_2
f61_3.Mright = {}

f60_1.zname = 'Floor 60, Room 1'
f60_1.zdescript = ''
f60_1.zsearch = ''
f60_1.zitems = []
f60_1.zmobs = ['Alpha Wolf']
f60_1.zoneunlocked = False
f60_1.zsearched = False
f60_1.zNPCs = []
f60_1.zkey = 'Floor-60 Key'
f60_1.Mup = f61_3
f60_1.Mdown = f59_1
f60_1.Mleft = {}
f60_1.Mright = {}

f59_1.zname = 'Floor 59, Room 1'
f59_1.zdescript = ''
f59_1.zsearch = ''
f59_1.zitems = []
f59_1.zmobs = []
f59_1.zoneunlocked = True
f59_1.zsearched = False
f59_1.zNPCs = []
f59_1.zkey = []
f59_1.Mup = f60_1
f59_1.Mdown = {}
f59_1.Mleft = f59_2
f59_1.Mright = {}

f59_2.zname = 'Floor 59, Room 2'
f59_2.zdescript = ''
f59_2.zsearch = ''
f59_2.zitems = ['']
f59_2.zmobs = []
f59_2.zoneunlocked = True
f59_2.zsearched = False
f59_2.zNPCs = []
f59_2.zkey = []
f59_2.Mup = {}
f59_2.Mdown = {}
f59_2.Mleft = f59_3
f59_2.Mright = f59_1

f59_3.zname = 'Floor 59, Room 3'
f59_3.zdescript = ''
f59_3.zsearch = ''
f59_3.zitems = ['']
f59_3.zmobs = []
f59_3.zoneunlocked = True
f59_3.zsearched = False
f59_3.zNPCs = []
f59_3.zkey = []
f59_3.Mup = {}
f59_3.Mdown = f58_1
f59_3.Mleft = {}
f59_3.Mright = f59_2

f58_1.zname = 'Floor 58, Room 1'
f58_1.zdescript = ''
f58_1.zsearch = ''
f58_1.zitems = []
f58_1.zmobs = []
f58_1.zoneunlocked = True
f58_1.zsearched = False
f58_1.zNPCs = []
f58_1.zkey = []
f58_1.Mup = f59_3
f58_1.Mdown = f57_1
f58_1.Mleft = f58_3
f58_1.Mright = f58_2

f58_2.zname = 'Floor 58, Room 2'
f58_2.zdescript = ''
f58_2.zsearch = ''
f58_2.zitems = []
f58_2.zmobs = []
f58_2.zoneunlocked = True
f58_2.zsearched = False
f58_2.zNPCs = []
f58_2.zkey = []
f58_2.Mup = {}
f58_2.Mdown = {}
f58_2.Mleft = f58_1
f58_2.Mright = {}

f58_3.zname = 'Floor 58, Room 3'
f58_3.zdescript = ''
f58_3.zsearch = ''
f58_3.zitems = ['Floor-57 Key']
f58_3.zmobs = []
f58_3.zoneunlocked = True
f58_3.zsearched = False
f58_3.zNPCs = []
f58_3.zkey = []
f58_3.Mup = {}
f58_3.Mdown = {}
f58_3.Mleft = {}
f58_3.Mright = f58_1

f57_1.zname = 'Floor 57, Room 1'
f57_1.zdescript = ''
f57_1.zsearch = ''
f57_1.zitems = []
f57_1.zmobs = []
f57_1.zoneunlocked = False
f57_1.zsearched = False
f57_1.zNPCs = []
f57_1.zkey = 'Floor-57 Key'
f57_1.Mup = f58_1
f57_1.Mdown = f56_2
f57_1.Mleft = {}
f57_1.Mright = f57_2

f57_2.zname = 'Floor 57, Room 2'
f57_2.zdescript = ''
f57_2.zsearch = ''
f57_2.zitems = []
f57_2.zmobs = []
f57_2.zoneunlocked = True
f57_2.zsearched = False
f57_2.zNPCs = []
f57_2.zkey = []
f57_2.Mup = {}
f57_2.Mdown = f56_1
f57_2.Mleft = f57_1
f57_2.Mright = f57_3

f57_3.zname = 'Floor 57, Room 3'
f57_3.zdescript = ''
f57_3.zsearch = ''
f57_3.zitems = ['Floor-56 Key']
f57_3.zmobs = []
f57_3.zoneunlocked = True
f57_3.zsearched = False
f57_3.zNPCs = []
f57_3.zkey = []
f57_3.Mup = {}
f57_3.Mdown = {}
f57_3.Mleft = f57_2
f57_3.Mright = {}

f56_1.zname = 'Floor 56, Room 1'
f56_1.zdescript = ''
f56_1.zsearch = ''
f56_1.zitems = []
f56_1.zmobs = []
f56_1.zoneunlocked = False
f56_1.zsearched = False
f56_1.zNPCs = []
f56_1.zkey = 'Floor-56 Key'
f56_1.Mup = f57_2
f56_1.Mdown = f55_1
f56_1.Mleft = f56_2
f56_1.Mright = f56_3

f56_2.zname = 'Floor 56, Room 2'
f56_2.zdescript = ''
f56_2.zsearch = ''
f56_2.zitems = []
f56_2.zmobs = []
f56_2.zoneunlocked = True
f56_2.zsearched = False
f56_2.zNPCs = []
f56_2.zkey = []
f56_2.Mup = f57_1
f56_2.Mdown = f55_3
f56_2.Mleft = {}
f56_2.Mright = f56_1

f56_3.zname = 'Floor 56, Room 3'
f56_3.zdescript = ''
f56_3.zsearch = ''
f56_3.zitems = []
f56_3.zmobs = []
f56_3.zoneunlocked = True
f56_3.zsearched = False
f56_3.zNPCs = []
f56_3.zkey = []
f56_3.Mup = {}
f56_3.Mdown = f55_2
f56_3.Mleft = f56_1
f56_3.Mright = {}

f55_1.zname = 'Floor 55, Room 1'
f55_1.zdescript = ''
f55_1.zsearch = ''
f55_1.zitems = []
f55_1.zmobs = []
f55_1.zoneunlocked = False
f55_1.zsearched = False
f55_1.zNPCs = []
f55_1.zkey = 'Floor-55 Key'
f55_1.Mup = f56_1
f55_1.Mdown = f54_2
f55_1.Mleft = {}
f55_1.Mright = f55_2

f55_2.zname = 'Floor 55, Room 2'
f55_2.zdescript = ''
f55_2.zsearch = ''
f55_2.zitems = []
f55_2.zmobs = []
f55_2.zoneunlocked = True
f55_2.zsearched = False
f55_2.zNPCs = []
f55_2.zkey = []
f55_2.Mup = f56_3
f55_2.Mdown = f54_1
f55_2.Mleft = f55_1
f55_2.Mright = {}

f55_3.zname = 'Floor 55, Room 3'
f55_3.zdescript = ''
f55_3.zsearch = ''
f55_3.zitems = ['Floor-55 Key']
f55_3.zmobs = []
f55_3.zoneunlocked = True
f55_3.zsearched = False
f55_3.zNPCs = []
f55_3.zkey = []
f55_3.Mup = f56_2
f55_3.Mdown = {}
f55_3.Mleft = {}
f55_3.Mright = {}

f54_1.zname = 'Floor 54, Room 1'
f54_1.zdescript = ''
f54_1.zsearch = ''
f54_1.zitems = ['Floor-54 Key']
f54_1.zmobs = []
f54_1.zoneunlocked = True
f54_1.zsearched = False
f54_1.zNPCs = []
f54_1.zkey = []
f54_1.Mup = f55_2
f54_1.Mdown = {}
f54_1.Mleft = f54_2
f54_1.Mright = {}

f54_2.zname = 'Floor 54, Room 2'
f54_2.zdescript = ''
f54_2.zsearch = ''
f54_2.zitems = []
f54_2.zmobs = []
f54_2.zoneunlocked = False
f54_2.zsearched = False
f54_2.zNPCs = []
f54_2.zkey = 'Floor-54 Key'
f54_2.Mup = f55_1
f54_2.Mdown = {}
f54_2.Mleft = f54_3
f54_2.Mright = f54_1

f54_3.zname = 'Floor 54, Room 3'
f54_3.zdescript = ''
f54_3.zsearch = ''
f54_3.zitems = []
f54_3.zmobs = []
f54_3.zoneunlocked = True
f54_3.zsearched = False
f54_3.zNPCs = []
f54_3.zkey = []
f54_3.Mup = {}
f54_3.Mdown = f53_1
f54_3.Mleft = {}
f54_3.Mright = f54_2

f53_1.zname = 'Floor 53, Room 1'
f53_1.zdescript = ''
f53_1.zsearch = ''
f53_1.zitems = []
f53_1.zmobs = []
f53_1.zoneunlocked = True
f53_1.zsearched = False
f53_1.zNPCs = []
f53_1.zkey = []
f53_1.Mup = f54_3
f53_1.Mdown = {}
f53_1.Mleft = f53_2
f53_1.Mright = {}

f53_2.zname = 'Floor 53, Room 2'
f53_2.zdescript = ''
f53_2.zsearch = ''
f53_2.zitems = []
f53_2.zmobs = []
f53_2.zoneunlocked = True
f53_2.zsearched = False
f53_2.zNPCs = []
f53_2.zkey = []
f53_2.Mup = {}
f53_2.Mdown = f52_1
f53_2.Mleft = f53_3
f53_2.Mright = f53_1

f53_3.zname = 'Floor 53, Room 3'
f53_3.zdescript = ''
f53_3.zsearch = ''
f53_3.zitems = []
f53_3.zmobs = []
f53_3.zoneunlocked = True
f53_3.zsearched = False
f53_3.zNPCs = []
f53_3.zkey = []
f53_3.Mup = {}
f53_3.Mdown = f52_2
f53_3.Mleft = {}
f53_3.Mright = f53_2

f52_1.zname = 'Floor 52, Room 1'
f52_1.zdescript = ''
f52_1.zsearch = ''
f52_1.zitems = ['Floor-52 Key']
f52_1.zmobs = []
f52_1.zoneunlocked = True
f52_1.zsearched = False
f52_1.zNPCs = []
f52_1.zkey = []
f52_1.Mup = f53_2
f52_1.Mdown = {}
f52_1.Mleft = f52_2
f52_1.Mright = {}

f52_2.zname = 'Floor 52, Room 2'
f52_2.zdescript = ''
f52_2.zsearch = ''
f52_2.zitems = []
f52_2.zmobs = []
f52_2.zoneunlocked = True
f52_2.zsearched = False
f52_2.zNPCs = []
f52_2.zkey = []
f52_2.Mup = f53_3
f52_2.Mdown = {}
f52_2.Mleft = f52_3
f52_2.Mright = f52_1

f52_3.zname = 'Floor 52, Room 3'
f52_3.zdescript = ''
f52_3.zsearch = ''
f52_3.zitems = []
f52_3.zmobs = []
f52_3.zoneunlocked = False
f52_3.zsearched = False
f52_3.zNPCs = []
f52_3.zkey = 'Floor-52 Key'
f52_3.Mup = {}
f52_3.Mdown = f51_1
f52_3.Mleft = {}
f52_3.Mright = f52_2

f51_1.zname = 'Floor 51, Room 1'
f51_1.zdescript = ''
f51_1.zsearch = ''
f51_1.zitems = []
f51_1.zmobs = []
f51_1.zoneunlocked = True
f51_1.zsearched = False
f51_1.zNPCs = []
f51_1.zkey = []
f51_1.Mup = f52_3
f51_1.Mdown = f50_1
f51_1.Mleft = f51_3
f51_1.Mright = f51_2

f51_2.zname = 'Floor 51, Room 2'
f51_2.zdescript = ''
f51_2.zsearch = ''
f51_2.zitems = []
f51_2.zmobs = []
f51_2.zoneunlocked = True
f51_2.zsearched = False
f51_2.zNPCs = []
f51_2.zkey = []
f51_2.Mup = {}
f51_2.Mdown = {}
f51_2.Mleft = f51_1
f51_2.Mright = {}

f51_3.zname = 'Floor 51, Room 3'
f51_3.zdescript = ''
f51_3.zsearch = ''
f51_3.zitems = ['Floor-50 Key']
f51_3.zmobs = []
f51_3.zoneunlocked = True
f51_3.zsearched = False
f51_3.zNPCs = []
f51_3.zkey = []
f51_3.Mup = {}
f51_3.Mdown = {}
f51_3.Mleft = {}
f51_3.Mright = f51_1

f50_1.zname = 'Floor 50, Room 1'
f50_1.zdescript = ''
f50_1.zsearch = ''
f50_1.zitems = []
f50_1.zmobs = ['Hobbiest Hobgoblin']
f50_1.zoneunlocked = False
f50_1.zsearched = False
f50_1.zNPCs = []
f50_1.zkey = 'Floor-50 Key'
f50_1.Mup = f51_1
f50_1.Mdown = f49_1
f50_1.Mleft = {}
f50_1.Mright = {}

f49_1.zname = 'Floor 49, Room 1'
f49_1.zdescript = ''
f49_1.zsearch = ''
f49_1.zitems = []
f49_1.zmobs = []
f49_1.zoneunlocked = True
f49_1.zsearched = False
f49_1.zNPCs = []
f49_1.zkey = []
f49_1.Mup = f50_1
f49_1.Mdown = {}
f49_1.Mleft = {}
f49_1.Mright = f49_2

f49_2.zname = 'Floor 49, Room 2'
f49_2.zdescript = ''
f49_2.zsearch = ''
f49_2.zitems = []
f49_2.zmobs = []
f49_2.zoneunlocked = True
f49_2.zsearched = False
f49_2.zNPCs = []
f49_2.zkey = []
f49_2.Mup = {}
f49_2.Mdown = {}
f49_2.Mleft = f49_1
f49_2.Mright = f49_3

f49_3.zname = 'Floor 49, Room 3'
f49_3.zdescript = ''
f49_3.zsearch = ''
f49_3.zitems = []
f49_3.zmobs = []
f49_3.zoneunlocked = True
f49_3.zsearched = False
f49_3.zNPCs = []
f49_3.zkey = []
f49_3.Mup = {}
f49_3.Mdown = f48_1
f49_3.Mleft = f49_2
f49_3.Mright = {}

f48_1.zname = 'Floor 48, Room 1'
f48_1.zdescript = ''
f48_1.zsearch = ''
f48_1.zitems = []
f48_1.zmobs = []
f48_1.zoneunlocked = True
f48_1.zsearched = False
f48_1.zNPCs = []
f48_1.zkey = []
f48_1.Mup = f49_3
f48_1.Mdown = f47_3
f48_1.Mleft = {}
f48_1.Mright = f48_2

f48_2.zname = 'Floor 48, Room 2'
f48_2.zdescript = ''
f48_2.zsearch = ''
f48_2.zitems = []
f48_2.zmobs = []
f48_2.zoneunlocked = True
f48_2.zsearched = False
f48_2.zNPCs = []
f48_2.zkey = []
f48_2.Mup = {}
f48_2.Mdown = f47_2
f48_2.Mleft = f48_1
f48_2.Mright = f48_3

f48_3.zname = 'Floor 48, Room 3'
f48_3.zdescript = ''
f48_3.zsearch = ''
f48_3.zitems = ['Floor-47 Key']
f48_3.zmobs = []
f48_3.zoneunlocked = False
f48_3.zsearched = False
f48_3.zNPCs = []
f48_3.zkey = 'Floor-48 Key'
f48_3.Mup = {}
f48_3.Mdown = f47_1
f48_3.Mleft = f48_2
f48_3.Mright = {}

f47_1.zname = 'Floor 47, Room 1'
f47_1.zdescript = ''
f47_1.zsearch = ''
f47_1.zitems = ['Floor-46 Key']
f47_1.zmobs = []
f47_1.zoneunlocked = True
f47_1.zsearched = False
f47_1.zNPCs = []
f47_1.zkey = []
f47_1.Mup = f48_3
f47_1.Mdown = {}
f47_1.Mleft = f47_2
f47_1.Mright = {}

f47_2.zname = 'Floor 47, Room 2'
f47_2.zdescript = ''
f47_2.zsearch = ''
f47_2.zitems = ['Floor-48 Key']
f47_2.zmobs = []
f47_2.zoneunlocked = True
f47_2.zsearched = False
f47_2.zNPCs = []
f47_2.zkey = []
f47_2.Mup = f48_2
f47_2.Mdown = {}
f47_2.Mleft = f47_3
f47_2.Mright = f47_1

f47_3.zname = 'Floor 47, Room 3'
f47_3.zdescript = ''
f47_3.zsearch = ''
f47_3.zitems = []
f47_3.zmobs = []
f47_3.zoneunlocked = True
f47_3.zsearched = False
f47_3.zNPCs = []
f47_3.zkey = 'Floor-47 Key'
f47_3.Mup = f48_1
f47_3.Mdown = f46_2
f47_3.Mleft = {}
f47_3.Mright = f47_2

f46_1.zname = 'Floor 46, Room 1'
f46_1.zdescript = ''
f46_1.zsearch = ''
f46_1.zitems = []
f46_1.zmobs = []
f46_1.zoneunlocked = True
f46_1.zsearched = False
f46_1.zNPCs = []
f46_1.zkey = 'Floor-46 Key'
f46_1.Mup = f47_3
f46_1.Mdown = {}
f46_1.Mleft = f46_2
f46_1.Mright = {}

f46_2.zname = 'Floor 46, Room 2'
f46_2.zdescript = ''
f46_2.zsearch = ''
f46_2.zitems = []
f46_2.zmobs = []
f46_2.zoneunlocked = True
f46_2.zsearched = False
f46_2.zNPCs = []
f46_2.zkey = []
f46_2.Mup = {}
f46_2.Mdown = f45_2
f46_2.Mleft = f46_3
f46_2.Mright = f46_1

f46_3.zname = 'Floor 46, Room 3'
f46_3.zdescript = ''
f46_3.zsearch = ''
f46_3.zitems = ['Floor-44 Key']
f46_3.zmobs = []
f46_3.zoneunlocked = True
f46_3.zsearched = False
f46_3.zNPCs = []
f46_3.zkey = []
f46_3.Mup = {}
f46_3.Mdown = f45_1
f46_3.Mleft = {}
f46_3.Mright = f46_2

f45_1.zname = 'Floor 45, Room 1'
f45_1.zdescript = ''
f45_1.zsearch = ''
f45_1.zitems = []
f45_1.zmobs = []
f45_1.zoneunlocked = True
f45_1.zsearched = False
f45_1.zNPCs = []
f45_1.zkey = []
f45_1.Mup = f46_3
f45_1.Mdown = f44_2
f45_1.Mleft = f45_3
f45_1.Mright = f45_2

f45_2.zname = 'Floor 45, Room 2'
f45_2.zdescript = ''
f45_2.zsearch = ''
f45_2.zitems = []
f45_2.zmobs = []
f45_2.zoneunlocked = True
f45_2.zsearched = False
f45_2.zNPCs = []
f45_2.zkey = []
f45_2.Mup = f46_2
f45_2.Mdown = {}
f45_2.Mleft = f45_1
f45_2.Mright = {}

f45_3.zname = 'Floor 45, Room 3'
f45_3.zdescript = ''
f45_3.zsearch = ''
f45_3.zitems = []
f45_3.zmobs = []
f45_3.zoneunlocked = True
f45_3.zsearched = False
f45_3.zNPCs = []
f45_3.zkey = []
f45_3.Mup = {}
f45_3.Mdown = f44_1
f45_3.Mleft = {}
f45_3.Mright = f45_1

f44_1.zname = 'Floor 44, Room 1'
f44_1.zdescript = ''
f44_1.zsearch = ''
f44_1.zitems = []
f44_1.zmobs = []
f44_1.zoneunlocked = True
f44_1.zsearched = False
f44_1.zNPCs = []
f44_1.zkey = []
f44_1.Mup = f45_3
f44_1.Mdown = {}
f44_1.Mleft = {}
f44_1.Mright = f44_2

f44_2.zname = 'Floor 44, Room 2'
f44_2.zdescript = ''
f44_2.zsearch = ''
f44_2.zitems = []
f44_2.zmobs = []
f44_2.zoneunlocked = False
f44_2.zsearched = False
f44_2.zNPCs = []
f44_2.zkey = 'Floor-44 Key'
f44_2.Mup = f45_1
f44_2.Mdown = {}
f44_2.Mleft = f44_1
f44_2.Mright = f44_3

f44_3.zname = 'Floor 44, Room 3'
f44_3.zdescript = ''
f44_3.zsearch = ''
f44_3.zitems = []
f44_3.zmobs = []
f44_3.zoneunlocked = True
f44_3.zsearched = False
f44_3.zNPCs = []
f44_3.zkey = []
f44_3.Mup = {}
f44_3.Mdown = f43_1
f44_3.Mleft = f44_2
f44_3.Mright = {}

f43_1.zname = 'Floor 43, Room 1'
f43_1.zdescript = ''
f43_1.zsearch = ''
f43_1.zitems = []
f43_1.zmobs = []
f43_1.zoneunlocked = True
f43_1.zsearched = False
f43_1.zNPCs = []
f43_1.zkey = []
f43_1.Mup = f44_3
f43_1.Mdown = {}
f43_1.Mleft = f43_2
f43_1.Mright = f43_3

f43_2.zname = 'Floor 43, Room 2'
f43_2.zdescript = ''
f43_2.zsearch = ''
f43_2.zitems = []
f43_2.zmobs = []
f43_2.zoneunlocked = True
f43_2.zsearched = False
f43_2.zNPCs = []
f43_2.zkey = []
f43_2.Mup = {}
f43_2.Mdown = f42_3
f43_2.Mleft = {}
f43_2.Mright = f43_1

f43_3.zname = 'Floor 43, Room 3'
f43_3.zdescript = ''
f43_3.zsearch = ''
f43_3.zitems = []
f43_3.zmobs = []
f43_3.zoneunlocked = False
f43_3.zsearched = False
f43_3.zNPCs = []
f43_3.zkey = 'Floor-43 Key'
f43_3.Mup = {}
f43_3.Mdown = f42_1
f43_3.Mleft = f43_1
f43_3.Mright = {}

f42_1.zname = 'Floor 42, Room 1'
f42_1.zdescript = ''
f42_1.zsearch = ''
f42_1.zitems = []
f42_1.zmobs = []
f42_1.zoneunlocked = True
f42_1.zsearched = False
f42_1.zNPCs = []
f42_1.zkey = []
f42_1.Mup = f43_3
f42_1.Mdown = {}
f42_1.Mleft = {}
f42_1.Mright = f42_2

f42_2.zname = 'Floor 42, Room 2'
f42_2.zdescript = ''
f42_2.zsearch = ''
f42_2.zitems = []
f42_2.zmobs = []
f42_2.zoneunlocked = True
f42_2.zsearched = False
f42_2.zNPCs = []
f42_2.zkey = []
f42_2.Mup = {}
f42_2.Mdown = f41_1
f42_2.Mleft = f42_1
f42_2.Mright = {}

f42_3.zname = 'Floor 42, Room 3'
f42_3.zdescript = ''
f42_3.zsearch = ''
f42_3.zitems = ['Floor-43 Key']
f42_3.zmobs = []
f42_3.zoneunlocked = True
f42_3.zsearched = False
f42_3.zNPCs = []
f42_3.zkey = []
f42_3.Mup = f43_2
f42_3.Mdown = {}
f42_3.Mleft = {}
f42_3.Mright = {}

f41_1.zname = 'Floor 41, Room 1'
f41_1.zdescript = ''
f41_1.zsearch = ''
f41_1.zitems = []
f41_1.zmobs = []
f41_1.zoneunlocked = True
f41_1.zsearched = False
f41_1.zNPCs = []
f41_1.zkey = []
f41_1.Mup = f42_2
f41_1.Mdown = {}
f41_1.Mleft = {}
f41_1.Mright = f41_2

f41_2.zname = 'Floor 41, Room 2'
f41_2.zdescript = ''
f41_2.zsearch = ''
f41_2.zitems = ['Floor-40 Key']
f41_2.zmobs = []
f41_2.zoneunlocked = True
f41_2.zsearched = False
f41_2.zNPCs = []
f41_2.zkey = []
f41_2.Mup = {}
f41_2.Mdown = {}
f41_2.Mleft = f41_1
f41_2.Mright = f41_3

f41_3.zname = 'Floor 41, Room 3'
f41_3.zdescript = ''
f41_3.zsearch = ''
f41_3.zitems = []
f41_3.zmobs = []
f41_3.zoneunlocked = True
f41_3.zsearched = False
f41_3.zNPCs = []
f41_3.zkey = []
f41_3.Mup = {}
f41_3.Mdown = f40_1
f41_3.Mleft = f41_2
f41_3.Mright = {}

f40_1.zname = 'Floor 40, Room 1'
f40_1.zdescript = ''
f40_1.zsearch = ''
f40_1.zitems = []
f40_1.zmobs = ['Vampire Lord 1']
f40_1.zoneunlocked = False
f40_1.zsearched = False
f40_1.zNPCs = []
f40_1.zkey = 'Floor-40 Key'
f40_1.Mup = f41_3
f40_1.Mdown = f39_1
f40_1.Mleft = {}
f40_1.Mright = {}

f39_1.zname = 'Floor 39, Room 1'
f39_1.zdescript = ''
f39_1.zsearch = ''
f39_1.zitems = []
f39_1.zmobs = []
f39_1.zoneunlocked = True
f39_1.zsearched = False
f39_1.zNPCs = []
f39_1.zkey = []
f39_1.Mup = f40_1
f39_1.Mdown = {}
f39_1.Mleft = f39_2
f39_1.Mright = {}

f39_2.zname = 'Floor 39, Room 2'
f39_2.zdescript = ''
f39_2.zsearch = ''
f39_2.zitems = []
f39_2.zmobs = []
f39_2.zoneunlocked = True
f39_2.zsearched = False
f39_2.zNPCs = []
f39_2.zkey = []
f39_2.Mup = {}
f39_2.Mdown = {}
f39_2.Mleft = f39_3
f39_2.Mright = f39_1

f39_3.zname = 'Floor 39, Room 3'
f39_3.zdescript = ''
f39_3.zsearch = ''
f39_3.zitems = []
f39_3.zmobs = []
f39_3.zoneunlocked = True
f39_3.zsearched = False
f39_3.zNPCs = []
f39_3.zkey = []
f39_3.Mup = {}
f39_3.Mdown = f38_1
f39_3.Mleft = {}
f39_3.Mright = f39_2

f38_1.zname = 'Floor 38, Room 1'
f38_1.zdescript = ''
f38_1.zsearch = ''
f38_1.zitems = []
f38_1.zmobs = []
f38_1.zoneunlocked = True
f38_1.zsearched = False
f38_1.zNPCs = []
f38_1.zkey = []
f38_1.Mup = f39_3
f38_1.Mdown = f39_1
f38_1.Mleft = f38_3
f38_1.Mright = f38_2

f38_2.zname = 'Floor 38, Room 2'
f38_2.zdescript = ''
f38_2.zsearch = ''
f38_2.zitems = []
f38_2.zmobs = []
f38_2.zoneunlocked = True
f38_2.zsearched = False
f38_2.zNPCs = []
f38_2.zkey = []
f38_2.Mup = {}
f38_2.Mdown = {}
f38_2.Mleft = f38_1
f38_2.Mright = {}

f38_3.zname = 'Floor 38, Room 3'
f38_3.zdescript = ''
f38_3.zsearch = ''
f38_3.zitems = ['Floor-37 Key']
f38_3.zmobs = []
f38_3.zoneunlocked = True
f38_3.zsearched = False
f38_3.zNPCs = []
f38_3.zkey = []
f38_3.Mup = {}
f38_3.Mdown = {}
f38_3.Mleft = {}
f38_3.Mright = f38_1

f37_1.zname = 'Floor 37, Room 1'
f37_1.zdescript = ''
f37_1.zsearch = ''
f37_1.zitems = []
f37_1.zmobs = []
f37_1.zoneunlocked = False
f37_1.zsearched = False
f37_1.zNPCs = []
f37_1.zkey = 'Floor-37 Key'
f37_1.Mup = f38_1
f37_1.Mdown = f36_2
f37_1.Mleft = {}
f37_1.Mright = f37_2

f37_2.zname = 'Floor 37, Room 2'
f37_2.zdescript = ''
f37_2.zsearch = ''
f37_2.zitems = []
f37_2.zmobs = []
f37_2.zoneunlocked = True
f37_2.zsearched = False
f37_2.zNPCs = []
f37_2.zkey = []
f37_2.Mup = {}
f37_2.Mdown = f36_1
f37_2.Mleft = f37_1
f37_2.Mright = f37_3

f37_3.zname = 'Floor 37, Room 3'
f37_3.zdescript = ''
f37_3.zsearch = ''
f37_3.zitems = ['Floor-36 Key']
f37_3.zmobs = []
f37_3.zoneunlocked = True
f37_3.zsearched = False
f37_3.zNPCs = []
f37_3.zkey = []
f37_3.Mup = {}
f37_3.Mdown = {}
f37_3.Mleft = f37_2
f37_3.Mright = {}

f36_1.zname = 'Floor 36, Room 1'
f36_1.zdescript = ''
f36_1.zsearch = ''
f36_1.zitems = []
f36_1.zmobs = []
f36_1.zoneunlocked = False
f36_1.zsearched = False
f36_1.zNPCs = []
f36_1.zkey = 'Floor-36 Key'
f36_1.Mup = f37_2
f36_1.Mdown = f35_1
f36_1.Mleft = f36_2
f36_1.Mright = f36_3

f36_2.zname = 'Floor 36, Room 2'
f36_2.zdescript = ''
f36_2.zsearch = ''
f36_2.zitems = []
f36_2.zmobs = []
f36_2.zoneunlocked = True
f36_2.zsearched = False
f36_2.zNPCs = []
f36_2.zkey = []
f36_2.Mup = f37_1
f36_2.Mdown = f35_3
f36_2.Mleft = {}
f36_2.Mright = f36_1

f36_3.zname = 'Floor 36, Room 3'
f36_3.zdescript = ''
f36_3.zsearch = ''
f36_3.zitems = []
f36_3.zmobs = []
f36_3.zoneunlocked = True
f36_3.zsearched = False
f36_3.zNPCs = []
f36_3.zkey = []
f36_3.Mup = {}
f36_3.Mdown = f35_2
f36_3.Mleft = f36_1
f36_3.Mright = {}

f35_1.zname = 'Floor 35, Room 1'
f35_1.zdescript = ''
f35_1.zsearch = ''
f35_1.zitems = []
f35_1.zmobs = []
f35_1.zoneunlocked = False
f35_1.zsearched = False
f35_1.zNPCs = []
f35_1.zkey = 'Floor-35 Key'
f35_1.Mup = f36_1
f35_1.Mdown = f34_2
f35_1.Mleft = {}
f35_1.Mright = f35_2

f35_2.zname = 'Floor 35, Room 2'
f35_2.zdescript = ''
f35_2.zsearch = ''
f35_2.zitems = []
f35_2.zmobs = []
f35_2.zoneunlocked = True
f35_2.zsearched = False
f35_2.zNPCs = []
f35_2.zkey = []
f35_2.Mup = f36_3
f35_2.Mdown = f34_1
f35_2.Mleft = f35_1
f35_2.Mright = {}

f35_3.zname = 'Floor 35, Room 3'
f35_3.zdescript = ''
f35_3.zsearch = ''
f35_3.zitems = ['Floor-35 Key']
f35_3.zmobs = []
f35_3.zoneunlocked = True
f35_3.zsearched = False
f35_3.zNPCs = []
f35_3.zkey = []
f35_3.Mup = f36_2
f35_3.Mdown = {}
f35_3.Mleft = {}
f35_3.Mright = {}

f34_1.zname = 'Floor 34, Room 1'
f34_1.zdescript = ''
f34_1.zsearch = ''
f34_1.zitems = ['Floor-34 Key']
f34_1.zmobs = []
f34_1.zoneunlocked = True
f34_1.zsearched = False
f34_1.zNPCs = []
f34_1.zkey = []
f34_1.Mup = f35_2
f34_1.Mdown = {}
f34_1.Mleft = f34_2
f34_1.Mright = {}

f34_2.zname = 'Floor 34, Room 2'
f34_2.zdescript = ''
f34_2.zsearch = ''
f34_2.zitems = []
f34_2.zmobs = []
f34_2.zoneunlocked = False
f34_2.zsearched = False
f34_2.zNPCs = []
f34_2.zkey = 'Floor-34 Key'
f34_2.Mup = f35_1
f34_2.Mdown = {}
f34_2.Mleft = f34_3
f34_2.Mright = f34_1

f34_3.zname = 'Floor 34, Room 3'
f34_3.zdescript = ''
f34_3.zsearch = ''
f34_3.zitems = []
f34_3.zmobs = []
f34_3.zoneunlocked = True
f34_3.zsearched = False
f34_3.zNPCs = []
f34_3.zkey = []
f34_3.Mup = {}
f34_3.Mdown = f33_1
f34_3.Mleft = {}
f34_3.Mright = f34_2

f33_1.zname = 'Floor 33, Room 1'
f33_1.zdescript = ''
f33_1.zsearch = ''
f33_1.zitems = []
f33_1.zmobs = []
f33_1.zoneunlocked = True
f33_1.zsearched = False
f33_1.zNPCs = []
f33_1.zkey = []
f33_1.Mup = f34_3
f33_1.Mdown = {}
f33_1.Mleft = f33_2
f33_1.Mright = {}

f33_2.zname = 'Floor 33, Room 2'
f33_2.zdescript = ''
f33_2.zsearch = ''
f33_2.zitems = []
f33_2.zmobs = []
f33_2.zoneunlocked = True
f33_2.zsearched = False
f33_2.zNPCs = []
f33_2.zkey = []
f33_2.Mup = {}
f33_2.Mdown = f32_1
f33_2.Mleft = f33_3
f33_2.Mright = f33_1

f33_3.zname = 'Floor 33, Room 3'
f33_3.zdescript = ''
f33_3.zsearch = ''
f33_3.zitems = []
f33_3.zmobs = []
f33_3.zoneunlocked = True
f33_3.zsearched = False
f33_3.zNPCs = []
f33_3.zkey = []
f33_3.Mup = {}
f33_3.Mdown = f32_2
f33_3.Mleft = {}
f33_3.Mright = f33_2

f32_1.zname = 'Floor 32, Room 1'
f32_1.zdescript = ''
f32_1.zsearch = ''
f32_1.zitems = ['Floor-32 Key']
f32_1.zmobs = []
f32_1.zoneunlocked = True
f32_1.zsearched = False
f32_1.zNPCs = []
f32_1.zkey = []
f32_1.Mup = f33_2
f32_1.Mdown = {}
f32_1.Mleft = f32_2
f32_1.Mright = {}

f32_2.zname = 'Floor 32, Room 2'
f32_2.zdescript = ''
f32_2.zsearch = ''
f32_2.zitems = []
f32_2.zmobs = []
f32_2.zoneunlocked = True
f32_2.zsearched = False
f32_2.zNPCs = []
f32_2.zkey = []
f32_2.Mup = f33_3
f32_2.Mdown = {}
f32_2.Mleft = f32_3
f32_2.Mright = f32_1

f32_3.zname = 'Floor 32, Room 3'
f32_3.zdescript = ''
f32_3.zsearch = ''
f32_3.zitems = []
f32_3.zmobs = []
f32_3.zoneunlocked = False
f32_3.zsearched = False
f32_3.zNPCs = []
f32_3.zkey = 'Floor-32 Key'
f32_3.Mup = {}
f32_3.Mdown = f31_1
f32_3.Mleft = {}
f32_3.Mright = f32_2

f31_1.zname = 'Floor 31, Room 1'
f31_1.zdescript = ''
f31_1.zsearch = ''
f31_1.zitems = []
f31_1.zmobs = []
f31_1.zoneunlocked = True
f31_1.zsearched = False
f31_1.zNPCs = []
f31_1.zkey = []
f31_1.Mup = f32_3
f31_1.Mdown = f30_1
f31_1.Mleft = f31_3
f31_1.Mright = f31_2

f31_2.zname = 'Floor 31, Room 2'
f31_2.zdescript = ''
f31_2.zsearch = ''
f31_2.zitems = []
f31_2.zmobs = []
f31_2.zoneunlocked = True
f31_2.zsearched = False
f31_2.zNPCs = []
f31_2.zkey = []
f31_2.Mup = {}
f31_2.Mdown = {}
f31_2.Mleft = f31_1
f31_2.Mright = {}

f31_3.zname = 'Floor 31, Room 3'
f31_3.zdescript = ''
f31_3.zsearch = ''
f31_3.zitems = ['Floor-30 Key']
f31_3.zmobs = []
f31_3.zoneunlocked = True
f31_3.zsearched = False
f31_3.zNPCs = []
f31_3.zkey = []
f31_3.Mup = {}
f31_3.Mdown = {}
f31_3.Mleft = {}
f31_3.Mright = f31_1

f30_1.zname = 'Floor 30, Room 1'
f30_1.zdescript = ''
f30_1.zsearch = ''
f30_1.zitems = []
f30_1.zmobs = ['Vampire Lord 2']
f30_1.zoneunlocked = False
f30_1.zsearched = False
f30_1.zNPCs = []
f30_1.zkey = 'Floor-30 Key'
f30_1.Mup = f31_1
f30_1.Mdown = f29_1
f30_1.Mleft = {}
f30_1.Mright = {}

f29_1.zname = 'Floor 29, Room 1'
f29_1.zdescript = ''
f29_1.zsearch = ''
f29_1.zitems = []
f29_1.zmobs = []
f29_1.zoneunlocked = True
f29_1.zsearched = False
f29_1.zNPCs = []
f29_1.zkey = ''
f29_1.Mup = f30_1
f29_1.Mdown = f28_1
f29_1.Mleft = {}
f29_1.Mright = f29_2

f29_2.zname = 'Floor 29, Room 2'
f29_2.zdescript = ''
f29_2.zsearch = ''
f29_2.zitems = []
f29_2.zmobs = []
f29_2.zoneunlocked = True
f29_2.zsearched = False
f29_2.zNPCs = []
f29_2.zkey = []
f29_2.Mup = {}
f29_2.Mdown = f28_2
f29_2.Mleft = f29_1
f29_2.Mright = f29_3

f29_3.zname = 'Floor 29, Room 3'
f29_3.zdescript = ''
f29_3.zsearch = ''
f29_3.zitems = []
f29_3.zmobs = []
f29_3.zoneunlocked = True
f29_3.zsearched = False
f29_3.zNPCs = []
f29_3.zkey = []
f29_3.Mup = {}
f29_3.Mdown = f28_3
f29_3.Mleft = f29_2
f29_3.Mright = {}

f28_1.zname = 'Floor 28, Room 1'
f28_1.zdescript = ''
f28_1.zsearch = ''
f28_1.zitems = []
f28_1.zmobs = []
f28_1.zoneunlocked = True
f28_1.zsearched = False
f28_1.zNPCs = []
f28_1.zkey = []
f28_1.Mup = f29_1
f28_1.Mdown = f27_1
f28_1.Mleft = {}
f28_1.Mright = f28_2

f28_2.zname = 'Floor 28, Room 2'
f28_2.zdescript = ''
f28_2.zsearch = ''
f28_2.zitems = []
f28_2.zmobs = []
f28_2.zoneunlocked = True
f28_2.zsearched = False
f28_2.zNPCs = []
f28_2.zkey = []
f28_2.Mup = f29_2
f28_2.Mdown = f27_2
f28_2.Mleft = f28_1
f28_2.Mright = f28_3

f28_3.zname = 'Floor 28, Room 3'
f28_3.zdescript = ''
f28_3.zsearch = ''
f28_3.zitems = []
f28_3.zmobs = []
f28_3.zoneunlocked = True
f28_3.zsearched = False
f28_3.zNPCs = []
f28_3.zkey = []
f28_3.Mup = f29_3
f28_3.Mdown = f27_3
f28_3.Mleft = f28_2
f28_3.Mright = {}

f27_1.zname = 'Floor 27, Room 1'
f27_1.zdescript = ''
f27_1.zsearch = ''
f27_1.zitems = []
f27_1.zmobs = []
f27_1.zoneunlocked = True
f27_1.zsearched = False
f27_1.zNPCs = []
f27_1.zkey = []
f27_1.Mup = f28_1
f27_1.Mdown = f26_1
f27_1.Mleft = {}
f27_1.Mright = f27_2

f27_2.zname = 'Floor 27, Room 2'
f27_2.zdescript = ''
f27_2.zsearch = ''
f27_2.zitems = []
f27_2.zmobs = []
f27_2.zoneunlocked = True
f27_2.zsearched = False
f27_2.zNPCs = []
f27_2.zkey = []
f27_2.Mup = f28_2
f27_2.Mdown = f26_2
f27_2.Mleft = f27_1
f27_2.Mright = f27_3

f27_3.zname = 'Floor 27, Room 3'
f27_3.zdescript = ''
f27_3.zsearch = ''
f27_3.zitems = []
f27_3.zmobs = []
f27_3.zoneunlocked = True
f27_3.zsearched = False
f27_3.zNPCs = []
f27_3.zkey = []
f27_3.Mup = f28_3
f27_3.Mdown = f26_3
f27_3.Mleft = f27_2
f27_3.Mright = {}

f26_1.zname = 'Floor 26, Room 1'
f26_1.zdescript = ''
f26_1.zsearch = ''
f26_1.zitems = []
f26_1.zmobs = []
f26_1.zoneunlocked = True
f26_1.zsearched = False
f26_1.zNPCs = []
f26_1.zkey = []
f26_1.Mup = f27_1
f26_1.Mdown = f25_1
f26_1.Mleft = {}
f26_1.Mright = f26_2

f26_2.zname = 'Floor 26, Room 2'
f26_2.zdescript = ''
f26_2.zsearch = ''
f26_2.zitems = []
f26_2.zmobs = []
f26_2.zoneunlocked = True
f26_2.zsearched = False
f26_2.zNPCs = []
f26_2.zkey = []
f26_2.Mup = f27_2
f26_2.Mdown = f25_2
f26_2.Mleft = f26_1
f26_2.Mright = f26_3

f26_3.zname = 'Floor 26, Room 3'
f26_3.zdescript = ''
f26_3.zsearch = ''
f26_3.zitems = []
f26_3.zmobs = []
f26_3.zoneunlocked = True
f26_3.zsearched = False
f26_3.zNPCs = []
f26_3.zkey = []
f26_3.Mup = f27_3
f26_3.Mdown = f25_3
f26_3.Mleft = f26_2
f26_3.Mright = {}

f25_1.zname = 'Floor 25, Room 1'
f25_1.zdescript = ''
f25_1.zsearch = ''
f25_1.zitems = []
f25_1.zmobs = []
f25_1.zoneunlocked = True
f25_1.zsearched = False
f25_1.zNPCs = []
f25_1.zkey = []
f25_1.Mup = f26_1
f25_1.Mdown = f24_1
f25_1.Mleft = {}
f25_1.Mright = f25_2

f25_2.zname = 'Floor 25, Room 2'
f25_2.zdescript = ''
f25_2.zsearch = ''
f25_2.zitems = []
f25_2.zmobs = []
f25_2.zoneunlocked = True
f25_2.zsearched = False
f25_2.zNPCs = []
f25_2.zkey = []
f25_2.Mup = f26_2
f25_2.Mdown = f24_2
f25_2.Mleft = f25_1
f25_2.Mright = f25_3

f25_3.zname = 'Floor 25, Room 3'
f25_3.zdescript = ''
f25_3.zsearch = ''
f25_3.zitems = []
f25_3.zmobs = []
f25_3.zoneunlocked = True
f25_3.zsearched = False
f25_3.zNPCs = []
f25_3.zkey = []
f25_3.Mup = f26_3
f25_3.Mdown = f24_3
f25_3.Mleft = f25_2
f25_3.Mright = {}

f24_1.zname = 'Floor 24, Room 1'
f24_1.zdescript = ''
f24_1.zsearch = ''
f24_1.zitems = []
f24_1.zmobs = []
f24_1.zoneunlocked = True
f24_1.zsearched = False
f24_1.zNPCs = []
f24_1.zkey = []
f24_1.Mup = f25_1
f24_1.Mdown = f23_1
f24_1.Mleft = {}
f24_1.Mright = f24_2

f24_2.zname = 'Floor 24, Room 2'
f24_2.zdescript = ''
f24_2.zsearch = ''
f24_2.zitems = []
f24_2.zmobs = []
f24_2.zoneunlocked = False
f24_2.zsearched = False
f24_2.zNPCs = []
f24_2.zkey = []
f24_2.Mup = f25_2
f24_2.Mdown = f23_2
f24_2.Mleft = f24_1
f24_2.Mright = f24_3

f24_3.zname = 'Floor 24, Room 3'
f24_3.zdescript = ''
f24_3.zsearch = ''
f24_3.zitems = []
f24_3.zmobs = []
f24_3.zoneunlocked = True
f24_3.zsearched = False
f24_3.zNPCs = []
f24_3.zkey = []
f24_3.Mup = f25_3
f24_3.Mdown = f23_3
f24_3.Mleft = f24_2
f24_3.Mright = {}

f23_1.zname = 'Floor 23, Room 1'
f23_1.zdescript = ''
f23_1.zsearch = ''
f23_1.zitems = []
f23_1.zmobs = []
f23_1.zoneunlocked = True
f23_1.zsearched = False
f23_1.zNPCs = []
f23_1.zkey = []
f23_1.Mup = f24_1
f23_1.Mdown = f22_1
f23_1.Mleft = {}
f23_1.Mright = f23_2

f23_2.zname = 'Floor 23, Room 2'
f23_2.zdescript = ''
f23_2.zsearch = ''
f23_2.zitems = []
f23_2.zmobs = []
f23_2.zoneunlocked = True
f23_2.zsearched = False
f23_2.zNPCs = []
f23_2.zkey = []
f23_2.Mup = f24_2
f23_2.Mdown = f22_2
f23_2.Mleft = f23_1
f23_2.Mright = f23_3

f23_3.zname = 'Floor 23, Room 3'
f23_3.zdescript = ''
f23_3.zsearch = ''
f23_3.zitems = []
f23_3.zmobs = []
f23_3.zoneunlocked = True
f23_3.zsearched = False
f23_3.zNPCs = []
f23_3.zkey = []
f23_3.Mup = f24_3
f23_3.Mdown = f22_3
f23_3.Mleft = f23_2
f23_3.Mright = {}

f22_1.zname = 'Floor 22, Room 1'
f22_1.zdescript = ''
f22_1.zsearch = ''
f22_1.zitems = []
f22_1.zmobs = []
f22_1.zoneunlocked = True
f22_1.zsearched = False
f22_1.zNPCs = []
f22_1.zkey = []
f22_1.Mup = f23_1
f22_1.Mdown = f21_1
f22_1.Mleft = {}
f22_1.Mright = f22_2

f22_2.zname = 'Floor 22, Room 2'
f22_2.zdescript = ''
f22_2.zsearch = ''
f22_2.zitems = []
f22_2.zmobs = []
f22_2.zoneunlocked = True
f22_2.zsearched = False
f22_2.zNPCs = []
f22_2.zkey = []
f22_2.Mup = f23_2
f22_2.Mdown = f21_2
f22_2.Mleft = f22_1
f22_2.Mright = f22_3

f22_3.zname = 'Floor 22, Room 3'
f22_3.zdescript = ''
f22_3.zsearch = ''
f22_3.zitems = []
f22_3.zmobs = []
f22_3.zoneunlocked = True
f22_3.zsearched = False
f22_3.zNPCs = []
f22_3.zkey = []
f22_3.Mup = f23_3
f22_3.Mdown = f21_3
f22_3.Mleft = f22_2
f22_3.Mright = {}

f21_1.zname = 'Floor 21, Room 1'
f21_1.zdescript = ''
f21_1.zsearch = ''
f21_1.zitems = []
f21_1.zmobs = []
f21_1.zoneunlocked = True
f21_1.zsearched = False
f21_1.zNPCs = []
f21_1.zkey = []
f21_1.Mup = f22_1
f21_1.Mdown = f20_1
f21_1.Mleft = {}
f21_1.Mright = f21_2

f21_2.zname = 'Floor 21, Room 2'
f21_2.zdescript = ''
f21_2.zsearch = ''
f21_2.zitems = []
f21_2.zmobs = []
f21_2.zoneunlocked = True
f21_2.zsearched = False
f21_2.zNPCs = []
f21_2.zkey = []
f21_2.Mup = f22_2
f21_2.Mdown = {}
f21_2.Mleft = f21_1
f21_2.Mright = f21_3

f21_3.zname = 'Floor 21, Room 3'
f21_3.zdescript = ''
f21_3.zsearch = ''
f21_3.zitems = []
f21_3.zmobs = []
f21_3.zoneunlocked = True
f21_3.zsearched = False
f21_3.zNPCs = []
f21_3.zkey = []
f21_3.Mup = f22_3
f21_3.Mdown = {}
f21_3.Mleft = f21_2
f21_3.Mright = {}

f20_1.zname = 'Floor 20, Room 1'
f20_1.zdescript = ''
f20_1.zsearch = ''
f20_1.zitems = []
f20_1.zmobs = ['Vampire Lord 3']
f20_1.zoneunlocked = True
f20_1.zsearched = False
f20_1.zNPCs = []
f20_1.zkey = []
f20_1.Mup = f21_1
f20_1.Mdown = f19_1
f20_1.Mleft = {}
f20_1.Mright = {}

f19_1.zname = 'Floor 19, Room 1'
f19_1.zdescript = ''
f19_1.zsearch = ''
f19_1.zitems = []
f19_1.zmobs = []
f19_1.zoneunlocked = True
f19_1.zsearched = False
f19_1.zNPCs = []
f19_1.zkey = ''
f19_1.Mup = f20_1
f19_1.Mdown = f18_1
f19_1.Mleft = {}
f19_1.Mright = f19_2

f19_2.zname = 'Floor 19, Room 2'
f19_2.zdescript = ''
f19_2.zsearch = ''
f19_2.zitems = []
f19_2.zmobs = []
f19_2.zoneunlocked = True
f19_2.zsearched = False
f19_2.zNPCs = []
f19_2.zkey = []
f19_2.Mup = {}
f19_2.Mdown = f18_2
f19_2.Mleft = f19_1
f19_2.Mright = f19_3

f19_3.zname = 'Floor 19, Room 3'
f19_3.zdescript = ''
f19_3.zsearch = ''
f19_3.zitems = []
f19_3.zmobs = []
f19_3.zoneunlocked = True
f19_3.zsearched = False
f19_3.zNPCs = []
f19_3.zkey = []
f19_3.Mup = {}
f19_3.Mdown = f18_3
f19_3.Mleft = f19_2
f19_3.Mright = {}

f18_1.zname = 'Floor 18, Room 1'
f18_1.zdescript = ''
f18_1.zsearch = ''
f18_1.zitems = []
f18_1.zmobs = []
f18_1.zoneunlocked = True
f18_1.zsearched = False
f18_1.zNPCs = []
f18_1.zkey = []
f18_1.Mup = f19_1
f18_1.Mdown = f17_1
f18_1.Mleft = {}
f18_1.Mright = f18_2

f18_2.zname = 'Floor 18, Room 2'
f18_2.zdescript = ''
f18_2.zsearch = ''
f18_2.zitems = []
f18_2.zmobs = []
f18_2.zoneunlocked = True
f18_2.zsearched = False
f18_2.zNPCs = []
f18_2.zkey = []
f18_2.Mup = f19_2
f18_2.Mdown = f17_2
f18_2.Mleft = f18_1
f18_2.Mright = f18_3

f18_3.zname = 'Floor 18, Room 3'
f18_3.zdescript = ''
f18_3.zsearch = ''
f18_3.zitems = []
f18_3.zmobs = []
f18_3.zoneunlocked = True
f18_3.zsearched = False
f18_3.zNPCs = []
f18_3.zkey = []
f18_3.Mup = f19_3
f18_3.Mdown = f17_3
f18_3.Mleft = f18_2
f18_3.Mright = {}

f17_1.zname = 'Floor 17, Room 1'
f17_1.zdescript = ''
f17_1.zsearch = ''
f17_1.zitems = []
f17_1.zmobs = []
f17_1.zoneunlocked = True
f17_1.zsearched = False
f17_1.zNPCs = []
f17_1.zkey = []
f17_1.Mup = f18_1
f17_1.Mdown = f16_1
f17_1.Mleft = {}
f17_1.Mright = f17_2

f17_2.zname = 'Floor 17, Room 2'
f17_2.zdescript = ''
f17_2.zsearch = ''
f17_2.zitems = []
f17_2.zmobs = []
f17_2.zoneunlocked = True
f17_2.zsearched = False
f17_2.zNPCs = []
f17_2.zkey = []
f17_2.Mup = f18_2
f17_2.Mdown = f16_2
f17_2.Mleft = f17_1
f17_2.Mright = f17_3

f17_3.zname = 'Floor 17, Room 3'
f17_3.zdescript = ''
f17_3.zsearch = ''
f17_3.zitems = []
f17_3.zmobs = []
f17_3.zoneunlocked = True
f17_3.zsearched = False
f17_3.zNPCs = []
f17_3.zkey = []
f17_3.Mup = f18_3
f17_3.Mdown = f16_3
f17_3.Mleft = f17_2
f17_3.Mright = {}

f16_1.zname = 'Floor 16, Room 1'
f16_1.zdescript = ''
f16_1.zsearch = ''
f16_1.zitems = []
f16_1.zmobs = []
f16_1.zoneunlocked = True
f16_1.zsearched = False
f16_1.zNPCs = []
f16_1.zkey = []
f16_1.Mup = f17_1
f16_1.Mdown = f15_1
f16_1.Mleft = {}
f16_1.Mright = f16_2

f16_2.zname = 'Floor 16, Room 2'
f16_2.zdescript = ''
f16_2.zsearch = ''
f16_2.zitems = []
f16_2.zmobs = []
f16_2.zoneunlocked = True
f16_2.zsearched = False
f16_2.zNPCs = []
f16_2.zkey = []
f16_2.Mup = f17_2
f16_2.Mdown = f15_2
f16_2.Mleft = f16_1
f16_2.Mright = f16_3

f16_3.zname = 'Floor 16, Room 3'
f16_3.zdescript = ''
f16_3.zsearch = ''
f16_3.zitems = []
f16_3.zmobs = []
f16_3.zoneunlocked = True
f16_3.zsearched = False
f16_3.zNPCs = []
f16_3.zkey = []
f16_3.Mup = f17_3
f16_3.Mdown = f15_3
f16_3.Mleft = f16_2
f16_3.Mright = {}

f15_1.zname = 'Floor 15, Room 1'
f15_1.zdescript = ''
f15_1.zsearch = ''
f15_1.zitems = []
f15_1.zmobs = []
f15_1.zoneunlocked = True
f15_1.zsearched = False
f15_1.zNPCs = []
f15_1.zkey = []
f15_1.Mup = f16_1
f15_1.Mdown = f14_1
f15_1.Mleft = {}
f15_1.Mright = f15_2

f15_2.zname = 'Floor 15, Room 2'
f15_2.zdescript = ''
f15_2.zsearch = ''
f15_2.zitems = []
f15_2.zmobs = []
f15_2.zoneunlocked = True
f15_2.zsearched = False
f15_2.zNPCs = []
f15_2.zkey = []
f15_2.Mup = f16_2
f15_2.Mdown = f14_2
f15_2.Mleft = f15_1
f15_2.Mright = f15_3

f15_3.zname = 'Floor 15, Room 3'
f15_3.zdescript = ''
f15_3.zsearch = ''
f15_3.zitems = []
f15_3.zmobs = []
f15_3.zoneunlocked = True
f15_3.zsearched = False
f15_3.zNPCs = []
f15_3.zkey = []
f15_3.Mup = f16_3
f15_3.Mdown = f14_3
f15_3.Mleft = f15_2
f15_3.Mright = {}

f14_1.zname = 'Floor 14, Room 1'
f14_1.zdescript = ''
f14_1.zsearch = ''
f14_1.zitems = []
f14_1.zmobs = []
f14_1.zoneunlocked = True
f14_1.zsearched = False
f14_1.zNPCs = []
f14_1.zkey = []
f14_1.Mup = f15_1
f14_1.Mdown = f13_1
f14_1.Mleft = {}
f14_1.Mright = f14_2

f14_2.zname = 'Floor 14, Room 2'
f14_2.zdescript = ''
f14_2.zsearch = ''
f14_2.zitems = []
f14_2.zmobs = []
f14_2.zoneunlocked = False
f14_2.zsearched = False
f14_2.zNPCs = []
f14_2.zkey = []
f14_2.Mup = f15_2
f14_2.Mdown = f13_2
f14_2.Mleft = f14_1
f14_2.Mright = f14_3

f14_3.zname = 'Floor 14, Room 3'
f14_3.zdescript = ''
f14_3.zsearch = ''
f14_3.zitems = []
f14_3.zmobs = []
f14_3.zoneunlocked = True
f14_3.zsearched = False
f14_3.zNPCs = []
f14_3.zkey = []
f14_3.Mup = f15_3
f14_3.Mdown = f13_3
f14_3.Mleft = f14_2
f14_3.Mright = {}

f13_1.zname = 'Floor 13, Room 1'
f13_1.zdescript = ''
f13_1.zsearch = ''
f13_1.zitems = []
f13_1.zmobs = []
f13_1.zoneunlocked = True
f13_1.zsearched = False
f13_1.zNPCs = []
f13_1.zkey = []
f13_1.Mup = f14_1
f13_1.Mdown = f12_1
f13_1.Mleft = {}
f13_1.Mright = f13_2

f13_2.zname = 'Floor 13, Room 2'
f13_2.zdescript = ''
f13_2.zsearch = ''
f13_2.zitems = []
f13_2.zmobs = []
f13_2.zoneunlocked = True
f13_2.zsearched = False
f13_2.zNPCs = []
f13_2.zkey = []
f13_2.Mup = f14_2
f13_2.Mdown = f12_2
f13_2.Mleft = f13_1
f13_2.Mright = f13_3

f13_3.zname = 'Floor 13, Room 3'
f13_3.zdescript = ''
f13_3.zsearch = ''
f13_3.zitems = []
f13_3.zmobs = []
f13_3.zoneunlocked = True
f13_3.zsearched = False
f13_3.zNPCs = []
f13_3.zkey = []
f13_3.Mup = f14_3
f13_3.Mdown = f12_3
f13_3.Mleft = f13_2
f13_3.Mright = {}

f12_1.zname = 'Floor 12, Room 1'
f12_1.zdescript = ''
f12_1.zsearch = ''
f12_1.zitems = []
f12_1.zmobs = []
f12_1.zoneunlocked = True
f12_1.zsearched = False
f12_1.zNPCs = []
f12_1.zkey = []
f12_1.Mup = f13_1
f12_1.Mdown = f11_1
f12_1.Mleft = {}
f12_1.Mright = f12_2

f12_2.zname = 'Floor 12, Room 2'
f12_2.zdescript = ''
f12_2.zsearch = ''
f12_2.zitems = []
f12_2.zmobs = []
f12_2.zoneunlocked = True
f12_2.zsearched = False
f12_2.zNPCs = []
f12_2.zkey = []
f12_2.Mup = f13_2
f12_2.Mdown = f11_2
f12_2.Mleft = f12_1
f12_2.Mright = f12_3

f12_3.zname = 'Floor 12, Room 3'
f12_3.zdescript = ''
f12_3.zsearch = ''
f12_3.zitems = []
f12_3.zmobs = []
f12_3.zoneunlocked = True
f12_3.zsearched = False
f12_3.zNPCs = []
f12_3.zkey = []
f12_3.Mup = f13_3
f12_3.Mdown = f11_3
f12_3.Mleft = f12_2
f12_3.Mright = {}

f11_1.zname = 'Floor 11, Room 1'
f11_1.zdescript = ''
f11_1.zsearch = ''
f11_1.zitems = []
f11_1.zmobs = []
f11_1.zoneunlocked = True
f11_1.zsearched = False
f11_1.zNPCs = []
f11_1.zkey = []
f11_1.Mup = f12_1
f11_1.Mdown = f10_1
f11_1.Mleft = {}
f11_1.Mright = f11_2

f11_2.zname = 'Floor 11, Room 2'
f11_2.zdescript = ''
f11_2.zsearch = ''
f11_2.zitems = []
f11_2.zmobs = []
f11_2.zoneunlocked = True
f11_2.zsearched = False
f11_2.zNPCs = []
f11_2.zkey = []
f11_2.Mup = f12_2
f11_2.Mdown = {}
f11_2.Mleft = f11_1
f11_2.Mright = f11_3

f11_3.zname = 'Floor 11, Room 3'
f11_3.zdescript = ''
f11_3.zsearch = ''
f11_3.zitems = []
f11_3.zmobs = []
f11_3.zoneunlocked = True
f11_3.zsearched = False
f11_3.zNPCs = []
f11_3.zkey = []
f11_3.Mup = f12_3
f11_3.Mdown = {}
f11_3.Mleft = f11_2
f11_3.Mright = {}

f10_1.zname = 'Floor 10, Room 1'
f10_1.zdescript = ''
f10_1.zsearch = ''
f10_1.zitems = []
f10_1.zmobs = ['Vampire Lord 4']
f10_1.zoneunlocked = True
f10_1.zsearched = False
f10_1.zNPCs = []
f10_1.zkey = []
f10_1.Mup = f11_1
f10_1.Mdown = f9_1
f10_1.Mleft = {}
f10_1.Mright = {}

f9_1.zname = 'Floor 9, Room 1'
f9_1.zdescript = ''
f9_1.zsearch = ''
f9_1.zitems = []
f9_1.zmobs = []
f9_1.zoneunlocked = True
f9_1.zsearched = False
f9_1.zNPCs = []
f9_1.zkey = ''
f9_1.Mup = f10_1
f9_1.Mdown = f8_1
f9_1.Mleft = {}
f9_1.Mright = f9_2

f9_2.zname = 'Floor 9, Room 2'
f9_2.zdescript = ''
f9_2.zsearch = ''
f9_2.zitems = []
f9_2.zmobs = []
f9_2.zoneunlocked = True
f9_2.zsearched = False
f9_2.zNPCs = []
f9_2.zkey = []
f9_2.Mup = {}
f9_2.Mdown = f8_2
f9_2.Mleft = f9_1
f9_2.Mright = f9_3

f9_3.zname = 'Floor 9, Room 3'
f9_3.zdescript = ''
f9_3.zsearch = ''
f9_3.zitems = []
f9_3.zmobs = []
f9_3.zoneunlocked = True
f9_3.zsearched = False
f9_3.zNPCs = []
f9_3.zkey = []
f9_3.Mup = {}
f9_3.Mdown = f8_3
f9_3.Mleft = f9_2
f9_3.Mright = {}

f8_1.zname = 'Floor 8, Room 1'
f8_1.zdescript = ''
f8_1.zsearch = ''
f8_1.zitems = []
f8_1.zmobs = []
f8_1.zoneunlocked = True
f8_1.zsearched = False
f8_1.zNPCs = []
f8_1.zkey = []
f8_1.Mup = f9_1
f8_1.Mdown = f7_1
f8_1.Mleft = {}
f8_1.Mright = f8_2

f8_2.zname = 'Floor 8, Room 2'
f8_2.zdescript = ''
f8_2.zsearch = ''
f8_2.zitems = []
f8_2.zmobs = []
f8_2.zoneunlocked = True
f8_2.zsearched = False
f8_2.zNPCs = []
f8_2.zkey = []
f8_2.Mup = f9_2
f8_2.Mdown = f7_2
f8_2.Mleft = f8_1
f8_2.Mright = f8_3

f8_3.zname = 'Floor 8, Room 3'
f8_3.zdescript = ''
f8_3.zsearch = ''
f8_3.zitems = []
f8_3.zmobs = []
f8_3.zoneunlocked = True
f8_3.zsearched = False
f8_3.zNPCs = []
f8_3.zkey = []
f8_3.Mup = f9_3
f8_3.Mdown = f7_3
f8_3.Mleft = f8_2
f8_3.Mright = {}

f7_1.zname = 'Floor 7, Room 1'
f7_1.zdescript = ''
f7_1.zsearch = ''
f7_1.zitems = []
f7_1.zmobs = []
f7_1.zoneunlocked = True
f7_1.zsearched = False
f7_1.zNPCs = []
f7_1.zkey = []
f7_1.Mup = f8_1
f7_1.Mdown = f6_1
f7_1.Mleft = {}
f7_1.Mright = f7_2

f7_2.zname = 'Floor 7, Room 2'
f7_2.zdescript = ''
f7_2.zsearch = ''
f7_2.zitems = []
f7_2.zmobs = []
f7_2.zoneunlocked = True
f7_2.zsearched = False
f7_2.zNPCs = []
f7_2.zkey = []
f7_2.Mup = f8_2
f7_2.Mdown = f6_2
f7_2.Mleft = f7_1
f7_2.Mright = f7_3

f7_3.zname = 'Floor 7, Room 3'
f7_3.zdescript = ''
f7_3.zsearch = ''
f7_3.zitems = []
f7_3.zmobs = []
f7_3.zoneunlocked = True
f7_3.zsearched = False
f7_3.zNPCs = []
f7_3.zkey = []
f7_3.Mup = f8_3
f7_3.Mdown = f6_3
f7_3.Mleft = f7_2
f7_3.Mright = {}

f6_1.zname = 'Floor 6, Room 1'
f6_1.zdescript = ''
f6_1.zsearch = ''
f6_1.zitems = []
f6_1.zmobs = []
f6_1.zoneunlocked = True
f6_1.zsearched = False
f6_1.zNPCs = []
f6_1.zkey = []
f6_1.Mup = f7_1
f6_1.Mdown = f5_1
f6_1.Mleft = {}
f6_1.Mright = f6_2

f6_2.zname = 'Floor 6, Room 2'
f6_2.zdescript = ''
f6_2.zsearch = ''
f6_2.zitems = []
f6_2.zmobs = []
f6_2.zoneunlocked = True
f6_2.zsearched = False
f6_2.zNPCs = []
f6_2.zkey = []
f6_2.Mup = f7_2
f6_2.Mdown = f5_2
f6_2.Mleft = f6_1
f6_2.Mright = f6_3

f6_3.zname = 'Floor 6, Room 3'
f6_3.zdescript = ''
f6_3.zsearch = ''
f6_3.zitems = []
f6_3.zmobs = []
f6_3.zoneunlocked = True
f6_3.zsearched = False
f6_3.zNPCs = []
f6_3.zkey = []
f6_3.Mup = f7_3
f6_3.Mdown = f5_3
f6_3.Mleft = f6_2
f6_3.Mright = {}

f5_1.zname = 'Floor 5, Room 1'
f5_1.zdescript = ''
f5_1.zsearch = ''
f5_1.zitems = []
f5_1.zmobs = []
f5_1.zoneunlocked = True
f5_1.zsearched = False
f5_1.zNPCs = []
f5_1.zkey = []
f5_1.Mup = f6_1
f5_1.Mdown = f4_1
f5_1.Mleft = {}
f5_1.Mright = f5_2

f5_2.zname = 'Floor 5, Room 2'
f5_2.zdescript = ''
f5_2.zsearch = ''
f5_2.zitems = []
f5_2.zmobs = []
f5_2.zoneunlocked = True
f5_2.zsearched = False
f5_2.zNPCs = []
f5_2.zkey = []
f5_2.Mup = f6_2
f5_2.Mdown = f4_2
f5_2.Mleft = f5_1
f5_2.Mright = f5_3

f5_3.zname = 'Floor 5, Room 3'
f5_3.zdescript = ''
f5_3.zsearch = ''
f5_3.zitems = []
f5_3.zmobs = []
f5_3.zoneunlocked = True
f5_3.zsearched = False
f5_3.zNPCs = []
f5_3.zkey = []
f5_3.Mup = f6_3
f5_3.Mdown = f4_3
f5_3.Mleft = f5_2
f5_3.Mright = {}

f4_1.zname = 'Floor 4, Room 1'
f4_1.zdescript = ''
f4_1.zsearch = ''
f4_1.zitems = []
f4_1.zmobs = []
f4_1.zoneunlocked = True
f4_1.zsearched = False
f4_1.zNPCs = []
f4_1.zkey = []
f4_1.Mup = f5_1
f4_1.Mdown = f3_1
f4_1.Mleft = {}
f4_1.Mright = f4_2

f4_2.zname = 'Floor 4, Room 2'
f4_2.zdescript = ''
f4_2.zsearch = ''
f4_2.zitems = []
f4_2.zmobs = []
f4_2.zoneunlocked = False
f4_2.zsearched = False
f4_2.zNPCs = []
f4_2.zkey = []
f4_2.Mup = f5_2
f4_2.Mdown = f3_2
f4_2.Mleft = f4_1
f4_2.Mright = f4_3

f4_3.zname = 'Floor 4, Room 3'
f4_3.zdescript = ''
f4_3.zsearch = ''
f4_3.zitems = []
f4_3.zmobs = []
f4_3.zoneunlocked = True
f4_3.zsearched = False
f4_3.zNPCs = []
f4_3.zkey = []
f4_3.Mup = f5_3
f4_3.Mdown = f3_3
f4_3.Mleft = f4_2
f4_3.Mright = {}

f3_1.zname = 'Floor 3, Room 1'
f3_1.zdescript = ''
f3_1.zsearch = ''
f3_1.zitems = []
f3_1.zmobs = []
f3_1.zoneunlocked = True
f3_1.zsearched = False
f3_1.zNPCs = []
f3_1.zkey = []
f3_1.Mup = f4_1
f3_1.Mdown = f2_1
f3_1.Mleft = {}
f3_1.Mright = f3_2

f3_2.zname = 'Floor 3, Room 2'
f3_2.zdescript = ''
f3_2.zsearch = ''
f3_2.zitems = []
f3_2.zmobs = []
f3_2.zoneunlocked = True
f3_2.zsearched = False
f3_2.zNPCs = []
f3_2.zkey = []
f3_2.Mup = f4_2
f3_2.Mdown = f2_2
f3_2.Mleft = f3_1
f3_2.Mright = f3_3

f3_3.zname = 'Floor 3, Room 3'
f3_3.zdescript = ''
f3_3.zsearch = ''
f3_3.zitems = []
f3_3.zmobs = []
f3_3.zoneunlocked = True
f3_3.zsearched = False
f3_3.zNPCs = []
f3_3.zkey = []
f3_3.Mup = f4_3
f3_3.Mdown = f2_3
f3_3.Mleft = f3_2
f3_3.Mright = {}

f2_1.zname = 'Floor 2, Room 1'
f2_1.zdescript = ''
f2_1.zsearch = ''
f2_1.zitems = []
f2_1.zmobs = []
f2_1.zoneunlocked = True
f2_1.zsearched = False
f2_1.zNPCs = []
f2_1.zkey = []
f2_1.Mup = f3_1
f2_1.Mdown = f1_1
f2_1.Mleft = {}
f2_1.Mright = f2_2

f2_2.zname = 'Floor 2, Room 2'
f2_2.zdescript = ''
f2_2.zsearch = ''
f2_2.zitems = []
f2_2.zmobs = []
f2_2.zoneunlocked = True
f2_2.zsearched = False
f2_2.zNPCs = []
f2_2.zkey = []
f2_2.Mup = f3_2
f2_2.Mdown = f1_2
f2_2.Mleft = f2_1
f2_2.Mright = f2_3

f2_3.zname = 'Floor 2, Room 3'
f2_3.zdescript = ''
f2_3.zsearch = ''
f2_3.zitems = []
f2_3.zmobs = []
f2_3.zoneunlocked = True
f2_3.zsearched = False
f2_3.zNPCs = []
f2_3.zkey = []
f2_3.Mup = f3_3
f2_3.Mdown = f1_3
f2_3.Mleft = f2_2
f2_3.Mright = {}

f1_1.zname = 'Floor 1, Room 1'
f1_1.zdescript = ''
f1_1.zsearch = ''
f1_1.zitems = []
f1_1.zmobs = []
f1_1.zoneunlocked = True
f1_1.zsearched = False
f1_1.zNPCs = []
f1_1.zkey = []
f1_1.Mup = f2_1
f1_1.Mdown = f0_1
f1_1.Mleft = {}
f1_1.Mright = f1_2

f1_2.zname = 'Floor 1, Room 2'
f1_2.zdescript = ''
f1_2.zsearch = ''
f1_2.zitems = []
f1_2.zmobs = []
f1_2.zoneunlocked = True
f1_2.zsearched = False
f1_2.zNPCs = []
f1_2.zkey = []
f1_2.Mup = f2_2
f1_2.Mdown = {}
f1_2.Mleft = f1_1
f1_2.Mright = f1_3

f1_3.zname = 'Floor 1, Room 3'
f1_3.zdescript = ''
f1_3.zsearch = ''
f1_3.zitems = []
f1_3.zmobs = []
f1_3.zoneunlocked = True
f1_3.zsearched = False
f1_3.zNPCs = []
f1_3.zkey = []
f1_3.Mup = f2_3
f1_3.Mdown = {}
f1_3.Mleft = f1_2
f1_3.Mright = {}

f0_1.zname = 'Floor 0, Room 1'
f0_1.zdescript = ''
f0_1.zsearch = ''
f0_1.zitems = ['Ground-Floor Key']
f0_1.zmobs = ['Vampire King']
f0_1.zoneunlocked = True
f0_1.zsearched = False
f0_1.zNPCs = []
f0_1.zkey = []
f0_1.Mup = f1_1
f0_1.Mdown = fG
f0_1.Mleft = {}
f0_1.Mright = {}

fG.zname = 'Ground Floor'
fG.zdescript = ''
fG.zsearch = ''
fG.zitems = []
fG.zmobs = []
fG.zoneunlocked = False
fG.zsearched = False
fG.zNPCs = []
fG.zkey = 'Ground-Floor Key'
fG.Mup = f0_1
fG.Mdown = {}
fG.Mleft = {}
fG.Mright = {}

#Tutorial rooms
fT_1 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})
fT_2 = Zonemap({},{},{},{},{},{},{},{},{},{},{},{},{})

fT_1.zname = 'Tutorial, Room 1'
fT_1.zdescript = 'The game opening, no-one knows how it got here.'
fT_1.zsearch = 'You find a glowing key on the floor, the voice just dropped it there.'
fT_1.zitems = ['Glowing Key']
fT_1.zmobs = []
fT_1.zoneunlocked = True
fT_1.zsearched = False
fT_1.zNPCs = []
fT_1.zkey = []
fT_1.Mup = {}
fT_1.Mdown = {}
fT_1.Mleft = {}
fT_1.Mright = fT_2

fT_2.zname = 'Tutorial, Room 2'
fT_2.zdescript = 'You successfully used the move action!'
fT_2.zsearch = 'You notice there is a staircase going downwards which is where you start the game.'
fT_2.zitems = []
fT_2.zmobs = []
fT_2.zoneunlocked = False
fT_2.zsearched = False
fT_2.zNPCs = ['voice']
fT_2.zkey = 'Glowing Key'
fT_2.Mup = {}
fT_2.Mdown = f100_1
fT_2.Mleft = fT_1
fT_2.Mright = {}

 #Imports
import time
import random
from random import randint
import os
import sys
import pickle

#Printing Function
message = ""

def Type(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.075)
    print('')

#Classes
class Weapons:
    def __init__(item, name, atk, ob):
        item.name = ''
        item.atk = 0
        item.ob = []

Wp1 = Weapons({},{},{})
Wp1.name = 'Notebook'
Wp1.atk = 1
Wp1.ob = ['Notebook']

Wp02 = Weapons({},{},{})
Wp02.name = 'Ruler'
Wp02.atk = 3
Wp02.ob = ['Ruler']

Wp2 = Weapons({},{},{})
Wp2.name = 'Blunt Pencil'
Wp2.atk = 4
Wp2.ob = ['Blunt Pencil']

Wp3 = Weapons({},{},{})
Wp3.name = 'Sharpened Pencil'
Wp3.atk = 5
Wp3.ob = ['Sharpened Pencil']

Wp4 = Weapons({},{},{})
Wp4.name = 'Small Dagger'
Wp4.atk = 6
Wp4.ob = ['Small Dagger']

Wp5 = Weapons({},{},{})
Wp5.name = 'Rusty Sword'
Wp5.atk = 7
Wp5.ob = ['Rusty Sword']

Wp6 = Weapons({},{},{})
Wp6.name = 'Shiny Sword'
Wp6.atk = 10
Wp6.ob = ['Shiny Sword']

Wp7 = Weapons({},{},{})
Wp7.name = 'Ancient Katana'
Wp7.atk = 12
Wp7.ob = ['Ancient Katana']

Wp8 = Weapons({},{},{})
Wp8.name = 'Refined Katana'
Wp8.atk = 15
Wp8.ob = ['Refined Katana']

class Exp_orb:
    def __init__(item, name, exp, ob):
        item.name = ''
        item.exp = 0
        item.ob = []

E1 = Exp_orb({},{},{})
E1.name = 'Miniscule Exp Orb'
E1.exp = 10
E1.ob = ['Miniscule Exp Orb']

E2 = Exp_orb({},{},{})
E2.name = 'Tiny Exp Orb'
E2.exp = 50
E2.ob = ['Tiny Exp Orb']

E3 = Exp_orb({},{},{})
E3.name = 'Medium Exp Orb'
E3.exp = 100
E3.ob = ['Medium Exp Orb']

E4 = Exp_orb({},{},{})
E4.name = 'Large Exp Orb'
E4.exp = 200
E4.ob = ['Large Exp Orb']

E5 = Exp_orb({},{},{})
E5.name = 'MASSIVE Exp Orb'
E5.exp = 500
E5.ob = ['MASSIVE Exp Orb']

E6 = Exp_orb({},{},{})
E6.name = 'Beyond Holy Exp Orb'
E6.exp = 2000
E6.ob = ['Beyond Holy Exp Orb']

class Hp_pots:
    def __init__(item, name, hp, ob):
        item.name = ''
        item.hp = 0
        item.ob = []

H1 = Hp_pots({},{},{})
H1.name = 'Miniscule Healing Potion'
H1.hp = 10
H1.ob = ['Miniscule Healing Potion']

H2 = Hp_pots({},{},{})
H2.name = 'Tiny Healing Potion'
H2.hp = 50
H2.ob = ['Tiny Healing Potion']

H3 = Hp_pots({},{},{})
H3.name = 'Medium Healing Potion'
H3.hp = 100
H3.ob = ['Medium Healing Potion']

H4 = Hp_pots({},{},{})
H4.name = 'Large Healing Potion'
H4.hpp = 150
H4.ob = ['Large Healing Potion']

H5 = Hp_pots({},{},{})
H5.name = 'MASSIVE Healing Potion'
H5.hp = 200
H5.ob = ['MASSIVE Healing Potion']

H6 = Hp_pots({},{},{})
H6.name = 'Beyond Holy Healing Potion'
H6.hp = 500
H6.ob = ['Beyond Holy Healing Potion']

class Goblin:
    def __init__(mob,name,hp,atk,exp,gold,):
        mob.name = 'Goblin'
        mob.hp = 15
        mob.atk = 1
        mob.exp = 5
        mob.gold = 2

class Slime:
    def __init__(mob,name,hp,atk,exp,gold,):
        mob.name = 'Slime'
        mob.hp = 30
        mob.atk = 1
        mob.exp = 7
        mob.gold = 3

class Zombie:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Zombie'
        mob.hp = 50
        mob.atk = 3
        mob.exp = 13
        mob.gold = 4

class Wolf:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Wolf'
        mob.hp = 20
        mob.atk = 8
        mob.exp = 15
        mob.gold = 5

class Hobgoblin:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Hobgoblin'
        mob.hp = 40
        mob.atk = 5
        mob.exp = 10
        mob.gold = 3

class Vampire:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Vampire'
        mob.hp = 70
        mob.atk = 6
        mob.exp = 20
        mob.gold = 5


#Bosses
class Goblin_King:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Goblin King'
        mob.hp = 150
        mob.atk = 6
        mob.exp = 50
        mob.gold = 20

class MASSIVE_Slime:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'MASSIVE Slime'
        mob.hp = 300
        mob.atk = 8
        mob.exp = 70
        mob.gold = 30

class Undecayed_Zombie:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Undecayed Zombie'
        mob.hp = 500
        mob.atk = 10
        mob.exp = 130
        mob.gold = 40

class Alpha_Wolf:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Alpha Wolf'
        mob.hp = 300
        mob.atk = 20
        mob.exp = 400
        mob.gold = 50

class Hobbiest_Hobgoblin:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Hobbiest Hobgoblin'
        mob.hp = 400
        mob.atk = 13
        mob.exp = 200
        mob.gold = 30

class Vampire_Lord1:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Vampire Lord 1'
        mob.hp = 800
        mob.atk = 20
        mob.exp = 300
        mob.gold = 60

class Vampire_Lord2:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Vampire Lord 2'
        mob.hp = 400
        mob.atk = 35
        mob.exp = 600
        mob.gold = 80

class Vampire_Lord3:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Vampire Lord 3'
        mob.hp = 1200
        mob.atk = 15
        mob.exp = 600
        mob.gold = 80

class Vampire_Lord4:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Vampire Lord 4'
        mob.hp = 900
        mob.atk = 30
        mob.exp = 800
        mob.gold = 100

class Vampire_King:
    def __init__(mob,name,hp,atk,exp,gold):
        mob.name = 'Vampire King'
        mob.hp = 1000 #Make it so Vampire either attacks or heals
        mob.atk = 40
        mob.exp = 1200
        mob.gold = 120

class Stats:
    def __init__(self, name, hp, lvl, exp, Rexp, atk, location, inv, gold, wp, beat, target, compq, curq, shard, maxhp): #compq is completed quests and curq is current quest.
     self.name = ''
     self.hp = 30
     self.lvl = 1
     self.exp = 0
     self.Rexp = 0
     self.atk = 0
     self.location = fT_1
     self.inv = []
     self.gold = 0
     self.wpatk = 0
     self.beat = {}
     self.target = {}
     self.compq = []
     self.curq = ''
     self.shard = 0
     self.maxhp = 0

player = Stats({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})
#Functions
def Save():
    pass
def NewGame():
    Type("Welcome to \"The Lift's Out of Order\"!")
    Type("Made by Marli Williams")
    Type("Dedicated to Eva, HAPPY BIRTHDAY!!!")
    Type("Thank you for always being supportful, helpful and overall an absolutely amazing best friend!")
    Type("I know you love video games so I decided to code my own for you :))")
    Type("It has over 300+ rooms, 6 Bosses and a Main Storyline with lots of quests!")
    Type("If there are any bugs I swear..... TvT")
    Type("Anyway! This game doesn't have a saving feature so if you die you start from scratch.\nOooh, maybe you're reading this for the second time!")
    Type("The main reason is as an expert save-scummer myself, I will not be allowing you to do the same.\nSo enjoy this painful game!")
    time.sleep(4)
    Type("I'm just messing though it's up to you to find out which action is saving!")
    Tutorial()

def LoadGame():
    pass

def RoomSave():
    pass

def RoomLoad():
    pass

def Tutorial():
    Type("[Tutorial]: Oh hello! Ummm... Err... What's your name?")
    player.name = input("[Tutorial]: Enter your name here after the '>'\n> ")
    Type(f"[Tutorial]: It's nice to meet you {player.name}!\n[Tutorial]: I'm here to guide you in your upcoming adventure!\n(Though I won't help much...)")
    Type("[Tutorial]: Anyway! During your adventure you'll have to do 'actions'.\n[Tutorial]: Why don't you try one now?")
    Type("Enter 'search' to search the room, maybe you'll find something useful!")
    heh = input("> ").lower()
    while heh != 'search':
        Type(f"[Tutorial]: Hey, {player.name}. That's not search...")
        Type("[Tutorial]: Make sure there isn't any spelling mistakes or spaces.")
        heh = input("> ").lower()
    player_search()
    Type("[Tutorial]: Well done!")
    time.sleep(2)
    Type(f"[Tutorial]: Is that what you wanted to hear?\n;-;\n[Tutorial]: {player.name}, typing search isn't hard...")
    Type("[Tutorial]: Now, I want you to try and move! Type 'move' and then 'right'!")
    heh = input("> ").lower()
    while heh != 'move':
        Type(f"[Tutorial]: Hey, {player.name}. That's not move...")
        Type("[Tutorial]: Make sure there isn't any spelling mistakes or spaces.")
        heh = input("> ").lower()
    heh = input("> ").lower()
    while heh != 'right':
        Type(f"[Tutorial]: Hey, {player.name}. That's not right...(Get it? heh..)")
        Type("[Tutorial]: Make sure there isn't any spelling mistakes or spaces. (DID YOU GET THE JOKE?!?!)")
        heh = input("> ").lower()
    destination = (player.location).Mright
    if destination in [fT_1,fT_2,f100_1, f100_2, f100_3, f99_1, f99_2, f99_3, f98_1, f98_2, f98_3, f97_1, f97_2, f97_3, f96_1, f96_2, f96_3, f95_1, f95_2, f95_3, f94_1, f94_2, f94_3, f93_1, f93_2, f93_3, f92_1, f92_2, f92_3, f91_1, f91_2, f91_3, f90_1, f89_1, f89_2, f89_3, f88_1, f88_2, f88_3, f87_1, f87_2, f87_3, f86_1, f86_2, f86_3, f85_1, f85_2, f85_3, f84_1, f84_2, f84_3, f83_1, f83_2, f83_3, f82_1, f82_2, f82_3, f81_1, f81_2, f81_3, f80_1, f79_1, f79_2, f79_3, f78_1, f78_2, f78_3, f77_1, f77_2, f77_3, f76_1, f76_2, f76_3, f75_1, f75_2, f75_3, f74_1, f74_2, f74_3, f73_1, f73_2, f73_3, f72_1, f72_2, f72_3, f71_1, f71_2, f71_3, f70_1, f69_1, f69_2, f69_3, f68_1, f68_2, f68_3, f67_1, f67_2, f67_3, f66_1, f66_2, f66_3, f65_1, f65_2, f65_3, f64_1, f64_2, f64_3, f63_1, f63_2, f63_3, f62_1, f62_2, f62_3, f61_1, f61_2, f61_3, f60_1, f59_1, f59_2, f59_3, f58_1, f58_2, f58_3, f57_1, f57_2, f57_3, f56_1, f56_2, f56_3, f55_1, f55_2, f55_3, f54_1, f54_2, f54_3, f53_1, f53_2, f53_3, f52_1, f52_2, f52_3, f51_1, f51_2, f51_3, f50_1, f49_1, f49_2, f49_3, f48_1, f48_2, f48_3, f47_1, f47_2, f47_3, f46_1, f46_2, f46_3, f45_1, f45_2, f45_3, f44_1, f44_2, f44_3, f43_1, f43_2, f43_3, f42_1, f42_2, f42_3, f41_1, f41_2, f41_3, f40_1, f39_1, f39_2, f39_3, f38_1, f38_2, f38_3, f37_1, f37_2, f37_3, f36_1, f36_2, f36_3, f35_1, f35_2, f35_3, f34_1, f34_2, f34_3, f33_1, f33_2, f33_3, f32_1, f32_2, f32_3, f31_1, f31_2, f31_3, f30_1, f29_1, f29_2, f29_3, f28_1, f28_2, f28_3, f27_1, f27_2, f27_3, f26_1, f26_2, f26_3, f25_1, f25_2, f25_3, f24_1, f24_2, f24_3, f23_1, f23_2, f23_3, f22_1, f22_2, f22_3, f21_1, f21_2, f21_3, f20_1, f19_1, f19_2, f19_3, f18_1, f18_2, f18_3, f17_1, f17_2, f17_3, f16_1, f16_2, f16_3, f15_1, f15_2, f15_3, f14_1, f14_2, f14_3, f13_1, f13_2, f13_3, f12_1, f12_2, f12_3, f11_1, f11_2, f11_3, f10_1, f9_1, f9_2, f9_3, f8_1, f8_2, f8_3, f7_1, f7_2, f7_3, f6_1, f6_2, f6_3, f5_1, f5_2, f5_3, f4_1, f4_2, f4_3, f3_1, f3_2, f3_3, f2_1, f2_2, f2_3, f1_1, f1_2, f1_3, f0_1, fG]:
        if (destination).zoneunlocked == True:
            move_handle(destination)
        elif (destination).zoneunlocked == False:
            Type("The door to this floor is locked!")
            if (destination).zkey in player.inv:
                Type("You unlocked the door with the key you found!")
                (player.inv).remove((destination).zkey)
                (destination).zoneunlocked = True
                move_handle(destination)
            else:
                Type("You need the key to open this door...")
    Type("[Tutorial]: You see you can't open the door until you have the key in your inventory.")
    Type("[Tutorial]: Try the 'status' action to check your current status!")
    heh = input("> ").lower()
    while heh != 'status':
        Type(f"[Tutorial]: Hey, {player.name}. That's not status...")
        Type("[Tutorial]: Make sure there isn't any spelling mistakes or spaces.")
        heh = input("> ").lower()
    player_status()
    Type("[Tutorial]: Now try the 'take' action to get the key!")
    Type("[Tutorial]: Make sure to spell the 'Glowing Key' correctly.")
    Type("[Tutorial]: Items are also case-sensitive unlike actions.")
    heh = input("> ").lower()
    while heh != 'take':
        Type(f"[Tutorial]: Hey, {player.name}. That's not take...")
        Type("[Tutorial]: Make sure there isn't any spelling mistakes or spaces.")
        heh = input("> ").lower()
    player_take()
    while 'Glowing Key' not in player.inv:
        Type("[Tutorial]: Seems like you didn't get the key... Try again!")
        heh = input("> ").lower()
        while heh != 'take':
            Type(f"[Tutorial]: Hey, {player.name}. That's not take...")
            Type("[Tutorial]: Make sure there isn't any spelling mistakes or spaces.")
            heh = input("> ").lower()
        player_take()
    Type("[Tutorial]: Now you can unlock the door!")
    heh = input("> ").lower()
    while heh != 'move':
        Type(f"[Tutorial]: Hey, {player.name}. That's not move...")
        Type("[Tutorial]: Make sure there isn't any spelling mistakes or spaces.")
        heh = input("> ").lower()
    heh = input("> ").lower()
    while heh != 'right':
        Type(f"[Tutorial]: Hey, {player.name}. That's not right...(Get it? heh..)")
        Type("[Tutorial]: Make sure there isn't any spelling mistakes or spaces. (DID YOU GET THE JOKE?!?!)")
        heh = input("> ").lower()
    destination = (player.location).Mright
    if destination in [fT_1,fT_2,f100_1, f100_2, f100_3, f99_1, f99_2, f99_3, f98_1, f98_2, f98_3, f97_1, f97_2, f97_3, f96_1, f96_2, f96_3, f95_1, f95_2, f95_3, f94_1, f94_2, f94_3, f93_1, f93_2, f93_3, f92_1, f92_2, f92_3, f91_1, f91_2, f91_3, f90_1, f89_1, f89_2, f89_3, f88_1, f88_2, f88_3, f87_1, f87_2, f87_3, f86_1, f86_2, f86_3, f85_1, f85_2, f85_3, f84_1, f84_2, f84_3, f83_1, f83_2, f83_3, f82_1, f82_2, f82_3, f81_1, f81_2, f81_3, f80_1, f79_1, f79_2, f79_3, f78_1, f78_2, f78_3, f77_1, f77_2, f77_3, f76_1, f76_2, f76_3, f75_1, f75_2, f75_3, f74_1, f74_2, f74_3, f73_1, f73_2, f73_3, f72_1, f72_2, f72_3, f71_1, f71_2, f71_3, f70_1, f69_1, f69_2, f69_3, f68_1, f68_2, f68_3, f67_1, f67_2, f67_3, f66_1, f66_2, f66_3, f65_1, f65_2, f65_3, f64_1, f64_2, f64_3, f63_1, f63_2, f63_3, f62_1, f62_2, f62_3, f61_1, f61_2, f61_3, f60_1, f59_1, f59_2, f59_3, f58_1, f58_2, f58_3, f57_1, f57_2, f57_3, f56_1, f56_2, f56_3, f55_1, f55_2, f55_3, f54_1, f54_2, f54_3, f53_1, f53_2, f53_3, f52_1, f52_2, f52_3, f51_1, f51_2, f51_3, f50_1, f49_1, f49_2, f49_3, f48_1, f48_2, f48_3, f47_1, f47_2, f47_3, f46_1, f46_2, f46_3, f45_1, f45_2, f45_3, f44_1, f44_2, f44_3, f43_1, f43_2, f43_3, f42_1, f42_2, f42_3, f41_1, f41_2, f41_3, f40_1, f39_1, f39_2, f39_3, f38_1, f38_2, f38_3, f37_1, f37_2, f37_3, f36_1, f36_2, f36_3, f35_1, f35_2, f35_3, f34_1, f34_2, f34_3, f33_1, f33_2, f33_3, f32_1, f32_2, f32_3, f31_1, f31_2, f31_3, f30_1, f29_1, f29_2, f29_3, f28_1, f28_2, f28_3, f27_1, f27_2, f27_3, f26_1, f26_2, f26_3, f25_1, f25_2, f25_3, f24_1, f24_2, f24_3, f23_1, f23_2, f23_3, f22_1, f22_2, f22_3, f21_1, f21_2, f21_3, f20_1, f19_1, f19_2, f19_3, f18_1, f18_2, f18_3, f17_1, f17_2, f17_3, f16_1, f16_2, f16_3, f15_1, f15_2, f15_3, f14_1, f14_2, f14_3, f13_1, f13_2, f13_3, f12_1, f12_2, f12_3, f11_1, f11_2, f11_3, f10_1, f9_1, f9_2, f9_3, f8_1, f8_2, f8_3, f7_1, f7_2, f7_3, f6_1, f6_2, f6_3, f5_1, f5_2, f5_3, f4_1, f4_2, f4_3, f3_1, f3_2, f3_3, f2_1, f2_2, f2_3, f1_1, f1_2, f1_3, f0_1, fG]:
        if (destination).zoneunlocked == True:
            move_handle(destination)
        elif (destination).zoneunlocked == False:
            Type("The door to this floor is locked!")
            if (destination).zkey in player.inv:
                Type("You unlocked the door with the key you found!")
                (player.inv).remove((destination).zkey)
                (destination).zoneunlocked = True
                move_handle(destination)
            else:
                Type("You need the key to open this door...")
    Type("[Tutorial]: Well you've basically got this! So I'll leave you with a few move actions you can try on your own!")
    Type("[Tutorial]: Try using the action 'talk' within this room!")
    Type("[Tutorial]: And don't forget you can move in all four directions:\n'up', 'down', 'right','left'.")
    Type("[Tutorial]: This place is similar to a maze but... the 'search' action gives a hint to which direction you can go!")
    Prompt()

def MaxHp():
    if player.hp > player.maxhp:
        if player.lvl == 1:
            player.hp = 30
        elif player.lvl == 2:
            player.hp = 50
        elif player.lvl == 3:
            player.hp = 75
        elif player.lvl == 4:
            player.hp = 100
        elif player.lvl == 5:
            player.hp = 150
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

def Levelatk(): #To work base atk based on lvl
        if player.lvl == 1:
            player.atk = 0
            player.maxhp = 25
        elif player.lvl == 2:
            player.atk = 1
            player.maxhp = 50
        elif player.lvl == 3:
            player.atk = 2
            player.maxhp = 75
        elif player.lvl == 4:
            player.atk = 3
            player.maxhp = 100
        elif player.lvl == 5:
            player.atk = 4
            player.maxhp = 150
        elif player.lvl == 6:
            player.atk = 5
            player.maxhp = 175
        elif player.lvl == 7:
            player.atk = 8
            player.maxhp = 200
        elif player.lvl == 8:
            player.atk = 12
            player.maxhp = 250
        elif player.lvl == 9:
            player.atk = 16
            player.maxhp = 300
        elif player.lvl == 10:
            player.atk = 20
            player.maxhp = 400

def Levelstats():
        if player.lvl == 1:
            player.Rexp = 100 - player.exp
        elif player.lvl == 2:
            player.Rexp = 300 - player.exp
        elif player.lvl == 3:
            player.Rexp = 600 - player.exp
        elif player.lvl == 4:
            player.Rexp = 1200 - player.exp
        elif player.lvl == 5:
            player.Rexp = 2500 - player.exp
        elif player.lvl == 6:
            player.Rexp = 5000 - player.exp
        elif player.lvl == 7:
            player.Rexp = 10000 - player.exp
        elif player.lvl == 8:
            player.Rexp = 20000 - player.exp
        elif player.lvl == 9:
            player.Rexp = 50000 - player.exp
        else:
            player.Rexp = 0

def Levelsys():
        if player.exp >= 100 and player.exp <= 399:
            player.lvl = 2
        elif player.exp >= 400 and player.exp <= 699:
            player.lvl = 3
        elif player.exp >= 700 and player.exp <= 1299:
            player.lvl = 4
        elif player.exp >= 1300 and player.exp <= 2599:
            player.lvl = 5
        elif player.exp >= 2600 and player.exp <= 4999:
            player.lvl = 6
        elif player.exp >= 5000 and player.exp <= 9999:
            player.lvl = 7
        elif player.exp >= 10000 and player.exp <= 19999:
            player.lvl = 8
        elif player.exp >= 20000 and player.exp <= 49999:
            player.lvl = 9
        elif player.exp >= 50000:
            player.lvl = 10
        else:
            player.lvl = 1

def PauseMen():
    Lol = False # For While Loop
    while Lol == False:
        Type(" \  Pause Menu  /") # For Display
        Type("   'Resume Game'")
        Type("      'Help'")
        Type("      'Quit'")
        ans = input("Pick an option. > ").lower()
        if ans == "resume game":
            Type("Resuming Game...")
            Type("Enjoy!")
            return
        elif ans == "help":
            Type("This game has many actions which can inputted when this symbol appears '>'.")
            Type("These actions are: ['move','search','use','take','pause','talk','status','info','quit']")
            t = 2
            while t == 2:
                Type("Would you like to know what these actions do?")
                help = input("Input the action or no > ").lower()
                if help == 'no':
                    t = 3
                elif help == 'move':
                    Type("'move', allows you to move around the office tower")
                    Type("After choosing to move you then input your direction,\n['right','left','up','down']\n Note that there is not a room in every direction.")
                elif help == 'search':
                    Type("'search', allows you to search the room for any useful items.\nThis action will also tell you in which direction the next rooms are.")
                elif help == 'use':
                    Type("'use', allows you use items like an exp orb or a health potion.\nNote that there is no max health points so your hp will be scaled based on how many healing potions you use.")
                elif help == 'take':
                    Type("'take', allows you to take any items you find and add them to your Inventory.\nNote that every item must be added individually and spelt correctly.")
                elif help == 'pause':
                    Type("'pause', you should know what this does... you just used it ;-;.")
                elif help == 'talk':
                    Type("'talk', allows you to talk to people within the office tower. Don't worry they're friendly!\nHint!: Sometimes tower merchants stock changes based on your level...")
                elif help == 'status':
                    Type("'status', allows you to see your progress within the game like your health points, level and inventory.")
                elif help == 'info':
                    Type("'info', allows you to read information about items in your inventory or ones you have yet to obtain.\nIt is very useful, especially if you don't know how to use certain items.")
                elif help == 'quit':
                    Type("'quit', allows you exit the game without having the 'Are you sure?' prompt.\nI suggest you DO NOT use this as its purpose was so the dev could quit the game easily to test it.")
                else:
                    t = 3
        elif ans == "quit":
            Type("Are you sure? Your progress will NOT be saved, unless you found the save action!. > ")
            ans1 = input(" Y or N ? > ").upper()
            if ans1 == "Y":
                Type("Bye. All your progress is deleted... Maybe...")
                Main()
            elif ans1 == "N":
                Type("Good. You better not try and quit again.")
                Type("I'll know.....")
                Lol = False
            else:
                Type("Error, only Y or N is accepted that includes unnecessary spaces.")
                Lol = False
        else:
            Type("Error, only correctly spelt 'keywords' are accepted.")
        os.system('cls')

def Expmi(): #Miniscule
    Exp = player.exp + 1
    player.exp = Exp
    return

def Expti(): #Tiny
    Exp = player.exp + 5
    player.exp = Exp
    return

def Expme(): #Medium
    Exp = player.exp + 10
    player.exp = Exp
    return

def Expla(): #Large
    Exp = player.exp + 20
    player.exp = Exp
    return

def Expma(): #MASSIVE
    Exp = player.exp + 50
    player.exp = Exp
    return

def Expbh(): #Beyond Holy
    Exp = player.exp + 200
    player.exp = Exp
    return

def Hmi(): #Miniscule
    Exp = player.hp + 15
    player.hp = Exp
    return

def Hti(): #Tiny
    Exp = player.hp + 20
    player.hp = Exp
    return

def Hme(): #Medium
    Exp = player.hp + 50
    player.hp = Exp
    return

def Hla(): #Large
    Exp = player.hp + 100
    player.hp = Exp
    return

def Hma(): #MASSIVE
    Exp = player.hp + 150
    player.hp = Exp
    return

def Hbh(): #Beyond Holy
    Exp = player.hp + 300
    player.hp = Exp
    return

def drops():
    expdice = random.randint(2,10)
    goldice = random.randint(1,4)
    mobexp = (player.beat).exp * expdice
    (player.beat).exp = mobexp
    mobgd = (player.beat).gold * goldice
    (player.beat).gold = mobgd
    if player.curq == 'Collect the Shards!':
        if player.shard <= 29:
            sharddice1 = random.randint(0,3)
            if sharddice1 == 2:
                Type(f"The {(player.beat).name} dropped one Escape Device Shard!")
                ge = player.shard + 1
                player.shard = ge
    Type(f"The {(player.beat).name} dropped {(player.beat).gold} Gold pieces.")
    Type(f"You gained {(player.beat).exp} exp!")
    pxp = (player.beat).exp + player.exp
    pg = (player.beat).gold + player.gold
    player.exp = pxp
    player.gold = pg
    return

def attack():
    dice = random.randint(0,6)
    dmg = (player.atk + player.wpatk) * dice
    if dmg == 0:
        Type(f"Your attack was dodged!")
    else:
        Type(f"You dealt {dmg} damage!")
        mobhp = (player.target).hp - dmg
        (player.target).hp = mobhp
    return

def battle_use():
    Type("In your Inventory you have:")
    Type(", ".join(player.inv))
    used = input("What item would you like to use? > ")
    if used not in player.inv:
        Type("You don't own that item or it doesn't exist...")
        Type("Check your spelling and for spaces!")
        return
    elif used == 'Miniscule Healing Potion':
        Type("You have just gained 10 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hmi()
        return
    elif used == 'Tiny Healing Potion':
        Type("You have just gained 20 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hti()
        return
    elif used == 'Medium Healing Potion':
        Type("You have just gained 50 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hme()
        return
    elif used == 'Large Healing Potion':
        Type("You have just gained 100 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hla()
        return
    elif used == 'MASSIVE Healing Potion':
        Type("You have just gained 150 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hma()
        return
    elif used == 'Beyond Holy Healing Potion':
        Type("You have just gained 300 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hbh()
        return

def BattlePrompt():
    action = input("Quick! Take action!!! > ").lower()
    valid_act = ['attack','use','pause','quit']
    while action not in valid_act:
        Type("Invaild action, check your spelling or any spaces.")
        action = input("Enter your action. > ").lower()
    if action == 'pause':
        PauseMen()
    elif action == 'attack':
        attack()
        return
    elif action == 'use':
        battle_use()
        return
    elif action == 'quit':
        quit()

def Battle():
    wpofc = ''
    while wpofc not in player.inv and wpofc not in ['Notebook','Ruler','Blunt Pencil','Sharpened Pencil','Small Dagger','Rusty Sword','Shiny Sword','Ancient Katana','Refined Katana'] or wpofc not in ['Notebook','Ruler','Blunt Pencil','Sharpened Pencil','Small Dagger','Rusty Sword','Shiny Sword','Ancient Katana','Refined Katana'] or wpofc not in player.inv:
        Type("Quick! Equip your weapon of choice!")
        Type(f"Your Inventory: (If you don't have anything type 'no'.)")
        Type(", ".join(player.inv))
        wpofc = input("> ")
        if wpofc == 'no':
            Type("You have no weapon, so you can't defend yourself...")
            Type("Next time use 'search' and 'take' to find items.")
            quit()
        elif wpofc not in player.inv:
            Type("That's not in your Inventory!")
            Type("Check your spelling and for any spaces!")
        elif wpofc not in ['Notebook','Ruler','Blunt Pencil','Sharpened Pencil','Small Dagger','Rusty Sword','Shiny Sword','Ancient Katana','Refined Katana']:
            Type("That's not a weapon, try something else.")
        else:
            if wpofc == 'Notebook':
                player.wpatk = Wp1.atk
                Type(f"You have equipped the {Wp1.name}.")
            elif wpofc == 'Ruler':
                player.wpatk = Wp02.atk
                Type(f"You have equipped the {Wp02.name}.")
            elif wpofc == 'Blunt Pencil':
                player.wpatk = Wp2.atk
                Type(f"You have equipped the {Wp2.name}.")
            elif wpofc == 'Sharpened Pencil':
                player.wpatk = Wp3.atk
                Type(f"You have equipped the {Wp3.name}.")
            elif wpofc == 'Small Dagger':
                player.wpatk = Wp4.atk
                Type(f"You have equipped the {Wp4.name}.")
            elif wpofc == 'Rusty Sword':
                player.wpatk = Wp5.atk
                Type(f"You have equipped the {Wp5.name}.")
            elif wpofc == 'Shiny Sword':
                player.wpatk = Wp6.atk
                Type(f"You have equipped the {Wp6.name}.")
            elif wpofc == 'Ancient Katana':
                player.wpatk = Wp7.atk
                Type(f"You have equipped the {Wp7.name}.")
            elif wpofc == 'Refined Katana':
                player.wpatk = Wp8.atk
                Type(f"You have equipped the {Wp8.name}.")
        Type(f"There is currently {len((player.location).zmobs)} mob(s) about to attack you!")
    if len((player.location).zmobs) == 1:
        if (player.location).zmobs[0] == 'Goblin':
            mob1 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Slime':
            mob1 = Slime({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Zombie':
            mob1 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Wolf':
            mob1 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Hobgoblin':
            mob1 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire':
            mob1 = Vampire({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Goblin King':
            mob1 = Goblin_King({},{},{},{},{})
        elif(player.location).zmobs[0] == 'MASSIVE Slime':
            mob1 = MASSIVE_Slime({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Undecayed Zombie':
            mob1 = Undecayed_Zombie({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Alpha Wolf':
            mob1 = Alpha_Wolf({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Hobbiest Hobgoblin':
            mob1 = Hobbiest_Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire Lord 1':
            mob1 = Vampire_Lord1({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire Lord 2':
            mob1 = Vampire_Lord2({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire Lord 3':
            mob1 = Vampire_Lord3({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire Lord 4':
            mob1 = Vampire_Lord4({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire King':
            mob1 = Vampire_King({},{},{},{},{})
    elif len((player.location).zmobs) == 2:
        if (player.location).zmobs[0] == 'Goblin':
            mob1 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Slime':
            mob1 = Slime({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Zombie':
            mob1 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Wolf':
            mob1 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Hobgoblin':
            mob1 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire':
            mob1 = Vampire({},{},{},{},{})
        if (player.location).zmobs[1] == 'Goblin':
            mob2 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Slime':
            mob2 = Slime({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Zombie':
            mob2 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Wolf':
            mob2 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Hobgoblin':
            mob2 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Vampire':
            mob2 = Vampire({},{},{},{},{})
    elif len((player.location).zmobs) == 3:
        if (player.location).zmobs[0] == 'Goblin':
            mob1 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Slime':
            mob1 = Slime({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Zombie':
            mob1 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Wolf':
            mob1 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Hobgoblin':
            mob1 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire':
            mob1 = Vampire({},{},{},{},{})
        if (player.location).zmobs[1] == 'Goblin':
            mob2 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Slime':
            mob2 = Slime({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Zombie':
            mob2 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Wolf':
            mob2 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Hobgoblin':
            mob2 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Vampire':
            mob2 = Vampire({},{},{},{},{})
        if (player.location).zmobs[2] == 'Goblin':
            mob3 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Slime':
            mob3 = Slime({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Zombie':
            mob3 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Wolf':
            mob3 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Hobgoblin':
            mob3 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Vampire':
            mob3 = Vampire({},{},{},{},{})
    elif len((player.location).zmobs) == 4:
        if (player.location).zmobs[0] == 'Goblin':
            mob1 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Slime':
            mob1 = Slime({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Zombie':
            mob1 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Wolf':
            mob1 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Hobgoblin':
            mob1 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire':
            mob1 = Vampire({},{},{},{},{})
        if (player.location).zmobs[1] == 'Goblin':
            mob2 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Slime':
            mob2 = Slime({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Zombie':
            mob2 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Wolf':
            mob2 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Hobgoblin':
            mob2 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Vampire':
            mob2 = Vampire({},{},{},{},{})
        if (player.location).zmobs[2] == 'Goblin':
            mob3 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Slime':
            mob3 = Slime({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Zombie':
            mob3 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Wolf':
            mob3 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Hobgoblin':
            mob3 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Vampire':
            mob3 = Vampire({},{},{},{},{})
        if (player.location).zmobs[3] == 'Goblin':
            mob4 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Slime':
            mob4 = Slime({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Zombie':
            mob4 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Wolf':
            mob4 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Hobgoblin':
            mob4 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Vampire':
            mob4 = Vampire({},{},{},{},{})
    elif len((player.location).zmobs) == 5:
        if (player.location).zmobs[0] == 'Goblin':
            mob1 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Slime':
            mob1 = Slime({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Zombie':
            mob1 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Wolf':
            mob1 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Hobgoblin':
            mob1 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[0] == 'Vampire':
            mob1 = Vampire({},{},{},{},{})
        if (player.location).zmobs[1] == 'Goblin':
            mob2 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Slime':
            mob2 = Slime({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Zombie':
            mob2 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Wolf':
            mob2 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Hobgoblin':
            mob2 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[1] == 'Vampire':
            mob2 = Vampire({},{},{},{},{})
        if (player.location).zmobs[2] == 'Goblin':
            mob3 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Slime':
            mob3 = Slime({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Zombie':
            mob3 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Wolf':
            mob3 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Hobgoblin':
            mob3 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[2] == 'Vampire':
            mob3 = Vampire({},{},{},{},{})
        if (player.location).zmobs[3] == 'Goblin':
            mob4 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Slime':
            mob4 = Slime({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Zombie':
            mob4 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Wolf':
            mob4 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Hobgoblin':
            mob4 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[3] == 'Vampire':
            mob4 = Vampire({},{},{},{},{})
        if (player.location).zmobs[4] == 'Goblin':
            mob5 = Goblin({},{},{},{},{})
        elif(player.location).zmobs[4] == 'Slime':
            mob5 = Slime({},{},{},{},{})
        elif(player.location).zmobs[4] == 'Zombie':
            mob5 = Zombie({},{},{},{},{})
        elif(player.location).zmobs[4] == 'Wolf':
            mob5 = Wolf({},{},{},{},{})
        elif(player.location).zmobs[4] == 'Hobgoblin':
            mob5 = Hobgoblin({},{},{},{},{})
        elif(player.location).zmobs[4] == 'Vampire':
            mob5 = Vampire({},{},{},{},{})

    if len((player.location).zmobs) == 1:
            while mob1.hp > 0:
                if player.hp <= 0:
                    Type(f"You have been defeated by {mob1.name}...")

                    Type("You'll get them next time!")

                    quit()
                else:
                    player.target = mob1
                    dice = random.randint(0,6)
                    dmg = mob1.atk * dice
                    if dmg == 0:
                        Type(f"{mob1.name} missed it's attack!")
                        BattlePrompt()
                    else:
                        Type(f"{mob1.name} dealt {dmg} damage!")
                        php = player.hp - dmg
                        player.hp = php
                        if player.hp <= 0:
                            Type(f"You have been defeated by {mob1.name}...")

                            Type("You'll get them next time!")

                            quit()
                        else:
                            Type(f"You are currently on {player.hp} health points!")
                            BattlePrompt()
                            Type(f"{mob1.name} currently has {mob1.hp} health points!")
            Type(f"You defeated the {mob1.name}!")
            ((player.location).zmobs).remove(mob1.name)
            player.beat = mob1
            drops()
    elif len((player.location).zmobs) == 2:
                while mob1.hp > 0 or mob2.hp > 0:
                    if player.hp <= 0:
                        Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                        Type("You'll get them next time!")

                        quit()
                    if mob1.hp > 0 and mob2.hp > 0:
                        Type(f"Which mob will you target? {mob1.name} or {mob2.name}.")
                        target = input(f"> ")
                        if target == mob1.name and target == mob2.name:
                            target = mob1
                            player.target = target
                        elif target == mob2.name:
                            target = mob2
                            player.target = target
                        else:
                            target = mob1
                            player.target = target
                        dice = random.randint(0,6)
                        dice2 = random.randint(0,6)
                        dmg = mob1.atk * dice
                        dmg2 = mob2.atk * dice2
                        if dmg == 0:
                            Type(f"{mob1.name} missed it's attack!")
                            Type(f"{mob2.name} dealt {dmg2} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                        elif dmg2 == 0:
                            Type(f"{mob2.name} missed it's attack!")
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                        elif dmg == 0 and dmg2 == 0:
                            Type(f"{mob1.name} and {mob2.name} missed their attacks!")
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                        else:
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            Type(f"{mob2.name} dealt {dmg2} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                    elif mob2.hp < 0:
                        player.target = mob1
                        dice = random.randint(0,6)
                        dmg = mob1.atk * dice
                        if dmg == 0:
                            Type(f"{mob1.name} missed it's attack!")
                            BattlePrompt()
                        else:
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            php = player.hp - dmg
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                    elif mob1.hp < 0:
                        player.target = mob2
                        dice = random.randint(0,6)
                        dmg = mob2.atk * dice
                        if dmg == 0:
                            Type(f"{mob2.name} missed it's attack!")
                            BattlePrompt()
                        else:
                            Type(f"{mob2.name} dealt {dmg} damage!")
                            php = player.hp - dmg
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                Type(f"You defeated the {mob1.name}!")
                ((player.location).zmobs).remove(mob1.name)
                player.beat = mob1
                drops()
                Type(f"You defeated the {mob2.name}!")
                ((player.location).zmobs).remove(mob2.name)
                player.beat = mob2
                drops()
    elif len((player.location).zmobs) == 3:
                while mob1.hp > 0 or mob2.hp > 0 or mob3.hp > 0:
                    if player.hp <= 0:
                        Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                        Type("You'll get them next time!")

                        quit()
                    if mob1.hp > 0 and mob2.hp > 0 and mob3.hp > 0:
                        Type(f"Which mob will you target? {mob1.name} or {mob2.name} or {mob3.name}.")
                        target = input(f"> ")
                        if target == mob1.name and target == mob2.name and target == mob3.name:
                            target = mob1
                            player.target = target
                        elif target == mob2.name and target == mob3.name:
                            target = mob2
                            player.target = mob2
                        elif target == mob2.name:
                            target = mob2
                            player.target = target
                        elif target == mob3.name:
                            target = mob3
                            player.target = target
                        else:
                            target = mob1
                            player.target = target
                        dice = random.randint(0,6)
                        dice2 = random.randint(0,6)
                        dice3 = random.randint(0,6)
                        dmg = mob1.atk * dice
                        dmg2 = mob2.atk * dice2
                        dmg3 = mob3.atk * dice3
                        if dmg == 0:
                            Type(f"{mob1.name} missed it's attack!")
                            Type(f"{mob2.name} dealt {dmg2} damage!")
                            Type(f"{mob3.name} dealt {dmg3} damage!")
                            php = player.hp - dmg - dmg2 - dmg3
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        elif dmg2 == 0:
                            Type(f"{mob2.name} missed it's attack!")
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            Type(f"{mob3.name} dealt {dmg3} damage!")
                            php = player.hp - dmg - dmg2 - dmg3
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        elif dmg3 == 0:
                            Type(f"{mob3.name} missed it's attack!")
                            Type(f"{mob2.name} dealt {dmg2} damage!")
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            php = player.hp - dmg - dmg2 - dmg3
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        elif dmg == 0 and dmg2 == 0 and dmg3 == 0:
                            Type(f"{mob1.name}, {mob2.name} and {mob3.name} missed their attacks!")
                            php = player.hp - dmg - dmg2 - dmg3
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        else:
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            Type(f"{mob2.name} dealt {dmg2} damage!")
                            Type(f"{mob3.name} dealt {dmg3} damage!")
                            php = player.hp - dmg - dmg2 - dmg3
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                    elif mob1.hp > 0 and mob2.hp > 0:
                        Type(f"Which mob will you target? {mob1.name} or {mob2.name}.")
                        target = input(f"> ")
                        if target == mob1.name and target == mob2.name:
                            target = mob1
                            player.target = target
                        elif target == mob2.name:
                            target = mob3
                            player.target = target
                        else:
                            target = mob1
                            player.target = target
                        dice = random.randint(0,6)
                        dice2 = random.randint(0,6)
                        dmg = mob1.atk * dice
                        dmg2 = mob2.atk * dice2
                        if dmg == 0:
                            Type(f"{mob1.name} missed it's attack!")
                            Type(f"{mob2.name} dealt {dmg2} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                        elif dmg2 == 0:
                            Type(f"{mob2.name} missed it's attack!")
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                        elif dmg == 0 and dmg2 == 0:
                            Type(f"{mob1.name} and {mob2.name} missed their attacks!")
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                        else:
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            Type(f"{mob2.name} dealt {dmg2} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                    elif mob2.hp > 0 and mob3.hp > 0:
                        Type(f"Which mob will you target? {mob2.name} or {mob3.name}.")
                        target = input(f"> ")
                        if target == mob2.name and target == mob3.name:
                            target = mob2
                            player.target = target
                        elif target == mob3.name:
                            target = mob3
                            player.target = target
                        else:
                            target = mob2
                            player.target = target
                        dice = random.randint(0,6)
                        dice2 = random.randint(0,6)
                        dmg = mob2.atk * dice
                        dmg2 = mob3.atk * dice2
                        if dmg == 0:
                            Type(f"{mob2.name} missed it's attack!")
                            Type(f"{mob3.name} dealt {dmg2} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob2.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        elif dmg2 == 0:
                            Type(f"{mob3.name} missed it's attack!")
                            Type(f"{mob2.name} dealt {dmg} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob2.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        elif dmg == 0 and dmg2 == 0:
                            Type(f"{mob2.name} and {mob3.name} missed their attacks!")
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob2.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        else:
                            Type(f"{mob2.name} dealt {dmg} damage!")
                            Type(f"{mob3.name} dealt {dmg2} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob2.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                    elif mob1.hp > 0 and mob3.hp > 0:
                        Type(f"Which mob will you target? {mob1.name} or {mob3.name}.")
                        target = input(f"> ")
                        if target == mob1.name and target == mob3.name:
                            target = mob1
                            player.target = target
                        elif target == mob3.name:
                            target = mob3
                            player.target = target
                        else:
                            target = mob1
                            player.target = target
                        dice = random.randint(0,6)
                        dice2 = random.randint(0,6)
                        dmg = mob1.atk * dice
                        dmg2 = mob3.atk * dice2
                        if dmg == 0:
                            Type(f"{mob1.name} missed it's attack!")
                            Type(f"{mob3.name} dealt {dmg2} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        elif dmg2 == 0:
                            Type(f"{mob3.name} missed it's attack!")
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        elif dmg == 0 and dmg2 == 0:
                            Type(f"{mob1.name} and {mob3.name} missed their attacks!")
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                        else:
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            Type(f"{mob3.name} dealt {dmg2} damage!")
                            php = player.hp - dmg - dmg2
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name} and {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                    elif mob1.hp > 0:
                        player.target = mob1
                        dice = random.randint(0,6)
                        dmg = mob1.atk * dice
                        if dmg == 0:
                            Type(f"{mob1.name} missed it's attack!")
                            BattlePrompt()
                        else:
                            Type(f"{mob1.name} dealt {dmg} damage!")
                            php = player.hp - dmg
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob1.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob1.name} currently has {mob1.hp} health points!")
                    elif mob2.hp > 0:
                        player.target = mob2
                        dice = random.randint(0,6)
                        dmg = mob2.atk * dice
                        if dmg == 0:
                            Type(f"{mob2.name} missed it's attack!")
                            BattlePrompt()
                        else:
                            Type(f"{mob2.name} dealt {dmg} damage!")
                            php = player.hp - dmg
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob2.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob2.name} currently has {mob2.hp} health points!")
                    elif mob3.hp > 0:
                        player.target = mob3
                        dice = random.randint(0,6)
                        dmg = mob3.atk * dice
                        if dmg == 0:
                            Type(f"{mob3.name} missed it's attack!")
                            BattlePrompt()
                        else:
                            Type(f"{mob3.name} dealt {dmg} damage!")
                            php = player.hp - dmg
                            player.hp = php
                            if player.hp <= 0:
                                Type(f"You have been defeated by {mob3.name}...")

                                Type("You'll get them next time!")

                                quit()
                            else:
                                Type(f"You are currently on {player.hp} health points!")
                                BattlePrompt()
                                Type(f"{mob3.name} currently has {mob3.hp} health points!")
                Type(f"You defeated the {mob1.name}!")
                ((player.location).zmobs).remove(mob1.name)
                player.beat = mob1
                drops()
                Type(f"You defeated the {mob2.name}!")
                ((player.location).zmobs).remove(mob2.name)
                player.beat = mob2
                drops()
                Type(f"You defeated the {mob3.name}!")
                ((player.location).zmobs).remove(mob3.name)
                player.beat = mob3
                drops()
    if player.location == f100_3:
        Cutscene()
    elif player.location == f90_1:
        Cutscene()
    Prompt()

def player_move():
    dest = input("Input the direction you would like to move. > ").lower()
    while dest not in ['up','down','left','right']:
        Type("Invaild direction, check your spelling or any spaces.")

        dest = input("Enter your direction. > ").lower()
    if dest == 'up':
        destination = (player.location).Mup
        if destination in [fT_1,fT_2,f100_1, f100_2, f100_3, f99_1, f99_2, f99_3, f98_1, f98_2, f98_3, f97_1, f97_2, f97_3, f96_1, f96_2, f96_3, f95_1, f95_2, f95_3, f94_1, f94_2, f94_3, f93_1, f93_2, f93_3, f92_1, f92_2, f92_3, f91_1, f91_2, f91_3, f90_1, f89_1, f89_2, f89_3, f88_1, f88_2, f88_3, f87_1, f87_2, f87_3, f86_1, f86_2, f86_3, f85_1, f85_2, f85_3, f84_1, f84_2, f84_3, f83_1, f83_2, f83_3, f82_1, f82_2, f82_3, f81_1, f81_2, f81_3, f80_1, f79_1, f79_2, f79_3, f78_1, f78_2, f78_3, f77_1, f77_2, f77_3, f76_1, f76_2, f76_3, f75_1, f75_2, f75_3, f74_1, f74_2, f74_3, f73_1, f73_2, f73_3, f72_1, f72_2, f72_3, f71_1, f71_2, f71_3, f70_1, f69_1, f69_2, f69_3, f68_1, f68_2, f68_3, f67_1, f67_2, f67_3, f66_1, f66_2, f66_3, f65_1, f65_2, f65_3, f64_1, f64_2, f64_3, f63_1, f63_2, f63_3, f62_1, f62_2, f62_3, f61_1, f61_2, f61_3, f60_1, f59_1, f59_2, f59_3, f58_1, f58_2, f58_3, f57_1, f57_2, f57_3, f56_1, f56_2, f56_3, f55_1, f55_2, f55_3, f54_1, f54_2, f54_3, f53_1, f53_2, f53_3, f52_1, f52_2, f52_3, f51_1, f51_2, f51_3, f50_1, f49_1, f49_2, f49_3, f48_1, f48_2, f48_3, f47_1, f47_2, f47_3, f46_1, f46_2, f46_3, f45_1, f45_2, f45_3, f44_1, f44_2, f44_3, f43_1, f43_2, f43_3, f42_1, f42_2, f42_3, f41_1, f41_2, f41_3, f40_1, f39_1, f39_2, f39_3, f38_1, f38_2, f38_3, f37_1, f37_2, f37_3, f36_1, f36_2, f36_3, f35_1, f35_2, f35_3, f34_1, f34_2, f34_3, f33_1, f33_2, f33_3, f32_1, f32_2, f32_3, f31_1, f31_2, f31_3, f30_1, f29_1, f29_2, f29_3, f28_1, f28_2, f28_3, f27_1, f27_2, f27_3, f26_1, f26_2, f26_3, f25_1, f25_2, f25_3, f24_1, f24_2, f24_3, f23_1, f23_2, f23_3, f22_1, f22_2, f22_3, f21_1, f21_2, f21_3, f20_1, f19_1, f19_2, f19_3, f18_1, f18_2, f18_3, f17_1, f17_2, f17_3, f16_1, f16_2, f16_3, f15_1, f15_2, f15_3, f14_1, f14_2, f14_3, f13_1, f13_2, f13_3, f12_1, f12_2, f12_3, f11_1, f11_2, f11_3, f10_1, f9_1, f9_2, f9_3, f8_1, f8_2, f8_3, f7_1, f7_2, f7_3, f6_1, f6_2, f6_3, f5_1, f5_2, f5_3, f4_1, f4_2, f4_3, f3_1, f3_2, f3_3, f2_1, f2_2, f2_3, f1_1, f1_2, f1_3, f0_1, fG]:
            if (destination).zoneunlocked == True:
                move_handle(destination)
            elif (destination).zoneunlocked == False:
                Type("The door to this floor is locked!")
                if (destination).zkey in player.inv:
                    Type("You unlocked the door with the key you found!")
                    (player.inv).remove((destination).zkey)
                    (destination).zoneunlocked = True
                    move_handle(destination)
                else:
                    Type("You need the key to open this door...")
                    Prompt()
            else:
                Type("ERROR GAME IS BUGGED")
        else:
            Type("You can't go in that direction!")
            Prompt()
    elif dest == 'down':
        destination = (player.location).Mdown
        if destination in [fT_1,fT_2,f100_1, f100_2, f100_3, f99_1, f99_2, f99_3, f98_1, f98_2, f98_3, f97_1, f97_2, f97_3, f96_1, f96_2, f96_3, f95_1, f95_2, f95_3, f94_1, f94_2, f94_3, f93_1, f93_2, f93_3, f92_1, f92_2, f92_3, f91_1, f91_2, f91_3, f90_1, f89_1, f89_2, f89_3, f88_1, f88_2, f88_3, f87_1, f87_2, f87_3, f86_1, f86_2, f86_3, f85_1, f85_2, f85_3, f84_1, f84_2, f84_3, f83_1, f83_2, f83_3, f82_1, f82_2, f82_3, f81_1, f81_2, f81_3, f80_1, f79_1, f79_2, f79_3, f78_1, f78_2, f78_3, f77_1, f77_2, f77_3, f76_1, f76_2, f76_3, f75_1, f75_2, f75_3, f74_1, f74_2, f74_3, f73_1, f73_2, f73_3, f72_1, f72_2, f72_3, f71_1, f71_2, f71_3, f70_1, f69_1, f69_2, f69_3, f68_1, f68_2, f68_3, f67_1, f67_2, f67_3, f66_1, f66_2, f66_3, f65_1, f65_2, f65_3, f64_1, f64_2, f64_3, f63_1, f63_2, f63_3, f62_1, f62_2, f62_3, f61_1, f61_2, f61_3, f60_1, f59_1, f59_2, f59_3, f58_1, f58_2, f58_3, f57_1, f57_2, f57_3, f56_1, f56_2, f56_3, f55_1, f55_2, f55_3, f54_1, f54_2, f54_3, f53_1, f53_2, f53_3, f52_1, f52_2, f52_3, f51_1, f51_2, f51_3, f50_1, f49_1, f49_2, f49_3, f48_1, f48_2, f48_3, f47_1, f47_2, f47_3, f46_1, f46_2, f46_3, f45_1, f45_2, f45_3, f44_1, f44_2, f44_3, f43_1, f43_2, f43_3, f42_1, f42_2, f42_3, f41_1, f41_2, f41_3, f40_1, f39_1, f39_2, f39_3, f38_1, f38_2, f38_3, f37_1, f37_2, f37_3, f36_1, f36_2, f36_3, f35_1, f35_2, f35_3, f34_1, f34_2, f34_3, f33_1, f33_2, f33_3, f32_1, f32_2, f32_3, f31_1, f31_2, f31_3, f30_1, f29_1, f29_2, f29_3, f28_1, f28_2, f28_3, f27_1, f27_2, f27_3, f26_1, f26_2, f26_3, f25_1, f25_2, f25_3, f24_1, f24_2, f24_3, f23_1, f23_2, f23_3, f22_1, f22_2, f22_3, f21_1, f21_2, f21_3, f20_1, f19_1, f19_2, f19_3, f18_1, f18_2, f18_3, f17_1, f17_2, f17_3, f16_1, f16_2, f16_3, f15_1, f15_2, f15_3, f14_1, f14_2, f14_3, f13_1, f13_2, f13_3, f12_1, f12_2, f12_3, f11_1, f11_2, f11_3, f10_1, f9_1, f9_2, f9_3, f8_1, f8_2, f8_3, f7_1, f7_2, f7_3, f6_1, f6_2, f6_3, f5_1, f5_2, f5_3, f4_1, f4_2, f4_3, f3_1, f3_2, f3_3, f2_1, f2_2, f2_3, f1_1, f1_2, f1_3, f0_1, fG]:
            if (destination).zoneunlocked == True:
                move_handle(destination)
            elif (destination).zoneunlocked == False:
                Type("The door to this floor is locked!")
                if (destination).zkey in player.inv:
                    Type("You unlocked the door with the key you found!")
                    (player.inv).remove((destination).zkey)
                    (destination).zoneunlocked = True
                    move_handle(destination)
                else:
                    Type("You need the key to open this door...")
                    Prompt()
            else:
                Type("ERROR GAME IS BUGGED")
        else:
            Type("You can't go in that direction!")
            Prompt()
    elif dest == 'left':
        destination = (player.location).Mleft
        if destination in [fT_1,fT_2,f100_1, f100_2, f100_3, f99_1, f99_2, f99_3, f98_1, f98_2, f98_3, f97_1, f97_2, f97_3, f96_1, f96_2, f96_3, f95_1, f95_2, f95_3, f94_1, f94_2, f94_3, f93_1, f93_2, f93_3, f92_1, f92_2, f92_3, f91_1, f91_2, f91_3, f90_1, f89_1, f89_2, f89_3, f88_1, f88_2, f88_3, f87_1, f87_2, f87_3, f86_1, f86_2, f86_3, f85_1, f85_2, f85_3, f84_1, f84_2, f84_3, f83_1, f83_2, f83_3, f82_1, f82_2, f82_3, f81_1, f81_2, f81_3, f80_1, f79_1, f79_2, f79_3, f78_1, f78_2, f78_3, f77_1, f77_2, f77_3, f76_1, f76_2, f76_3, f75_1, f75_2, f75_3, f74_1, f74_2, f74_3, f73_1, f73_2, f73_3, f72_1, f72_2, f72_3, f71_1, f71_2, f71_3, f70_1, f69_1, f69_2, f69_3, f68_1, f68_2, f68_3, f67_1, f67_2, f67_3, f66_1, f66_2, f66_3, f65_1, f65_2, f65_3, f64_1, f64_2, f64_3, f63_1, f63_2, f63_3, f62_1, f62_2, f62_3, f61_1, f61_2, f61_3, f60_1, f59_1, f59_2, f59_3, f58_1, f58_2, f58_3, f57_1, f57_2, f57_3, f56_1, f56_2, f56_3, f55_1, f55_2, f55_3, f54_1, f54_2, f54_3, f53_1, f53_2, f53_3, f52_1, f52_2, f52_3, f51_1, f51_2, f51_3, f50_1, f49_1, f49_2, f49_3, f48_1, f48_2, f48_3, f47_1, f47_2, f47_3, f46_1, f46_2, f46_3, f45_1, f45_2, f45_3, f44_1, f44_2, f44_3, f43_1, f43_2, f43_3, f42_1, f42_2, f42_3, f41_1, f41_2, f41_3, f40_1, f39_1, f39_2, f39_3, f38_1, f38_2, f38_3, f37_1, f37_2, f37_3, f36_1, f36_2, f36_3, f35_1, f35_2, f35_3, f34_1, f34_2, f34_3, f33_1, f33_2, f33_3, f32_1, f32_2, f32_3, f31_1, f31_2, f31_3, f30_1, f29_1, f29_2, f29_3, f28_1, f28_2, f28_3, f27_1, f27_2, f27_3, f26_1, f26_2, f26_3, f25_1, f25_2, f25_3, f24_1, f24_2, f24_3, f23_1, f23_2, f23_3, f22_1, f22_2, f22_3, f21_1, f21_2, f21_3, f20_1, f19_1, f19_2, f19_3, f18_1, f18_2, f18_3, f17_1, f17_2, f17_3, f16_1, f16_2, f16_3, f15_1, f15_2, f15_3, f14_1, f14_2, f14_3, f13_1, f13_2, f13_3, f12_1, f12_2, f12_3, f11_1, f11_2, f11_3, f10_1, f9_1, f9_2, f9_3, f8_1, f8_2, f8_3, f7_1, f7_2, f7_3, f6_1, f6_2, f6_3, f5_1, f5_2, f5_3, f4_1, f4_2, f4_3, f3_1, f3_2, f3_3, f2_1, f2_2, f2_3, f1_1, f1_2, f1_3, f0_1, fG]:
            if (destination).zoneunlocked == True:
                move_handle(destination)
            elif (destination).zoneunlocked == False:
                Type("The door to this floor is locked!")
                if (destination).zkey in player.inv:
                    Type("You unlocked the door with the key you found!")
                    (player.inv).remove((destination).zkey)
                    (destination).zoneunlocked = True
                    move_handle(destination)
                else:
                    Type("You need the key to open this door...")
                    Prompt()
            else:
                Type("ERROR GAME IS BUGGED")
        else:
            Type("You can't go in that direction!")
            Prompt()
    elif dest == 'right':
        destination = (player.location).Mright
        if destination in [fT_1,fT_2,f100_1, f100_2, f100_3, f99_1, f99_2, f99_3, f98_1, f98_2, f98_3, f97_1, f97_2, f97_3, f96_1, f96_2, f96_3, f95_1, f95_2, f95_3, f94_1, f94_2, f94_3, f93_1, f93_2, f93_3, f92_1, f92_2, f92_3, f91_1, f91_2, f91_3, f90_1, f89_1, f89_2, f89_3, f88_1, f88_2, f88_3, f87_1, f87_2, f87_3, f86_1, f86_2, f86_3, f85_1, f85_2, f85_3, f84_1, f84_2, f84_3, f83_1, f83_2, f83_3, f82_1, f82_2, f82_3, f81_1, f81_2, f81_3, f80_1, f79_1, f79_2, f79_3, f78_1, f78_2, f78_3, f77_1, f77_2, f77_3, f76_1, f76_2, f76_3, f75_1, f75_2, f75_3, f74_1, f74_2, f74_3, f73_1, f73_2, f73_3, f72_1, f72_2, f72_3, f71_1, f71_2, f71_3, f70_1, f69_1, f69_2, f69_3, f68_1, f68_2, f68_3, f67_1, f67_2, f67_3, f66_1, f66_2, f66_3, f65_1, f65_2, f65_3, f64_1, f64_2, f64_3, f63_1, f63_2, f63_3, f62_1, f62_2, f62_3, f61_1, f61_2, f61_3, f60_1, f59_1, f59_2, f59_3, f58_1, f58_2, f58_3, f57_1, f57_2, f57_3, f56_1, f56_2, f56_3, f55_1, f55_2, f55_3, f54_1, f54_2, f54_3, f53_1, f53_2, f53_3, f52_1, f52_2, f52_3, f51_1, f51_2, f51_3, f50_1, f49_1, f49_2, f49_3, f48_1, f48_2, f48_3, f47_1, f47_2, f47_3, f46_1, f46_2, f46_3, f45_1, f45_2, f45_3, f44_1, f44_2, f44_3, f43_1, f43_2, f43_3, f42_1, f42_2, f42_3, f41_1, f41_2, f41_3, f40_1, f39_1, f39_2, f39_3, f38_1, f38_2, f38_3, f37_1, f37_2, f37_3, f36_1, f36_2, f36_3, f35_1, f35_2, f35_3, f34_1, f34_2, f34_3, f33_1, f33_2, f33_3, f32_1, f32_2, f32_3, f31_1, f31_2, f31_3, f30_1, f29_1, f29_2, f29_3, f28_1, f28_2, f28_3, f27_1, f27_2, f27_3, f26_1, f26_2, f26_3, f25_1, f25_2, f25_3, f24_1, f24_2, f24_3, f23_1, f23_2, f23_3, f22_1, f22_2, f22_3, f21_1, f21_2, f21_3, f20_1, f19_1, f19_2, f19_3, f18_1, f18_2, f18_3, f17_1, f17_2, f17_3, f16_1, f16_2, f16_3, f15_1, f15_2, f15_3, f14_1, f14_2, f14_3, f13_1, f13_2, f13_3, f12_1, f12_2, f12_3, f11_1, f11_2, f11_3, f10_1, f9_1, f9_2, f9_3, f8_1, f8_2, f8_3, f7_1, f7_2, f7_3, f6_1, f6_2, f6_3, f5_1, f5_2, f5_3, f4_1, f4_2, f4_3, f3_1, f3_2, f3_3, f2_1, f2_2, f2_3, f1_1, f1_2, f1_3, f0_1, fG]:
            if (destination).zoneunlocked == True:
                move_handle(destination)
            elif (destination).zoneunlocked == False:
                Type("The door to this floor is locked!")
                if (destination).zkey in player.inv:
                    Type("You unlocked the door with the key you found!")
                    (player.inv).remove((destination).zkey)
                    (destination).zoneunlocked = True
                    move_handle(destination)
                else:
                    Type("You need the key to open this door...")
                    Prompt()
            else:
                Type("ERROR GAME IS BUGGED")
        else:
            Type("You can't go in that direction!")
            Prompt()

def move_handle(destination):
    Type("Traveling......")
    time.sleep(1)
    os.system('cls')
    player.location = destination
    if destination == f100_1:
        Cutscene()
        if ((player.location).zmobs) != []:
            Type("You have been pulled into battle!")
            Type("Get Ready to Fight!")
            Battle()
    elif destination == f100_3:
        Cutscene()
        if ((player.location).zmobs) != []:
            Type("You have been pulled into battle!")
            Type("Get Ready to Fight!")
            Battle()
    elif destination == f96_2 and 'Adagios Notebook' not in player.curq or destination == f96_2 and 'Adagios Notebook' not in player.compq:
        Cutscene()
        if ((player.location).zmobs) != []:
            Type("You have been pulled into battle!")
            Type("Get Ready to Fight!")
            Battle()
    elif destination == f82_1 and 'Kaintaras Bag' not in player.curq or destination == f82_1 and 'Kaintaras Bag' not in player.compq:
        Cutscene()
        if ((player.location).zmobs) != []:
            Type("You have been pulled into battle!")
            Type("Get Ready to Fight!")
            Battle()
    elif destination == f69_1:
        Type("You have reached the limits of the Demo version. The Game will be completed in ~2 weeks. Thank you for Playing!")
    Type(f"You have moved to {(player.location).zname}.")
    prt_loc()
    return

def prt_loc():
    Type((player.location).zdescript)
    if ((player.location).zmobs) != []:
        Type("You have been pulled into battle!")
        Type("Get Ready to Fight!")
        Battle()
    else:
        return

def player_search():
    Type("Searching...")
    (player.location).zsearched = True
    Type((player.location).zsearch)
    return

def player_use():
    Type("In your Inventory you have:")
    Type(", ".join(player.inv))
    used = input("What item would you like to use? > ")
    if used not in player.inv:
        Type("You don't own that item or it doesn't exist...")
        Type("Check your spelling and for spaces!")
        Prompt()
    elif used == 'Miniscule Exp Orb':
        Type("You have just gained 1 exp!")
        (player.inv).remove(used)
        MaxHp()
        Expmi()
        return
    elif used == 'Tiny Exp Orb':
        Type("You have just gained 5 exp!")
        (player.inv).remove(used)
        MaxHp()
        Expti()
        return
    elif used == 'Medium Exp Orb':
        Type("You have just gained 10 exp!")
        (player.inv).remove(used)
        MaxHp()
        Expme()
        return
    elif used == 'Large Exp Orb':
        Type("You have just gained 20 exp!")
        (player.inv).remove(used)
        MaxHp()
        Expla()
        return
    elif used == 'MASSIVE Exp Orb':
        Type("You have just gained 50 exp!")
        (player.inv).remove(used)
        MaxHp()
        Expma()
        return
    elif used == 'Beyond Holy Exp Orb':
        Type("You have just gained 200 exp!")
        (player.inv).remove(used)
        MaxHp()
        Expbh()
        return
    elif used == 'Miniscule Healing Potion':
        Type("You have just gained 10 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hmi()
        return
    elif used == 'Tiny Healing Potion':
        Type("You have just gained 20 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hti()
        return
    elif used == 'Medium Healing Potion':
        Type("You have just gained 50 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hme()
        return
    elif used == 'Large Healing Potion':
        Type("You have just gained 100 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hla()
        return
    elif used == 'MASSIVE Healing Potion':
        Type("You have just gained 150 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hma()
        return
    elif used == 'Beyond Holy Healing Potion':
        Type("You have just gained 300 hp!")
        (player.inv).remove(used)
        MaxHp()
        Hbh()
        return
    elif used == 'Wallet':
        Type(f"You currently have {player.gold} Gold pieces in your wallet.")
        return
    elif used == 'Orange Chocolate':
        Type(f"You ate Orange Chocolate.")
        Type("You took 10 damage!")
        php = player.hp - 10
        player.hp = php
        if player.hp <= 0:
            Type(f"You have been defeated by Orange Chocolate...")
            Type("You'll get them next time!")
            quit()
        (player.inv).remove('Orange Chocolate')
        return
    elif used == 'Brownie':
        Type(f"You ate Brownie.")
        Type("You gained 20 Health Points!")
        php = player.hp + 20
        player.hp = php
        return
        (player.inv).remove('Brownie')
    elif used == 'Burnt Pizza':
        Type(f"You ate Burnt Pizza.")
        Type("You took 30 damage!")
        php = player.hp - 30
        player.hp = php
        if player.hp <= 0:
            Type(f"You have been defeated by Burnt Pizza...")
            Type("You'll get them next time!")
            quit()
        (player.inv).remove('Burnt Pizza')
        return
    elif used == 'Note1':
        Type(f"[Sone]: {player.name}, I knew that you were going to steal from me yet again...\n[Sone]: I made the small potion but bigger as a thanks.\n[Sone]: It's a new recipe that's why I'm letting you try it.")
        (player.inv).remove('Note1')
        return
    elif used == 'Note2':
        Type(f"[Sone]: Wow, you really are a thief, huh?\n[Sone]: Well, because I am so good at predicting your immoral habits, I have more potions for you.")
        (player.inv).remove('Note2')
        return
    elif used == 'Note3':
        Type(f"[Sone]: Here have some faulty healing potions.\n[Sone]: I think you deserve it, Ltleti hTfie!") #Little Theif
        (player.inv).remove('Note3')
        return
    elif used == 'Note4':
        Type(f"[Sone]: Even if this Room is locked you probably got in here somehow.\n[Sone]: See if you're reading this you broke into my room.")
        Type(f"[Sone]: I don't really mind though as I'm glad you tested some of my new Potions.\n[Sone]: In exchange, you buy from more from me, ok?")
        Type(f"[Tutorial]: Use 'talk' then 'sone' to access the Healing Potion Shop.")
        (player.inv).remove('Note4')
        return
    elif used == 'Bag':
        Type(f"You currently have {player.shard} escape device pieces in your bag.")
        return
    elif used == 'Unsealed Bag':
        Type(f"The bag is filled with what looks like a bunch of shards.")
        return
    else:
        Type("You can't use that item.")
        return

def player_take():
    if (player.location).zsearched == False:
        Type("You haven't found anything to take.\nTry the action 'Search' to look for items.")
        Prompt()
    elif (player.location).zitems == []:
        Type("There is nothing of value to take.")
        Prompt()
    else:
        Type("What item do you want to take? The items in the area are:")
        Type(", ".join((player.location).zitems))
        take = input("> ")
        take2 = [take]
        if take not in (player.location).zitems:
            Type("That item doesn't exist. Check your spelling or any spaces.")
            return
        elif take == 'Gold':
            ((player.location).zitems).remove(take)
            con = random.randint(1,10)
            nah = player.gold + con
            player.gold = nah
            Type(f"You now have {player.gold} Gold pieces.")
            return
        else:
            Type(f"You have obtained {take}")
            count = player.inv + take2
            player.inv = count
            ((player.location).zitems).remove(take)
            return

def player_status():
    Levelsys()
    Levelatk()
    Levelstats()
    Type(f"You are {player.name}")
    Type(f"You currently have {player.hp} health points.")
    Type(f"You are at Level {player.lvl} and need {player.Rexp} exp to level up.")
    Type(f"Your attack is {(player.atk + player.wpatk)}.")
    Type(f"You are currently on {(player.location).zname}.")
    Type(f"Your Inventory:")
    Type(", ".join(player.inv))
    if player.curq != '':
        Type(f"You are currently doing {(player.curq)} Quest.")
    if player.compq != []:
        Type(f"You have completed these Quests:")
        Type(", ".join(player.compq))
    return

def ExpShop():
    Type("[Eleri]: Welcome to my shop!")
    Type("[Eleri]: This is what I have! Tell me what item you would like!")
    if player.lvl == 1:
        Type("Miniscule Exp Orb: 1 Gold")
        Type("Tiny Exp Orb: 2 Gold")
        item = input("[Eleri]: Oh, you want? > ")
        if item not in ['Miniscule Exp Orb','Tiny Exp Orb']:
            Type("[Eleri]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Exp Orb':
            if player.gold < 1:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Miniscule Exp Orb.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Exp Orb':
            if player.gold < 2:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Tiny Exp Orb.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    elif player.lvl == 2 or player.lvl == 3:
        Type("Miniscule Exp Orb: 1 Gold")
        Type("Tiny Exp Orb: 2 Gold")
        Type("Medium Exp Orb: 5 Gold")
        item = input("[Eleri]: Oh, you want? > ")
        if item not in ['Miniscule Exp Orb','Tiny Exp Orb','Medium Exp Orb']:
            Type("[Eleri]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Exp Orb':
            if player.gold < 1:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Miniscule Exp Orb.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Exp Orb':
            if player.gold < 2:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Tiny Exp Orb.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Medium Exp Orb':
            if player.gold < 5:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Medium Exp Orb.")
             hehe = player.gold - 5
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    elif player.lvl == 4 or player.lvl == 5:
        Type("Miniscule Exp Orb: 1 Gold")
        Type("Tiny Exp Orb: 2 Gold")
        Type("Medium Exp Orb: 5 Gold")
        Type("Large Exp Orb: 10 Gold")
        item = input("[Eleri]: Oh, you want? > ")
        if item not in ['Miniscule Exp Orb','Tiny Exp Orb','Medium Exp Orb','Large Exp Orb']:
            Type("[Eleri]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Exp Orb':
            if player.gold < 1:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Miniscule Exp Orb.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Exp Orb':
            if player.gold < 2:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Tiny Exp Orb.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Medium Exp Orb':
            if player.gold < 5:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Medium Exp Orb.")
             hehe = player.gold - 5
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Large Exp Orb':
            if player.gold < 10:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Large Exp Orb.")
             hehe = player.gold - 10
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    elif player.lvl == 6 or player.lvl == 7:
        Type("Miniscule Exp Orb: 1 Gold")
        Type("Tiny Exp Orb: 2 Gold")
        Type("Medium Exp Orb: 5 Gold")
        Type("Large Exp Orb: 10 Gold")
        Type("MASSIVE Exp Orb: 30 Gold")
        item = input("[Eleri]: Oh, you want? > ")
        if item not in ['Miniscule Exp Orb','Tiny Exp Orb','Medium Exp Orb','Large Exp Orb','MASSIVE Exp Orb']:
            Type("[Eleri]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Exp Orb':
            if player.gold < 1:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Miniscule Exp Orb.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Exp Orb':
            if player.gold < 2:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Tiny Exp Orb.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Medium Exp Orb':
            if player.gold < 5:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Medium Exp Orb.")
             hehe = player.gold - 5
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Large Exp Orb':
            if player.gold < 10:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Large Exp Orb.")
             hehe = player.gold - 10
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'MASSIVE Exp Orb':
            if player.gold < 30:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a MASSIVE Exp Orb.")
             hehe = player.gold - 30
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    elif player.lvl >= 8:
        Type("Miniscule Exp Orb: 1 Gold")
        Type("Tiny Exp Orb: 2 Gold")
        Type("Medium Exp Orb: 5 Gold")
        Type("Large Exp Orb: 10 Gold")
        Type("MASSIVE Exp Orb: 30 Gold")
        Type("Beyond Holy Exp Orb: 150 Gold")
        item = input("[Eleri]: Oh, you want? > ")
        if item not in ['Miniscule Exp Orb','Tiny Exp Orb','Medium Exp Orb','Large Exp Orb','MASSIVE Exp Orb','Beyond Holy Exp Orb']:
            Type("[Eleri]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Exp Orb':
            if player.gold < 1:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Miniscule Exp Orb.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Exp Orb':
            if player.gold < 2:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Tiny Exp Orb.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Medium Exp Orb':
            if player.gold < 5:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Medium Exp Orb.")
             hehe = player.gold - 5
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Large Exp Orb':
            if player.gold < 10:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Large Exp Orb.")
             hehe = player.gold - 10
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'MASSIVE Exp Orb':
            if player.gold < 30:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a MASSIVE Exp Orb.")
             hehe = player.gold - 30
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Beyond Holy Exp Orb':
            if player.gold < 150:
                Type("[Eleri]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Eleri]: Come again!")
             Type("You gained a Beyond Holy Exp Orb.")
             hehe = player.gold - 150
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    return

def player_talk():
    if player.location == fT_2:
        Tutorial_Talk()
        return
    elif player.location == f93_3:
        FindBookQ()
        return
    elif player.location == f92_2:
        ClearLabQ()
        return
    elif player.location == f89_3:
        ClearHouseQ()
        return
    elif player.location == f87_1:
        HollysRingQ()
        return
    elif player.location == f86_2:
        TestofWis()
        return
    elif player.location == f85_2:
        TestofStr()
        return
    elif player.curq == 'Robbed!':
        if player.location == f76_3 or f74_3 or f73_3 or f72_2 or f71_2:
            Robbed()
            return
    elif player.location == f72_2:
        StolenG()
        return
    elif player.location == f76_3:
        DeliverPack()
        return
    elif player.location == f74_3:
        WeaponTest()
        return
    elif player.location == f73_3:
        StolenGlass()
        return
    elif player.location == f71_3 and 'DmgGift' not in player.inv:
        DeliverPack()
        return
    if ((player.location).zNPCs) == []:
        Type("There is no-one here to talk to...")

        Type("I guess you can talk to yourself?")
    else:
        ask = input("Who would you like to talk to? > ").lower()
        if ask not in ((player.location).zNPCs):
            Type("This person isn't here or doesn't exist...")
            Type("Check your spelling or for any spaces.")
        elif ask == 'eleri':
            ExpShop()
            return
        elif ask == 'sone':
            HealShop()
            return
        elif ask == 'cyprus':
            WepShop()
            return
        elif ask == 'voice':
            Tutorial_Talk()
            return
        elif ask == 'jin':
            ShardShop()
            return
        elif ask == 'adagio':
            if player.curq == 'Adagios Notebook':
                AdagioTalk1()
            return
        elif ask == 'kaintara':
            if player.curq == 'Kaintaras Bag':
                KaintaraTalk1()
            return
        elif ask == 'nanaka':
            if player.curq == 'Robbed!':
                NanakaTalk1()
            return

def Tutorial_Talk():
    Type("[Tutorial]: Did you know that the action, 'pause' pauses the game!")
    Type("[Tutorial]: You can see a help menu if you forget actions or what they do!")
    Type("[Tutorial]: Bye!")
    Type("(I'll be seeing you soon...)")
    return

def ShardShop():
    if player.curq == 'Collect the Shards!':
        Type("[Jin]: Hey, I heard you were looking for these...")
        Type("[Jin]: Don't worry, I know you need these so I'll give them to you for a very inflated price.")
        Type("[Jin]: There isn't anyone else selling these you know?")
        if player.shard >= 30:
            Type("[Jin]: Sorry, I don't have anything for you... Even if you're my favourite money bag.\nI mean, customer...")
        elif jshard == 0:
            Type("[Jin]: You've bought all of my stock... Unless you want to give me free gold???")
        else:
            Type("[Cyprus]: I can make you a small dagger out of 15 Gold pieces if you want!")
            if player.gold < 25:
                Type("[Jin]: It's shame you don't have enough gold...")
            else:
                Type("[Jin]: Thanks for the Gold, NO REFUNDS!")
                to = jshard - 1
                jshard = to
                hehe = player.shard + 1
                player.shard = hehe
                hehe = player.gold - 25
                player.gold = hehe
                Type("You obtained a Shard.")
                return
    else:
        Type("[Jin]: You wouldn't happen to give some gold would you?")

def WepShop():
    Type("[Cyprus]: Hey, need your weapon sharpened?")
    Type("[Cyprus]: You've come to the right place.")
    if player.lvl == 1:
        Type("[Cyprus]: Sorry, I don't have anything for you...")
    elif player.lvl == 2 or player.lvl == 3:
        Type("[Cyprus]: I can sharpen a blunt pencil for you if you have one. Oh, and gold of course!")
        if 'Blunt Pencil' not in player.inv:
            Type("[Cyprus]: It's a shame you don't have one...")
        elif player.gold < 5:
                Type("[Cyprus]: It's shame you don't have enough gold...")
        else:
             Type("[Cyprus]: Nice pencil, I'll sharpen it right up for you!")
             (player.inv).remove('Blunt Pencil')
             to = ['Sharpened Pencil']
             count = player.inv + to
             player.inv = count
             hehe = player.gold - 5
             player.gold = hehe
             Type("You obtained a Sharpened Pencil.")
             return
    elif player.lvl == 4 or player.lvl == 5:
        Type("[Cyprus]: I can make you a small dagger out of 15 Gold pieces if you want!")
        if player.gold < 15:
            Type("[Cyprus]: It's shame you don't have enough gold...")
        else:
            Type("[Cyprus]: Thanks for the Gold, I'll get right to it!")
            to = ['Small Dagger']
            count = player.inv + to
            player.inv = count
            hehe = player.gold - 15
            player.gold = hehe
            Type("You obtained a Small Dagger.")
            return
    elif player.lvl == 6 or player.lvl == 7:
        Type("[Cyprus]: I can clean up a Rusty Sword for you if you have one. Oh, and gold of course!")
        if 'Rusty Sword' not in player.inv:
                Type("[Cyprus]: It's a shame you don't have one...")
        elif player.gold < 35:
            Type("[Cyprus]: It's shame you don't have enough gold...")
        else:
            Type("[Cyprus]: Nice sword, I'll clean it right up for you!")
            (player.inv).remove('Rusty Sword')
            to = ['Shiny Sword']
            count = player.inv + to
            player.inv = count
            hehe = player.gold - 35
            player.gold = hehe
        Type("You obtained a Shiny Sword.")
        return
    elif player.lvl >= 8:
        Type("[Cyprus]: I can refine a Katana for you if you have one. Oh, and gold of course!")
        if 'Ancient Katana' not in player.inv:
                Type("[Cyprus]: It's a shame you don't have one...")
        elif player.gold < 50:
            Type("[Cyprus]: It's shame you don't have enough gold...")
        else:
            Type("[Cyprus]: Nice sword, I'll clean it right up for you!")
            (player.inv).remove('Ancient Katana')
            to = ['Refined Katana']
            count = player.inv + to
            player.inv = count
            hehe = player.gold - 50
            player.gold = hehe
            Type("You obtained a Refined Katana.")
            return

def HealShop():
    Type("[Sone]: Ooh, Hi! Want to try a potion? You look like you'll need it.")
    Type("[Sone]: These are all my potions! Come on tell me which one you want!")
    if player.lvl == 1:
        Type("Miniscule Healing Potion: 1 Gold")
        Type("Tiny Healing Potion: 2 Gold")
        item = input("[Sone]: Oh, you want? > ")
        if item not in ['Miniscule Healing Potion','Tiny Healing Potion']:
            Type("[Sone]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Healing Potion':
            if player.gold < 1:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Miniscule Healing Potion.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Healing Potion':
            if player.gold < 2:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Tiny Healing Potion.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    elif player.lvl == 2 or player.lvl == 3:
        Type("Miniscule Healing Potion: 1 Gold")
        Type("Tiny Healing Potion: 2 Gold")
        Type("Medium Healing Potion: 5 Gold")
        item = input("[Sone]: Oh, you want? > ")
        if item not in ['Miniscule Healing Potion','Tiny Healing Potion','Medium Healing Potion']:
            Type("[Sone]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Healing Potion':
            if player.gold < 1:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Miniscule Healing Potion.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Healing Potion':
            if player.gold < 2:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Tiny Healing Potion.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Medium Healing Potion':
            if player.gold < 5:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Medium Healing Potion.")
             hehe = player.gold - 5
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    elif player.lvl == 4 or player.lvl == 5:
        Type("Miniscule Healing Potion: 1 Gold")
        Type("Tiny Healing Potion: 2 Gold")
        Type("Medium Healing Potion: 5 Gold")
        Type("Large Healing Potion: 10 Gold")
        item = input("[Sone]: Oh, you want? > ")
        if item not in ['Miniscule Healing Potion','Tiny Healing Potion','Medium Healing Potion','Large Healing Potion']:
            Type("[Sone]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Healing Potion':
            if player.gold < 1:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Miniscule Healing Potion.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Healing Potion':
            if player.gold < 2:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Tiny Healing Potion.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Medium Healing Potion':
            if player.gold < 5:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Medium Healing Potion.")
             hehe = player.gold - 5
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Large Healing Potion':
            if player.gold < 10:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Large Healing Potion.")
             hehe = player.gold - 10
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    elif player.lvl == 6 or player.lvl == 7:
        Type("Miniscule Healing Potion: 1 Gold")
        Type("Tiny Healing Potion: 2 Gold")
        Type("Medium Healing Potion: 5 Gold")
        Type("Large Healing Potion: 10 Gold")
        Type("MASSIVE Healing Potion: 30 Gold")
        item = input("[Sone]: Oh, you want? > ")
        if item not in ['Miniscule Healing Potion','Tiny Healing Potion','Medium Healing Potion','Large Healing Potion','MASSIVE Healing Potion']:
            Type("[Sone]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Healing Potion':
            if player.gold < 1:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Miniscule Healing Potion.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Healing Potion':
            if player.gold < 2:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Tiny Healing Potion.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Medium Healing Potion':
            if player.gold < 5:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Medium Healing Potion.")
             hehe = player.gold - 5
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Large Healing Potion':
            if player.gold < 10:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Large Healing Potion.")
             hehe = player.gold - 10
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'MASSIVE Healing Potion':
            if player.gold < 30:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a MASSIVE Healing Potion.")
             hehe = player.gold - 30
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    elif player.lvl >= 8:
        Type("Miniscule Healing Potion: 1 Gold")
        Type("Tiny Healing Potion: 2 Gold")
        Type("Medium Healing Potion: 5 Gold")
        Type("Large Healing Potion: 10 Gold")
        Type("MASSIVE Healing Potion: 30 Gold")
        Type("Beyond Holy Healing Potion: 150 Gold")
        item = input("[Sone]: Oh, you want? > ")
        if item not in ['Miniscule Healing Potion','Tiny Healing Potion','Medium Healing Potion','Large Healing Potion','MASSIVE Healing Potion','Beyond Holy Healing Potion']:
            Type("[Sone]: Sorry that's not in stock, come back later and I might have it!")
        elif item == 'Miniscule Healing Potion':
            if player.gold < 1:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Miniscule Healing Potion.")
             hehe = player.gold - 1
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Tiny Healing Potion':
            if player.gold < 2:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Tiny Healing Potion.")
             hehe = player.gold - 2
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Medium Healing Potion':
            if player.gold < 5:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Medium Healing Potion.")
             hehe = player.gold - 5
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Large Healing Potion':
            if player.gold < 10:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Large Healing Potion.")
             hehe = player.gold - 10
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'MASSIVE Healing Potion':
            if player.gold < 30:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a MASSIVE Healing Potion.")
             hehe = player.gold - 30
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
        elif item == 'Beyond Holy Healing Potion':
            if player.gold < 150:
                Type("[Sone]: Umm... You can't buy that if you don't have the gold.")
            else:
             Type("[Sone]: Come again!")
             Type("You gained a Beyond Holy Healing Potion.")
             hehe = player.gold - 150
             player.gold = hehe
             item2 = [item]
             count = player.inv + item2
             player.inv = count
    return

def AdagioTalk1():
    if 'Sealed Notebook' in player.inv:
        winsound.PlaySound("Adagio2.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        Type("You gave Adagio the Notebook, and she smiled at you happy that you found it.")
        Type("[Adagio]: So? What's your questions? I'll give you three.")
        Type(f"[{player.name}]: You're only giving me three questions?!?!")
        Type("[Adagio]: Yes. You only have two more questions left now.")
        Type("You just stared at her in disbelief. She just laughed wholeheartedly.")
        Type("[Adagio]: I'm only joking, look at your face!")
        Type(f"[{player.name}]: Ok, first question: What is this place?")
        Type("[Adagio]: The Vampire's Clan Tower.")
        Type(f"[{player.name}]: Ok, second question: How do I get out of here?")
        Type("[Adagio]: You go to the bottom of the tower, simple. It'll take some time to get to the bottom but you'll be fine.")
        Type(f"[{player.name}]: No I meant how do I get back to my world!")
        Type("[Adagio]: Well you should of worded your question better. I can't read your mind. (I'm not that bitch, Meratsu)")
        Type("[Adagio]: Anyway to answer your final question, I have no clue. You'll need to speak to the creator of the tower to find out about that.")
        Type(f"[{player.name}]: Who is that? How can I talk to them???")
        Type("[Adagio]: That was your final question unfortunately, I'll see ya around hopefully! Bye!")
        Type("Quest completed!")
        Type("Rewards are: Floor-90 Key, Ruler, 30 exp, 10 Gold")
        con = 10
        nah = player.gold + con
        player.gold = nah
        take2 = ['Ruler']
        count = player.inv + take2
        player.inv = count
        con = 30
        nah = player.exp + con
        player.exp = nah
        take2 = ['Floor-90 Key']
        count = player.inv + take2
        player.inv = count
        take2 = ['Adagios Notebook']
        count = player.compq + take2
        player.compq = count
        player.curq = ''
        (player.inv).remove('Sealed Notebook')

    else:
        Type("[Adagio]: I think I might of left my notebook on Floor 91 or maybe 92...")

def KaintaraTalk1():
    if 'Unsealed Bag' in player.inv:
        Type("You gave Kaintara her bag, and she smiled at you happy that you found it.")
        Type("[Kaintara]: Thank you! I'm very grateful. I usually hangout around Floor 60 to Floor 40. So meet me around there, ok?")
        Type(f"[{player.name}]: That's so far away?!?!")
        Type("[Kaintara]: Well, unfortunately for you, you are not my only priority. I do have many others I need to do. This tower doesn't run itself.")
        Type("Before you could a say another word. She vanished right infront of you.")
        Type(f"[{player.name}]: Woah! Did she just teleport? Damn- I wish I could that. This would make this whole journey so much easier.")
        Type("Quest completed!")
        Type("Rewards are: Floor-80 Key, 100 exp, 50 Gold, Health Spell (150 hp)")
        con = 50
        nah = player.gold + con
        player.gold = nah
        con = 150
        nah = player.hp + con
        player.hp = nah
        con = 100
        nah = player.exp + con
        player.exp = nah
        take2 = ['Floor-80 Key']
        count = player.inv + take2
        player.inv = count
        take2 = ['Kaintaras Bag']
        count = player.compq + take2
        player.compq = count
        player.curq = ''
        (player.inv).remove('Unsealed Bag')
    else:
        Type("[Kaintara]: I think I misplaced my Bag on Floor 86, 85 or 84...")

def FindBookQ():
    if 'Find Book' in player.compq:
        return
    if player.curq != '' and player.curq != 'Find Book':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    else:
        if player.curq != 'Find Book':
            Type(f"[{player.name}]: Umm, Excuse me? Is it ok if you give me a moment of your time?")
            Type("[Eleri]: Huh? Yeah, of course!")
            Type(f"[{player.name}]: Do you know anything that would be useful about this tower?")
            Type("[Eleri]: Not really! But if you do me a favour quickly I'll give you some Exp Orbs!")
            Type("[Eleri]: They usually help you increase wisdom so hopefully you can work that out yourself!")
            Type("Accept Quest? Type Y or N.")
            inr = input("> ")
            if inr == 'Y':
                Type("[Eleri]: Great! All you have to do is get me my book 'epacsE oN'.")
                Type("[Eleri]: You should have the key to my floor 95, the book is in my libary; room 2.")
                player.curq = 'Find Book'
                f93_3.zsearch = 'You found nothing worth noting.'
                f93_3.zdescript = 'Eleri is awaiting your arrival in this lobby.'
                f95_2.zitems = ['esreveR','eht','sdrow','staht','hsiflE','epacsE oN']
                f95_2.zdescript = 'This room was extremely clean, yet every space was filled with either books or bookselves.\nMost definitely Eleri\'s Libray.'
            else:
                Type("[Eleri]: Oh, ok. I guess you don't want pretty much FREE exp orbs...")
        elif player.curq == 'Find Book':
            if 'epacsE oN' in player.inv:
                Type("[Eleri]: Thank you SO much!!")
                Type("Quest completed!")
                Type("Rewards are: 3 Miniscule Exp Orbs, 2 Gold!")
                Type("[Tutorial]: You befriended Eleri! You can now talk to Eleri whenever using the 'talk' action then enter 'Eleri'")
                take2 = ['eleri']
                count = f93_3.zNPCs + take2
                f93_3.zNPCs = count
                f93_3.zdescript = 'This lobby is now empty TvT'
                con = 2
                nah = player.gold + con
                player.gold = nah
                take2 = ['Miniscule Exp Orb','Miniscule Exp Orb','Miniscule Exp Orb']
                count = player.inv + take2
                player.inv = count
                take2 = ['Find Book']
                count = player.compq + take2
                player.compq = count
                player.curq = ''
                (player.inv).remove('epacsE oN')
            else:
                Type("[Eleri]: I said this already but my book is in my libary, on the 95th floor, room 2.")

def ClearLabQ():
    if 'Clear Lab' in player.compq:
        return
    if player.curq != '' and player.curq != 'Clear Lab':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    else:
        if player.curq != 'Clear Lab':
            winsound.PlaySound("Sone1.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            Type(f"[{player.name}]: Umm, Hi? Could you speak to me for a bit?")
            Type(f"[Sone]: Oh? You're {player.name} that I've heard about... Sure.")
            Type(f"[{player.name}]: Do you know who the creator of this tower is?")
            Type("[Sone]: No but I know the leader. If you do want to know, clear out my lab.")
            Type("[Sone]: I'll let you even take some of my low-priced healing potions you keep stealing.")
            Type("Accept Quest? Type Y or N.")
            inr = input("> ")
            if inr == 'Y':
                winsound.PlaySound("Sone2.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                Type("[Sone]: Nice. All you have to do is kill a few monsters, should be easy.")
                Type("[Sone]: You should have the key to my floor 94, my lab is in room 3. Don't steal anything, ok?")
                player.curq = 'Clear Lab'
                f92_2.zdescript = 'This was the second communal washing room, Sone was in here waiting for you.'
                f94_3.zdescript = 'This is Sone\'s Lab. That makes a lot more sense now.'
                f94_3.zsearch = 'You found a large vial of green liquid, though Sone did say not to take anything...'
                f94_3.zitems = ['Tiny Healing Potion']
                f94_3.zmobs = ['Goblin','Slime','Slime']
            else:
                winsound.PlaySound("Sone3.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                Type("[Sone]: Oh, ok. I guess you are just a selfish thief...")
        elif player.curq == 'Clear Lab':
            if f94_3.zmobs == []:
                winsound.PlaySound("Sone4.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                Type("[Sone]: Oh, you want a thanks? We're not friends...")
                Type("Quest completed!")
                Type("Rewards are: 3 Miniscule Healing Potion, 2 Gold!")
                Type("[Tutorial]: You became aquaintances with Sone!\nYou can now talk to Sone whenever using the 'talk' action then enter 'Sone'")
                take2 = ['sone']
                count = f92_2.zNPCs + take2
                f92_2.zNPCs = count
                f92_2.zdescript = 'This communal washing room is now empty TvT'
                con = 2
                nah = player.gold + con
                player.gold = nah
                take2 = ['Miniscule Healing Potion','Miniscule Healing Potion','Miniscule Healing Potion']
                count = player.inv + take2
                player.inv = count
                take2 = ['Clear Lab']
                count = player.compq + take2
                player.compq = count
                player.curq = ''
            else:
                winsound.PlaySound("Sone4.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
                Type("[Sone]: Why am I repeating myself? You should of recalled my lab is on floor 94, room 3. Do better.")

def HollysRingQ():
    if 'Hollys Ring' in player.compq:
        return
    if player.curq != '' and player.curq != 'Hollys Ring':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    else:
        if player.curq != 'Hollys Ring':
            Type(f"[{player.name}]: Umm, Hi? Is ok if I just walk through your apartment, I promise I won't take anything. (Maybe...)")
            Type("[Holly]: Umm, no. I have half a mind to kick you out, why should I let you waltz through my house?")
            Type(f"[{player.name}]: Well, no-ones had a problem with it before.")
            Type("[Holly]: Have you ever asked anyone? From what I've heard, you've just been walking where-ever you want.")
            Type(f"[{player.name}]: Oh, who told you that? Sone?")
            Type("[Holly]: That is extremely rude! Do you even know who Sone is? Ah that doesn't matter right now...")
            Type("[Holly]: I'll let you walk around my house if you go find something I'd lost, my ring. I'll even give you the key to the next floor.")
            Type("Accept Quest? Type Y or N.")
            inr = input("> ")
            if inr == 'Y':
                Type("[Holly]: Thank you, though really you should be thanking me, (on ges ckiv mnfnia ute hrmo)") # I'm not even asking for much in Spiritian
                Type("[Holly]: Here's the key to Floor 86, I pretty sure I lost my ring between Floor 84 and 86.")
                player.curq = 'Hollys Ring'
                f87_1.zdescript = 'Holly\'s apartment. She is not very happy about you walking around in her house...'
                Type("You have obtained Floor-86 Key.")
                take2 = ['Floor-86 Key']
                count = player.inv + take2
                player.inv = count
            else:
                Type("[Holly]: You do realise I have the key to the next floor. You can't leave unless you agree to find my ring.")
        elif player.curq == 'Hollys Ring':
            if 'Ring' in player.inv:
                Type("[Holly]: Took you long enough.")
                Type("Quest completed!")
                Type("Rewards are: 15 Gold!")
                Type("You are no longer enemies with Holly!")
                f93_3.zdescript = 'Holly has her head engrossed in a book, maybe don\'t bother her?'
                con = 15
                nah = player.gold + con
                player.gold = nah
                take2 = ['Hollys Ring']
                count = player.compq + take2
                player.compq = count
                player.curq = ''
                (player.inv).remove('Ring')
            else:
                Type("[Holly]: Seriously, you forgot? I'm pretty sure my ring is on the 84th Floor, Get to stepping, ok?")

def ClearHouseQ():
    if 'Clear House' in player.compq:
        return
    if player.curq != '' and player.curq != 'Clear House':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    else:
        if player.curq != 'Clear House':
            Type(f"[{player.name}]: Hey, are you okay? You seem quite stressed.")
            Type(f"[Bixby]: Huh? No, I am not okay I just got beat up by low level monsters that are squatting in my new apartment.")
            Type(f"[{player.name}]: Oh, that sounds horrible. That's a bit funny though. LOL.")
            Type(f"[Bixby]: What?!?! How is that funny? Wait. Are you the one who just killed the Goblin King, {player.name}?")
            Type(f"[{player.name}]: Yeah, that's me. Do you want me to clear out your apartment for you?")
            Type(f"[Bixby]: You took the words right out of my mouth!\n[Bixby]: I'll even give you spare healing potions I bought from Sone after getting beat.")
            Type("Accept Quest? Type Y or N.")
            inr = input("> ")
            if inr == 'Y':
                Type("[Bixby]: Thank you so much!!")
                Type("[Bixby]: My apartment is on Floor 88 and Room 3 is locked so you don't need to clear that room.")
                player.curq = 'Clear House'
                f89_3.zdescript = 'The entrance to another apartment complex, Bixby was in here still looking a bit stressed.'
                f88_1.zdescript = 'This is Bixby\'s new apartment, this room was the living room/dining room.'
                f88_1.zsearch = 'You found some Gold and an Exp Orb dropped by the Slime.'
                f88_1.zitems = ['Gold','Miniscule Exp Orb']
                f88_1.zmobs = ['Slime']
                f88_2.zdescript = 'This is Bixby\'s new apartment, this room was the bathroom/laundry room.'
                f88_2.zsearch = 'You found a large vial of green liquid, it seemed Sone didn\'t leave a note this time...'
                f88_2.zitems = ['Tiny Healing Potion']
                f88_2.zmobs = ['Zombie','Slime']
            else:
                Type("[Bixby]: You are SO heartless,(...uoy llik yletinifed lliw ukoruS)")
        elif player.curq == 'Clear House':
            if f88_1.zmobs == [] and f88_2.zmobs == [] :
                Type("[Bixby]: You are a complete LIVESAVER!")
                Type("Quest completed!")
                Type("Rewards are: 2 Tiny Healing Potion, 5 Gold!")
                Type("You have befriended Bixby!")
                f89_3.zdescript = 'The entrance to another apartment complex.'
                con = 5
                nah = player.gold + con
                player.gold = nah
                take2 = ['Tiny Healing Potion','Tiny Healing Potion']
                count = player.inv + take2
                player.inv = count
                take2 = ['Clear House']
                count = player.compq + take2
                player.compq = count
                player.curq = ''
            else:
                Type("[Bixby]: Umm, there are still monsters in my apartment.\n[Bixby]: Do you want to see me get beat up or something?")

def TestofWis():
    if 'TestofWis' in player.compq:
        return
    if player.curq != '' and player.curq != 'TestofWis':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    else:
        if player.curq != 'TestofWis':
            Type(f"[{player.name}]: Umm, Excuse me? Is it ok if I just walk through your apartment? I promise I won't take anything.")
            Type(f"[Eli]: Huh? Oh are you the new arrival to the tower? Umm, {player.name}?")
            Type(f"[{player.name}]: Yeah that's me. Does that mean it's okay?")
            Type("[Eli]: Of course! I don't belive you have any malicious intentions. However if you solve a riddle I'll give you three Exp Orbs!")
            Type("[Eli]: These are high quality ones I use myself sometimes so it is very much worth it.")
            Type("Accept Quest? Type Y or N.")
            inr = input("> ")
            if inr == 'Y':
                Type(f"[Eli]: You are very interesting {player.name}, hopefully you are as intelligent as you are intriguing.")
                Type("[Eli]: The riddle is quite simple and refers to a room you have already come across.")
                Type("[Riddle]: I am everywhere and nowhere.")
                Type("[Riddle]: You can see me wherever you look.")
                Type("[Riddle]: I am both in the sky and on the ground.")
                Type("[Riddle]: I have no mass or elemental structure.")
                Type("[Riddle]: What Am I?")
                Type("[Eli]: The Room I am refering to is full of this. Good Luck!")
                Type("[Tutorial]: To solve the puzzle use the 'solve' action when you belive you are in the correct room.")
                player.curq = 'TestofWis'
                f86_2.zdescript = 'Eli\'s apartment, he did not seem to mind at all if you walked around.'
                f86_1.zdescript = 'Eli\'s apartment, he did not seem to mind at all if you walked around.'
            else:
                Type("[Eli]: That's a shame, I thought you were interested... You're welcome to come back!")
        elif player.curq == 'TestofWis':
            if 'Solved1!' in player.inv:
                Type("[Eli]: Well Done for completing that riddle!")
                Type("Quest completed!")
                Type("Rewards are: 3 Medium Exp Orbs, 10 Gold!")
                Type("You befriended Eli!")
                con = 10
                nah = player.gold + con
                player.gold = nah
                take2 = ['Medium Exp Orb','Medium Exp Orb','Medium Exp Orb']
                count = player.inv + take2
                player.inv = count
                take2 = ['TestofWis']
                count = player.compq + take2
                player.compq = count
                player.curq = ''
                (player.inv).remove('Solved1!')
            else:
                Type("[Eli]: Here's a hint, the room is between Floor 89 and 87. I am confident you can solve this riddle!")
                Type("[Tutorial]: To solve the puzzle use the 'solve' action when you belive you are in the correct room.")

def TestofStr():
    if 'TestofStr' in player.compq:
        return
    if player.curq != '' and player.curq != 'TestofStr':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    else:
        if player.curq != 'TestofStr':
            Type(f"[{player.name}]: Woah, you are really good with that sword! Do you have any spare?")
            Type(f"[Yonaite]: What? Ah, hi! Thank you, I do actually have a spare sword but you have to prove you can use it first.")
            Type(f"[{player.name}]: Well, I defeated the Goblin King with a Ruler if that means anything?")
            Type(f"[Yonaite]: You're the one who killed him? Well done! You must be very strong then, however I can't just give you a sword for that feat alone.")
            Type(f"[{player.name}]: What?!? Why not? You got my hopes up...")
            Type(f"[Yonaite]: I'll give you a better weapon with more potential then a ruler\n[Yonaite]: All you have to do is defeat two Zombies and three Slimes, they're pretty easy to kill.")
            Type("Accept Quest? Type Y or N.")
            inr = input("> ")
            if inr == 'Y':
                Type("[Yonaite]: I'll summon some monsters to this Floor and Floor 83.")
                Type("[Yonaite]: These are basic monsters so this test should be a piece of cake.")
                player.curq = 'TestofStr'
                f85_2.zdescript = 'Yonaite\'s Training room, she was working very hard on her swordmanship. It looked so cool!'
                f85_2.zsearch = 'You couldn\'t search very much without alerting the person in the room. Maybe you should talk to them?'
                f85_1.zdescript = 'This was Yonaite\'s gym, it seemed like the monsters she summoned are here.'
                f85_1.zsearch = 'You found some Healing Potions dropped by the Zombies.'
                f85_1.zitems = ['Tiny Healing Potion','Miniscule Healing Potion']
                f85_1.zmobs = ['Zombie','Zombie']
                f83_2.zdescript = 'This was Yonaite\'s walk-in wardrobe, it seemed like the monsters she summoned are here.'
                f83_2.zsearch = 'You found some green vials dropped by the Slimes.'
                f83_2.zitems = ['Tiny Healing Potion','Miniscule Healing Potion']
                f83_2.zmobs = ['Slime','Slime','Slime']
            else:
                Type("[Yonaite]: Are you really too weak to defeat five basic monsters? I think I overestimated you... How unfortunate.")
        elif player.curq == 'TestofStr':
            if f85_1.zmobs == [] and f83_2.zmobs == [] :
                Type("[Yonaite]: Wow, you look extremely tired. I don't think you are fit to carry a sword or even a dagger just yet.")
                Type("Quest completed!")
                Type("Rewards are: Blunt Pencil, 2 Tiny Healing Potion!")
                Type("You have befriended Yonaite!")
                f85_2.zdescript = 'Yonaite\'s Training room, Yonaite was somewhere else now though.'
                f85_2.zsearch = 'You found one of Yonaite\'s spare swords. It looked cool but you won\'t be able to use it.'
                take2 = ['Tiny Healing Potion','Tiny Healing Potion','Blunt Pencil']
                count = player.inv + take2
                player.inv = count
                take2 = ['TestofStr']
                count = player.compq + take2
                player.compq = count
                player.curq = ''
            else:
                Type("[Yonaite]: You haven't passed my test just yet. Check this Floor and Floor 83.\n[Yonaite]: You're not trying to trick me, right? I was the one who summoned the monsters, silly.")

def Robbed():
    if 'Robbed!' in player.compq:
        return
    if player.curq != '' and player.curq != 'Robbed!':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    if player.curq == 'Robbed' and player.location == f76_3:
        Type(f"[{player.name}]: Hi... You wouldn't have seen a short, hooded figure run pass here have you?")
        Type("[Minx]: Huh? Oh, no darling. Though I have heard the robberies in on these floors are have become very common.")
        Type(f"[{player.name}]: (Well, that would've been helpful to know BEFORE I came here huh.)")
        Type(f"[{player.name}]: Have you at least heard of 'Mochaii' coming through here?")
        Type("[Minx]: Nope, sorry I couldn't be very helpful darling. My Taylor is currently going towards Floor 71, Room 3. Maybe she'll be more helpful?")
        Type(f"[{player.name}]: Oh, ok. Thanks anyway.")
        f76_3.zdescript = 'Minx was here and she seemed to be wrapping a present... Maybe you should ask about it?'
    elif player.curq == 'Robbed' and player.location == f74_3:
        Type(f"[{player.name}]: Hey, have seen a short, hooded figure run pass here?")
        Type("[Cyprus]: Oh! Yeah, I have luckily for you. I think... They ran closer to Floor 72!")
        Type(f"[{player.name}]: Thanks! That was extremely helpful.")
        Type(f"[{player.name}]: I have another question for you though. Have you heard of 'Mochaii' coming through here?")
        Type("[Cyprus]: No, but I do know her. I mean we're no where near close but she promised she would sort out this thief problem.\n[Cyprus]: Oh sorry, that's probably too much information.")
        Type(f"[{player.name}]: I don't mind, thanks for your help!")
        f74_3.zdescript = 'Cyprus was here and she seemed to be making a weapon. Maybe you should ask about it?'
    elif player.curq == 'Robbed' and player.location == f73_3:
        Type(f"[{player.name}]: Hello, have you seen anyone suspicious running through here?")
        Type("[Saide]: Sorry, I haven't. My sight isn't very good in the first place, I might have just missed them.")
        Type(f"[{player.name}]: Oh, ok.")
        Type(f"[{player.name}]: Before I go, have you heard of 'Mochaii' coming through here?")
        Type("[Saide]: Lord Mochaii?!? It would be an honour for her to come up here, she usually hangs around Floor 10 I believe.")
        Type(f"[{player.name}]: (Floor 10! I'm not going to find her if she's all the way down there)")
        Type(f"[{player.name}]: Thanks for your help!")
        f73_3.zdescript = 'Saide was here and she was crying. You should help her.'
    elif player.curq == 'Robbed' and player.location == f72_2:
        Type(f"[{player.name}]: Hi... You wouldn't have seen a short, hooded figure run pass here have you?")
        Type("[Amir]: Huh? No. Sorry. Most people have left Floor 80 to 70 because of the robberies. How do I know you're not part those crimes?")
        Type(f"[{player.name}]: That's a bit rude. I'm just trying to find someone who mugged me. It doesn't seem as though this tower has any policing.")
        Type("[Amir]: If there was I wouldn't know, I'm just wandering through here. Now leave me alone, ok? ")
        Type(f"[{player.name}]: Ok... (Geez, I just asked a simple question.) Actually I need to ask one more.")
        Type("[Amir]: Do you not understand what leave me alone means?")
        Type(f"[{player.name}]: (Sorry Nanaka, but I'm not getting anything else out of him.)")
        f72_2.zdescript = 'Amir was here and he looked extremely stressed. You should help him.'
    elif player.curq == 'Robbed' and player.location == f71_2:
        Type(f"You entered the room, not expecting to find the thief here in a large room which looks extremely small due to all the stolen things within it.")
        Type(f"You equipped your {wpofc}, readying for an attack. You could see them counting gold, all of it no doubt stolen.")
        Type(f"They didn't notice you at all, too engrossed in your gold.")
        Type(f"[{player.name}]: Don't move. Hand me back my wallet. Now.")
        Type("[Jin]: Shit- You weren't supposed to to find this room. Mr Batsubami was going to take care you. How are you even here?")
        Type(f"[{player.name}]: Who is Batsubami? And don't even think about running my {wpofc} doesn't look very threatening but it's killed countless monsters.")
        Type("Jin started to visably sweat drop, he tried to speak but when he opened his mouth no words came out.")
        Type(f"[{player.name}]: Either answer my question or hand me back my wallet. Quickly.")
        Type("He did just that placing all the gold into your wallet and handing it straight to you. He even put more gold then you already had in there.")
        Type(f"[{player.name}]: Now answer my question.")
        Type("You said as you placed the wallet back in your pocket.")
        Type("[Jin]: He's the Leader of the Werewolf Clan: Nanaka Batsubami. Lord Mochaii must've not told him to kill you yet.")
        Type(f"[{player.name}]: That's why he was looking for her... If what you're saying is true that is...")
        Type("[Jin]: I swear I'm not lying! I couldn't disobey a direct order from Lord Mochaii, plus all the gold I got made it completely worth it.")
        Type(f"[{player.name}]: Really? Well, if I found out you're lying I'll make sure my {wpofc} ends up in both your eyes.")
        Type("You threatened though Jin did not flinch.")
        Type(f"[{player.name}]: (He's probably telling the truth.).")
        Type("Quest completed!")
        Type("Rewards are: Floor-70 Key, Wallet, 300 exp, 30 Gold")
        con = 30
        nah = player.gold + con + Tempwal
        player.gold = nah
        take2 = ['Wallet']
        count = player.inv + take2
        player.inv = count
        con = 300
        nah = player.exp + con
        player.exp = nah
        take2 = ['Floor-70 Key']
        count = player.inv + take2
        player.inv = count
        take2 = ['Robbed!']
        count = player.compq + take2
        player.compq = count
        player.curq = ''

def StolenG():
    if 'Stolen Gold' in player.compq:
        return
    if player.curq != '' and player.curq != 'Stolen Gold':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    else:
        if player.curq != 'Stolen Gold':
            Type(f"[{player.name}]: Err, Hi... I know you said to leave you alone but I couldn't help but notice how stressed you look.")
            Type("[Amir]: I'm fine. It's a problem I should fix myself.")
            Type(f"[{player.name}]: Are you sure? I'm offering you help here. What's the problem?")
            Type("[Amir]: You're so nosy aren't you? But I guess there isn't anyone better to ask then you.\n[Amir]: I'm assuming you got your stuff back from that thief?")
            Type(f"[{player.name}]: Yep! He was pretty weak and didn't really want to rob me anyway.")
            Type("[Amir]: Well, I got mugged just like you. But by a slime... I know it's embarrassing. I just have a fear of those weird gooey creatures.")
            Type("[Amir]: I just dropped my Gold and ran. I think this happened on Floor 77. Can you get my Gold for me please?")
            Type("Accept Quest? Type Y or N.")
            inr = input("> ")
            if inr == 'Y':
                Type("[Amir]: I think it happened on Floor 77, I can't remember the room though.")
                player.curq = 'Stolen Gold'
                f72_2.zdescript = 'Amir looked a lot less stressed out and was waiting for you return.'
                f77_2.zdescript = 'It looks like this is the room Amir dropped his Gold. He failed to mention the fact there wasn\'t only a Slime here.'
                f77_2.zsearch = 'You found his pouch with Gold within it.'
                f77_2.zitems = ['Amirs Gold']
                f77_2.zmobs = ['Slime','Wolf']
            else:
                Type("[Amir]: I just told you that embarrassing secret and you still won't help me? Look I'll give some of the Gold for your troubles, ok?\nPLEASE, don't tell anyone about this.")
        elif player.curq == 'Stolen Gold':
            if 'Amirs Gold' in player.inv:
                Type("[Amir]: Thank you, I appreciate this so much.")
                Type("[Amir]: I guess I should apologize for being short with you.")
                Type("Quest completed!")
                Type("Rewards are: 15 Gold and 50 Exp.")
                Type("You are no longer enemies with Amir!")
                f72_2.zdescript = 'This room is empty like majority of the rooms on this Floor.'
                con = 50
                nah = player.exp + con
                player.exp = nah
                con = 15
                nah = player.gold + con
                player.gold = nah
                take2 = ['Stolen Gold']
                count = player.compq + take2
                player.compq = count
                player.curq = ''
                (player.inv).remove('Amirs Gold')
            else:
                Type("[Amir]: I'm pretty sure the Slime was on Floor 77 maybe Room 2?")

def DeliverPack():
    if 'Deliver Package' in player.compq:
        return
    if player.curq != '' and player.curq != 'Deliver Package':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    else:
        if player.curq != 'Deliver Package':
            Type(f"[{player.name}]: Hey! Whatcha doing?")
            Type(f"[Minx]: Oh hey darling! I'm just wrapping a present for my friend Taylor!\n[Minx]: She's been ignoring me so I thought I would get her a present to cheer her up!")
            Type(f"[{player.name}]: That sounds like a good idea but shouldn't you find out why she's ignoring you?")
            Type("[Minx]: Well, I can't really if she won't talk to me.")
            Type(f"[{player.name}]: Damn- That's a real shame.")
            Type("[Minx]: You know what! You could give this to her for me! She'll probably be more tempted to accept it.")
            Type("Accept Quest? Type Y or N.")
            inr = input("> ")
            if inr == 'Y':
                Type("[Minx]: You will! Great, here's the package! She should definitely be at Floor 71, Room 3 now.")
                player.curq = 'Deliver Package'
                f76_3.zdescript = 'Minx looked very happy thinking it would be Taylor coming to see her, but it was you with the remains of the package...'
                Type("You have obtained Taylor's Gift.")
                take2 = ['TGift']
                count = player.inv + take2
                player.inv = count
            else:
                Type("[Minx]: Oh, That's okay! You're probably busy right? You can back later I guess.")
        elif player.curq == 'Hollys Ring':
            if 'TGift' in player.inv:
                Type(f"[{player.name}]: Hi! Are you Taylor?")
                Type("[Taylor]: Yeah, who are you?")
                Type(f"[{player.name}]: I'm {player.name}, I have a present for you. Here!")
                Type("[Taylor]: Weird... I don't know you why are you giving me a random present?")
                Type("[Taylor]: Ugh. Let me guess its that annoyance, Minx trying to get on my good side again isn't it?")
                Type(f"[{player.name}]: She's so nice! Minx went out of her way to make you a present. The least you can do is appreciate it.")
                Type("[Taylor]: You don't know her like I do.")
                Type("[Taylor]: Here give this back to her.")
                Type("You obtained Damaged Gift.")
                take2 = ['DmgGift']
                count = player.inv + take2
                player.inv = count
                Type("You became enemies with Taylor.")
                Type("[Taylor]: Bye, Weirdo.")
                f71_3.zdescript = 'This room is empty like majority of the rooms on this Floor.'
                (player.inv).remove('TGift')
            elif 'DmgGift' in player.inv:
                Type("[Minx]: She destoryed it, huh.")
                Type("[Minx]: I guess I'll have to come up with something else. Thanks darling!")
                Type("Quest completed!")
                Type("Rewards are: 30 Gold and 100 Exp!")
                Type("You befriended Minx!")
                f76_3.zdescript = 'This room is empty like majority of the rooms on this Floor.'
                con = 100
                nah = player.exp + con
                player.exp = nah
                con = 30
                nah = player.gold + con
                player.gold = nah
                take2 = ['Deliver Package']
                count = player.compq + take2
                player.compq = count
                player.curq = ''
                (player.inv).remove('DmgGift')

def WeaponTest():
    if 'Weapon Test' in player.compq:
        return
    if player.curq != '' and player.curq != 'Weapon Test':
        Type(f"[{player.name}]: I should probably finsh {player.curq} Quest first.")
    else:
        if player.curq != 'Weapon Test':
            Type(f"[{player.name}]: Hey! Whatcha doing, it looks cool!")
            Type(f"[Cyprus]: What? Ah, hi! Thank you, I'm actually a blacksmith so I make weapons swords and such.")
            Type(f"[{player.name}]: Amazing! Could you make me a sword?")
            Type(f"[Cyprus]: Not at the moment, I'm working on extension which would make a Ruler a very dangerous weapon. Funny, right?")
            Type(f"[{player.name}]: Yeah, could I try the extension? I have a Ruler which I use a lot to fight.")
            Type(f"[Cyprus]: You use a Ruler as a weapon? Wow. You must be very strong, of course you try it out!")
            Type("Accept Quest? Type Y or N.")
            inr = input("> ")
            if inr == 'Y':
                Type("[Cyprus]: There should be monsters on Floor 76 to 74.")
                player.curq = 'Weapon Test'
                f74_3.zdescript = 'Cyprus was working on another project whilst she waited for you.'
                Wp02.name = 'RulerEx'
                Wp02.atk = 6
                Wp02.ob = ['RulerEx']
                Type("You have obtained Ruler Extension.")
                take2 = ['RulerEx']
                count = player.inv + take2
                player.inv = count
                (player.inv).remove('Ruler')
                f74_2.zdescript = 'The room had two monsters, perfect for testing your new extension.'
                f74_2.zsearch = 'You found nothing of use.'
                f74_2.zmobs = ['Wolf','Slime']
                f75_1.zdescript = 'The room had two monsters, perfect for testing your new extension.'
                f75_1.zsearch = 'You found nothing of use.'
                f75_1.zmobs = ['Zombie','Slime']
                f76_1.zdescript = 'The room had two monsters, perfect for testing your new extension.'
                f76_1.zsearch = 'You found nothing of use.'
                f76_1.zmobs = ['Wolf','Zombie']
            else:
                Type(f"[{player.name}]: I'll come back later!")
        elif player.curq == 'Weapon Test':
            if f75_1.zmobs == [] and f76_1.zmobs == [] and f74_2.zmobs == [] :
                Type("[Cyprus]: Well, you're still alive so it must of worked well! Give me the extension back, please.")
                Type("Quest completed!")
                Type("Rewards are: Access to the Weapons Shop, 2 Tiny Healing Potion!")
                Type("You have befriended Cyprus and unlocked the Weapons Shop!")
                f74_3.zdescript = 'Cyprus left a note in this empty room. (Use search to read it.)'
                f74_3.zsearch = '"I\'ve left for the Hotel on Floor 69 to Floor 40. You should be able to find one of shops there."'
                take2 = ['Tiny Healing Potion','Tiny Healing Potion','Ruler']
                count = player.inv + take2
                player.inv = count
                take2 = ['Weapon Test']
                count = player.compq + take2
                player.compq = count
                player.curq = ''
                (player.inv).remove('RulerEx')
            else:
                Type("[Cyprus]: You haven't tested out in all the rooms just yet. Check this Floor 74, 75 and 76. I believe in you!")

def StolenGlass():
    pass

def QuinnsRid():
    pass

def ClearStore():
    pass

def TestofWis2():
    pass

def TestofStr2():
    pass

def Bathwater():
    pass

def HairStrands():
    pass

def StealG():
    pass

def UltiQ():
    pass

def UltiQ2():
    pass

def TestofWis3():
    pass

def TestofStr3():
    pass

def player_info():
    Save()
    return

def Teleport():
    ruh = input("Enter Location > ")
    uh = {}
    if ruh == 'f100_1':
        uh = f100_1
    elif ruh == 'f100_2':
        uh = f100_2
    elif ruh == 'f100_3':
        uh = f100_3
    elif ruh == 'f99_1':
        uh = f99_1
    elif ruh == 'f99_2':
        uh = f99_2
    elif ruh == 'f99_3':
        uh = f99_3
    elif ruh == 'f98_1':
        uh = f98_1
    elif ruh == 'f98_2':
        uh = f98_2
    elif ruh == 'f98_3':
        uh = f98_3
    elif ruh == 'f97_1':
        uh = f97_1
    elif ruh == 'f97_2':
        uh = f97_2
    elif ruh == 'f97_3':
        uh = f97_3
    elif ruh == 'f96_1':
        uh = f96_1
    elif ruh == 'f96_2':
        uh = f96_2
    elif ruh == 'f96_3':
        uh = f96_3
    elif ruh == 'f95_1':
        uh = f95_1
    elif ruh == 'f95_2':
        uh = f95_2
    elif ruh == 'f95_3':
        uh = f95_3
    elif ruh == 'f94_1':
        uh = f94_1
    elif ruh == 'f94_2':
        uh = f94_2
    elif ruh == 'f94_3':
        uh = f94_3
    elif ruh == 'f93_1':
        uh = f93_1
    elif ruh == 'f93_2':
        uh = f93_2
    elif ruh == 'f93_3':
        uh = f93_3
    elif ruh == 'f92_1':
        uh = f92_1
    elif ruh == 'f92_2':
        uh = f92_2
    elif ruh == 'f92_3':
        uh = f92_3
    elif ruh == 'f91_1':
        uh = f91_1
    elif ruh == 'f91_2':
        uh = f91_2
    elif ruh == 'f91_3':
        uh = f91_3
    elif ruh == 'f90_1':
        uh = f90_1
    elif ruh == 'f89_1':
        uh = f89_1
    elif ruh == 'f89_2':
        uh = f89_2
    elif ruh == 'f89_3':
        uh = f89_3
    elif ruh == 'f88_1':
        uh = f88_1
    elif ruh == 'f88_2':
        uh = f88_2
    elif ruh == 'f88_3':
        uh = f88_3
    elif ruh == 'f87_1':
        uh = f87_1
    elif ruh == 'f87_2':
        uh = f87_2
    elif ruh == 'f87_3':
        uh = f87_3
    elif ruh == 'f86_1':
        uh = f86_1
    elif ruh == 'f86_2':
        uh = f86_2
    elif ruh == 'f86_3':
        uh = f86_3
    elif ruh == 'f85_1':
        uh = f85_1
    elif ruh == 'f85_2':
        uh = f85_2
    elif ruh == 'f85_3':
        uh = f85_3
    elif ruh == 'f84_1':
        uh = f84_1
    elif ruh == 'f84_2':
        uh = f84_2
    elif ruh == 'f84_3':
        uh = f84_3
    elif ruh == 'f83_1':
        uh = f83_1
    elif ruh == 'f83_2':
        uh = f83_2
    elif ruh == 'f83_3':
        uh = f83_3
    elif ruh == 'f82_1':
        uh = f82_1
    elif ruh == 'f82_2':
        uh = f82_2
    elif ruh == 'f82_3':
        uh = f82_3
    elif ruh == 'f81_1':
        uh = f81_1
    elif ruh == 'f81_2':
        uh = f81_2
    elif ruh == 'f81_3':
        uh = f81_3
    elif ruh == 'f80_1':
        uh = f80_1
    elif ruh == 'f79_1':
        uh = f79_1
    elif ruh == 'f79_2':
        uh = f79_2
    elif ruh == 'f79_3':
        uh = f79_3
    elif ruh == 'f78_1':
        uh = f78_1
    elif ruh == 'f78_2':
        uh = f78_2
    elif ruh == 'f78_3':
        uh = f78_3
    elif ruh == 'f77_1':
        uh = f77_1
    elif ruh == 'f77_2':
        uh = f77_2
    elif ruh == 'f77_3':
        uh = f77_3
    elif ruh == 'f76_1':
        uh = f76_1
    elif ruh == 'f76_2':
        uh = f76_2
    elif ruh == 'f76_3':
        uh = f76_3
    elif ruh == 'f75_1':
        uh = f75_1
    elif ruh == 'f75_2':
        uh = f75_2
    elif ruh == 'f75_3':
        uh = f75_3
    elif ruh == 'f74_1':
        uh = f74_1
    elif ruh == 'f74_2':
        uh = f74_2
    elif ruh == 'f74_3':
        uh = f74_3
    elif ruh == 'f73_1':
        uh = f73_1
    elif ruh == 'f73_2':
        uh = f73_2
    elif ruh == 'f73_3':
        uh = f73_3
    elif ruh == 'f72_1':
        uh = f72_1
    elif ruh == 'f72_2':
        uh = f72_2
    elif ruh == 'f72_3':
        uh = f72_3
    elif ruh == 'f71_1':
        uh = f71_1
    elif ruh == 'f71_2':
        uh = f71_2
    elif ruh == 'f71_3':
        uh = f71_3
    elif ruh == 'f70_1':
        uh = f70_1
    elif ruh == 'f69_1':
        uh = f69_1
    elif ruh == 'f69_2':
        uh = f69_2
    elif ruh == 'f69_3':
        uh = f69_3
    elif ruh == 'f68_1':
        uh = f68_1
    elif ruh == 'f68_2':
        uh = f68_2
    elif ruh == 'f68_3':
        uh = f68_3
    elif ruh == 'f67_1':
        uh = f67_1
    elif ruh == 'f67_2':
        uh = f67_2
    elif ruh == 'f67_3':
        uh = f67_3
    elif ruh == 'f66_1':
        uh = f66_1
    elif ruh == 'f66_2':
        uh = f66_2
    elif ruh == 'f66_3':
        uh = f66_3
    elif ruh == 'f65_1':
        uh = f65_1
    elif ruh == 'f65_2':
        uh = f65_2
    elif ruh == 'f65_3':
        uh = f65_3
    elif ruh == 'f64_1':
        uh = f64_1
    elif ruh == 'f64_2':
        uh = f64_2
    elif ruh == 'f64_3':
        uh = f64_3
    elif ruh == 'f63_1':
        uh = f63_1
    elif ruh == 'f63_2':
        uh = f63_2
    elif ruh == 'f63_3':
        uh = f63_3
    elif ruh == 'f62_1':
        uh = f62_1
    elif ruh == 'f62_2':
        uh = f62_2
    elif ruh == 'f62_3':
        uh = f62_3
    elif ruh == 'f61_1':
        uh = f61_1
    elif ruh == 'f61_2':
        uh = f61_2
    elif ruh == 'f61_3':
        uh = f61_3
    elif ruh == 'f60_1':
        uh = f60_1
    elif ruh == 'f59_1':
        uh = f59_1
    elif ruh == 'f59_2':
        uh = f59_2
    elif ruh == 'f59_3':
        uh = f59_3
    elif ruh == 'f58_1':
        uh = f58_1
    elif ruh == 'f58_2':
        uh = f58_2
    elif ruh == 'f58_3':
        uh = f58_3
    elif ruh == 'f57_1':
        uh = f57_1
    elif ruh == 'f57_2':
        uh = f57_2
    elif ruh == 'f57_3':
        uh = f57_3
    elif ruh == 'f56_1':
        uh = f56_1
    elif ruh == 'f56_2':
        uh = f56_2
    elif ruh == 'f56_3':
        uh = f56_3
    elif ruh == 'f55_1':
        uh = f55_1
    elif ruh == 'f55_2':
        uh = f55_2
    elif ruh == 'f55_3':
        uh = f55_3
    elif ruh == 'f54_1':
        uh = f54_1
    elif ruh == 'f54_2':
        uh = f54_2
    elif ruh == 'f54_3':
        uh = f54_3
    elif ruh == 'f53_1':
        uh = f53_1
    elif ruh == 'f53_2':
        uh = f53_2
    elif ruh == 'f53_3':
        uh = f53_3
    elif ruh == 'f52_1':
        uh = f52_1
    elif ruh == 'f52_2':
        uh = f52_2
    elif ruh == 'f52_3':
        uh = f52_3
    elif ruh == 'f51_1':
        uh = f51_1
    elif ruh == 'f51_2':
        uh = f51_2
    elif ruh == 'f51_3':
        uh = f51_3
    elif ruh == 'f50_1':
        uh = f50_1
    elif ruh == 'f49_1':
        uh = f49_1
    elif ruh == 'f49_2':
        uh = f49_2
    elif ruh == 'f49_3':
        uh = f49_3
    elif ruh == 'f48_1':
        uh = f48_1
    elif ruh == 'f48_2':
        uh = f48_2
    elif ruh == 'f48_3':
        uh = f48_3
    elif ruh == 'f47_1':
        uh = f47_1
    elif ruh == 'f47_2':
        uh = f47_2
    elif ruh == 'f47_3':
        uh = f47_3
    elif ruh == 'f46_1':
        uh = f46_1
    elif ruh == 'f46_2':
        uh = f46_2
    elif ruh == 'f46_3':
        uh = f46_3
    elif ruh == 'f45_1':
        uh = f45_1
    elif ruh == 'f45_2':
        uh = f45_2
    elif ruh == 'f45_3':
        uh = f45_3
    elif ruh == 'f44_1':
        uh = f44_1
    elif ruh == 'f44_2':
        uh = f44_2
    elif ruh == 'f44_3':
        uh = f44_3
    elif ruh == 'f43_1':
        uh = f43_1
    elif ruh == 'f43_2':
        uh = f43_2
    elif ruh == 'f43_3':
        uh = f43_3
    elif ruh == 'f42_1':
        uh = f42_1
    elif ruh == 'f42_2':
        uh = f42_2
    elif ruh == 'f42_3':
        uh = f42_3
    elif ruh == 'f41_1':
        uh = f41_1
    elif ruh == 'f41_2':
        uh = f41_2
    elif ruh == 'f41_3':
        uh = f41_3
    elif ruh == 'f40_1':
        uh = f40_1
    elif ruh == 'f39_1':
        uh = f39_1
    elif ruh == 'f39_2':
        uh = f39_2
    elif ruh == 'f39_3':
        uh = f39_3
    elif ruh == 'f38_1':
        uh = f38_1
    elif ruh == 'f38_2':
        uh = f38_2
    elif ruh == 'f38_3':
        uh = f38_3
    elif ruh == 'f37_1':
        uh = f37_1
    elif ruh == 'f37_2':
        uh = f37_2
    elif ruh == 'f37_3':
        uh = f37_3
    elif ruh == 'f36_1':
        uh = f36_1
    elif ruh == 'f36_2':
        uh = f36_2
    elif ruh == 'f36_3':
        uh = f36_3
    elif ruh == 'f35_1':
        uh = f35_1
    elif ruh == 'f35_2':
        uh = f35_2
    elif ruh == 'f35_3':
        uh = f35_3
    elif ruh == 'f34_1':
        uh = f34_1
    elif ruh == 'f34_2':
        uh = f34_2
    elif ruh == 'f34_3':
        uh = f34_3
    elif ruh == 'f33_1':
        uh = f33_1
    elif ruh == 'f33_2':
        uh = f33_2
    elif ruh == 'f33_3':
        uh = f33_3
    elif ruh == 'f32_1':
        uh = f32_1
    elif ruh == 'f32_2':
        uh = f32_2
    elif ruh == 'f32_3':
        uh = f32_3
    elif ruh == 'f31_1':
        uh = f31_1
    elif ruh == 'f31_2':
        uh = f31_2
    elif ruh == 'f31_3':
        uh = f31_3
    elif ruh == 'f30_1':
        uh = f30_1
    elif ruh == 'f39_1':
        uh = f39_1
    elif ruh == 'f39_2':
        uh = f39_2
    elif ruh == 'f39_3':
        uh = f39_3
    elif ruh == 'f38_1':
        uh = f38_1
    elif ruh == 'f38_2':
        uh = f38_2
    elif ruh == 'f38_3':
        uh = f38_3
    elif ruh == 'f37_1':
        uh = f37_1
    elif ruh == 'f37_2':
        uh = f37_2
    elif ruh == 'f37_3':
        uh = f37_3
    elif ruh == 'f36_1':
        uh = f36_1
    elif ruh == 'f36_2':
        uh = f36_2
    elif ruh == 'f36_3':
        uh = f36_3
    elif ruh == 'f35_1':
        uh = f35_1
    elif ruh == 'f35_2':
        uh = f35_2
    elif ruh == 'f35_3':
        uh = f35_3
    elif ruh == 'f34_1':
        uh = f34_1
    elif ruh == 'f34_2':
        uh = f34_2
    elif ruh == 'f34_3':
        uh = f34_3
    elif ruh == 'f33_1':
        uh = f33_1
    elif ruh == 'f33_2':
        uh = f33_2
    elif ruh == 'f33_3':
        uh = f33_3
    elif ruh == 'f32_1':
        uh = f32_1
    elif ruh == 'f32_2':
        uh = f32_2
    elif ruh == 'f32_3':
        uh = f32_3
    elif ruh == 'f31_1':
        uh = f31_1
    elif ruh == 'f31_2':
        uh = f31_2
    elif ruh == 'f31_3':
        uh = f31_3
    elif ruh == 'f30_1':
        uh = f30_1
    elif ruh == 'f29_1':
        uh = f29_1
    elif ruh == 'f29_2':
        uh = f29_2
    elif ruh == 'f29_3':
        uh = f29_3
    elif ruh == 'f28_1':
        uh = f28_1
    elif ruh == 'f28_2':
        uh = f28_2
    elif ruh == 'f28_3':
        uh = f28_3
    elif ruh == 'f27_1':
        uh = f27_1
    elif ruh == 'f27_2':
        uh = f27_2
    elif ruh == 'f27_3':
        uh = f27_3
    elif ruh == 'f26_1':
        uh = f26_1
    elif ruh == 'f26_2':
        uh = f26_2
    elif ruh == 'f26_3':
        uh = f26_3
    elif ruh == 'f25_1':
        uh = f25_1
    elif ruh == 'f25_2':
        uh = f25_2
    elif ruh == 'f25_3':
        uh = f25_3
    elif ruh == 'f24_1':
        uh = f24_1
    elif ruh == 'f24_2':
        uh = f24_2
    elif ruh == 'f24_3':
        uh = f24_3
    elif ruh == 'f23_1':
        uh = f23_1
    elif ruh == 'f23_2':
        uh = f23_2
    elif ruh == 'f23_3':
        uh = f23_3
    elif ruh == 'f22_1':
        uh = f22_1
    elif ruh == 'f22_2':
        uh = f22_2
    elif ruh == 'f22_3':
        uh = f22_3
    elif ruh == 'f21_1':
        uh = f21_1
    elif ruh == 'f21_2':
        uh = f21_2
    elif ruh == 'f21_3':
        uh = f21_3
    elif ruh == 'f20_1':
        uh = f20_1
    elif ruh == 'f19_1':
        uh = f19_1
    elif ruh == 'f19_2':
        uh = f19_2
    elif ruh == 'f19_3':
        uh = f19_3
    elif ruh == 'f18_1':
        uh = f18_1
    elif ruh == 'f18_2':
        uh = f18_2
    elif ruh == 'f18_3':
        uh = f18_3
    elif ruh == 'f17_1':
        uh = f17_1
    elif ruh == 'f17_2':
        uh = f17_2
    elif ruh == 'f17_3':
        uh = f17_3
    elif ruh == 'f16_1':
        uh = f16_1
    elif ruh == 'f16_2':
        uh = f16_2
    elif ruh == 'f16_3':
        uh = f16_3
    elif ruh == 'f15_1':
        uh = f15_1
    elif ruh == 'f15_2':
        uh = f15_2
    elif ruh == 'f15_3':
        uh = f15_3
    elif ruh == 'f14_1':
        uh = f14_1
    elif ruh == 'f14_2':
        uh = f14_2
    elif ruh == 'f14_3':
        uh = f14_3
    elif ruh == 'f13_1':
        uh = f13_1
    elif ruh == 'f13_2':
        uh = f13_2
    elif ruh == 'f13_3':
        uh = f13_3
    elif ruh == 'f12_1':
        uh = f12_1
    elif ruh == 'f12_2':
        uh = f12_2
    elif ruh == 'f12_3':
        uh = f12_3
    elif ruh == 'f11_1':
        uh = f11_1
    elif ruh == 'f11_2':
        uh = f11_2
    elif ruh == 'f11_3':
        uh = f11_3
    elif ruh == 'f10_1':
        uh = f10_1
    elif ruh == 'f9_1':
        uh = f9_1
    elif ruh == 'f9_2':
        uh = f9_2
    elif ruh == 'f9_3':
        uh = f9_3
    elif ruh == 'f8_1':
        uh = f8_1
    elif ruh == 'f8_2':
        uh = f8_2
    elif ruh == 'f8_3':
        uh = f8_3
    elif ruh == 'f7_1':
        uh = f7_1
    elif ruh == 'f7_2':
        uh = f7_2
    elif ruh == 'f7_3':
        uh = f7_3
    elif ruh == 'f6_1':
        uh = f6_1
    elif ruh == 'f6_2':
        uh = f6_2
    elif ruh == 'f6_3':
        uh = f6_3
    elif ruh == 'f5_1':
        uh = f5_1
    elif ruh == 'f5_2':
        uh = f5_2
    elif ruh == 'f5_3':
        uh = f5_3
    elif ruh == 'f4_1':
        uh = f4_1
    elif ruh == 'f4_2':
        uh = f4_2
    elif ruh == 'f4_3':
        uh = f4_3
    elif ruh == 'f3_1':
        uh = f3_1
    elif ruh == 'f3_2':
        uh = f3_2
    elif ruh == 'f3_3':
        uh = f3_3
    elif ruh == 'f2_1':
        uh = f2_1
    elif ruh == 'f2_2':
        uh = f2_2
    elif ruh == 'f2_3':
        uh = f2_3
    elif ruh == 'f1_1':
        uh = f1_1
    elif ruh == 'f1_2':
        uh = f1_2
    elif ruh == 'f1_3':
        uh = f1_3
    elif ruh == 'f0_1':
        uh = f0_1
    elif ruh == 'fG':
        uh = fG
    destination = uh
    if (destination).zoneunlocked == True:
        move_handle(destination)
    elif (destination).zoneunlocked == False:
        Type("The door to this floor is locked!")
        if (destination).zkey in player.inv:
            Type("You unlocked the door with the key you found!")
            (player.inv).remove((destination).zkey)
            (destination).zoneunlocked = True
            move_handle(destination)
        else:
                Type("You need the key to open this door...")
                Prompt()

def Solve():
    if player.curq != 'TestofWis' and player.curq != 'TestofWis2' and player.curq != 'TestofWis3' and player.curq != 'QuinnsRid':
        Type("There is nothing for you to solve.🤦🏾‍♀️")
    elif player.curq == 'TestofWis':
        if player.location == f89_2:
            Type("You solved the riddle! Go back to Eli to complete the quest.")
            take2 = ['Solved1!']
            count = player.inv + take2
        else:
            Type("Nothing happened... Go back to Eli if you've forgotten the Riddle.")

def Prompt():
    action = input("What would you like to do? > ").lower()
    valid_act = ['move','search','use','take','pause','talk','status','info','quit','port','solve']
    while action not in valid_act:
        Type("Invaild action, check your spelling or any spaces.")

        action = input("Enter your action. > ").lower()
    if action == 'pause':
        PauseMen()
    elif action == 'move':
        player_move()
    elif action == 'search':
        player_search()
    elif action == 'use':
        player_use()
    elif action == 'take':
        player_take()
    elif action == 'talk':
        player_talk()
    elif action == 'status':
        player_status()
    elif action == 'info':
        player_info()
    elif action == 'quit':
        quit()
    elif action == 'port':
        Teleport()
    elif action == 'solve':
        Solve()

def Main():
    Type("NEW GAME - 1")
    Type("LOAD GAME - 2")
    Type("EXIT GAME - 3")
    rtr = 2
    while rtr == 2:
        ene = input("Enter number based on your command. > ")
        if ene == '1':
            NewGame()
            rtr = 1
        elif ene == '2':
            LoadGame()
            Prompt()
            rtr = 1
        elif ene == '3':
            quit()
        else:
            Type("That was not a valid number, try again.")

def Cutscene():
    if player.location == f100_1:
        Type("Sitting in front of your desk mindnumbingly entering in digits, you didn't notice the time dwindle by...")
        Type("After finally finishing your report, you look up at the clock in your office.")
        Type(f"[{player.name}]: It's 7 already?!?!?")
        Type(f"[{player.name}]: Damn, that report took a long time to write.")
        Type(f"The more you looked at the clock the brighter it seemed to glow until your eyes were filled with a blinding light.")
        Type(f"[{player.name}]: What the fu-")
        Type(f"You were dropped back into what seemed to be your office, though something felt off...")
        return
    elif player.location == f100_3 and (player.location).zmobs != []:
        Type("Walking into the next room you moved instinctively towards the closest lift, eyes glued to your phone.")
        Type(f"[{player.name}]: Huh? No service? I usually get full bars, what's going on?")
        Type("Putting your phone in your coat pocket, you went to press the down button for the lift.\nOnly to realise the horrid sign displayed in large red letters,'OUT OF ORDER, Please use the stairs.'")
        Type(f"[{player.name}]: You've got to be kidding me! I have to walk all the way down the stairs!?!?")
        Type(f"Looking at the staircase nearby, you noticed a small creature seemily guarding it, the same time it noticed you.")
        Type(f"[{player.name}]: What even is that?")
        Type(f"[Tutorial]: Well, hello again! I hope you were using the 'search' and 'take' actions because you're about to be pulled into a battle!")
        if len(player.inv) < 3:
            Type(f"[Tutorial]: I see you weren't... You don't have the necessary items to continue. I'll send you back to Floor 100, Room 1!")
            player.location = f100_1
        else:
            Type("[Tutorial]: Good, you did! So now I'll explain to you how the battle system works.")
            Type("[Tutorial]: First you'll equip your weapon! Use 'info' action outside battle to find out your weapon atk.")
            Type("[Tutorial]: When prompted you can do three actions:")
            Type("[Tutorial]: 'attack','use','pause','quit'")
            Type("[Tutorial]: Most are self-explantory but 'use' requires a bit more context!")
            Type("[Tutorial]: 'use' allows you to use healing potions during battle.\n[Tutorial]: You can also use this action outside of battle for other items as well as healing potions.")
            Type("[Tutorial]: Hopefully that helped! Don't forget you can use 'help' in the pause menu if you need help.")
        return
    elif player.location == f100_3 and (player.location).zmobs == []:
        Type(f"The Goblin fell, vaporising once it hit the ground. It's last word spoken in elfish:\n'.!!koobetoN a htiw em dellik uoY !ouy kucf'")
        Type(f"[{player.name}]: That little thing was vicious! All these scratches are starting to burn...")
    elif player.location == f96_2 and player.curq != 'Adagios Notebook':
        winsound.PlaySound("Adagio1.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
        Type("You walked cautiously into the room scared the sign was a trap...")
        Type("A tall figure started to get closer and you readied your now bloodly Notebook.")
        Type("[Adagio]: Hey! You're new here right? I've never seen you around before.")
        Type("A tall woman who looked about 22 approached you, here curly locks bouncing as she got stopped infront of you.")
        Type(f"[{player.name}]: Err... Hi. You're not going to attack me right?")
        Type("[Adagio]: No, not today. Unless you want me too, though that Notebook is not going to do anything to me.")
        Type("[Adagio]: Don't worry, you can rest. No pesky Goblins will bother you while I'm here.")
        Type(f"[{player.name}]: Oh that's a relief! Well you see, I'm not suppose to be here, maybe you could help me?")
        Type("[Adagio]: Well, I could answer any questions you have.")
        Type(f"[{player.name}]: That's amazing, do you kno-")
        Type("[Adagio]: Wait. Not for nothing that is. You have to help ME first.")
        Type(f"[{player.name}]: Oh. What do you need help with?")
        Type("[Adagio]: I've lost my own notebook somewhere around here... Find it and bring it back to me, K?")
        Type("Accept the Quest?")
        Type(">Yes (Lol, you don't have a choice! <3 )")
        player.curq = 'Adagios Notebook'
        pl = f96_2.zNPCs + ['adagio']
        f96_2.zNPCs = pl
    elif player.location == f90_1 and (player.location).zmobs == []:
        Type(f"Somehow you managed to survive, the Goblin King speaking its last words before it vaporised into to nothingness.\n[Goblin King]: uoy dne lliw aratniak drol.")
        Type(f"You took the leftover gold pieces, finally relaxing as you had killed the abnormal, large Goblin.")
        Type(f"[{player.name}]: It's annoying that I can't understand what it just said, what language even is that?")
        Type(f"[{player.name}]: Eh, it's ok. The bigger problem lies with this flimsy ruler which might break at anytime...")
        Type(f"[{player.name}]: I need a better weapon, especially if I'm going to eventually face monster like this again.")
    elif player.location == f82_1 and player.curq != 'Kaintaras Bag':
        Type("You walked downstairs half expecting to still be in Yonaite's apartment.\nInstead, you found yourself in another lobby area with decent seating leading to yet another hallway.")
        Type("There was someone sitting on a sofa far in the corner, looking very deep in thought. I didn't seem like they noticed your prescene.")
        Type("After talking to at least a few people in the Tower, you assumed that she would not attack you.\nAnd seeing as this was a public space. (That you knew of.) They most likely will entertain a pleasant conversation.")
        Type(f"[{player.name}]: Hey? Do you mind if I ask you a few questions? I'm pretty new to this Tower so I was wondering if I could learn more?")
        Type("The seemily air-headed woman looked up at you, her face showing an expression of regcognition despite you never meeting her.")
        Type(f"[Kaintara]: Ah, Hello, you can call me Kaintara. {player.name}? Is that right?")
        Type(f"[{player.name}]: Yeah, that's me. How do you know?")
        Type("[Kaintara]: Well, word spreads fast around here, especially to long-time residents like me. Congrats to killing the Goblin King by the way.")
        Type("[Kaintara]: He is extremely whiny. Anyways, what questions do you have for me? I'll give you three for now.")
        Type(f"[{player.name}]: (Seriously, what's with these residents and answering only three questions?).")
        Type(f"[{player.name}]: Ok then! So do you know who is the creator of the tower?")
        Type("[Kaintara]: Yes, but even if you ask I can't tell you about her.")
        Type(f"[{player.name}]: That's a shame. I really thought someone could help me get back to my world...")
        Type("[Kaintara]: Does that count as an indirect question?")
        Type(f"[{player.name}]: Wait! You know a way back? Tell me!            ...Please.")
        Type("[Kaintara]: Well, I know of this device which makes a portal to wherever you want to go. It's extremely useful but annoying to bulid.")
        Type(f"[{player.name}]: Could you tell me how to bulid it?")
        Type("[Kaintara]: Of course but I haven't got a blueprint on hand. I can meet you later on in the tower but in the meantime could you do me a favour?")
        Type(f"[{player.name}]: But where would me me-")
        Type("[Kaintara]: I've just answered your questions, no? The least you could do is find my misplaced Bag.")
        Type("[Kaintara]: It's not a very difficult task and I'll heavily reward you for it if you do.")
        Type("Accept the Quest?")
        Type(">Yes (Lol, you don't have a choice! <3 )")
        player.curq = 'Kaintaras Bag'
        thingy = ['Unsealed Bag']
        count = f85_3.zitems + thingy
        f85_3.zitems = count
        pl = f82_1.zNPCs + ['kaintara']
        f82_1.zNPCs = pl
    elif player.location == f77_1 and player.curq != 'Robbed!':
        Tempwal = 0
        Type("You walked down the staircase picking up the gold pieces as you went.\n You were careful not to slip or trip as walking down stairs whilst picking things up is very dangerous.")
        Type("Abruptly, you felt a hand on the middle of your back sending you tumbling down the stairs your speed opening the door to Floor 77, Room 1.")
        Type("You took 40 damage!")
        php = player.hp - 25
        player.hp = php
        if player.hp <= 0:
            Type(f"You have been defeated by Jin...")
            Type("You'll get them next time!")
            quit()
        Type("You looked up weakly to see a short man rifling through your stuff. It only took him a few seconds to grab your wallet and dash.")
        (player.inv).remove('Wallet')
        Tempwal = player.gold
        Type(f"He just stole {Tempwal} Gold pieces from you.")
        player.gold = 0
        Type(f"[???]: Thanks for doing business with me!")
        Type("He spoke throwing you a small green vial in exchange.")
        Type(f"[{player.name}]: Hey! Asshole! Half my wallet isn't worth this! Come back here! I'LL FIND YOU!!!")
        Type("Your shouts did nothing as the thief had already ran into the darkness.")
        Type(f"[{player.name}]: Damnit! I need that back, that's the only way I can afford to buy healing potions and exp orbs. Without them... I don't want to think about that.")
        Type(f"[{player.name}]: I could't see the robber's face so I'll have to ask around if people have seen him.")
        Type("Quest Started!")
        player.curq = 'Robbed!'
    elif player.location == f76_2 and player.curq == 'Robbed!':
        Type("Walking into the next room, you expected it to be pitch-black. It wasn't instead you could see a brown-haired man walking in the deolate room.")
        Type("He looked a lot taller then the figure who robbed you, so you thought it might be helpful to ask if he'd seen anyone similar.")
        Type("Because as of right now you have not a single hint or clue.")
        Type(f"[{player.name}]: Excuse me, I just want to ask if you seen a hooded, short person coming through here? They just mugged me.")
        Type("The man turned around to face you, his features holding a soft smile.")
        Type(f"[Nanaka]: Oh, how horrible! You're {player.name} so I guess that puts a target on your back.\nPersonally, I wasn't a smart idea to walk around with {Tempwal} carelessly.")
        Type(f"[{player.name}]: Wow, word really does spread fast here. Well, I didn't I would have to worry about people pushing me down staircases. I wouldn't say I was walking around 'carelessly'.")
        Type("[Nanaka]: Hmm, that's not what I've heard. Eli told me all about how you've been walking through people's apartments without care.")
        Type(f"[{player.name}]: I mean I ask the owners if its ok to walk through their rooms, if that counts for something?")
        Type("[Nanaka]: Well, it doesn't but who am I to tell you what to do?")
        Type(f"[{player.name}]: So have you seen the thief or not?")
        Type("[Nanaka]: Yes, they just contiuned to run down the floors.")
        Type(f"[{player.name}]: Thank you! (That wasn't even that helpful in the end...)")
        Type("[Nanaka]: Actually, could you do me a favour? I've been looking for a person of my own interest. Her name is Mochaii.")
        Type("[Nanaka]: I have no doubt that you'll ask more people about your mugger so I would appreciate it if you could ask for her as well.")
        Type("[Nanaka]: I'll meet you here once you're done asking around or you found Mochaii.")
        Type("Accept the Quest?")
        Type(">Yes (Lol, you don't have a choice! <3 )")
    elif 'cuts' == '11':
        pass
    elif 'cuts' == '12':
        pass
    elif 'cuts' == '13':
        pass
    elif 'cuts' == '14':
        pass
    elif 'cuts' == '15':
        pass
    elif 'cuts' == '16':
        pass
    elif 'cuts' == '17':
        pass
    elif 'cuts' == '18':
        pass


Main()

no = 1
while no == 1:
    Prompt()
