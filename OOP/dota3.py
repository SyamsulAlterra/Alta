import random
import subprocess as sp

class Hero():
    def __init__(self, name, maxDamage, defense, health):
        self.__name=name
        self.__maxDamage=maxDamage
        self.__defense=defense
        self.__health=health

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def getDefense(self):
        return self.__defense

    def attack(self):
        return random.randint(0, self.__maxDamage)

    def takeDamage(self, atck):
        if atck<=self.__defense:
            return self.__health
        else:
            self.__health-=atck-self.__defense

class Game():
    def __init__(self):
        name, maxAttack, defense, health=self.createHero()
        self.__hero1=Hero(name, maxAttack, defense, health)
        name, maxAttack, defense, health=self.createHero()
        self.__hero2=Hero(name, maxAttack, defense, health)
        self.__round=0
        print(self.__hero1.getName()+' vs '+self.__hero2.getName())

    def createHero(self):
        print('''
        Create your own Hero
        =====================
        Rules
        1. You get 100 point to create your hero status.
        2. Your hero attack + defense can't exceed 50.
        3. Your hero health is determined by points left after you define attack and defense for your hero.
        ''')
        print('Enter your hero name: ', end='')
        name=input()
        print('attack: ', end='')
        attack=input()
        attack=int(attack)
        print('defense: ', end='')
        defense=input()
        defense=int(defense)
        if attack+defense>50:
            sp.call('clear', shell=True)
            print('your previous hero is invalid, i told you not to spent more than 50 points in attack and defense')
            self.createHero()
        else:
            print('=================================')
            print('Your hero are succesfully created')
            print('Name: '+name)
            print('Attack: '+str(attack))
            print('Defense: '+str(defense))
            print('Health: '+str(100-attack-defense))
            print('Please take a look at your hero status, enter to continue')
            dummy=input()
            sp.call('clear', shell=True)

        return name,attack,defense,100-attack-defense

    def battle(self,hero1,hero2):
        print('================')
        print(hero2.getName()+' current health: '+str(hero2.getHealth()))
        attack=hero1.attack()
        hero2.takeDamage(attack)
        print(hero1.getName()+' do '+str(attack)+' attack')
        if hero2.getHealth()<=0:
            print(hero2.getName() + ' died')
            print(hero1.getName() + ' won the battle')
        else:
            print(hero2.getName()+ '('+str(hero2.getDefense())+')' +' has '+str(hero2.getHealth())+' health left')

    # def cekCondition(self):
    #     if self.__hero1.getHealth()<0:
    #         return 2
    #     elif self.__hero2.getHealth()<0:
    #         return 1
    #     else:
    #         return 0

    def start(self):
        while self.__hero1.getHealth()>0 and self.__hero2.getHealth()>0:
            self.__round+=1
            if (self.__round%2)==1:
                self.battle(self.__hero1, self.__hero2)
            else:
                self.battle(self.__hero2, self.__hero1)


        # if self.__hero1.getHealth()<0:
        #     print(self.__hero2.getName()+' win the battle')
        # elif self.__hero2.getHealth()<0:
        #     print(self.__hero1.getName()+' win the battle')



