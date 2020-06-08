import random

def pool_updater (einsatz = [], pool=[]):
    i = len(einsatz)
    while i>0:
        pool.remove(einsatz[i-1])
        i = i-1
    return pool

def pool_maker (anzahl, seitenzahl):
    i = 0
    pool = []
    while i < anzahl:
        pool.append(random.randint(1,seitenzahl))
        i = i+1
    return pool

def pool_appender (pool1, pool2):
    i = len(pool1)
    while i>0:
        pool2.append(pool1[i-1])
        i = i-1
    return pool2

def einsatz_getter ():
    einsatz = []
    einsatz_yn = 'y'

    while einsatz_yn == 'y':
        ein = int(input("einen Raise angeben: "))
        einsatz.append(ein)
        einsatz_yn = input("nächster Einsatz y/N")
    return einsatz

pool = []
einsatz = []
traits_yn = 'y'


stats = int(input("Anzahl Statwürfel: "))
statpool = (pool_maker(stats, 6))
pool = pool_appender(pool, statpool)
traits_yn = input("Traits mitwürfeln? [y/N]")
while traits_yn == 'y':
    trait = input("Bitte einen Trait angeben: ")
    anzahl = int(trait[0])
    seitenzahl = int(trait[2])
    pool = pool_appender(pool, pool_maker(anzahl, seitenzahl))
    traits_yn = input("Weitere Trait? [y/N]")

print("Dein Würfelpool ist: ", pool)

einsatz = einsatz_getter()

print("Dein Einsatz ist: ", einsatz)
updated_pool = list(pool_updater(einsatz, pool))
print(updated_pool)
