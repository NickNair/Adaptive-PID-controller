import matplotlib.pyplot as plt
import numpy as np

import RBF


def y(yd):


    rbf = RBF.RBF(0.13,0.21,0.25,0.9,0.98)

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
    yt_1 = 0.4
    yt_2 = 0.46
    yt_3 = 0.42

    initial_states = [ yt_1, yt_2 , yt_3]

    dt = 1/400

    Ki = -0.07709546
    Kd = 0.58844546
    Kp = -0.01747239

    ut_1 = 0


    y=[]
    x=[]

    
    for i in range(0, int(t/dt) ):

        e_t = yd[i] - yt_1
        del_y =  yt_1 - yt_2
        del2_y = yt_1 - 2*yt_2 + yt_3

        rbf.X[:,0] = [ e_t , -del_y ,  -del2_y]
        rbf.HiddenLayer()
        rbf.OutputLayer()
        
        
        ut_1 = ut_1 + rbf.K[1]*e_t - rbf.K[0]*del_y - rbf.K[2]*del2_y
        
        y1,y2,y3 = yt_1 , yt_2, yt_3

        yt_1 , yt_2, yt_3 = yt_1*yt_2*(yt_1 + 2.5) / ( 1 + yt_1**2 + yt_2**2 )+ ut_1 +np.random.normal(0,0.01) , yt_1 , yt_2 

        y0 = yt_1


        rbf.Update(yd[i],y0,y1,y2,y3)

        y.append(yt_1)
        x.append(i*dt)
        
    return y,x,initial_states


if __name__=="__main__":


    yd = [2.1 for i in range(100) ] + [3.5 for i in range(100) ] + [2 for i in range(100) ] +  [3 for i in range(100) ]


    ## Generate Reference array here

    y,x,i = y(yd)

    plt.plot(x,yd, label="Reference Signal")
    plt.plot(x,y,label ="Output")

    plt.title( " Initial States y(t-1) , y(t-2) and y(t-3) are " + str(i[0]) + ", " + str(i[1]) +" and "+ str(i[2]) )

    plt.legend()

    plt.ylabel(" Output from System ")
    plt.xlabel("Time (s)")


    plt.show()

