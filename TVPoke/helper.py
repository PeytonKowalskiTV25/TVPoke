from os import walk
from os import listdir

def getAllPokemonNames():
    names = []
    for (dirpath, dirnames, filenames) in walk('./TVPoke/Pokemon'):
        names.extend(filenames)
        break
    return [name[:-3] for name in names]