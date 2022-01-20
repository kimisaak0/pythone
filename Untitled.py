class Unit:
	def __init__(self, name, hp, speed) :
		self.name = name
		self.hp = hp
		self.speed = speed

	def damaged(self, damage) :
		self.hp -= damage
		print(f"{self.name} : {damage}를 입었습니다. HP가 {self.hp} 남았습니다.")
		if self.hp <= 0 :
			print(f"{self.name} : 파괴되었습니다.")
	
	def move(self, location) :
		print("[지상유닛]", end=" ")
		print(f"{self.name} : {location}시 방향으로 {self.speed}의 속도로 이동합니다.")


class Attack:
	def __init__(self,damage) :
		self.damage = damage
	
	def attack(self,locataion) :
		print(f"{self.name} : {locataion}시 방향을 {self.damage}로 공격합니다.")

class AttackUnit(Unit,Attack) :
	def __init__(self, name, hp, speed, damage) :
		Unit.__init__(self, name, hp, speed)
		Attack.__init__(self, damage)
	
class Flyable :
	def __init__(self, bFly) :
		self.bFly = bFly

class FlyingUnit(Unit,Flyable) :
	def __init__(self, name, hp, speed, bFly):
		Unit.__init__(self, name, hp, speed)
		Flyable.__init__(self, bFly)

	def Move(self,location) :
		print("[공중유닛]", end=" ")
		print(f"{self.name} : {location}시 방향으로 {self.speed}의 속도로 날아갑니다.")

class FlyAttackUnit(FlyingUnit,Attack) :
	def __init__(self, name, hp, speed, damage, bFly):
		FlyingUnit.__init__(self, name, hp, speed, bFly)
		Attack.__init__(self,damage)

class BuildingUnit(Unit):
	def __init__(self, name, hp, location):
		pass

supply_depot = BuildingUnit("서플라이 디폿", 500, 7)

def game_start():
	print("[알림] 새로운 게임을 시작합니다.")

def game_over():
	pass


game_start()
game_over()