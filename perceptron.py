import numpy
def avg_perceptron(D,MaxIter):
	W 	#<0,0,.....,0,0>
	b=0
	U	#<0,0,.....,0,0>
	beta=0
	c=1

	for(i in range(0,MaxIter)):
		for (x,y) in D:
			a=numpy.multiply(W,x)+b
			ya=numpy.multiply(a,y)
			if(ya<=0):
				yx=numpy.multiply(y,x)
				W=numpy.add(W,yx)
				b+=y
				ycx=numpy.multiply(yx,c)
				U=numpy.add(U,ycx)
				beta+=y
			else:
				c+=1	
	Un=numpy.divide(U,c)			
	betan=numpy.divide(beta,c)
	W=numpy.subtract(W,Un)			
	b=numpy.subtract(b,betan)			
	return (W,b)

