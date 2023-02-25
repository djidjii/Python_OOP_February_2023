class Hero:
    def __int__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        self.health -= damage

        if self.health <= 0:
            self.health = 0

            return