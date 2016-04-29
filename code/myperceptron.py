import numpy
positive=open("positive.txt","r")
p=positive.read()
pline=p.split("\n")

negative=open("negative.txt","r")
n=negative.read()
nline=n.split("\n")

#initialize
W=[0,0,0] 	#<0,0,.....,0,0>
b=0
U=[0,0,0]	#<0,0,.....,0,0>
beta=0
c=1
MaxIter=100

for i in range(0,MaxIter):
	y=1
	for line in pline:
		#print(line)	
		x=map(int, line.split())
		#x=line.split() #attributes
		#print(x)
		wx=numpy.multiply(W,x)
		a=sum(wx)+b
		ya=y*a
		if(ya<=0):
			yx=numpy.multiply(x,y)

			W=numpy.add(W,yx)
			b+=y
			ycx=numpy.multiply(yx,c)
			U=numpy.add(U,ycx)
			beta+=y
		else:
			c+=1	
	y=-1
	for line in nline:
		#print(line)	
		x=map(int, line.split())
		#x=line.split() #attributes
		#print(x)
		wx=numpy.multiply(W,x)
		a=sum(wx)+b
		ya=y*a
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

print(W)
print(b)
