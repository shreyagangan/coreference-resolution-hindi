# coding=utf8
from collections import defaultdict

M={} #mentions (key),(class,NP,HN)
E = defaultdict(list)
#E={} #equivalence class (key),(M,MType)
outfile=open("output.txt","w+")
linefile=open("lines.txt","w+")
mentionfile=open("mentions.txt","w+")

f=open("new_ann.txt","r")
utf=f.read()
lines=utf.split("\n")
count=0

for line in lines:
    print(line)

    #get mentions:
    print("mentions")
    beg=0
    end=len(line)
    while(beg<end):
        if(line.find("[",beg)==-1):
            break
        start=line.find("[",beg)+1
        ending=line.find("]",beg)
        mention1=line[start:ending]
        print(mention1)
        info=mention1[mention1.find("<")+1:mention1.find(">")].split(",")
        eclasslist=map(int,info[0]);
        eclass=eclasslist[0]
        print(eclass)
        E[eclass].append({'m':count,'mtype':info[1]})
        hn=mention1[mention1.find("(")+1:mention1.find(")")]
        print(hn)
        np=mention1[mention1.find(">")+1:end]
        np=np.replace("(","")
        np=np.replace(")","")
        print(np)
        M[count]={'np':np,'hn':hn,'mtype':info[1]}
        beg=line.find("]",beg)+1
        count+=1
    print("\n")

print(E)
#print(M)



positive=set()
negative=set()
for eclass in E:
    #print(E[eclass])
    for i in range(0,len(E[eclass])-1):
        m1=E[eclass][i]['m']
        m2=E[eclass][i+1]['m']
        #print(E[eclass][i]['m'])
        #print(E[eclass][i+1]['m'])
        positive.add((m1,m2))

print("negative")

for i in range(1,len(E)+1):
    for j in range(i+1,len(E)+1):
        print(E[i])
        print(E[j])
        for e1 in E[i]:
            for e2 in E[j]:
                m1=e1['m']
                m2=e2['m']
                #print(m1)
                #print(m2)
                negative.add((m1,m2))
print(negative)        


attributes={}
#mtype
#hmatch
#submatch

#ematch
positivetrain=open("positive.txt","w+")



print(positive)
for (m1,m2) in positive:
    mtype=0 #1-T 2-F
    hmatch=0  #1-T 2-F
    submatch=0  #1-T 2-F
    mtype1=M[m1]['mtype']
    mtype2=M[m2]['mtype']
    hn1=M[m1]['hn']
    hn2=M[m2]['hn']
    if(mtype1==mtype2):
        mtype=1
    else:
        mtype=2
    #print(mtype)
    print("head")
    print(hn1)
    print(hn2)
    if(hn1==hn2):
        hmatch=1
    else:
        hmatch=2
    if(hn1 in hn2 or hn2 in hn1):
        submatch=1
    else:
        submatch=2
    print(submatch)
    positivetrain.write(str(mtype)+" "+str(hmatch)+" "+str(submatch)+" "+"\n")

negativetrain=open("negative.txt","w+")
print(negative)
for (m1,m2) in negative:
    mtype=0 #1-T 2-F
    hmatch=0  #1-T 2-F
    submatch=0  #1-T 2-F
    mtype1=M[m1]['mtype']
    mtype2=M[m2]['mtype']
    hn1=M[m1]['hn']
    hn2=M[m2]['hn']
    if(mtype1==mtype2):
        mtype=1
    else:
        mtype=2
    #print(mtype)
    print("head")
    print(hn1)
    print(hn2)
    if(hn1==hn2):
        hmatch=1
    else:
        hmatch=2
    if(hn1 in hn2 or hn2 in hn1):
        submatch=1
    else:
        submatch=2
    print(submatch)
    negativetrain.write(str(mtype)+" "+str(hmatch)+" "+str(submatch)+" "+"\n")

