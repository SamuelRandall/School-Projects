import nltk

gramstring = r"""
% start S
S[SEM = <?np(?vp)>] -> NP[SEM=?np] VP[SEM=?vp]

VP[SEM=?vbar] -> VBAR[SEM=?vbar]

NP[SEM=<?det(?n)>] -> DET[SEM=?det] NBAR[SEM=?n]
NP[SEM=?pn] -> PN[SEM=?pn]
NP[SEM=?n] -> DET[SEM=?det] Adj[SEM=?adj] N[SEM=?n]

NBAR[SEM=?n] -> N[SEM=?n]

VBAR[SEM=?v] -> IV[SEM=?v]
VBAR[SEM=<?v(?np)>] -> TV[SEM=?v] NP[SEM=?np]
VBAR[SEM=<?cop(?np)>] -> COP[SEM=?cop] NP[SEM=?np]
VBAR[SEM=<?cop(?np)>] -> COP[SEM=?cop] Adj[SEM=?adj]

############## lexicon:

COP[SEM=<\X x.X(\y.equals(x,y))>] -> 'is'

DET[SEM=<\P Q.all x.(P(x) -> Q(x))>] -> 'every'
DET[SEM=<\P Q.exists x.(P(x) & Q(x))>] -> 'a'

IV[SEM=<\X x.X(\y.collapse(x, y))>] -> 'collapses'

IV[SEM=<\y.dance(y)>] -> 'dances'

N[SEM=<\y.boxer(y)>] -> 'boxer'
N[SEM=<\y.criminal(y)>] -> 'criminal'
N[SEM=<\y.woman(y)>] -> 'woman'
N[SEM=<\y.robber(y)>] -> 'robber'

Adj[SEM=<happy>] -> 'happy'

PN[SEM=<\X.X(vincent)>] -> 'Vincent'
PN[SEM=<\X.X(mia)>] -> 'Mia'

TV[SEM=<\X x.X(\y.kill(x, y))>] -> 'kills'
TV[SEM=<\X x.X(\y.know(x, y))>] -> 'knows'
TV[SEM=<\X x.X(\y.love(x, y))>] -> 'loves'
"""

inputs = ["Vincent dances", "every criminal kills a boxer",
          "Mia knows a happy boxer", "Vincent is happy", "Mia collapses"]

grammar = nltk.grammar.FeatureGrammar.fromstring(gramstring)

parser = nltk.parse.FeatureChartParser(grammar)

for sent in inputs:
    print("\nsentence:", sent, "\n")
    trees = parser.parse(sent.split())
    for tree in trees:
        print(tree)
