import requests

class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.goals = goals
        self.assists = assists
        self.team = team
        self.nationality = nationality
        self.penalties = penalties
        self.games = games
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name: <21} {self.team} {self.assists} + {self.goals} = {self.points}"


class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    
    def get_players(self):
        players = []

        for player_dict in self.response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            players.append(player)
        
        return players

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = filter(lambda n: n.nationality == nationality, self.reader.get_players())
        sortedd = sorted(players, key=lambda x: x.points, reverse=True)
        return sortedd

        
    



