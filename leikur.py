import random
import sys
import time

# Version 1.1

#death = False

class life():
    """Klasinn sem heldur utan um líf leikmanns"""
    def __init__(self):
        self.countLife = 4
        self.gameOver = False
        self.death = False

    def __des__(self):
        print ("Þetta er destructor")

    def changeLife(self, death):
        if self.death == True:
            self.countLife -= 1
            self.death == False
        if self.countLife == 0:
            self.gameOver = True
        return self.countLife           # skilar fjölda lífa


class levelUp():
    """docstring for levelUp."""
    def __init__(self):
        self.level = 0
        self.gameVictory = False
        self.newLevel = 0
        self.isVictory = False

    def __des__(self):
        print ("Þetta er destructor")

    def setLevel(newLevel):
        level = newLevel

    def nextLevel(isVictory):
        if isVictory == True and level != 4:
            level += 1
        elif isVictory == True and level == 4:
            gameVictory = True




class Level():
    """docstring for Level."""
    def __init__(self):
        self.level = 0
        self.isVictory = False
        self.level1Done = False
        self.level2Done = False
        self.level3Done = False

    def overview(self):
        print("Velkominn á yfirlitssíðu leiksins. Hér getur þú valið um borð til þess að fara í.")
        while True:
            choise = int(input("Veldu borð (1/2/3/4): "))
            if choise == 1:
                print("  Þú hefur valið borð 1.")
                time.sleep(1)
                Level.level1(self)
            elif choise == 2 and self.level1Done == True:
                print("  Þú hefur valið borð 2.")
                time.sleep(1)
                Level.level2(self)
            elif choise == 3 and self.level2Done == True:
                print("  Þú hefur valið borð 3.")
                time.sleep(1)
                Level.level3(self)
            elif choise == 4 and self.level3Done == True:
                print("  Þú hefur valið borð 4.")
                time.sleep(1)
                Level.level4(self)
            elif choise == 2 or choise == 3 or choise == 4:
                print("  Þú hefur ekki aðgang að þessu borði. Vinsamlegast kláraðu borðið á undan fyrst.")
            elif choise == 0:
                print("  Þú hefur valið að hætta í leiknum.")
                sys.exit()
            else:
                print("Vitlaust val.")

    def level1(self):
        print("Velkomin/nn í borð 1.")
        levelOverview = Level()

        count = 0
        chance = False
        win = 0

        r = random.randint(1, 10)
        #print("Random: %d" % r)
        print("  Óþreyjufullir mótmælendur hafa valið tölu milli 1 og 10.")
        print("  Giskaðu á tölu frá 1 upp í 10 en gættu þín að fá ekki sömu tölu og mótmælendur.")
        guess = int(input("Hvaða tölu má bjóða þér? "))

        while count < 5:
            count += 1
            if guess == r and chance == True:
                print("  Ónei, þú hefur aftur valið sömu tölu!")
                print("  Lukkan er uppurin, þú þarft því miður að byrja upp á nýtt.")
                death = True
                newlife = life.changeLife(death)
                break
            elif guess == r and chance == False and count != 5:
                chance = True
                print("  Óheppin/nn, þú hefur valið sömu tölu og mótmælendurnir!")
                print("  Gæfan er þó með þér svo þú færð séns í viðbót.")
                count += 1
                r = random.randint(1, 10)
                #print("Random: %d" % r)
                guess = int(input("Hvaða tölu má bjóða þér? "))
            elif guess == r and chance == False and count == 5:
                print("  Óheppin/nn, þú hefur valið sömu tölu og mótmælendurnir!")
                print("  Það kemur þó ekki af sök þar sem þetta var seinasta umferðin.")
                print("Þú hefur sigrað þrautina!")
                self.isVictory = True
            elif count == 5:
                win += 1
                print("Þú hefur sigrað þrautina!")
                self.isVictory = True
            else:
                win += 1
                print("  Vel gert, þú blekktir mótmælendurna!")
                print("  Þú hefur sigrað %i sinnum." % (win))
                r = random.randint(1, 10)
                #print("Random: %d" % r)
                guess = int(input("Hvaða tölu má bjóða þér? "))

        print("Leikurinn er búinn.")
        if self.isVictory == True:
            self.level1Done = True
            self.isVictory = False
            playNext = input("Viltu fara áfram í næsta borð? (y/n): ").lower()
            if playNext == "y" or playNext == "yes":
                print("Þú ferð áfram í næsta borð")
                Level.level2(self)
            else:
                print("Þú ferð á upphafsreit")
                levelOverview.setLevel(0)
                print(levelOverview.level)
                Level.overview(self)
        else:
            playAgain = input("Viltu reyna aftur? (y/n): ").lower()
            if playAgain == "y" or playAgain == "yes":
                print("Þú byrjar upp á nýtt í borðinu")
                Level.level1(self)
            else:
                print("Þú ferð á upphafsreit")
                levelOverview.setLevel(0)
                print(levelOverview.level)
                Level.overview(self)

    def level2(self):
        print("Velkomin/nn í borð 2.")
        print("  Í þessu borði færðu fimm tilraunir til þess að giska á tölu sem óvinir Sigmundar á Alþingi hafa valið.")
        print("  Talan er á milli 1 og 100.")

        attempt = 0
        r = random.randint(1, 100)
        guess = int(input("Sláðu inn þitt gisk: "))

        while attempt < 5:
            attempt += 1
            if guess == r:
                print("  Til hamingju, þú hefur unnið!")
                self.isVictory = True
                break
            elif guess < r and guess >= 1:
                guess = int(input("  Of lágt. Reyndu aftur: "))
            elif guess > r and guess <= 100:
                guess = int(input("  Of hátt. Reyndu aftur: "))
            else:
                int(input("  Vitlaut gildi. Reyndu aftur: "))

        if self.isVictory == True:
            self.level2Done = True
            self.isVictory = False
            playNext = input("Viltu fara áfram í næsta borð? (y/n): ").lower()
            if playNext == "y" or playNext == "yes":
                print("  Þú ferð áfram í næsta borð")
                Level.level3(self)
            else:
                print("  Þú ferð á upphafsreit")
                #levelOverview.setLevel(0)
                #print(levelOverview.level)
                Level.overview(self)
        else:
            print("Þú tapaðir.")
            playAgain = input("Viltu reyna aftur? (y/n): ").lower()
            if playAgain == "y" or playAgain == "yes":
                print("Þú byrjar upp á nýtt í borðinu")
                Level.level2(self)
            else:
                print("Þú ferð á upphafsreit")
                levelOverview.setLevel(0)
                print(levelOverview.level)
                Level.overview(self)

    def level3(self):
        print("Þetta er borð 3.")
        playNext = input("Viltu fara áfram í næsta borð? (y/n): ").lower()
        if playNext == "y" or playNext == "yes":
            print("Þú ferð áfram í næsta borð")
            Level.level4(self)
        else:
            print("Þú ferð á upphafsreit")
            #levelOverview.setLevel(0)
            #print(levelOverview.level)
            Level.overview(self)

    def level4(self):
        print("Þetta er borð 4.")

    def setLevel(self, newLevel):
        self.level = newLevel


class Character():
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.points = 0
        self.countLife = 4

    def moveUp():           # færir leikmann upp um 1
        self.posy += 1

    def moveDown():         # færir leikmann niður um 1
        self.posy -= 1

    def moveRight():        # færir leikmann til hægri um 1
        self.posx += 1

    def moveLeft():         # færir leikmann til vinstri um 1
        self.posx -= 1




if __name__ == '__main__':

    life = life()
    levelUp = levelUp()
    levelOv = Level()
    death = False


    levelOv.overview()
