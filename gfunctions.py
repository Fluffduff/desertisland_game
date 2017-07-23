from rooms import *
import items
import collections



        
def parsecommand(userinput):
    '''This is where i separates the command into the 'verb' (e.g. get), and the 'item' (e.g. coconut)'''
    ParsedCommand = collections.namedtuple('ParsedCommand', ['verb', 'item'])
    tokens = userinput.split(' ')
    verb = tokens.pop(0)
    if len(tokens) > 0:
        return ParsedCommand(verb, ' '.join(tokens))
    else:
        return ParsedCommand(verb, '')

def finditem(itemname, container):
    for i in container:
        if i['name'] == itemname:
            return i

def death():
    respawn = input('You died! Would you like to respawn? ')
    if respawn == 'yes':
        it = initialisation()
        global character
        character = it.character
        turn_no = it.turn_no
    else:
        exit()

def chooseroom(character):
    """This is where it decides where the character is."""
    if character.loc == [1,2]:
        character.room = beach1
    elif character.loc == [1,1]:
        character.room = rocks1
    elif character.loc == [2,2]:
        character.room = jungle1
    elif character.loc == [2.5,2]:
        character.room = clearing1
    elif character.loc == [3,2]:
        character.room = mountains1
    elif character.loc == [2,1]:
        character.room = village1
    elif character.loc == [2.5,1]:
        character.room = house1
    elif character.loc == [3,3]:
        character.room = waterfall1
    elif character.loc == [2,3]:
        character.room = hill1
    elif character.loc == [1,3]:
        character.room = cliff1
    else:
        print('I can\'t choose a room!!!')

def roomreset():
    beach1['items'] = [coconut1, coconut2, coconut3, rope, seagull]
    rocks1['items'] = [rock, starfish, shellfish]


def get(item, character):
    if item not in character.inventory:
        character.inventory.append(item)
    else:
        item['inv'] = item['inv'] + 1

def invcheck(character, item):
    for item in character.inventory:
        if item['inv'] < 1:
            character.inventory.remove(item)

def clone(item):
    index = 1
    newitem = item.copy()
    write(text, newitem)
    return newitem
