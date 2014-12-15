import unittest
from score.score import *


class TestScore(unittest.TestCase):

    def test_score_object_returns_the_score(self):
        score = Score('team1',10, 0)
        self.assertEqual(score.score, 10)

    def test_score_is_initially_empty(self):
        team = Team()
        self.assertEqual({},team.team1) 
        self.assertEqual(len(team.team1),0)


