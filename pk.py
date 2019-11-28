party = []

boxes = []


class pkbase():
    def __init__(self, name, baseHealth, baseAtt, baseDef, baseSpAtt, baseSpDef, baseSpeed, maxHealth, maxAtt, maxDef, maxSpAtt, maxSpDef, maxSpeed):
        self.name = name
        self.baseHealth = baseHealth
        self.baseAtt = baseAtt
        self.baseDef = baseDef
        self.baseSpAtt = baseSpAtt
        self.baseSpDef = baseSpDef
        self.baseSpeed = baseSpeed

        self.maxHealth = maxHealth
        self.maxAtt = maxAtt
        self.maxDef = maxDef
        self.maxSpAtt = maxSpAtt
        self.maxSpDef = maxSpDef
        self.maxSpeed = maxSpeed

charmander = pkbase("Charmander", 5, 5, 5, 5, 5, 5, 600, 500, 400, 300, 200, 100)
bulbasaur = pkbase("Bulbasaur", 5, 5, 5, 5, 5, 5, 200, 200, 200, 200, 200, 200)

class pk():
    def __init__(self, basepk, name, level, moves):
        self.basepk = basepk
        self.name = name
        self.level = level
        self.moves = []

        self.health = self.getHealth()
        self.attack = self.getAttack()
        self.defence = self.getDefence()
        self.spAttack = self.getSpAtt()
        self.spDefence = self.getSpDef()
        self.speed = self.getSpeed()

    def getHealth(self):
        return int(self.basepk.maxHealth*(self.level/100)+self.basepk.baseHealth)
    def getAttack(self):
        return int(self.basepk.maxAtt*(self.level/100)+self.basepk.baseAtt)
    def getDefence(self):
        return int(self.basepk.maxDef*(self.level/100)+self.basepk.baseDef)
    def getSpAtt(self):
        return int(self.basepk.maxSpAtt*(self.level/100)+self.basepk.baseSpAtt)
    def getSpDef(self):
        return int(self.basepk.maxSpDef*(self.level/100)+self.basepk.baseSpDef)
    def getSpeed(self):
        return int(self.basepk.maxSpeed*(self.level/100)+self.basepk.baseSpeed)

    
    


charchar = pk(charmander, "CharChar", 1, [])

print(charchar.health)
print(charchar.attack)
print(charchar.defence)
print(charchar.spAttack)
print(charchar.spDefence)
print(charchar.speed)




# ///////////////////////////////
# def getParty():
#     for p in party:
#         print(p.name)

print(charmander.name)

def game_loop():
    print("Hello")


game_loop()

# getParty()