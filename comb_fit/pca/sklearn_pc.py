from sklearn.decomposition import PCA

import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import sys

rn=np.random.normal

def pca_trans(arr):
	pca=PCA(n_components=1)
	pca.fit(arr)

	return pca.transform(arr)
def boots(arr, nsamp=1000):
	mean_ar=[]
	for num in range(nsamp):
		ar=[]
		for k in range(len(arr)):
			ind=int(len(arr)*np.random.uniform(0, 1))
			ar.append(arr[ind])
		mean_ar.append(np.mean(ar))
	return mean_ar
def main():
	
	inp=np.loadtxt('../../out_files/bivar_regress.txt', usecols=(1, 2, 3))

	X=inp[:,[1, 2]]
	
	ncomp=int(sys.argv[3])
	
	pca=PCA(n_components=ncomp)

	pca.fit(X)
	
	l=pca.transform(X)
	print "Doing an \t"+str(ncomp)+"\t component PCA \n\n----------------"
	#l[:,0]-=pca.mean_[0]
	
	#l[:,1]-=pca.mean_[1]
	
	res=sm.OLS(inp[:,0], l).fit()
	
	t2_new=float(sys.argv[1])
	err_t2_new=float(sys.argv[2])
	
	ar=np.array([rn(-0.0264, 0.004)*pca.transform([rn(t2_new, err_t2_new)])+np.mean(inp[:,0]) for k in range(1000)])
	
	print "The estimated L_max is\t "+ str(np.mean(ar)) 
	print "The error from the PCA is\t "+ str(np.std(ar))
	print  "Standard error on y mean is \t "+ str(np.std(inp[:,0])/np.sqrt(len(inp[:,0])))
	print "Error by bootstrapping is \t"+ str(np.std(boots(inp[:,0])))


main()






