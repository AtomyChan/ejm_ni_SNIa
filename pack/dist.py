from scipy.interpolate import interp1d

import numpy as np

rn=np.random.normal
c=2.99e5
def h0_sne(M, zp):
	"""
	Hubble constant from SNe observed in different passbands

	"""
	val=M+25-zp
	h0=pow(10, 0.2*val)
	return h0

def h0_mc(M, zp, n):
	arr=np.array([h0_sne(rn(M[0], M[1]), rn(zp[0], zp[1])) for k in range(n)])
	return np.mean(arr), np.std(arr)

def h0_withcosm(dl, z, om=0.27, ol=0.73):
	q0=(om/2)-ol
	a=z*(1-q0)/(np.sqrt(1+2*q0*z)+1+q0*z )
	h0=(1+a)*c*z/dl
	return h0

def h0_nocosm(dl, z):
	return c*z/dl 
def arr_crt(fil1, fil2):
	a1=np.loadtxt(fil1, dtype='string')
	a2=np.loadtxt(fil2, dtype='string')
	arr1=[float(i[1]) for i in a1 if i[0] in a2[:,0]]
	arr2=[float(a2[a2[:,0]==i[0]][0][1]) for  i in a1  if i[0] in a2[:,0] ]
	return arr1, arr2




