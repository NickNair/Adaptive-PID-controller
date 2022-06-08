import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.function_base import append

import warnings
warnings.filterwarnings("ignore")


from two_area import *

import neuralnetwork


def y(yd):

    PL1 = 0
    PL2 = 0

    # rbf = RBF.RBF( aw = 0.000065, av = 0.022, au = 0.025 , asig = 0.01, gamma = 0.95)
    
    nn1 = neuralnetwork.NeuralNetwork( aw = 0.000065, av = 0.022, au = 0.025 ,  gamma = 0.98)
    nn2 = neuralnetwork.NeuralNetwork( aw = 0.000065, av = 0.022, au = 0.025 ,  gamma = 0.98)

    # av=0.021,au = 0.025, aw = 0.0003asig = 0.01 gamma = 0.9

    # ( aw = 0.0003, av = 0.021, au = 0.025 , asig = 0.01, gamma = 0.9) ---> Steady State Error : 0.00474099
    # ( aw = 0.00008, av = 0.021, au = 0.025 , asig = 0.01, gamma = 0.9) ---> Steady State Error : 0.00037917 Settling Time ~ 70
    # ( aw = 0.00007, av = 0.021, au = 0.025 , asig = 0.01, gamma = 0.9)  ---> Steady State Error : 0.00033166 Settling Time ~ 60
    # ( aw = 0.000065, av = 0.022, au = 0.025 , asig = 0.01, gamma = 0.9) ---> Steady State Error : 0.00031556 Settling Time ~ 60
    # ( aw = 0.000065, av = 0.022, au = 0.025 , asig = 0.01, gamma = 0.98) ----> Steady State Error : 0.00118022

    



    Tg = 0.08
    Tp = 20
    Tt = 0.3
    Kp = 120
    T12 = 0.545/(2*np.pi)
    a12 = -1
    R = 5
    T = dt = 1/80
    beta1 = 0.425
    beta2 = 0.425

    yt_1 = 0
    yt_2 = 0 
    yt_3 = 0

    yt_1_ = 0
    yt_2_ = 0 
    yt_3_ = 0

    System = TwoAreaPS( Tg, Tp, Tt, Kp, T12, a12, R, T, beta1, beta2,  yt_1,yt_2,yt_3  , yt_1_ ,yt_2_,yt_3_  )



    initial_states = [ yt_1, yt_2 , yt_3 , yt_1_ , yt_2_ , yt_3_]

    plot_data = {"ut1":[] , "pl1" : [] , "delF1":[] , "ut2":[] , "pl2" : [] , "delF2":[]  , "time" : []}

    # KP1 = 1.32579169e-07
    # KI1 = 3.09193550e-04
    # KD1 = 1.91587817e-08
    
    # KP2 = 1.18316184e-07
    # KI2 = 2.70082882e-04
    # KD2 = 1.85194296e-08
    
    KP1 = -1.35204764e-06
    KI1 = 4.30298026e-04
    KD1 = -5.84913513e-07
    
    KP2 = -1.16255511e-06
    KI2 = 2.09594022e-04
    KD2 = -5.96951511e-07


    ut_1 = 0
    ut_2 = 0

    t = 200

    y=[]
    x=[]

    
    for i in range(0, int(t/dt) ):

        # print(System.yt_1)
        e_t_a1 = 0 - System.yt_1_a1
        del_y_a1 =  System.yt_1_a1 - System.yt_2_a1
        del2_y_a1 = System.yt_1_a1 - 2*System.yt_2_a1 + System.yt_3_a1

        e_t_a2 = 0 - System.yt_1_a2
        del_y_a2 =  System.yt_1_a2 - System.yt_2_a2
        del2_y_a2 = System.yt_1_a2 - 2*System.yt_2_a2 + System.yt_3_a2
        
        
        # ut_1 = ut_1 + 0.00043*e_t - 0.01*del_y - 0*del2_y
        ut_1 = ut_1 + KI1*e_t_a1 - KP1*del_y_a1 - KD1*del2_y_a1

        ut_2 = ut_2 + KI2*e_t_a2 - KP2*del_y_a2 - KD2*del2_y_a2
        
        
        plot_data["ut1"].append(ut_1)
        plot_data["ut2"].append(ut_2)

        # Load Graph 1 

        # if(  i*dt >= 40 ):
        #     PL = 0.2
        # elif ( i*dt >= 10 ):
        #     PL = 0.8
        # else:
        #     PL =  0

        # Load Graph 2 

        # if(  i*dt <=10 ):
        #     PL = 0.2
        # elif ( i*dt <= 20 ):
        #     PL = 0.3
        # elif ( i*dt <= 30 ):
        #     PL = 0.4
        # elif ( i*dt <= 40 ):
        #     PL = 0.5
        # elif ( i*dt <= 50 ):
        #     PL = 0.6
        # else:
        #     PL =  0.6

        # Load Graph 3

        # if(  i*dt <=10 ):
        #     PL = 0.2
        # elif ( i*dt <= 20 ):
        #     PL = 0.3
        # elif ( i*dt <= 30 ):
        #     PL = 0.4
        # elif ( i*dt <= 40 ):
        #     PL = 0.5
        # elif ( i*dt <= 50 ):
        #     PL = 0.6
        # elif ( i*dt <= 60 ):
        #     PL = 0.6
        # elif ( i*dt <= 70 ):
        #     PL = 0.5
        # elif ( i*dt <= 80 ):
        #     PL = 0.4
        # elif ( i*dt <= 90 ):
        #     PL = 0.3
        # elif ( i*dt <= 100 ):
        #     PL = 0.2
        # else:
        #     PL =  0.1

        # Load Graph 4

        # PL = np.random.normal(0.5,0.1)

        # Load Graph 5

        if(  (i*dt)%10==0 and (i*dt)!=0 ):
            PL1 = np.random.normal(0.5,0.1)
            PL2 = np.random.normal(0.5,0.1)

        # Load Graph 6

        # if ( i*dt > 50 and  i*dt <130):
        #     PL1 = 0.5

        # else:
        #     PL1 = 0

        # if ( i*dt > 20 and  i*dt <70):
        #     PL2 = 0.5

        # else:
        #     PL2 = 0 
        

        plot_data["pl1"].append(PL1)
        plot_data["pl2"].append(PL2)
        
        Ut = [ [ut_1] , [ut_2] , [ PL1] , [PL2] ]

        System.Output(Ut)


        plot_data["delF1"].append(System.Y[0,0])

        plot_data["delF2"].append(System.Y[1,0])

        plot_data["time"].append(i*dt)


    print("The steady state error of area 1 system is : ", System.Y[0][0])


    print("The steady state error of area 2 system is : ", System.Y[1][0])
        
    return plot_data,initial_states


