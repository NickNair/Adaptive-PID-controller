import numpy as np
from numpy.core.numeric import NaN
from scipy.linalg import expm
import math

class SingleArea:

    def __init__(self,Tg,Tt,M,D,R,T,yt_1,yt_2,yt_3):

        self.yt_1 = yt_1
        self.yt_2 = yt_2
        self.yt_3 = yt_3

        self.Xprev = np.zeros( (3,1) )
        self.Y = np.zeros( (1,1) )

        self.Tg = Tg 
        self.Tt = Tt 
        self.M = M
        self.D = D 
        self.R = R 

        self.T = T

        self.CalcDiscreteCoef()

    def CalcDiscreteCoef(self):

        # Calculating Continous coef

        self.A  = np.array( [ [-self.D/self.M , 1/self.M , 0] , [ 0 , -1/self.Tt , 1/self.Tt ] , [-1/( self.Tg*self.R ) , 0 , -1/self.Tg ] ] )

        self.B = np.array( [ [0 , -1/self.M ] , [ 0 , 0 ] , [ 1/self.Tg , 0 ] ])

        self.C = np.array( [[1 , 0 , 0]] )

        # Calculating Discrete Coefs 

        self.Ad = expm(self.A*self.T)

        # Add check later

        self.Bd = np.dot( np.dot(np.linalg.inv(self.A),(self.Ad - np.eye(3) )), self.B )

    def Output(self,Ut):

        self.yt_1 , self.yt_2 , self.yt_3  = self.Y[0,0] , self.yt_1, self.yt_2

        self.X = np.dot( self.Ad, self.Xprev )  + np.dot( self.Bd, Ut )

        self.Y = np.dot( self.C,  self.Xprev) 

        # print("Chooth :" , self.Y)

        self.Xprev = self.X

        if (math.isnan(self.Y[0,0])):

            return True

        return False













