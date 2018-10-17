from match import Matcher

G1 = dict((g1m, prefs.split(', ')) for [g1m, prefs] in (line.rstrip().split(': ')
                                for line in open('men.txt')))

G2 = dict((g2m, prefs.split(', ')) for [g2m, prefs] in (line.rstrip().split(': ')
                                for line in open('women.txt')))

match = Matcher(G1, G2)

def is_stable(g2groups, verbose=False):
    for g2m, g1m in g2groups.items():
        i = G1[g1m].index(g2m)
        preferred = G1[g1m][:i]
        for p in preferred:
            h = g2groups[p]
            if G2[p].index(g1m) < G2[p].index(h):
                msg = "{}'s marriage to {} is unstable: " + \
                      "{} prefers {} over {} and {} prefers " + \
                      "{} over her current husband {}"
                if verbose:
                    print msg.format(g1m, g2m, g1m, p, g2m, p, g1m, h)
                return False
    return True

g2groups = match()
assert is_stable(g2groups)             # should be a stable matching
assert match.is_stable()            # should be a stable matching

# swap the husbands of two g2groups, which should make the matching unstable
g2groups['fay'], g2groups['gay'] = g2groups['gay'], g2groups['fay']

assert is_stable(g2groups) is False    # should not be a stable matching

# with the perturbed matching we find that gav's marriage to fay is unstable:
#
#   * gav prefers gay over fay
#   * gay prefers gav over her current husband dan
