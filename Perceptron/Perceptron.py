import numpy as np 

def sigmoid (x):
    return 1/(1 + np.exp(-x))

def pochodna(x):
    return x * (1 - x)

wejścia = np.array([[0,0],[0,1],[1,0],[1,1]])
wyjście = np.array([[0],[0],[1],[0]])

epoki = 1000
u = 0.1

wyjściowe_wagi = np.random.uniform(0.1,0.2,size=(2,1)).dot(np.random.choice([1.,3.])-2)
wejście_ukryte_wyjściowych = np.random.uniform(1,1,size=(1,1))

for i in range(epoki):
	
	wyjściowa_warstwa_aktywacja = np.dot(wejścia,wyjściowe_wagi)
	wyjściowa_warstwa_aktywacja += wejście_ukryte_wyjściowych
	przewidywane_wyjście = sigmoid(wyjściowa_warstwa_aktywacja)

	blad = wyjście - przewidywane_wyjście
	d_przewidywane_wyjście = blad * pochodna(przewidywane_wyjście)
	
	wyjściowe_wagi += wejścia.T.dot(d_przewidywane_wyjście) * u
	wejście_ukryte_wyjściowych += np.sum(d_przewidywane_wyjście,axis=0,keepdims=True) * u

print("Wyjście z sieci neuronowej po 1,000 epok: ",end='')
print(*przewidywane_wyjście)