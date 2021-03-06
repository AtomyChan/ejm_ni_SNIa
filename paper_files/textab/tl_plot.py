import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['axes.linewidth']=2.5
tl=np.loadtxt('lira_tab.tex',  dtype='string', usecols=(0, 2, 4, 6, 8))
ni=np.loadtxt('../../arn_dev/tr_var_mni.dat', usecols=( 5, 4, 3,  2))
"""
function to plot 
t_L versus MNi
"""
def tlpl():	
	mni=[float(ni[ni[:,0]=='SN'+i[0]][0][1]) for i in tl if 'SN'+i[0] in ni[:,0]]
	emni=[float(ni[ni[:,0]=='SN'+i[0]][0][2]) for i in tl if 'SN'+i[0] in ni[:,0]]
	lr=[float(i[3]) for i in tl if 'SN'+i[0] in ni[:,0]]
	elr=[float(i[4][1:5]) for i in tl if 'SN'+i[0] in ni[:,0]]
	s=plt.subplot(111)
	print 'SN'+i[0] in ni[:,0]
	s.minorticks_on()
	s.tick_params('both', length=15, width=2, which='major')
	s.tick_params('both', length=7, which='minor')
	plt.errorbar(lr, mni, xerr=elr, yerr=emni, fmt='ro')
	plt.xlabel('$t_L$')
	plt.ylabel('$L_{max}$')
"""
histogram plots of MNi from different estimation methods (eg. ddc, arnett)
"""
def nicomp():
	plt.subplot(310)
	plt.xlabel('$M_{Ni}$')
	plt.hist(ni[:,0], alpha=0.3, color='g', label='DDC')
	plt.legend(loc=0)
	plt.subplot(311)
	plt.hist(ni[:,1], alpha=0.3, color='r',label='Arnett-fixed')
	plt.legend(loc=0)
	plt.subplot(312)
	plt.hist(ni[:,2], alpha=0.3, color='b', label='Arnett-var')
	plt.legend(loc=0)
	plt.ylabel('$N_{SN}$')
def niscat():
	s=plt.subplot(210)
	s.minorticks_on()
	s.tick_params('both', length=15, width=2, which='major')
	plt.xlabel('$M_{Ni}$')
	plt.errorbar(ni[:,1], ni[:,1]-ni[:,2], ni[:,3], fmt='ro', label='Arnett-var')
	plt.legend(loc=0)
	s=plt.subplot(211)
	s.minorticks_on()
	s.tick_params('both', length=15, width=2, which='major')
	plt.errorbar(ni[:,1], ni[:,1]-ni[:,0], ni[:,3], fmt='g^', label='DDC')
	plt.legend(loc=0)
	plt.ylabel('$DIF$')
niscat()

plt.show()











