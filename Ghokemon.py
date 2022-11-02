"""
Logy's Advanture in Ghokemon world

Muhammad Naufal Setiawan
1152100035
Informatika-A 
"""

r,c = 0, 0
ghokemon = 0
trainers = 0
inventory = 0
map = []
data_trainers = []
data_ghokemon = []

def convert(string)
    list1=[]
    list1[:0]=string
    return list1

def mode():
    global r, c, ghokemon, trainers, inventory
    while True:
        error = False
        data_input = input('input data([r] [c] [ghokemon] [trainers] [inventory])\n> ')
        data_cut = data_input.split(' ')
        if len(data_cut) < 5:
            print('input data yang sesuai')
        elif len(data_cut) == 5:
            for i in range(len(data_cut)):
                if data_cut[i].isnumeric():
                    pass
                else: error = True; break
            if error == True:
                print('input data sesuai angka')
            else:
                r, c = int(data_cut[0]),int(data_cut[1])
                ghokemon = int(data_cut[2])
                trainers = int(data_cut[3])
                inventory = int(data_cut[4])
                break
        else: print('input data sesuai')

def map_config():
    global r, c, ghokemon, trainers
    while True:
        trainers = 0
        logy = 0
        ghokemon = 0 
        map_temporary_list_storage = []
        for i in range(c):
            while True:
                unknown_symbols = False                               