#
# Note that written answers should be commented out to allow us to run your
# code easily while grading your problem set.

from hungry_games import *
import random



#################################################################################
#                                                                               #
# PASTE YOUR "Hungry Game Part I" CODE HERE                                               #
#                                                                               #
#################################################################################
class Weapon(Thing):
   
    def __init__(self, name, min_dmg, max_dmg):
        self.name = name
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.owner = None
    
    def min_damage(self):
        return self.min_dmg

    def max_damage(self):
        return self.max_dmg
    
    def damage(self):
        return random.randint(self.min_dmg, self.max_dmg)

class Ammo(Thing):
    def __init__(self, name, weapon, qty):
        self.name = name
        self.weapon = weapon.name
        self.qty = qty

    def get_quantity(self):
        return self.qty

    def weapon_type(self):
        return self.weapon

    def remove_all(self):
        self.qty = 0

class RangedWeapon(Weapon):
    def __init__(self, name, min_dmg, max_dmg):
        super().__init__(name, min_dmg, max_dmg)
        self.shots = 0
        self.owner = None
        
    def shots_left(self):
        return self.shots

    def load(self, ammo):
        if ammo.weapon_type() == self.name:
            self.shots += ammo.get_quantity()
            ammo.remove_all()

    def damage(self):
        if self.shots == 0:
            return 0
        else:
            self.shots -= 1
            return super().damage()


class Food(Thing):
    def __init__(self, name, food_val):
        self.name = name
        self.food_val = food_val
        self.owner = None

    def get_food_value(self):
        return self.food_val         
    
class Medicine(Food):
    def __init__(self, name, food_val, med_val):
        super().__init__(name, food_val)
        self.med_val = med_val
        self.owner = None

    def get_medicine_value(self):
        return self.med_val

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

#################################################################################
#                                                                               #
# Hungry Game Part II                                                            #
# TESTING CODE IS BELOW ALL THE TASKS                                           #
#                                                                               #
#################################################################################


############
##  Task1 ##
############

class Tribute(Person):


    ############
    #  Task 1a #
    ############
    def __init__(self, name, health, *threshold):
        # Tributes will not move by themselves, so set threshold to -1
        super().__init__(name, health, -1 )
        # add hunger property
        self.hunger = 0 



    ############
    #  Task 1b #
    ############
    # definition of get_hunger here
    def get_hunger(self):
        return self.hunger

    ############
    #  Task 1c #
    ############
    # definition of add_hunger here
    def add_hunger(self, hunger):
        self.hunger += hunger
        if self.hunger == 100:
            return super().go_to_heaven()
            



    ############
    #  Task 1d #
    ############
    # definition of reduce_hunger here
    def reduce_hunger(self, hunger):
        self.hunger -= hunger
        if self.hunger < 0:
            self.hunger = 0


    ############
    ##  Task2 ##
    ############
    # definition of eat here
    def eat(self, food):
        if food in self.get_inventory():
            self.hunger -= food.get_food_value()
            self.remove_item(food)
            if self.hunger < 0:
                self.hunger = 0
            if type(food) == Medicine:
                self.health += food.get_medicine_value()
                if self.health > 100:
                    self.health = 100
                    
class Tribute(Person):
    def __init__(self, name, health, *threshold):
        super().__init__(name, health, threshold)
    ############
    #  Task 3a #
    ############
    # definition of get_weapons here
    def get_weapons(self):
        weaps = ()
        for ele in self.get_inventory():
            if isinstance(ele, Weapon):
                weaps += (ele,)

        return weaps

    ############
    #  Task 3b #
    ############
    # definition of get_food here
    def get_food(self):
        f = ()
        for ele in self.get_inventory():
            if isinstance(ele, Food):
                f += (ele,)

        return f




    ############
    #  Task 3c #
    ############
    # definition of get_medicine here
    def get_medicine(self):
        meds = ()
        for ele in self.get_inventory():
            if isinstance(ele, Medicine):
                meds += (ele,)

        return meds

    #############
    ##  Task 4 ##
    #############
    #definition of attack here
    def attack(self, living_thing, weapon):
        health = living_thing.get_health()
        if living_thing in self.place.get_objects():
            if weapon in self.get_inventory(): 
                damage = weapon.damage()
                living_thing.reduce_health(damage)

            




