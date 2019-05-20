class Work:
    def __init__(self, x):
        self.var = x

    def get_check(self):
        print(self.var)


aditi = Work(5)
ted = Work(18)

aditi.get_check()
ted.get_check()


class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)


vine = Enemy(9)
adi = Enemy(18)

vine.get_energy()
adi.get_energy()

