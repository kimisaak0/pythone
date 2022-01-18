from asyncore import write
from xml.dom.expatbuilder import FilterVisibilityController


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"\n{self.name} 생성 // 체력 : {self.hp}, 속도 : {self.speed}", end=" ")

    def move(self, location) :
        print(f"\n{self.name} : {location} 방향으로 {self.speed}의 속도로 이동중입니다.", end=" ")

    def damaged(self, damage):
        self.hp -= damage
        print(f"\n{self.name}: {damage} 데미지를 입었습니다.", end=" ")
        print(f"\n{self.name}: 현재 체력 {self.hp}", end=" ")
        if self.hp <= 0 :
           print(f"\n{self.name}이 파괴되었습니다.", end=" ")

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
        print(f"공격력 : {self.damage}", end=" ")

    def attack(self, location) :
        print(f"\n{self.name}: {location} 방향을 공격 [데미지 {self.damage}]", end=" ")

class Flyable:
    def __init__(self) :
        self.bFly = True

class FlyingUnit(Flyable,Unit) :
    def __init__(self, name, hp, speed):
        Unit.__init__(self, name, hp, speed)
        Flyable.__init__(self)
        print(f"공중유닛 ", end=" ") 

    def move(self, location) :
        print(f"\n{self.name} : {location} 방향으로 {self.speed}의 속도로 날아갑니다. ", end=" ")

class FlyingAttackUnit(AttackUnit, Flyable) :
    def __init__(self, name, hp, speed, damage):
        super().__init__(name, hp, speed, damage)
        Flyable.__init__(self)

class Marine(AttackUnit) :
    def __init__(self, name="마린"):
        super().__init__(name, 40, 5, 10)
        self.bSteampack = False
    
    def steampack(self) :
        if self.bSteampack == False :
            if self.hp > 10 :
                print(f"\n{self.name} : 스팀팩 사용. [체력-10|속도*2'|'공격력+5]", end=" ")
                self.hp -= 10
                self.speed *= 2
                self.damage -= 5
                self.bSteampack = True
            else :
                print(f"\nhp가 부족하여 스팀팩을 사용할 수 없습니다.", end=" ")
        else :
            self.bSteampack = False
            print(f"\n{self.name} : 스팀팩 해제. [속도/2|공격력-5]", end=" ")
            self.hp -= 10
            self.speed *= 2
            self.damage -= 5
            self.bSteampack = False

class SeizeTank(AttackUnit) :
    def __init__(self, name="시즈탱크"):
        super().__init__(name, 150, 1, 35)
        self.bSeize = False
        self.bSeizeDevelop = False
    
    def seize_mode_develop(self) :
        if self.bSeizeDevelop == False :
            self.bSeizeDevelop = True
            print("\n시즈 모드가 개발되었습니다.", end=" ")
        else :
            print("\n시즈모드는 이미 개발되어 있습니다.", end=" ")

    def seize_mode_switch(self):
        if self.bSeizeDevelop == True :
            if self.bSeize == False :
                self.bSeize = True
                self.speed = 0
                self.damage *= 2
                print(f"\n{self.name} : 시즈모드가 되었습니다.", end=" ")
            else :
                self.bSeize = False
                self.speed = 1
                self.damage /= 2
                print(f"\n{self.name} : 시즈모드가 해제되었습니다.", end=" ")
        else :
            print("\n시즈모드가 아직 개발되지 않았습니다.", end=" ")

class Wraith(FlyingAttackUnit) :
    def __init__(self, name="레이쓰"):
        super().__init__(name, 80, 20, 5)
        self.bClocking = False

    def Clocking(self) :
        if self.bClocking == False :
            self.bClocking = True
            print(f"\n{self.name} : 클로킹 상태가 되었습니다.", end=" ")
        else :
            self.bClocking = False
            print(f"\n{self.name} : 클로킹 상태가 해제되었습니다.", end=" ")

def game_start() :
    print("\n[알림] 새로운 게임을 시작합니다.", end=" ")

def game_over() :
    print("\nplayer2 : gg", end=" ")
    print("\nplayer2가 게임을 나갔습니다.", end=" ")


game_start()

MarineList = list()
for i in range(0,12) :
    MarineList.append(Marine("마린"+str(i+1))) 

T1 = SeizeTank()
W1 = Wraith()

attack_unit = []
for i in range(0,12) :
    attack_unit.append(MarineList[i]) 
attack_unit.append(T1)
attack_unit.append(W1)

# for i in range(0,12) :
#     MarineList[i].move("1시")
#     MarineList[i].attack("2시")

T1.seize_mode_switch()
T1.seize_mode_develop()
T1.seize_mode_develop()
T1.seize_mode_switch()
T1.attack("2시")
T1.seize_mode_switch()

# 전군 공격
for Unit in attack_unit :
    Unit.move("1시")
    if isinstance(Unit,Marine) :
        Unit.steampack()
    elif isinstance(Unit,SeizeTank) :
        Unit.seize_mode_switch()
    elif isinstance(Unit,Wraith) :
        Unit.Clocking()
    Unit.attack("2시")

game_over()