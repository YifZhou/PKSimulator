"""
a class for a soccer team taking penalty shootout
"""

import numpy as np


class Team:
    def __init__(self, basicProb, extraProb):
        """A team that is taking a penalty shootout.

        :param basicProb: basic probability
            of a player making a penalty
        :param extraProb: changes in basic probability
            that is correlated with current score
        """
        self.score = 0
        self.nTake = 0
        self.scoreBook = ['-', '-', '-', '-', '-']
        self.basicProb = basicProb
        self.extraProb = extraProb

    def successProb(self, otherScore):
        """calculate current success probability

        :param otherScore: current score of the opponent team
        :returns: prob
        :rtype: float (1 >= prob >= 0)

        """
        scoreDiff = self.score - otherScore
        prob = self.basicProb + scoreDiff * self.extraProb
        if prob < 0:
            return 0
        elif prob > 1:
            return 1
        else:
            return prob

    def takePenalty(self, otherScore, nRound):
        """Take a penalty, simulate if the penalty is made, update everything

        :param otherScore: current score of the other team
        :param nRound: number of current round (starts with 0)
        :returns: pkMade
        :rtype: int

        """
        prob = self.successProb(otherScore)
        pkMade = np.random.binomial(1, prob, 1)[0]
        # update scorebook, separate the scenario of first five rounds
        # or beyong five rounds
        if nRound < 5:
            if pkMade:
                self.scoreBook[nRound] = 'o'
            else:
                self.scoreBook[nRound] = 'x'
        else:
            if pkMade:
                self.scoreBook.append('o')
            else:
                self.scoreBook.append('x')
        self.score += pkMade
        self.nTake += 1
        return pkMade

    def reset(self):
        """ reset score and score book
        """
        self.score = 0
        self.nTake = 0
        self.scoreBook = ['-', '-', '-', '-', '-']
