"""
Simple RPG-game with procedural approach
Game have 3 classes: Warrior, Mage, Rouge
Warrior have 20% more hp than other classes.
Mage have 20% of hp as energy shield. If Mage have energy shield, he takes damage from energy shield, instead of HP.
Rouge have 20% chance to dodge attacks. If rouge successfully dodges, he takes 0 damage from attack.
"""
import random
# define Warrior, Mage and Rouge as dictionaries
# all classes have key "class" with appropriate string for class name, key "HP", "MP", "Damage"
# all classes have 100 hp, 100 mp and 10 damage if not statet otherwise
# Warrior have 20% more hp than default value
# Mage have additional key "ES" witch equals 20
# Rouge have additional key "Dodge" witch equals 0.2
DEFAULT_HP = 100
DEFAULT_MP = 100
DEFAULT_ATTACK = 9
warrior = {"class": "Warrior", "HP": DEFAULT_HP*1.2, "MP": DEFAULT_MP, "Damage": DEFAULT_ATTACK}
mage = {"class": "Mage", "HP": DEFAULT_HP, "MP": DEFAULT_MP, "Damage": DEFAULT_ATTACK, "ES": DEFAULT_HP*0.2}
rouge = {"class": "Rouge", "HP": DEFAULT_HP, "MP": DEFAULT_MP, "Damage": DEFAULT_ATTACK, "Dodge":0.2}

# define Monster enemy as a dictionary
# Monster have 4 keys: class, HP, MP, Damage
# Monster have 100 hp, 100 mp and 10 damage
monster = {"class": "Monster", "HP": DEFAULT_HP, "MP": DEFAULT_MP, "Damage": DEFAULT_ATTACK}

# Write a function is_alive that takes one parameter - players class or monster
# to check if a player of monster is dead.
# It returns True it player have HP > 0 and 0 otherwise
def is_alive(thing):
    return thing["HP"] > 0

# Write a function deal_damage that takes two parameters - damage dealer and damage reciever
# If the damage reciever is warrior or monster - just substract damage of attacker from the HP
# If the damage reciever is mage - check if ES > 0. If so - substuct from ES as much as it could absorb, and the remaining damage goes to HP
# If the damage reciever is rouge - make a random check with his dodge probablility. So if dodge chance is 0.1, in 10% of times rouge will dodge
# Dodge means taking 0 damage from a hit
# After dealing the damage, fuction prints a line with iformation who attacked who, and what is the status of damage reciever after the damage

def deal_damage(dealer, reciever):
    r_class = reciever["class"]
    dmg = dealer["Damage"]
    if r_class == "Mage":
        if reciever["ES"]>0:
            if reciever["ES"]>dmg:
                reciever["ES"] -= dmg
            else:
                dmg_to_hp = dmg - reciever["ES"]
                reciever["ES"] = 0
                reciever["HP"] -= dmg_to_hp
        else:
            reciever["HP"] -= dmg
    elif r_class == "Rouge":
        if random.random() > reciever["Dodge"]:
            reciever["HP"] -= dmg
    else:
        reciever["HP"] -= dmg
    print("{}, dealt damage to {}, parameters after hit: ".format(dealer["class"], r_class))
    print(reciever)
    
# Write a function battle_until_dead that takes two entities witch will battle untill one of them is dead.
# first parameter to the fuction attacks first.
# After one of them is dead, print a winner along with some fancy message
def battle_until_dead(first, second):
    while is_alive(first) and is_alive(second):
        deal_damage(first, second)
        deal_damage(second, first)
    winner = first if is_alive(first) else second
    print("The winner is: {}!".format(winner["class"]))
    
    
battle_until_dead(mage, rouge)
