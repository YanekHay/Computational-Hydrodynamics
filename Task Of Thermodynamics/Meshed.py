import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

try:
    epsilion = 1e-3
    N = 10 # For length of y[]
    M = 10 # For length of x[]
    J = 10 + 2* N**2     # For Time

    A = 2 # Coeficent for the function
    b = 1 # Coeficent for the function

    x = np.zeros(N)
    y = np.zeros(M)
    t = np.zeros(J)
    T = np.zeros(((N,M,J)))
    #print(len(T[0][0]))
    def function(x,y):
        return A * np.exp(-1 * b*((x-0.5)**2 + (y-0.5)**2))

    def scale_number(unscaled, to_min, to_max, from_min, from_max):
        return (to_max-to_min)*(unscaled-from_min)/(from_max-from_min)+to_min



    t[0] = epsilion
    t[-1] = 1


    x[0] = 0
    x[-1] = 1
    h_x = (x[-1]-x[0])/N

    y[0] = 0
    y[-1] = 1
    h_y = (y[-1]-y[0])/M
    tau=0.25*h_x**2

    # i is for indexes of x[]
    for i in range(N):
        x[i] = x[0] + h_x*i
    # j is for indexes of y[]
    for j in range(M):
        y[j] = y[0] + h_y * j
    # k is for indexes of t[] (Time)
    for k in range(J):
        t[k] = t[0] + tau * k


    for k in range(J-1):
        for i in range(1,N-1,1):
            for j in range(1, M-1, 1):
                T[i,j,k+1] = tau * ( (T[i+1,j,k] - 2 * T[i,j,k] + T[i-1,j,k])/(h_x**2)
                                     + (T[i,j+1,k] - 2 * T[i,j,k] + T[i,j-1,k])/(h_y**2)
                                     + function(x[i],y[j]) ) +  T[i,j,k]

    #Find max T
    max = 0
    for k in range(J-1):
        for i in range(1,N-1,1):
            for j in range(1, M-1, 1):
                if(T[i,j,k]>max):
                    max = T[i,j,k]

    text = ""
    num =0
    fig = plt.figure()
    ax = plt.axes(projection='3d')

    x, y = np.meshgrid(x, y)
    z = np.zeros((N,M))

    def animate_func(num):
        ax.clear()  # Clears the figure to update the line, point,
                    # title, and axes
        print(num)
        # Updating Trajectory Line (num+1 due to Python indexing)

        for i in range(N):
            for j in range(M):
                z[i, j] = T[i, j, num]

        red = scale_number(T[i, j, num], 0, 1, 0, max+max/100)
        ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap="gist_heat", linewidth=0, antialiased=True)


        # Setting Axes Limits
        ax.set_xlim3d([0, 1])
        ax.set_ylim3d([0, 1])
        ax.set_zlim3d([0, max])

        # Adding Figure Labels
        ax.set_title('Time = ' + str(np.round(t[num],
                     decimals=2)) + ' sec')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('T')


        ax.view_init(num/10, num*2)
    numDataPoints = len(T[0][0])-1

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    angle = 50

    line_ani = animation.FuncAnimation(fig, animate_func, interval=30,frames=numDataPoints)

    plt.show()

    f = r"//Users/user/Desktop/animate_func3.gif"
    writergif = animation.PillowWriter(fps=30)
    line_ani.save(f, writer=writergif)

    # text += str(x[i]) + "  " + str(y[j]) + "  " + str(T[i, j, k]) + "\n"
    # with open('readme.txt', 'w') as f:
    #     f.writelines(text)
except KeyboardInterrupt:
    sys.exit()



