# Exercise 45: Make Your Own Game

# For this exercise you are meant to design your own game in the style
# of Exercise 43. I am going to work on developing a Pokemon-type
# game. I don't know how much I will develop the narrative, but I will
# spend the most time creating a relatively rounded combat system
# because this is where I stand to learn the most about how classes,
# objects, and inheritance function. I'll also have to develop
# a way to automate the the opponent's actions

# Use a random system to assign the likelihood of dodging and other AI actions

from random import randint

# So Pokemon will be dictionaries that store all relevant information
# in keys

Charizard = {'name': 'Charizard',
             'health': 220,
             'dodge': 25,
             'attacks': [
                 {
                     "name" : "Flamethrower",
                     "strength" : 50,
                     "pp": 5},
                 {
                    "name" : "Ember",
                    "strength" : 15,
                    "pp": 20}],
             'type': 'Fire',
             'weakness': 'Water'
             }
Blastoise = {'name': 'Blastoise',
             'health': 230,
             'dodge': 15,
             'attacks': [
                 {
                    "name" : "Hydro Pump",
                    "strength" : 50,
                    "pp": 5},
                {
                    "name" : "Water Gun",
                    "strength" : 10,
                    "pp": 20}],
             'type': 'Water',
             'weakness': 'Thunder'
             }
Venusaur = {'name': 'Venusaur',
            'health': 240,
            'dodge': 10,
            'attacks': [
                {
                 "name" : "Solar Beam",
                 "strength" : 40,
                 "pp": 5},
                {
                 "name" : "Vine Whip",
                 "strength" : 10,
                 "pp": 20}],
            'type': 'Grass',
            'weakness': 'Fire'
            }

pokedex = []
pokedex.append(Charizard)
pokedex.append(Blastoise)
pokedex.append(Venusaur)

pokemon_names = []
pokemon_names.append(Charizard['name'])
pokemon_names.append(Blastoise['name'])
pokemon_names.append(Venusaur['name'])

party = []
activePartySlot = 0;

number_of_pokemon = len(pokemon_names)

attack1_turns = 5
rand_attack1_turns = 5

class Pokemon(object):
    
    def __init__(self, pokemonDictionary):
        self.name = pokemonDictionary['name']
        self.health = pokemonDictionary['health']
        self.dodge = pokemonDictionary['dodge']
        self.attacks = pokemonDictionary['attacks']
        self.type = pokemonDictionary['type']
        self.weakness = pokemonDictionary['weakness']
        

class SelectPokemon(object):

    def play(self):
        global party

        print ''
        print "[string cues]"
        print ''
        print "*" * 34
        print "* SOMETIME IN THE NEAR FUTURE... *"
        print "*" * 34

    # first scene where you select a pokemon
        print ''
        print "You enter into the building. Immediately you are greeted by a man"
        print "In a white lab coat."
        print "\'Welcome to the Pokemon lab! My name is Professor Elm."
        print "Here you can select your Pokemon.\'"
        print "\'We have the following Pokemon available for you:\'"

        index = 0

        for monster in pokedex:
            print ""
            print "Name: %s" % monster['name']
            print "Type: %s" % monster['type']
            print "Health: %s" % monster['health']
            print "Dodge: %s" % monster['dodge']
            print "Main attack: %s" % monster['attacks'][0]['name']
            print "Secondary attack: %s" % monster['attacks'][1]['name']
            print "Weakness: %s" % monster['weakness']
            print ""
        # this increases the index variable each time it cycles through
        # a pokemon
            index += 1
        # this condition stops looping through once you reach the last pokemon
        # based on the specific index
            if index < len(pokedex):
                raw_input("See next Pokemon? ")

        print "The professor smiles at you. 'So, which Pokemon would you like to"
        print "select?\'"
        print ''
        print "You can select:"
        print ""
        for poke in pokemon_names:
            print poke

        print ""

        choice = raw_input('Type the name of the Pokemon you wish to select. ')
    # as long as the player's choice is not amongst the selectable pokemon_names
    # it will prompt them to reenter the name
        while choice not in pokemon_names:
            print ""
            print "Sorry, I didn't get that."
            print ""
            choice = raw_input('Type the name of the Pokemon you wish to select. ')
        else:
            print ""
            print "You have selected %s!" % choice
            print ""

        for monster in pokedex:
            if choice == monster['name']:
                party.append(Pokemon(monster))
                pokemon = party[0];
                print "As a reminder, here are the stats of your Pokemon: "
                print "Name: %s" % pokemon.name
                print "Type: %s" % pokemon.type
                print "Health: %s" % pokemon.health
                print "Dodge: %s" % pokemon.dodge
                print "Main attack: %s" % pokemon.attacks[0]
                print "Secondary attack: %s" % pokemon.attacks[1]
                print "Weakness: %s" % pokemon.weakness
                print ""

        print "\'Very good! You are ready to set out there on your own and"
        print "become the best trainer in all the land!\'"
        print ""
        print "The professor opens the door and you embark on your journey."
        print ""
        print "*" * 25
        print "* QUINN'S POKEMON QUEST *"
        print '*' * 25

        return 'battle'

