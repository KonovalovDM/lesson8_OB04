# Задача: Разработать простую игру, где игрок может использовать различные типы оружия для борьбы с монстрами.
# Программа должна быть спроектирована таким образом, чтобы легко можно было добавлять новые типы оружия,
# не изменяя существующий код бойцов или механизм боя.

from abc import ABC, abstractmethod

# Создаем абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self, fighter_name,target):
        pass

# Создаем конкретные типы оружия
class Sword(Weapon):
    def __init__(self, damage):
        self.damage = damage

    def attack(self, fighter_name, target):
        print(f"Боец {fighter_name} наносит удар мечом - {self.damage} урона нанесено {target}")
        target.health -= self.damage

class Bow(Weapon):
    def __init__(self, damage):
        self.damage = damage

    def attack(self, fighter_name, target):
        print(f"Боец {fighter_name} производит выстрел из лука - {self.damage} урона нанесено {target}")
        target.health -= self.damage

# Создаем класс бойца - Fighter
class Fighter:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack_count = 0 # Счетчик атак

    def attack(self, target):
        self.weapon.attack(self.name, target)
        self.attack_count += 1
        if self.attack_count >= 4:
            self.switch_weapon()

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f'{self.name} сменил оружие на {new_weapon.__class__.__name__.lower()}')

    def switch_weapon(self):
        # Смена оружия автоматически после 4х атак
        if isinstance(self.weapon, Sword):
            self.change_weapon(bow)
        elif isinstance(self.weapon, Bow):
            self.change_weapon(sword)
        self.attack_count = 0 # Сброс счетчика атак


class Monster:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

# Реализация боя
def battle(fighter, monster):
    while monster.health > 0:
        fighter.attack(monster)
        if monster.health <= 0:
            print(f'{fighter.name} победил {monster.name}!')
            break

# Пример использования
sword = Sword(damage=10)
bow = Bow(damage=5)

fighter = Fighter(name="Алеша Попович", health=100, weapon=sword)
monster = Monster(name="Змей Горыныч", health=70, damage=5)

# Демонстрация смены оружия и боя
fighter.change_weapon(sword)
battle(fighter, monster)

# Если монстр не побежден, сменим оружие и попробуем снова
if monster.health > 0:
    monster.health = 20  # восстановим здоровье монстра для повторного боя
    fighter.change_weapon(bow)
    battle(fighter, monster)





