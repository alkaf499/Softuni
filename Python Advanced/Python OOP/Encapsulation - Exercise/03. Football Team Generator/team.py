from project.player import Player

class Team:

    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if any(x.name == player.name for x in self.__players):
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        if all(x.name != player_name for x in self.__players):
            return f"Player {player_name} not found"
        for x in self.__players:
            if x.name == player_name:
                self.__players.remove(x)
                return x
