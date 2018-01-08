import numpy as np
import pandas as pd
from collections import defaultdict
 
def hashJoin(df01, df02):
	h = defaultdict(list)
	g = defaultdict(list)
	
	# hash phase
	for r in df01.iterrows():
	    h[r[1]['id']].extend([r[1]['feature_1'],r[1]['feature_2'],r[1]['feature_3']])
	for r in df02.iterrows():
	    g[r[1]['id']].extend([r[1]['feature_4'], r[1]['feature_5']])    
	
	# join phase    
	for k,v in g.items():
	    if h[k]:
	        #extend features
	        h[k].extend(g[k])
	    else: h[k] = v
	return h    

def testHashJoin():
	df01 = pd.DataFrame({"id":np.arange(10), "feature_1":np.random.randn(10), \
                     "feature_2":np.random.randn(10),\
                     "feature_3":np.random.randn(10)})
	df02 = pd.DataFrame({"id":np.arange(5,15), "feature_4":np.random.randn(10),\
	                     "feature_5":np.random.randn(10)})
	print(hashJoin(df01, df02))

testHashJoin()	
