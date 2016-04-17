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
        eclass=map(int,info[0]);
        print(eclass)
        E[eclass[0]].append({'m':count,'mtype':info[1]})
        hn=mention1[mention1.find("(")+1:mention1.find(")")]
        print(hn)
        np=mention1[mention1.find(">")+1:end]
        np=np.replace("(","")
        np=np.replace(")","")
        print(np)
        M[count]={'np':np,'hn':hn}
        beg=line.find("]",beg)+1
        count+=1
    print("\n")

print(E)
