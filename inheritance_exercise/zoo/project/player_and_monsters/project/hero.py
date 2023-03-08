class Hero:
    def __int__(self, username, level):
        self.username = username
        self.level = level

    def __str__(self) -> str:
        return f"{self.username} of type {self.__class__.__name__} has level {self.level}"
