

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

"""
Question 3:
(a) A map for each of the individual bacteriums in the body.
    A map that encompasses all the bacterium in the body.
    I prefer reading 2.
(b) Every workplace within an organization.
    The workplace for every organization.
    I prefer reading 2.
(c) Both rooms had access to one private balcony.
    Both rooms had access to their own individual private balconies.
    I prefer reading 2.
(d) We distributed a survey to every member of the network.
    We distributed a survey to only members of the network.
    I prefer reading 1.
(e) No merchandise is evidence.
    Some, but not all merchandise is evidence.
    I prefer reading 2
"""
