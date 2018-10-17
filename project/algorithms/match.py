from collections import defaultdict


class Matcher:

    def __init__(self, g1, g2):
        self.G1 = g1
        self.G2 = g2
        self.g2groups = {}
        self.groups = []

        self.g1rank = defaultdict(dict)
        self.g2rank = defaultdict(dict)

        for g1m, prefs in g1.items():
            for i, g2m in enumerate(prefs):
                self.g1rank[g1m][g2m] = i

        for g2m, prefs in g2.items():
            for i, g1m in enumerate(prefs):
                self.g2rank[g2m][g1m] = i


    def __call__(self):
        return self.match()

    def prefers(self, g2m, g1m, h):
        return self.g2rank[g2m][g1m] < self.g2rank[g2m][h]

    def after(self, g1m, g2m):
        i = self.g1rank[g1m][g2m] + 1
        return self.G1[g1m][i]

    def match(self, g1=None, next=None, g2groups=None):
        if g1 is None:
            g1 = self.G1.keys()
        if next is None:
            next = dict((g1m, rank[0]) for g1m, rank in self.G1.items())
        if g2groups is None:
            g2groups = {}
        if not len(g1):
            self.groups = [(h, g2m) for g2m, h in g2groups.items()]
            self.g2groups = g2groups
            return g2groups
        g1m, g1 = g1[0], g1[1:]
        g2m = next[g1m]
        next[g1m] = self.after(g1m, g2m)
        if g2m in g2groups:
            h = g2groups[g2m]
            if self.prefers(g2m, g1m, h):
                g1.append(h)
                g2groups[g2m] = g1m
            else:
                g1.append(g1m)
        else:
            g2groups[g2m] = g1m
        return self.match(g1, next, g2groups)

    def is_stable(self, g2groups=None, verbose=False):
        if g2groups is None:
            g2groups = self.g2groups
        for g2m, g1m in g2groups.items():
            i = self.G1[g1m].index(g2m)
            preferred = self.G1[g1m][:i]
            for p in preferred:
                h = g2groups[p]
                if self.G2[p].index(g1m) < self.G2[p].index(h):
                    msg = "{}'s marriage to {} is unstable: " + \
                          "{} prefers {} over {} and {} prefers " + \
                          "{} over her current husband {}"
                    if verbose:
                        print msg.format(g1m, g2m, g1m, p, g2m, p, g1m, h)
                    return False
        return True
