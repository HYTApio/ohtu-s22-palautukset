class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def equal_score(self):
        scorenames = {0 : "Love-All", 1 : "Fifteen-All", 2 : "Thirty-All", 3 : "Forty-All", 4: "Deuce"}
        return scorenames[self.m_score1] if self.m_score1 < 4 else scorenames[4]

    def over_four_points(self):
        scorenames = {1 : "Advantage player1", 2 : "Win for player1", -2 : "Win for player2", -1 : "Advantage player2"}
        return scorenames[self.m_score1-self.m_score2] if abs(self.m_score1-self.m_score2) < 3 else scorenames[2] if self.m_score1 > self.m_score2 else scorenames[-2]
    
    def under_four_points(self):
        scorenames = {0 : "Love", 1 : "Fifteen", 2 : "Thirty", 3 : "Forty"}
        return f"{scorenames[self.m_score1]}-{scorenames[self.m_score2]}"

    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            score = self.equal_score()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.over_four_points()

        else:
            score = self.under_four_points()

        return score
