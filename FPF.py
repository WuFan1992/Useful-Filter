#!/usr/bin/env python


import numpy as np


def FPF(img,c,fp):
	#get the length and the width of img, 
	height = img.shape[0]
	width =  img.shape[1]
	# img must be a grid_scale image and normalising
	D = (np.pow(abs(img),fp)).sum(0)
	D = D/width
	#now D is a 1x width matrix
	Y = (img/np.sqrt(D)).transpose()
	Yc = Y.conjugate().transpose()
	Q = np.dot(Y,Yc)
	# if height = 1 , it means that Q is just a value not a matrix	
	if height == 1:
		Q = 1/Q
	else:
		Q = np.linaly.inv(Q)
	Rc = np.dot(Q,c)
	H = np.dot(Y,Rc)/np.sqrt(img)

	return H



		
		
	
			
	
