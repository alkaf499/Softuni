from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []


    def assign_player(self, player: Player):
        if player in self.players:
            return f'Player {player.name} is already in the guild.'

        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):

        try:
            player = next(filter(lambda  p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        player.guild = "Unaffiliated"
        self.players.remove(player)

        return f"Player {player_name} has been removed from the guild."


    def guild_info(self):
        result = [f"Guild: {self.name}"]
        for a in self.players:
            result.append(a.player_info())

        return "\n".join(result)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
