from scipy.interpolate import interp1d

import numpy as np

rn=np.random.normal
class bol_func:
	"""
	Class to store all functions required for evaluating parameters from bolometric light curves (calculated using mklcbol.pro)

	Functions also to calculate the rise from half maximum a la contardo 2000


	"""

	def bolpeak(self, fil):
		"""
		Interpolate to find bolometric peak ##TOADD: exceptions for when the peak is not measured
		
		note: written on top of interp1d from scipy.interpolate (boss function it is!)
		"""
		lc=np.loadtxt(fil)
		ter=interp1d(lc[:,0], lc[:,1], kind='cubic')
		l=np.linspace(lc[:,0].min(), lc[:,0].max())
		gpl=ter(l)
		return max(gpl), l[gpl==max(gpl)][0]
	def dm15_bol(self,fil):

		"""

		Delta m 15 for the bolometric light curve 
		"""
		lc1=np.loadtxt(fil)
		
		sp=interp1d(lc1[:,0], lc1[:,1], kind='cubic')
		
		l=np.linspace(min(lc1[:,0]), max(lc1[:,0]), 100)
		
		gp=np.log10(sp(l))
		
		tm=l[gp==max(gp)]
		
		ph=lc1[:,0]-tm
		
		if min(ph)<0 and max(ph)>15:
		
			ph1=abs(l-15)
			m15=gp[ph1==min(ph1)][0]
		
			return max(gp)-m15#np.log10(max(gp))-np.log10(m15)	
		else:
			return 99.0
def spl_fit(arr, val):
	"""
	interpolate value for Nickel mass
	"""
	real=rn(arr[:,0], arr[:,1])
	terp=interp1d(real, rn(arr[:,2], arr[:,3]), kind='cubic')
	l=np.linspace(real.min(), real.max())
	gpl=terp(l)
	l1=abs(l-val)
	return gpl[l1==min(l1)][0]
def arn_coef(rt, alp=1):
	"""
	For a given rise time, calculate the coefficient for the relation between Nickel mass and peak bolometric luminosity (arnett's rule, instantaneous energy deposition is output energy at max )
	

	Default alpha is 1 (arguments in Branch+ 1992, stritzinger 2006)
	"""

	eni=6.45e43*np.exp(-rt/8.8)+1.45e43*np.exp(-rt/111.1)

	return alp*eni/1e43

def arn_coef_mc(n, rt=[19, 3], alp=1):
	"""
	n realisations of the coefficient from arnett's rule

	rise time value, default from Stritzinger+

	"""

	ar=[arn_coef(rn(rt[0], rt[1]), alp=1) for k in range(n)]	

	return np.mean(ar), np.std(ar)

def t_half_rise(fil, kind):
	"""
	Calculate the time to rise to max from half the luminosity 
	
	kind: spline, polyfit
	"""
	
	peak=bol_func().bolpeak(fil); tmax=peak[1]
	#load LC
	lc=np.loadtxt(fil)
	#use only the pre-max light curve 
	ph=lc[:,0]-tmax
	ph1=ph[ph<0]; mag1=lc[:,1][ph<0]
	
	if kind == "spline":
		
	
		spl=interp1d(ph1, mag1, kind='cubic')
		l=np.linspace(ph1.min(), ph1.max()); gpl=spl(l)
		arr=abs(gpl-(peak[0]/2.0))
		minval=l[arr==min(arr)][0]
		
		if minval>min(ph):
			return minval
		else:
			return 99.0	

	if kind=="polyfit":
		coef=np.polyfit(ph1, mag1, 2.0)
		lp=np.linspace(-20, 0.0)
		magval=coef[0]*(lp**2)+coef[1]*lp+coef[2]
		mhalf=peak[0]/2.0
		thalf=lp[abs(magval-mhalf)==min(abs(magval-mhalf))]
		
		return thalf
	






