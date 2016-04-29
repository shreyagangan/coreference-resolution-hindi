# coding=utf8
import numpy
from collections import defaultdict
import os

#M[count]={'np':np,'hn':hn,'mtype':info[0]}
#attributes
#mtype
#hmatch
#submatch
parameters=open("Output/parameters.txt","r")
param=parameters.read().split("\n")
print(param)
W=map(int,param[0].split(" "))
b=map(int,param[1].split())
print(W)
print(b)

folder_name="Test/"
for filename in os.listdir(folder_name):
    M={} #mentions (key),(class,NP,HN)
    E = defaultdict(list)
    #E ={} #(mention number)
    count=0
    ecount=0
    complete_path=folder_name+filename;
    f=open(complete_path,"r")
    utf=f.read()
    lines=utf.split("\n")
    lines=filter(None,lines)
    #print(lines[0])
    for line in lines:
        print("line:")
        print(line)
		#get mentions:
        print("mentions:")
        beg=0
        end=len(line)
        while(beg<end):
            if(line.find("[",beg)==-1):
                break
            start=line.find("[",beg)+1
            ending=line.find("]",beg)
            mention1=line[start:ending]
            info=mention1[mention1.find("<")+1:mention1.find(">")].split()
            mtype1=info[0]
            hn1=mention1[mention1.find("(")+1:mention1.find(")")]
            np1=mention1[mention1.find(">")+1:end]
            np1=np1.replace("(","")
            np1=np1.replace(")","")
            print("current mention:")
            print(mention1+" "+hn1+" "+mtype1)
            beg=line.find("]",beg)+1
            assigned=False
            maxvalue=-9999999
            maxindex=-1
            print("find argmax:")
            for m in M:
                  #print(m)
                  #M[m]['hn']
                  mtype=0 #1-T (-1)-F
                  hmatch=0  #1-T (-1)-F
                  submatch=0  #1-T (-1)-F
                  mtype2=M[m]['mtype']
                  hn2=M[m]['hn']
                  print("hn1:"+hn1)
                  print("hn2:"+hn2)
                  if(mtype1==mtype2):
                  	mtype=1
                  else:
                  	mtype=-1
                  if(hn1==hn2):
                  	hmatch=1
                  else:
                  	hmatch=-1
                  if(hn1 in hn2 or hn2 in hn1):
                  	submatch=1
                  else:
                  	submatch=-1
                  x=[mtype,hmatch,submatch]
                  print(x)
                  wx=numpy.multiply(W,x)
                  y=sum(wx)+b
                  print(y)
                  print("\n")
                  if(y>maxvalue):
                        maxvalue=y
                        maxindex=m    
            print("argmax done") 
            print("argmax")
            threshold=0
            if(maxvalue>=threshold): #add mention to that eq class
                  maxeclass=M[maxindex]['eclass']
                  M[count]={'np':np1,'hn':hn1,'mtype':mtype1, 'eclass':maxeclass}
                  E[maxeclass].append(count)
            else: #add mention to a new equivalence class
                  M[count]={'np':np1,'hn':hn1,'mtype':mtype1, 'eclass':ecount}
                  E[ecount].append(count)
                  ecount+=1
            #print(M[count])
            count+=1
        print("\n")
    print(len(M))  

    print("mentions:")
    for m in M:
      print(str(M[m]['hn'])+" "+str(M[m]['eclass']))

    outputfile=open("Coref_Res/ann_99.txt","w+")  
    print("eclass:")  
    print(len(E))
    for e in E:
    	outputfile.write(str(e)+":")
    	print(str(e)+":")
    	for m in E[e]:
    		print(str(M[m]['hn']))
    		outputfile.write(str(M[m]['hn'])+" ")
    	outputfile.write("\n")

