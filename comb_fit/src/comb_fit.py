import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt

from time import time
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D
#define path to the second maximum files
start=time()
pt='/home/sdhawan/tests_paper/csp_sn/sec_max_files/'

#function to define arrays
def arr_def():
	#load the x1, x2, y files
	jb=np.loadtxt(pt+'j_sec_max_csp.dat', dtype='string')
	yb=np.loadtxt(pt+'y_sec_max_csp.dat', dtype='string')
	fl=np.loadtxt('../../tables/u_flags.txt', dtype='string', skiprows=1)
	
	#define the arrays
	lb=np.array([float(i[1]) for i in fl if i[0] in jb[:,0] and i[0] in yb[:,0]])
	yt2=np.array([float(yb[yb[:,0]==i[0]][0][1]) for i in fl if i[0] in jb[:,0] and i[0] in yb[:,0]])
	jt2=np.array([float(jb[jb[:,0]==i[0]][0][1]) for i in fl if i[0] in jb[:,0] and i[0] in yb[:,0]])
	
	#error arrays
	elb=np.array([float(i[2]) for i in fl if i[0] in jb[:,0] and i[0] in yb[:,0]])
	eyt2=np.array([float(yb[yb[:,0]==i[0]][0][2]) for i in fl if i[0] in jb[:,0] and i[0] in yb[:,0]])
	ejt2=np.array([float(jb[jb[:,0]==i[0]][0][2]) for i in fl if i[0] in jb[:,0] and i[0] in yb[:,0]])
	
	#names of the SNae in the three arrays
	nm=np.array([i[0] for i in fl if i[0] in jb[:,0] and i[0] in yb[:,0]])
	
	arr=np.vstack([nm, lb, elb, yt2, eyt2,  jt2, ejt2]).T
	arr1=np.vstack([nm, lb, yt2, jt2]).T
	#np.savetxt('../../out_files/bivar_regress.txt', arr1, fmt='%s')
	
	#stack arrays in a shape that is readable by sm modules
	x1=np.vstack([yt2, jt2]).T
	x=np.vstack([x1[:,0], x1[:,1], np.ones(len(yt2))]).T
	x=sm.add_constant(x)
	
	#perform regression
	est=sm.OLS(lb, x).fit()
	
	return est, lb, yt2, jt2
def plot_3d():
	#load arrays and coefs
	r=arr_def()
	#
	xx1, xx2=np.meshgrid(np.linspace(r[2].min(), r[2].max(), 100), np.linspace(r[3].min(), r[3].max(), 100))	
	Z=r[0].params[0]*xx1+r[0].params[1]*xx2+r[0].params[2]
	fig = plt.figure(figsize=(12, 8))
	ax = Axes3D(fig, azim=-115, elev=15)
	surf = ax.plot_surface(xx1, xx2, Z, cmap=plt.cm.RdBu_r, alpha=0.6, linewidth=0)
	
	#scatter plot for the residuals
	
	#x=[r[2], r[3]]
	#resid=r[1]-r[0].predict(x)
	#ax.scatter(x[resid>=0][0],x[resid>=0][1], r[1][resid>=0], color='black', facecolor='white')
	#ax.scatter(x[resid<0][0],x[resid<0][1], r[1][resid<0], color='black')
def main():
	res=arr_def()
	plot_3d()
	#print res[1], res[2], res[3]
	#plt.show()
main()
end=time()
print "The complete combined fit code took" +str(end-start)+ "seconds"
