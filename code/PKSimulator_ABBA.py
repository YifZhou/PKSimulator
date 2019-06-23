"""
simulate a PK shootout with ABBA pattern
"""

from team import Team
import numpy as np


def isGameOver(t1, t2, iRound, print_result=False):
    """test if shootout shoud be ended
    """
    if iRound < 2:
        return False
    if 5 > iRound >= 2:
        if t1.score == t2.score:
            return False
        if t1.score > t2.score:
            t2Max = t2.score + 5 - t2.nTake
            if t1.score > t2Max:
                if print_result:
                    print(t1.score, '\t:\t', t2.core)
                    print(''.join(t1.scoreBook), '\t:\t', ''.join(t1.scoreBook))
                return True
            else:
                return False
        if t1.score < t2.score:
            t1Max = t1.score + 5 - t1.nTake
            if t1Max < t2.score:
                if print_result:
                    print(t1.score, '\t:\t', t2.core)
                    print(''.join(t1.scoreBook), '\t:\t', ''.join(t1.scoreBook))
                return True
            else:
                return False
    if iRound >= 5:
        if t1.nTake != t2.nTake:
            return False
        else:
            if t1.score == t2.score:
                return False
            else:
                if print_result:
                    print(t1.score, '\t:\t', t2.core)
                    print(''.join(t1.scoreBook), '\t:\t', ''.join(t1.scoreBook))
                return True


def pkSimulator(t1Prob, t1Extra, t2Prob, t2Extra,
                print_result=False):
    """Simulate a PK shootout

    :param t1Prob: basic probability for team1
    :param t1Extra: extra probability for team1
    :param t2Prob: basic probability for team2
    :param t2Extra: extra probability for team2
    :param print_result: if print the final result
    :returns: t1Win (if team1 win, return 1, else return 0), resultString
    :rtype: integer, string

    """
    t1 = Team(t1Prob, t1Extra)
    t2 = Team(t2Prob, t2Extra)

    iRound = 0
    while True:
        t1.takePenalty(t2.score, iRound)
        if isGameOver(t1, t2, iRound, print_result):
            break
        t2.takePenalty(t1.score, iRound)
        if isGameOver(t1, t2, iRound, print_result):
            break
        iRound += 1
        t2.takePenalty(t1.score, iRound)
        if isGameOver(t1, t2, iRound, print_result):
            break
        t1.takePenalty(t2.score, iRound)
        if isGameOver(t1, t2, iRound, print_result):
            break
        iRound += 1
    if t1.score > t2.score:
        t1Win = 1
        resultString = 't1\t{0}:{1}\t{2} : {3}'.format(t1.score,
                                                    t2.score,
                                                    ''.join(t1.scoreBook),
                                                    ''.join(t2.scoreBook))
    else:
        t1Win = 0
        resultString = 't2\t{0}:{1}\t{2} : {3}'.format(t1.score,
                                                    t2.score,
                                                    ''.join(t1.scoreBook),
                                                    ''.join(t2.scoreBook))
    return t1Win, resultString


if __name__ == '__main__':
    # prob = 0.9
    # extra = 0
    # t1win, resultString = pkSimulator(prob, extra, prob, extra)
    # print(resultString)
    probList = [0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
    extraList = np.linspace(0, 0.15, 16)
    for prob in probList:
        summaryFileName = '../results/summary_{0:d}_ABBA.dat'.format(int(prob*100))
        nT1WinList = np.zeros_like(extraList)
        for j, extra in enumerate(extraList):
            logFileName = '../results/{0:d}_{1:d}_ABBA.dat'.format(int(prob*100),
                                                             int(extra*100))
            nSim = 10000
            nT1Win = 0
            with open(logFileName, 'w') as f:
                for i in range(nSim):
                    t1Win, resultString = pkSimulator(prob, extra, prob, extra)
                    nT1Win += t1Win
                    f.write(resultString + '\n')
            nT1WinList[j] = nT1Win / nSim
        np.savetxt(summaryFileName, np.array([extraList, nT1WinList]).T)
        print('Result for prob={0:.1f}% saved'.format(prob*100))
