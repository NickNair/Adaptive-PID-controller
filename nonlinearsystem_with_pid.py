import matplotlib.pyplot as plt
import numpy as np


def y(yd):

    t = 1
    yt_1 = 0.9
    yt_2 = 1.1
    yt_3 = 1.1
    dt = 1/400

    Ki = 0.8
    Kd = 0.001
    Kp = 0.61

    ut_1 = 0


    y=[]
    x=[]

    
    for i in range(0, int(t/dt) ):

        e_t = yd[i] - yt_1
        del_y =  yt_1 - yt_2
        del2_y = yt_1 - 2*yt_2 + yt_3

        
        ut_1 = ut_1 + Ki*e_t - Kp*del_y - Kd*del2_y
        
        yt_1,yt_2,yt_3 = yt_1*yt_2*(yt_1 + 2.5) / ( 1 + yt_1**2 + yt_2**2 )+ ut_1 +np.random.normal(0,0.01) , yt_1 , yt_2 

        y.append(yt_1)
        x.append(i*dt)
        
    return y,x


if __name__=="__main__":


    yd = [2.5 for i in range(100) ] + [3.5 for i in range(100) ] + [1 for i in range(100) ] +  [3 for i in range(100) ] 


    ## Generate Reference array here

    y,x = y(yd)

    plt.plot(x,yd, label="Reference Signal")
    plt.plot(x,y,label ="Output")

    plt.legend()


    plt.show()

