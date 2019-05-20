class Enemy:
    life = 5

    def fight(self):
        print("So, bad")
        self.life -= 1

    def live(self):
        if self.life <= 0:
            print("Dead")
        else:
            print(self.life, " lives are left")


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.fight()
enemy1.fight()
enemy1. live()
enemy2. live()
