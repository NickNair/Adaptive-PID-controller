import matplotlib.pyplot as plt
import numpy as np


def y(yd):


    # Initial Conditions 
    t = 1

    # Initial State 1
    # yt_1 = 1.1
    # yt_2 = 1.1
    # yt_3 = 1.1

    # Initial State 2 
    # yt_1 = 3.23
    # yt_2 = 0.32
    # yt_3 = 0.23

    # Initial State 3 
    yt_1 = 2.3
    yt_2 = 1.1
    yt_3 = 1.1



    initial_states = [ yt_1, yt_2 , yt_3]

    # Defining dt for 400 steps
    dt = 1/400

    # PID controller Parameters 
    Ki = 0.8
    Kd = 0.34
    Kp =  0.01



    # Initial Control Signal 
    ut_1 = 0


    y=[]
    x=[]
    et =[]
    
    for i in range(0, int(t/dt) ):

        # State Equations 
        e_t = yd[i] - yt_1
        del_y =  yt_1 - yt_2
        del2_y = yt_1 - 2*yt_2 + yt_3

        et.append(e_t)
        
        # Control Signal 

        ut_1 = ut_1 + Ki*e_t - Kp*del_y - Kd*del2_y
        
        # Passing Signal to Non-linear system

        yt_1,yt_2,yt_3 = yt_1*yt_2*(yt_1 + 2.5) / ( 1 + yt_1**2 + yt_2**2 )+ ut_1 +np.random.normal(0,0.01) , yt_1 , yt_2 

        y.append(yt_1)
        x.append(i*dt)
        
    return y,x,et,initial_states


if __name__=="__main__":


    # Reference Signal 
    yd = [2.5 for i in range(100) ] + [3.5 for i in range(100) ] + [1 for i in range(100) ] +  [3 for i in range(100) ] 


    ## Generate Reference array here

    y,x,et,i = y(yd)

    plt.plot(x,yd, label="Reference Signal")
    plt.plot(x,y,label ="Output")

    for j in et:
        print(j)

    plt.title( " Initial States y(t-1) , y(t-2) and y(t-3) are " + str(i[0]) + ", " + str(i[1]) +" and "+ str(i[2]) )

    plt.legend()

    plt.ylabel(" Output from System ")
    plt.xlabel("Time (s)")


    plt.show()

