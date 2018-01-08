import numpy as np
import pandas as pd
from collections import defaultdict
 
def hashJoin(df01, df02):
    h = defaultdict(list)
    g = defaultdict(list)
    feat1 = []
    feat2 = []

    # Find all features of two df
    for i in set(list(df01.columns)):
        if 'feature' in i:
            feat1.append(i)
    for i in set(list(df02.columns)):
        if 'feature' in i:
            feat2.append(i) 

    # Get all unique user_id
    user_ids = set(list(df01['usr_id']) + list(df02['usr_id']))

    # Init joined dict with all user_id and features
    # This helps to display joined into data frame
    feat_dict = dict.fromkeys(feat1 + feat2)
    joined = dict.fromkeys(user_ids, feat_dict)       

    # HASH PHASE
    for r in df01.iterrows():
        features = {f:r[1][f] for f in feat1}
        h[r[1]['usr_id']] = features

    for r in df02.iterrows():
        features = {f:r[1][f] for f in feat2}
        g[r[1]['usr_id']] = features

    # JOIN PHASE    
    for k_joined, v_joined in joined.items():
        if h[k_joined]:
            # a = {**dict1, **dict2} is to merge dict1 & dict2
            joined[k_joined] = {**v_joined, **h[k_joined]}

    for k_joined, v_joined in joined.items():
        if g[k_joined]:
            joined[k_joined] = {**v_joined, **g[k_joined]}

    return pd.DataFrame(joined).T   


def testHashJoin():
	df01 = pd.DataFrame({"usr_id":np.arange(10), "feature_1":np.random.randn(10), \
                     "feature_2":np.random.randn(10),\
                     "feature_3":np.random.randn(10)})
                    
	df02 = pd.DataFrame({"usr_id":np.arange(5,15), "feature_4":np.random.randn(10),\
	                     "feature_5":np.random.randn(10)})
	print(hashJoin(df01, df02))

testHashJoin()