class Battle(object):

    def play(self):
        random_number = randint(0,(number_of_pokemon-1))
        self.wildPokemon = Pokemon(pokedex[random_number])

        print ""
        print "As you wander through the wilderness, you take in the natural"
        print "wonder presented to you. What a life to be living!"
        print "Suddenly, you stop. You hear a rustle in the nearby bushes."
        print ""
        print "A wild %s appears!" % self.wildPokemon.name
        print "[energetic music starts]"

        return self.attack()
    def attack(self):
        pokemon = party[activePartySlot]
        print ""
        print "Which attack do you choose?"
        for i in range(0,len(pokemon.attacks)):
            attack = pokemon.attacks[i]
            print "Attack %d: %s, Strength: %d, PP: %d" % (i+1,attack['name'],attack['strength'],attack['pp'])
        print ""
        attackIndex = int(input('Selected attack: (1/2)'))
        print ""
        if attackIndex <= len(pokemon.attacks) and attackIndex > 0:
            attack = pokemon.attacks[attackIndex-1]
            if attack['pp'] == 0:
                print "Oops! You can't use %s anymore." % attack['name']
                print ""
                return self.attack()
            else:
                print "%s used %s!" % (pokemon.name,attack['name'])
                pokemon.attacks[attackIndex-1]['pp'] -= 1
                if self.wildPokemon.dodge >= randint(1,100):
                    print "The wild %s dodged your attack!" % self.wildPokemon.name
                    print ""
                    return self.opponent_attack()
                else:
                    if self.wildPokemon.weakness == pokemon.type:
                        self.wildPokemon.health -= (attack['strength'])*1.2
                        print "It was super effective!"
                    else:
                        self.wildPokemon.health -= (attack['strength'])
                        print "Direct hit!"
                        
                    if self.wildPokemon.health <= 0:
                        self.wildPokemon.health = 0;
                        print "Wild %s fainted" % (self.wildPokemon.name)
                        return 'onward'
                    print "Wild %s's health is now %d" % (self.wildPokemon.name, self.wildPokemon.health)
                    print ""
                    return self.opponent_attack()
        else:
            print "Sorry, I didn't get that."
            print "Which attack do you choose?"
            return self.attack()

    def opponent_attack(self):
        pokemon = party[activePartySlot]
        attackIndex = randint(1,2)
        attack = self.wildPokemon.attacks[attackIndex-1]
        print "Wild %s used %s!" % (self.wildPokemon.name,attack['name'])
        if pokemon.dodge >= randint(1,100):
            print "Wild %s's attack missed!" % self.wildPokemon.name
            return self.attack()
        else:
            if pokemon.weakness == self.wildPokemon.type:
                pokemon.health -= attack['strength'] * 1.2
                print "It was super effective!"
                if pokemon.health <= 0:
                    pokemon.health = 0;
                    return 'faint'
            else:
                pokemon.health -= attack['strength']
                print "Direct hit!"
                if pokemon.health <= 0:
                    pokemon.health = 0;
                    print "%s can no longer fight" % (pokemon.name)
                    return 'faint'
            print "%s's health is now %d" % (pokemon.name,pokemon.health)
            print ""
            return self.attack()
                    

class Journey(object):

    def play(self):
        print "cool"
        return 'end'


class Faint(object):
    def play(self):
        print ""
        print "Uh oh! Your Pokemon fainted!."
        print "welp"
        print ""
        return 'end'
        
class End(object):

    def play(self):
        print "GAME OVER"

class Map(object):

    scenes = {
    'select': SelectPokemon(),
    'battle': Battle(),
    'onward': Journey(),
    'faint': Faint(),
    'end': End()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def playthrough(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('end')

        while current_scene != last_scene:
            next_scene_name = current_scene.play()
            current_scene = self.scene_map.next_scene(next_scene_name)
        last_scene.play()


# Beginning the game.
the_map = Map('select')
a_game = Engine(the_map)
a_game.playthrough()
