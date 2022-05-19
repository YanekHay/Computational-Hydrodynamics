import numpy as np


epsilion = 1e-3
N = 10            # x[] կոորդինատների զանգվածի չափը
M = 10            # y[] կոորդինատների զանգվածի չափը
J = 30 + 2* N**2  # k[] Ժամանակի զանգվածի չափը

A = 2 # Տրված ֆունկցիայի 'A' գործակիցը
b = 1 # Տրված ֆունկցիայի 'b' գործակիցը

x = np.zeros(N)             # Ստեղծում ենք համախատասխան 
y = np.zeros(M)             # զանգվածներ մեր տվյալները 
t = np.zeros(J)             # պահելու համար
T = np.zeros(((N,M,J)))     # -------------------------

def function(x,y):          # Մեզ տրված ֆունկցիայի նկարագրությունը
    return A * np.exp(-1 * b*((x-0.5)**2 + (y-0.5)**2))  

t[0] = epsilion        # Նկարագրում ենք զանգվածների առաջին, 
t[-1] = 1              # վերջին տարրերը և ամեն տարրի
                        # աճման քայլը  
x[0] = 0
x[-1] = 1
h_x = (x[-1]-x[0])/N

y[0] = 0
y[-1] = 1
h_y = (y[-1]-y[0])/M
tau=0.25*h_x**2        #

    # i is for indexes of x[]
for i in range(N):              # Լցնում ենք տարրերի զանգվածները
    x[i] = x[0] + h_x*i
# j is for indexes of y[]
for j in range(M):
    y[j] = y[0] + h_y * j
# k is for indexes of t[] (Time)
for k in range(J):
    t[k] = t[0] + tau * k

text = ""  #վերջնական արդյունքի բոլոր տարրերը տպվելու են այս փոփոխականի միջոցով

for k in range(J-1):           # Ցիկլերում ստանում ենք ջերմության փոփոխման
    for i in range(1,N-1,1):         # արդյունքները և դրանք լցնում եռաչափ զանգվածում
        for j in range(1, M-1, 1):         # ժամանակից x և y կոորդինատներից կախված
            T[i,j,k+1] = tau * ( (T[i+1,j,k] - 2 * T[i,j,k] + T[i-1,j,k])/(h_x**2)
                                    + (T[i,j+1,k] - 2 * T[i,j,k] + T[i,j-1,k])/(h_y**2)
                                    + function(x[i],y[j]) ) +  T[i,j,k]
            text += str(x[i]) + "  " + str(y[j]) + "  " + str(T[i, j, k]) + "\n"

#Արդյունքը տպում ենք 'result.txt' ֆայլի մեջ
with open('result.txt', 'w') as f:
    f.writelines(text)
