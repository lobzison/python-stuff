"""
Simple RPG-game with procedural approach
Game have 3 classes: Warrior, Mage, Rouge
Warrior have 20% more hp than other classes.
Mage have 20% of hp as energy shield. If Mage have energy shield, he takes damage from energy shield, instead of HP.
Rouge have 20% chance to dodge attacks. If rouge successfully dodges, he takes 0 damage from attack.
"""
import random

class Character:
    def __init__(self):
        self._hp = 100
        self._mp = 100
        self._attack = 9
        self._class = "Character"
        
    def get_hp(self):
        return self._hp
    
    def get_attack(self):
        return self._attack
    
    def is_alive(self):
        return self._hp > 0
    
    def take_damage(self, damage):
        self._hp -= damage
        
    def deal_damage(self, other):
        other.take_damage(self.get_attack())
        
    def get_class(self):
        return self._class
        
    def print_stats(self):
        print("Class: {}, HP: {}, MP: {}".format(self.get_class(). self.get_hp()))
        
    def battle_until_dead(self, other):
        while self.is_alive() and other.is_alive():
            self.deal_damage(other)
            other.deal_damage(self)
        winner = self if self.is_alive() else other
        print("The winner is :{}!".format(winner.get_class()))
        
class Warrior(Character):
    def __init__(self):
        Character.__init__()
        self._hp *= 1.2
        self._class = "Warrior"
        
class Mage(Character):
    def __init__(self):
        Character.__init__(self)
        self._es = self._hp * 0.2
        self._class = "Mage"
        
    def get_es(self):
        return self._es
    
    def take_damage(self, damage):
        if self.get_es() > damage:
            self._es -= damage
        elif self.get_es() > 0:
            dmg_to_hp = damage - self.get_es()
            self._es = 0 
            self._hp -= dmg_to_hp
        else:
            Character.take_damage(self,damage)
            
    def print_stats(self):
        Character.print_stats(self)
        print("ES: {}".format(self.get_es()))
            
class Rouge(Character):
    def __init__(self):
        Character.__init__(self)
        self._dodge = 0.2
        self._class = "Rouge"
        
    def get_dodge(self):
        return self._dodge
    
    def take_damage(self, damage):
        if random.random() > self.get_dodge():
            Character.take_damage(self,damage)
            
    
    
rouge = Rouge()
mage = Mage()

mage.battle_until_dead(rouge)
    
