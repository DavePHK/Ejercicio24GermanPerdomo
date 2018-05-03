import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1,20,1000)
c = np.linspace(0.0001,100,1000)
xs = [1.2,2.5,2.8,5.0]

def funcion(c,x):
	return (1.0/c) * np.exp(-x/c)

def norm(c):
	return (np.exp(-1.0/c) - np.exp(-20.0/c))

def probxc(c,x):
	return (funcion(c,x)/norm(c))

probc = 0.01

PROBCX = []

for i in range(0,len(c)):
	aqui=1.0
	for j in range(0,len(xs)):
		aqui = aqui * probxc(c[i],xs[j])

	PROBCX.append(aqui)


plt.figure()
plt.scatter(c, PROBCX)
plt.title('Probabilidad dado mediciones')
plt.savefig('prob.pdf')




	


