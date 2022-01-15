import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.function_base import append

from singlearea import *

import RBF


def y(yd):

    rbf = RBF.RBF( aw = 0.0003, av = 0.021, au = 0.025 , asig = 0.01, gamma = 0.9)

    Tg = 0.08
    Tt = 0.3
    M = 0.2
    D = 0.01
    R = 2
    T = dt = 1/400

    yt_1 = 0
    yt_2 = 0 
    yt_3 = 0

    System = SingleArea( Tg , Tt , M , D , R , T , yt_1 , yt_2 , yt_3  )



    initial_states = [ yt_1, yt_2 , yt_3]

    plot_data = {"ut":[] , "pl" : [] , "delF":[] , 'KI' : [], 'KP' : [] , 'KD' : [] , "time" : []}


    Ki = 0
    Kd = 0
    Kp = 0

    ut_1 = 0

    t = 10

    y=[]
    x=[]

    
    for i in range(0, int(t/dt) ):

        # print(System.yt_1)
        e_t = 0 - System.yt_1
        del_y =  System.yt_1 - System.yt_2
        del2_y = System.yt_1 - 2*System.yt_2 + System.yt_3

        rbf.X[:,0] = [ e_t , -del_y ,  -del2_y]
        rbf.HiddenLayer()
        rbf.OutputLayer()
        
        
        # ut_1 = ut_1 + 0.00043*e_t - 0.01*del_y - 0*del2_y
        ut_1 = ut_1 + rbf.K[1]*e_t - rbf.K[0]*del_y - rbf.K[2]*del2_y
        
        plot_data["ut"].append(ut_1)


        
        PL = 0.2 if(  i*dt >= 0.2 ) else 0 
        plot_data["pl"].append(PL)
        
        Ut = [ [ut_1] , [ PL]  ]

        System.Output(Ut)

        print(rbf.K)

        rbf.Update(0 ,System.Y[0,0] ,System.yt_1 , System.yt_2, System.yt_3 )

        plot_data["delF"].append(System.Y[0,0])
        plot_data["time"].append(i*dt)
        plot_data["KI"].append(rbf.K[1])
        plot_data["KP"].append(rbf.K[0])
        plot_data["KD"].append(rbf.K[2])
        
    return plot_data,initial_states


if __name__=="__main__":


    yd = [0 for i in range(10*400) ] 


    ## Generate Reference array here

    plot_data,i = y(yd)


    plt.subplot(2,2,1)
    plt.plot(plot_data["time"],plot_data["pl"], label="Reference Signal")
    plt.title( "Load vs Time")
    plt.ylabel(" Output from System ")
    plt.xlabel("Time (s)")

    plt.subplot(2,2,2)
    plt.plot(plot_data["time"],plot_data["KI"], label="KI")
    plt.plot(plot_data["time"],plot_data["KP"], label="KP")
    plt.plot(plot_data["time"],plot_data["KD"], label="KD")
    plt.title( "KI, KP, KD vs Time")
    plt.ylabel("KI, KP, KD")
    plt.xlabel("Time (s)")
    plt.legend()
    
    plt.subplot(2,2,3)
    plt.plot(plot_data["time"],plot_data["ut"], label="Reference Signal")
    plt.title( "Control Signal vs Time")
    plt.ylabel("Control Signal")
    plt.xlabel("Time (s)")
    
    plt.subplot(2,2,4)
    plt.plot(plot_data["time"],yd, label="Reference Signal")
    plt.plot(plot_data["time"],plot_data["delF"],label ="Output")


    plt.title( " Initial States y(t-1) , y(t-2) and y(t-3) are " + str(i[0]) + ", " + str(i[1]) +" and "+ str(i[2]) )

    plt.legend()

    plt.ylabel(" Output from System ")
    plt.xlabel("Time (s)")


    plt.show()

