def hackathon1():
	# This Python 3 environment comes with many helpful analytics libraries installed
	# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
	# For example, here's several helpful packages to load in 

	import numpy as np # linear algebra
	import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

	# Input data files are available in the "../input/" directory.
	# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

	import os
	import pandas as pd

	pd.set_option('display.max_columns', 500)
	pd.set_option('display.max_rows',500)




	X_train_small.loc[X_train_small['isBid']==False,'ask_ratio'] = ((X_train_small[X_train_small['isBid']==False]['price'] - X_train_small[X_train_small['isBid']==False]['bestAsk']) / X_train_small[X_train_small['isBid']==False]['bestAsk'])*100
	X_train_small.loc[X_train_small['isBid']==False,'volume_ask_ratio'] = (X_train_small[X_train_small['isBid']==False]['volume']) / (X_train_small[X_train_small['isBid']==False]['bestAskVolume']) * 100

	X_train_small.loc[X_train_small['isBid']==True,'bid_ratio'] = ((X_train_small[X_train_small['isBid']==True]['price'] - X_train_small[X_train_small['isBid']==True]['bestBid']) / X_train_small[X_train_small['isBid']==True]['bestBid'])*100
	X_train_small.loc[X_train_small['isBid']==True,'volume_bid_ratio'] = (X_train_small[X_train_small['isBid']==True]['volume']) / (X_train_small[X_train_small['isBid']==True]['bestBidVolume']) * 100

	import copy 
	train = copy.copy(X_train_small)

	train['class'] = y_train_small

	for orderId in train[train['class']==1]['orderId'].unique():
	    display(train[train['orderId']==orderId])
	train['endUserRef'].unique()

	for orderId in train[train.endUserRef=='ERNFZXWDE']['orderId'].unique():
	    display(train[train['orderId']==orderId])

	train[train.endUserRef=='ERNFZXWDE'].to_csv('partial_output.csv')

	train[train['class']==2].to_csv('class2.csv')

	for orderId in train[train['class']==2]['orderId'].unique():
	    display(train[train['orderId']==orderId])

	train['ask_ratio'].value_counts() 


	train['pred'] = 0

	modified_train = train[(train.bid_ratio!=0)|((train.ask_ratio!=0))]

	time_diff = 20000
	count = 0
	num = modified_train.endUserRef.nunique()
	for userId in modified_train.endUserRef.unique():
	    print(count,'/',num)
	    count+=1
	    df_index = modified_train[modified_train.endUserRef==userId].index.to_list()
	    
	    for i in range(len(df_index)):
	        if modified_train.loc[df_index[i],'pred'] == 0:
	            for j in range(i+1, len(df_index)):
	                if (train.loc[df_index[j],'timestamp']-train.loc[df_index[i],'timestamp'])<=20000:
	                    if train.loc[df_index[j],'pred'] == 0:
	                        if modified_train.loc[df_index[i],'isBid']==True and modified_train.loc[df_index[i],'operation']=='INSERT' and modified_train.loc[df_index[j],'operation']=='CANCEL' and modified_train.loc[df_index[i],'bid_ratio']==modified_train.loc[df_index[j],'bid_ratio']:
	                            train.loc[df_index[i],'pred'] = 2
	                            train.loc[df_index[j],'pred'] = 2
	                            break
	                        elif modified_train.loc[df_index[i],'isBid']==False and modified_train.loc[df_index[i],'operation']=='INSERT' and modified_train.loc[df_index[j],'operation']=='CANCEL' and modified_train.loc[df_index[i],'ask_ratio']==modified_train.loc[df_index[j],'ask_ratio']:
	                            train.loc[df_index[i],'pred'] = 2
	                            train.loc[df_index[j],'pred'] = 2
	                            break
	                    #else: 
	                     #   df_index.pop(df_index[j])
	train[train.pred==2]


















