from time import *
sum=0
def probfind(p,q,N):
	sum=0
	for i in range(1,N):
		sum=sum+((p)**i)*(q**(i-1))*(1-q)
	return {'sum': sum, "last": i}

M=1000000
s=time()
a=probfind(0.7,0.8,M)["sum"]*probfind(0.85,0.85,M)["sum"]*probfind(0.95,0.9,M)["sum"]+probfind(0.7,0.8,M)["sum"]*probfind(0.85,0.9,M)["sum"]*probfind(0.9,0.85,M)["sum"]+probfind(0.7,0.9,M)["sum"]*probfind(0.75,0.8,M)["sum"]*probfind(0.9,0.85,M)["sum"]+probfind(0.7,0.9,M)["sum"]*probfind(0.75,0.85,M)["sum"]*probfind(0.85,0.8,M)["sum"]+probfind(0.7,0.85,M)["sum"]*probfind(0.8,0.8,M)["sum"]*probfind(0.95,0.9,M)["sum"]+probfind(0.7,0.85,M)["sum"]*probfind(0.8,0.9,M)["sum"]*probfind(0.85,0.8,M)["sum"]
t=time()
print a,t-s
