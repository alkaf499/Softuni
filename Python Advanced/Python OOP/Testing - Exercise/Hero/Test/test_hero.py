from unittest import TestCase, main

from project.hero import Hero


class TestmMamal(TestCase):
    def setUp(self):
        self.hero = Hero('Alex', 10, 400, 20)
        self.enemy = Hero("Eni", 10, 400, 20)
        self.enemy_1 = Hero("Eni", 10, 100, 20)

    def test_initialisation(self):
        self.assertEqual('Alex', self.hero.username)
        self.assertEqual(14, self.hero.level)
        self.assertEqual(50, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_battle_with_yourself_raise_execption(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_with_zero_health(self):
        with self.assertRaises(Exception) as ex:
            self.hero.username = "Bate"
            self.hero.health = 0
            self.hero.battle(self.enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_with_negative_health(self):
        with self.assertRaises(Exception) as ex:
            self.hero.health = -1
            self.hero.battle(self.enemy)
        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_with_enemy_with_zero_health(self):
        with self.assertRaises(Exception) as ex:
            self.enemy.health = 0
            self.hero.battle(self.enemy)
        self.assertEqual('You cannot fight Eni. He needs to rest', str(ex.exception))

    def test_battle_with_enemy_with_negative_health(self):
        with self.assertRaises(Exception) as ex:
            self.enemy.health = -1
            self.hero.battle(self.enemy)
        self.assertEqual('You cannot fight Eni. He needs to rest', str(ex.exception))

    def test_battle_health_after(self):
        self.hero.health = 200
        self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(205, self.enemy.health)

    def test_battle_draw(self):
        self.hero.health = 200
        self.enemy_1.health = 190
        result = self.hero.battle(self.enemy_1)

        self.assertEqual('Draw', result)


    def test_battle_hero_wins(self):
        result = self.hero.battle(self.enemy_1)
        self.assertEqual('You win', result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual(205, self.hero.health)

    def test_battle_enemy_wins(self):
        result = self.hero.battle(self.enemy)
        self.assertEqual('You lose', result)
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(25, self.enemy.damage)
        self.assertEqual(205, self.enemy.health)

    def test_repr(self):
        self.assertEqual("Hero Alex: 10 lvl\n" \
               f"Health: 400\n" \
               f"Damage: 20\n", str(self.hero))






if __name__ == '__main__':
    main()
