from os import walk
from os import listdir

def getAllPokemonNames():
    names = []
    for (dirpath, dirnames, filenames) in walk('./TVPoke/Pokemon'):
        names.extend(filenames)
    ret = []
    for name in names:
        if name[-3:] == ".py":
            ret.append(name[:-3])
        else:
            break
    return ret