class BasePokemon:
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __str__(self):
        return f'{self.name}/{self.poketype}'


class EmojiMixin:
    map_emoji = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡',
    }

    def __str__(self):
        self.poketype = self.map_emoji[self.poketype]
        return f'{self.name}/{self.poketype}'


class Pokemon(EmojiMixin, BasePokemon):
    pass


if __name__ == "__main__":
    bulbasaur = Pokemon(name='Bulbasaur', poketype='grass')
    print(bulbasaur)