#############
##  Task 5 ##
#############
# You can either draw it here or attach a image file when you submit.



################
# Testing Code #
################


def test_task1():
    print("===== Task 1b ======")
    cc = Tribute("Chee Chin", 100)
    print(cc.get_hunger())          # 0

    print("===== Task 1c ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    Base.add_object(cc)
    print(cc.get_place().get_name())    # base
    cc.add_hunger(50)
    print(cc.get_hunger())              # 50
    cc.add_hunger(50)                   # Chee Chin went to heaven!
    print(cc.get_hunger())              # 100
    print(cc.get_place().get_name())    # Heaven

    print("===== Task 1d ======")
    cc = Tribute("Chee Chin", 100)
    cc.add_hunger(10)
    print(cc.get_hunger())          # 10
    cc.reduce_hunger(20)
    print(cc.get_hunger())          # 0

# Uncomment to test task 1
# test_task1()

def test_task2():
    print("===== Task 2 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)

    cc.reduce_health(10)
    cc.add_hunger(4)
    print(named_col(cc.get_inventory()))    # []

    cc.eat(chicken)
    print(cc.get_hunger())                  # 4

    cc.take(chicken)                        # Chee Chin took chicken
    cc.take(aloe_vera)                      # Chee Chin took aloe vera
    print(named_col(cc.get_inventory()))    # ['chicken', 'aloe vera']

    cc.eat(aloe_vera)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 2

    print(named_col(cc.get_inventory()))    # ['chicken']

    cc.eat(chicken)
    print(cc.get_health())                  # 95
    print(cc.get_hunger())                  # 0
    print(named_col(Base.get_objects()))    # ['Chee Chin']

# Uncomment to test task 2
# test_task2()

def test_task3():
    print("===== Task 3 ======")
    cc = Tribute("Chee Chin", 100)
    chicken = Food("chicken", 5)
    aloe_vera = Medicine("aloe vera", 2, 5)
    bow = RangedWeapon("bow", 4, 10)
    sword = Weapon("sword", 2, 5)

    Base = Place("base")
    Base.add_object(cc)
    Base.add_object(chicken)
    Base.add_object(aloe_vera)
    Base.add_object(bow)
    Base.add_object(sword)

    cc.take(bow)                           # Chee Chin took bow
    cc.take(sword)                         # Chee Chin took sword
    cc.take(chicken)                       # Chee Chin took chicken
    cc.take(aloe_vera)                     # Chee Chin took aloe_vera

    print(named_col(cc.get_inventory()))   # ['bow', 'sword', 'chicken', 'aloe vera']
    print(named_col(cc.get_weapons()))     # ('bow', 'sword')
    print(named_col(cc.get_food()))        # ('chicken', 'aloe vera')
    print(named_col(cc.get_medicine()))    # ('aloe vera',)

# Uncomment to test task 3
# test_task3()

def test_task4():
    print("===== Task 4 ======")
    Base = Place("base")
    cc = Tribute("Chee Chin", 100)
    sword = Weapon("sword", 10, 10)
    bear = Animal("bear", 20, 10)

    Base.add_object(cc)
    Base.add_object(sword)
    Base.add_object(bear)
    

    print(bear.get_health())                # 20

    cc.attack(bear, sword)
    print(bear.get_health())                # 20

    cc.take(sword)                          # Chee Chin took sword
    cc.attack(bear, sword)
    print(bear.get_health())                # 10

    cc.attack(bear, sword)                  # bear went to heaven
    print(named_col(Base.get_objects()))    # ['Chee Chin', 'bear meat']

# Uncomment to test task 4
# test_task4()
