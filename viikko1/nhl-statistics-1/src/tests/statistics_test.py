import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_search_name_returns_player(self):
        player = self.statistics.search("Semenko")
        self.assertAlmostEqual(player.name, "Semenko")
        self.assertAlmostEqual(player.team, "EDM")
        self.assertAlmostEqual(player.goals, 4)
        self.assertAlmostEqual(player.assists, 12)

    def test_search_name_returns_none(self):
        self.assertAlmostEqual(self.statistics.search("ö"), None)
    
    def test_team_returns_players(self):
        players = self.statistics.team("DET")
        self.assertAlmostEqual(players[0].name, "Yzerman")
        self.assertAlmostEqual(players[0].goals, 42)
        self.assertAlmostEqual(players[0].assists, 56)
    
    def test_top_returns_players(self):
        players = self.statistics.top(1)
        self.assertAlmostEqual(players[0].name, "Gretzky")
        self.assertAlmostEqual(players[0].team, "EDM")
        self.assertAlmostEqual(players[0].goals, 35)
        self.assertAlmostEqual(players[0].assists, 89)
        

