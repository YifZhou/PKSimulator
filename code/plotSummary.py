import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('paper')

probList = [0.3, 0.5, 0.7, 0.8, 0.9, 0.95]
colors = plt.cm.viridis(np.linspace(0, 1, len(probList)))[::-1]
plt.close('all')
for i, prob in enumerate(probList[::-1]):
    summaryFileName = '../results/summary_{0:d}.dat'.format(int(prob*100))
    extraProb, t1WinRate = np.loadtxt(summaryFileName, unpack=True)
    plt.fill_between(extraProb*100, t1WinRate*100+1, t1WinRate*100-1,
                     lw=3, color=colors[i],
                     label='Prob={0:.0f}%'.format(prob*100),
                     alpha=.8)

plt.legend(loc='upper left')
plt.xlabel('Extra Probability [%]')
plt.ylabel('Team I Winning Percentage')
plt.title('Normal PK Shootout Patter')
plt.ylim([46, 84])
plt.savefig('../plot/T1win_vs_ExtraProb_normal.png', dpi=300)


plt.figure()
colors = plt.cm.magma(np.linspace(0, 1, len(probList)))[::-1]
for i, prob in enumerate(probList[::-1]):
    summaryFileName = '../results/summary_{0:d}_ABBA.dat'.format(int(prob*100))
    extraProb, t1WinRate = np.loadtxt(summaryFileName, unpack=True)
    plt.fill_between(extraProb*100, t1WinRate*100+1, t1WinRate*100-1,
                     lw=3, color=colors[i],
                     label='Prob={0:.0f}%'.format(prob*100),
                     alpha=.8)

plt.legend(loc='upper left')
plt.xlabel('Extra Probability [%]')
plt.ylabel('Team I Winning Percentage')
plt.ylim([46, 84])
plt.title('ABBA PK Shootout Patter')
plt.savefig('../plot/T1win_vs_ExtraProb_ABBA.png', dpi=300)
plt.show()
