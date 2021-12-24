import matplotlib.pyplot as plt
import numpy as np

noise = np.random.normal(0,1,100)


def y(t):



    yt_1 = 1

    yt_2 = 1
    dt = 1/400

    y=[]
    x=[]

    
    for i in range(0, int(t/dt) ):
        yt_1,yt_2 = yt_1*yt_2*(yt_1 + 2.5) / ( 1 + yt_1**2 + yt_2**2 ) , yt_1 + np.random.normal(0,0.01)

        # print(yt_1," ",yt_2)
        y.append(yt_1)
        x.append(i*dt)
        
    return y,x


if __name__=="__main__":

    x,y = y(1)

    plt.plot(y,x)

    plt.show()

