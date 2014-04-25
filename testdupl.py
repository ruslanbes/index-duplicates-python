### testing alorithms in http://stackoverflow.com/questions/5419204/index-of-duplicates-items-in-a-python-list
from collections import Counter, defaultdict

def _duplicates_eat(lst):
    cnt= Counter(lst)
    return [key for key in cnt.keys() if cnt[key]> 1]

def dupl_eat(lst):
    dup, ind= _duplicates_eat(lst), defaultdict(list)
    for i, v in enumerate(lst):
        if v in dup: ind[v].append(i)
    return ind
    
def dupl_utdemir(n):
    counter= Counter(n)
    dups=[i for i in counter if counter[i]!=1]
    result={}
    for item in dups:
        result[item]=[i for i,j in enumerate(n) if j==item] 
    return result
    
def _duplicates_lthaulow(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

def dupl_lthaulow(lst):
    return dict((x, _duplicates_lthaulow(lst, x)) for x in set(lst) if lst.count(x) > 1)
    
    
def dupl_pmcguire(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return dict([(key,locs) for key,locs in tally.items() 
                            if len(locs)>1])
                            
def dupl_ivazques_abrams(L):
    dups = defaultdict(list)
    for i, e in enumerate(L):
      dups[e].append(i)
    return dict([(k, v) for k, v in sorted(dups.iteritems()) if len(v) >= 2])
    
def dupl_rbespal(c):
	alreadyAdded = False
	dupl_c = dict()
	sorted_ind_c = sorted(range(len(c)), key=lambda x: c[x])
	
	for i in xrange(len(c) - 1):
		if c[sorted_ind_c[i]] == c[sorted_ind_c[i+1]]:
			if not alreadyAdded:
				dupl_c[c[sorted_ind_c[i]]] = [sorted_ind_c[i], sorted_ind_c[i+1]]
				alreadyAdded = True
			else:
				dupl_c[c[sorted_ind_c[i]]].append( sorted_ind_c[i+1] )
		else:
			alreadyAdded = False
	return dupl_c