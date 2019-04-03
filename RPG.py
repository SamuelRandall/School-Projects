#  File: RPG.py
#  Description:
#  Student's Name: Samuel Randall
#  Student's UT EID: spr699
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 9/18/17
#  Date Last Modified: 9/22/17

# create class to define weapon attributes
class Weapon:

    def __init__(self, type):
        self.type = type
        self.damage = self.damage()

    def damage(self):

        # Assign the damage to each type of weapon
        type = self.type 
        if(type == "dagger"):
            return 4
        elif(type == "axe"):
            return 6
        elif(type == "staff"):
            return 6
        elif(type == "sword"):
            return 10
        elif(type == "none"):
            return 1

#does nothing right now
class Armor:
    
    def __init__(self, type):
        self.type = type
        self.armorClass = self.armorClass()
        
    def armorClass(self):
        type = self.type
        if(type == "plate"):
            return 2
        elif(type == "chain"):
            return 5
        elif(type == "leather"):
            return 8
        elif(type == "none"):
            return 10

# creates the character with certain specs
class RPGCharacter:

    def __init__(self):
        pass

    # assigning the proper weapon to a character upon creation
    def wield(self, weapon):
        if weapon.type in self.weaponTypes:
            print(self.name, "is now wielding a(n)", weapon.type)
            self.weapon = weapon
        else:
            print("Weapon not allowed for this character class.")

    # removal of a weapon for a character
    def unwield(self):
        print(self.name, "is no longer wielding anything.")
        self.weapon = Weapon("none")

    # assigning of the proper armor for the class
    def putOnArmor(self, armor):
        if armor.type in self.armorTypes:
            print(self.name, "is now wearing", armor.type)
            self.armor = armor
        else:
            print("Armor not allowed for this character class.")

    # removal of armor for a character        
    def takeOffArmor(self):
        print(self.name, "is no longer wearing anything.")
        self.armor = Armor("none")

    # creating the events of a battle
    def fight(self, opponent):
        print(self.name, "attacks", opponent.name, "with a(n)", self.weapon.type)
        opponent.health -= self.weapon.damage
        print(self.name, "does", self.weapon.damage, "damage to", opponent.name)
        print(opponent.name, "is now down to", opponent.health, "health")
        opponent.checkForDefeat()

    # print the stats of the character included in a print
    def __str__(self):
        return("\n" + str(self.name) +
                "\n   Current Health: " + str(self.health) +\
                "\n   Current Spell Points: " + str(self.spellPoints) +\
                "\n   Wielding: " + str(self.weapon.type) +\
                "\n   Wearing: " + str(self.armor.type) +\
                "\n   Armor class: " + str(self.armor.armorClass) +\
                "\n")
        '''
        return("   Current Health: %d" % self.health)
        return("   Current Spell Points: %d" % self.spellPoints)
        return("   Wielding: %s" % self.weapon.type)
        return("   Wearing: %s" % self.armor.type)
        return("   Armor class: %d" % self.armor.armorClass)
        '''

        
    # checks the character's health and decides if they are defeated or not
    def checkForDefeat(self):        
        if (self.health <= 0):
            print(self.name, "has been defeated!")

# defining of a fighters's attributes
class Fighter(RPGCharacter):
    maxHealth = 40
    maxSpellPoints = 0
    weaponTypes = ["dagger", "axe", "staff", "sword", "none"]
    armorTypes = ["plate", "chain", "leather", "none"]

    def __init__(self, name):
        self.name = name
        self.health = Fighter.maxHealth
        self.spellPoints = Fighter.maxSpellPoints
        self.weapon = Weapon("none")
        self.armor = Armor("none")

# defining of a wizard's attributes
class Wizard(RPGCharacter):
    maxHealth = 16
    maxSpellPoints = 20
    weaponTypes = ["dagger", "staff", "none"]
    armorTypes = ["none"]
    
    def __init__(self, name):
        self.name = name
        self.health = Wizard.maxHealth
        self.spellPoints = Wizard.maxSpellPoints
        self.weapon = Weapon("none")
        self.armor = Armor("none")

    # creation of the wizard's spells
    def castSpell(self, spell, target):
        if(spell in ["Fireball", "Lightning Bolt", "Heal"]):
            print(self.name, "casts", spell, "at", target.name)
        else:
            print("Unknown spell name. Spell failed.")
            return
        if(spell == "Fireball"):
            spellCost = -3
            effect = -5

            if(-spellCost > self.spellPoints):
                print("Insufficient spell points")
                return
            
            self.spellPoints += spellCost
            target.health += effect
            print(self.name, "does", -effect, "damage to", target.name)
            print(target.name, "is now down to", target.health, "health")
            target.checkForDefeat()

        elif(spell == "Lightning Bolt"):
            spellCost = -10
            effect = -10

            if(-spellCost > self.spellPoints):
                print("Insufficient spell points")
                return

            self.spellPoints += spellCost
            target.health += effect

            print(self.name, "does", -effect, "damage to", target.name)
            print(target.name, "is now down to", target.health, "health")
            target.checkForDefeat()

        elif(spell == "Heal"):

            spellCost = -6
            effect = 6

            if(-spellCost > self.spellPoints):
                print("Insufficient spell points")
                return
            newHealth = target.maxHealth - target.health
            if(newHealth < effect):
                effect = newHealth

            self.spellPoints += spellCost
            target.health += effect

            print(self.name, "heals", target.name, "for", effect, "health points.")
            print(target.name, "is now at", target.health, "health")
        
        
def main():

    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)
    
    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)
    
    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    print(gandalf)
    print(aragorn)

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    print(gandalf)
    print(aragorn)


main()
