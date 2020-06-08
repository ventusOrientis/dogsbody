import random

def roll_dice (dicepool: str):
    dice_elemente = list(dicepool.split(','))
    endergebnis: str = ""
    x = len(dice_elemente)
    i = 0
    while x>i:
        anzahl = int(dice_elemente[i])
        seitenzahl = int(dice_elemente[i+1])
        wurf = [
            str(random.choice(range(1, seitenzahl +1)))
            for _ in range(anzahl)
        ]
        ergebnis = ','.join(wurf)
        endergebnis = ergebnis + ',' + endergebnis
        i = i+2
    print(endergebnis)

roll_dice("100,20")

