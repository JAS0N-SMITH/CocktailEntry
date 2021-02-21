class Cocktail:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.ingredients = kwargs.get("ingredients")
        self.directions = kwargs.get("directions")
        self.image = kwargs.get("image")

    def print(self):
        return (f"{self.name},\n{self.ingredients},\n"
                f"{self.directions},\n{self.image}")
