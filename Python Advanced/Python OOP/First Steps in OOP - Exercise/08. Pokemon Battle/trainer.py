from project.pokemon import Pokemon

class Trainer():

    def __init__(self, name):
        self.pokemons = []
        self.name = name

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return f"This pokemon is already caught"

        pokemon.pokemon_details()
        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        try:
            pokemon = next(filter(lambda p: p.name == pokemon_name, self.pokemons))

        except StopIteration:
            return f"Pokemon is not caught"

        self.pokemons.remove(pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = []
        result.append(f"Pokemon Trainer {self.name}")
        result.append(f"Pokemon count {len(self.pokemons)}")
        [result.append(f"- {p.pokemon_details()}") for p in self.pokemons]

        return '\n'.join(result)
