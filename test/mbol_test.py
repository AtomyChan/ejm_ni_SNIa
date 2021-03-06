import numpy as np
import matplotlib.pyplot as plt

import scipy

def bol_mag(lbol, lsun=4e33):
	return 4.8-2.5*np.log10(lbol*1e43/3.84e33)
def main():
	jj=np.loadtxt('../out_files/new_lbolhist_y.txt', skiprows=1, usecols=(1, 2))
	
	loss=np.loadtxt('li_loss_mr.dat', dtype='string', usecols=(0, 1,4,5,6))
	
	norm=loss[loss[:,2]=='IaN']
	mlss=norm[:,3].astype('float32')	
	
	mbol=bol_mag(jj[:,0])
	print np.median(mbol), np.median(mlss)
	
	print np.std(mbol)/np.sqrt(len(mbol)), np.std(mlss)/np.sqrt(len(mlss))
	plt.hist(mbol, alpha=0.3, label='from $t_2$')
	plt.hist(mlss, alpha=0.3, label='Li+2011')
	plt.xlabel('$M$')
	plt.ylabel('$N_{SN}$')
	plt.legend(loc=0)
	plt.show()
main()












