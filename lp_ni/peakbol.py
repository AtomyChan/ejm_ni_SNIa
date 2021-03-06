import numpy as np
import sys
import mag2fl as mf

#from bol_lc import lpeak_ni as ln

from scipy.interpolate import interp1d
pt='/home/sdhawan/bol_ni_ej/'

class ni2p:
	def p_est(self, ni, bnum, mn):
		val=np.loadtxt(pt+'lpeak_m56ni.dat', usecols=(1, 3, 4, 7))	
		if bnum==4:
			ind=1
		else:	
			ind=3
		ter=interp1d(val[:,mn], val[:,ind], kind='cubic')	
		l=np.linspace(min(val[:,mn]), max(val[:,mn]), 100)
		gp=ter(l)
		l1=abs(l-ni)
		return gp[l1==min(l1)]
	 	
print ni2p().p_est(float(sys.argv[1]), 8, int(sys.argv[2])), 
