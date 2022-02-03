import numpy as np
from numpy.core.numeric import NaN
from scipy.linalg import expm
import math

class TwoAreaPS:

    def __init__(self, Tg, Tp, Tt, Kp, T12, a12, R, T, beta1, beta2,  yt_1,yt_2,yt_3):

        self.yt_1 = yt_1
        self.yt_2 = yt_2
        self.yt_3 = yt_3

        self.Xprev = np.zeros( (7,1) )
        self.Y = np.zeros( (2,1) )

        self.Tg = Tg
        self.Tp = Tp 
        self.Tt = Tt 
        self.Kp = Kp
        self.T12 = T12 
        self.a12 = a12
        self.R = R 

        self.beta1 = beta1
        self.beta2 = beta2

        self.T = T

        self.CalcDiscreteCoef()

    def CalcDiscreteCoef(self):

        # Calculating Continous coef

        Tg = self.Tg
        Tp = self.Tp
        Tt = self.Tt
        Kp = self.Kp
        T12 = self.T12 
        a12 = self.a12
        R = self.R 

        self.A  = np.array( [ [-1/Tp , Kp/Tp , 0 , -Kp/Tp , 0 , 0 , 0 ] ,
                              [0 , -1/Tt , 1/Tt , 0 , 0 ,0 , 0 ] , 
                              [-1/(R*Tg) , 0 , -1/Tg , 0 , 0, 0, 0 ] , 
                              [ 2*np.pi*T12 , 0 , 0 , 0 , -2*np.pi*T12 , 0 , 0  ] , 
                              [0 ,0 ,0 , -Kp*a12/Tp , -1/Tp , Kp/Tp , 0 ] , 
                              [ 0,0,0,0,0, -1/Tt, 1/Tt] , 
                              [0,0,0,0,-1/(R*Tg) , 1/Tg , -1/Tg ] ] )

        self.B = np.array( [ [0 ,0, -Kp/Tp , 0 ],
                             [0 , 0, 0 ,0 ],
                             [1/Tg, 0 , 0, 0],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,0,0,0],
                             [0,1/Tg,0,-Kp/Tp]  ])

        self.C = np.array( [ [ self.beta1 , 0 , 0 ,1 , 0, 0 , 0 ] ])
                            #  [ 0 , 0, 0, 1, self.beta2, 0, 0 ] ] )


        # Calculating Discrete Coefs 

        self.Ad = expm(self.A*self.T)

        # Add check later

        self.Bd = np.dot( np.dot(np.linalg.inv(self.A),(self.Ad - np.eye(7) )), self.B )

    def Output(self,Ut):

        self.yt_1 , self.yt_2 , self.yt_3  = self.Y[0,0], self.yt_1, self.yt_2

        self.X = np.dot( self.Ad, self.Xprev )  + np.dot( self.Bd, Ut )

        self.Y = np.dot( self.C,  self.Xprev) 

        # print("Chooth :" , self.Y)

        self.Xprev = self.X

        if (math.isnan(self.Y[0,0])):

            return True

        return False













