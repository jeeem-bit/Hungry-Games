#
# Note that written answers should be commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games import *

############
##  Task1 ##
############
import random

class Weapon(Thing):

    ###########
    # Task 1a #
    ###########

    def __init__(self, name, min_dmg, max_dmg):
        # your code here
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
       


    ###########
    # Task 1b #
    ###########

    def min_damage(self):
        # your code here
        return self.min_dmg

    def max_damage(self):
        # your code here
        return self.max_dmg


    ###########
    # Task 1c #
    ###########

    def damage(self):
        # your code here
        return random.randint(self.min_dmg, self.max_dmg)
    

def test_task1():
    print('=== Task 1 ===')
    sword = Weapon('sword', 3, 10)
    print(isinstance(sword, Weapon))    # True
    print(isinstance(sword, Thing))     # True

    print('=== Task 1b ===')
    print(sword.min_damage())           # 3
    print(sword.max_damage())           # 10

    print('=== Task 1c ===')
    print(sword.damage())               # Random value between 3 to 10

# uncomment to test task1
# test_task1()


############
##  Task2 ##
############

class Ammo(Thing):

    ###########
    # Task 2a #
    ###########
    # constructor here
    def __init__(self, name, weapon, qty):
        self.name = name
        self.weapon = weapon.name
        self.qty = qty


    ###########
    # Task 2b #
    ###########
    # definition of get_quantity here
    def get_quantity(self):
        return self.qty


    ###########
    # Task 2c #
    ###########
    # definition of weapon_type here
    def weapon_type(self):
        return self.weapon 

    ###########
    # Task 2d #
    ###########
    # definition of remove_all here
    def remove_all(self):
        self.qty = 0


def test_task2():
    print('=== Task 2 ===')
    bow = Weapon('bow', 10, 20)
    arrows = Ammo('arrow', bow, 5)
    print(arrows.get_quantity())        # 5
    print(arrows.weapon_type())         # bow
    arrows.remove_all()
    print(arrows.get_quantity())        # 0

# uncomment to test task2
# test_task2()


############
##  Task3 ##
############

class RangedWeapon(Weapon):

    ###########
    # Task 3a #
    ###########
    # constructor here
    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name, min_dmg, max_dmg)
        self.shots = 0 


    ###########
    # Task 3b #
    ###########
    # definition of shots_left here
    def shots_left(self):
        return self.shots 


    ###########
    # Task 3c #
    ###########
    # definition of load here
    def load(self, ammo):
        if ammo.weapon_type() == self.name:
            self.shots += ammo.get_quantity()
            ammo.remove_all()
            


    ###########
    # Task 3d #
    ###########
    # definition of damage here
    def damage(self):
        if self.shots == 0:
            return 0
        else:
            self.shots -= 1
            return super().damage()



def test_task3():
    print('=== Task 3a ===')
    bow = RangedWeapon('bow', 10, 40)
    print(isinstance(bow, RangedWeapon)) # True
    print(isinstance(bow, Weapon))       # True

    print('=== Task 3b/c ===')
    crossbow = RangedWeapon('crossbow', 15, 45)
    arrows = Ammo('arrow', bow, 5)
    bolts = Ammo('bolt', crossbow, 10)

    bow.load(bolts)
    print(bow.shots_left())         # 0
    print(bolts.get_quantity())     # 10

    bow.load(arrows)
    print(bow.shots_left())         # 5
    print(arrows.get_quantity())    # 0

    print('=== Task 3d===')
    print(crossbow.damage())        # 0
    crossbow.load(bolts)
    print(crossbow.shots_left())    # 10
    print(bolts.get_quantity())     # 0
    print(crossbow.damage())        # Random value between 15 and 45
    print(crossbow.shots_left())    # 9

# uncomment to test task3
# test_task3()


###########
# Task 4a #
###########
# definition of Food class here
class Food(Thing):
    def __init__(self, name, food_val):
        self.name = name
        self.food_val = food_val

    def get_food_value(self):
        return self.food_val

###########
# Task 4b #
###########
# definition of Medicine class here
class Medicine(Food):
    def __init__(self, name, food_val, med_val):
        super().__init__(name, food_val)
        self.med_val = med_val

    def get_medicine_value(self):
        return self.med_val

def test_task4():
    print('=== Task 4 ===')
    apple = Food('apple', 4)
    print(apple.get_food_value())               # 4
    panadol = Medicine('paracetamol', 0, 5)
    print(panadol.get_food_value())             # 0
    print(panadol.get_medicine_value())         # 5

# uncomment to test task4
# test_task4()


##############
# Task 5a&b  #
##############
# definition of Animal class here
class Animal(LivingThing):
    def __init__(self, name, health, food_val, *threshold):
        self.name = name
        self.health = health
        self.food_val = food_val
        if threshold == 0:
            self.treshold = random.randint(0,4)
        else:
            self.threshold = threshold

    def get_food_value(self):
        return self.food_val

    def go_to_heaven(self):
        self.get_place().add_object(Food(self.get_name() + " meat", self.get_food_value))
        return super().go_to_heaven()

def test_task5():
    print('=== Task 5a ===')
    bear = Animal('bear', 20, 10, 3)
    print(bear.get_threshold())             # 3
    print(bear.get_food_value())            # 10

    deer = Animal('deer', 15, 6)
    print(deer.get_threshold())             # Random value between 0 and 4 inclusive

    print('=== Task 5b ===')
    BASE.add_object(bear)
    print(named_col(BASE.get_objects()))    # ['bear']
    print(bear.get_place().get_name())      # Base
    bear.go_to_heaven()                     # bear went to heaven!
    print(named_col(BASE.get_objects()))    # ['bear meat']

# uncomment to test task5
#test_task5()