if __name__=="__main__":


    yd = [0 for i in range(200*80) ] 


    ## Generate Reference array here

    plot_data,i = y(yd)


    plt.subplot(2,3,1)
    plt.plot(plot_data["time"],plot_data["pl1"], label="Reference Signal")
    plt.title( "Load vs Time")
    plt.ylabel(" Output from System ")
    plt.xlabel("Time (s)")

    
    
    plt.subplot(2,3,2)
    plt.plot(plot_data["time"],plot_data["ut1"], label="Reference Signal")
    plt.title( "Control Signal vs Time")
    plt.ylabel("Control Signal")
    plt.xlabel("Time (s)")

    plt.subplot(2,3,3)
    plt.plot(plot_data["time"],yd, label="Reference Signal")
    plt.plot(plot_data["time"],plot_data["delF1"],label ="Output")


    plt.title( " Initial States y(t-1) , y(t-2) and y(t-3) are " + str(i[0]) + ", " + str(i[1]) +" and "+ str(i[2]) )

    plt.legend()

    plt.subplot(2,3,4)

    plt.plot(plot_data["time"],plot_data["pl2"], label="Reference Signal")
    plt.title( "Load vs Time")
    plt.ylabel(" Output from System ")
    plt.xlabel("Time (s)")


    

    
    plt.subplot(2,3,5)
    plt.plot(plot_data["time"],plot_data["ut2"], label="Reference Signal")
    plt.title( "Control Signal vs Time")
    plt.ylabel("Control Signal")
    plt.xlabel("Time (s)")


    

    plt.subplot(2,3,6)
    plt.plot(plot_data["time"],yd, label="Reference Signal")
    plt.plot(plot_data["time"],plot_data["delF2"],label ="Output")

    
    
    
    

    plt.ylabel(" Output from System ")
    plt.xlabel("Time (s)")


    plt.show()


