import json


def init_pool (player: str, pool:str): 
    dice_pools = {}
    dice_pools['Spieler'] = []
    dice_pools['Spieler'].append({
        'Name': player,
        'pool': pool
    })

    with open("dice_pools.json", "w") as outfile:
        json.dump(dice_pools, outfile)

def save_pool (player: str, pool:str):
     with open("dice_pools.json", "r") as infile:
        dice_pools = json.load(infile)
     infile.close()
     dice_pools['Spieler'].append({
         'Name': player,
         'pool': pool
     })
     with open("dice_pools.json", "w") as outfile:
         json.dump(dice_pools, outfile, indent=4)
    
def update_pool (player: str, pool_new:str):
    with open("dice_pools.json", "r") as infile:
        dice_pools = json.load(infile)
    infile.close()

    x = 0
    while x < len(dice_pools["Spieler"]):
        if dice_pools["Spieler"][x]['Name'] == player:
            dice_pools["Spieler"][x].update(pool = pool_new)
            break
        else:
            x = x+1


    with open("dice_pools.json", "w") as outfile:
        json.dump(dice_pools, outfile, indent=4)

def load_pool (player: str):
    with open("dice_pools.json") as infile:
        dice_pools = json.load(infile)
    x = 0
    while x < len(dice_pools["Spieler"]):

            if dice_pools["Spieler"][x]['Name'] == player:
                return dice_pools["Spieler"][x]["pool"]
            else:
                x = x+1
"""
while True:
    befehl = input("Was möchtest du tun?\n")
    
    if befehl == "save":
        player = input("Spielername angeben: ")
        pool = input("Würfelpool angeben: ")
        save_pool(player, pool)
    
    elif befehl == 'load':
        player = input("Spielername angeben: ")
        print(load_pool(player))

    elif befehl == 'update':
        player = input("Spielername angeben: ")
        pool = input("Pool angeben: ")
        update_pool(player, pool)

    elif befehl == "quit":
        break

    else:
        print("Habe ich nicht verstanden")
"""