#estimate mb for highly reddened objects from their t2 measurements 

import mag2fl as mf		#mag2fl has the lc readout functions as well as the 
import numpy as np
import matplotlib.pyplot as plt 
import sys
arg=sys.argv

from scipy.stats import pearsonr
from scipy.odr	import *
rn=np.random.normal
def f(B, x):
	return B[0]*x+B[1]
fn=mf.spl_fit().bdmax
pt='/home/sdhawan/bol_ni_ej/'
pt1='/home/sdhawan/tests_paper/csp_sn/sec_max_files/'
pt2='/home/sdhawan/tests_paper/ni/files_snpy/'
dis=np.loadtxt('/home/sdhawan/dist_err_csp.txt', dtype='string', skiprows=1)
bred=np.loadtxt(pt+'burns14_ebv.tex', dtype='string', delimiter='&', usecols=(0, 5))
t=np.loadtxt(pt1+'j_sec_max_csp.dat', dtype='string')
dec=np.loadtxt(pt2+'tmax_dm15.dat', dtype='string')
'''
sb=[[float(t[t[:,0]=='SN'+i[0][0:-1]][0][1]),  fn('SN'+i[0][0:-1], 'B', 'csp')[0]-float(dis[dis[:,0]=='SN'+i[0][0:-1]][0][1])-3.1*float(i[1][3:7]), float(t[t[:,0]=='SN'+i[0][0:-1]][0][2]), float(dis[dis[:,0]=='SN'+i[0][0:-1]][0][2]), float(dec[dec[:,0]=='SN'+i[0][0:-1]][0][1])] for i in bred if float(i[1][3:7]) <0.1 and 'SN'+i[0][0:-1] in t[:,0] and 'SN'+i[0][0:-1] in dis[:,0]]
sb=np.array(sb)
sb=sb[sb[:,1]<0]
vs=np.vstack([sb[:,0], np.ones(len(sb))]).T
m=np.linalg.lstsq(vs, sb[:,1])[0]
rd=RealData(sb[:,0], sb[:,1], sx=sb[:,2], sy=sb[:,3])
f1=Model(f)
out=ODR(rd,f1,beta0=[1., 2.])
o=out.run()
arr=[rn(o.beta[0], o.sd_beta[0])*rn(28.13, 0.23)+rn(o.beta[1], o.sd_beta[1]) for j in range(1000)]
#print pearsonr(sb[:,0], sb[:,1]), np.mean(arr), np.std(arr), 
'''
rc=mf.t2corr().rcorr
plt.plot(rc(arg[1])[0], rc(arg[1])[1], 'r+')
plt.show()
