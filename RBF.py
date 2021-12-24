import numpy as np
from numpy.lib.function_base import average

class RBF:

    def __init__(self , aw , av , au , asig , gamma ,h = 3 ):

        # TODO : Initialize all parameters

        self.X = np.zeros((3,1))
        self.h = h
        self.mu = np.zeros( (3,h) )
        self.sigma = np.ones( (1,h) )

        self.K =np.zeros( (3,1) )
        self.Vprev = 0
        self.V = 0

        self.w = np.zeros( (3, h) )
        self.v = np.zeros( (1, h) )
        self.output = np.zeros( (h,1) )
        # Learning Rates

        self.aw = aw
        self.av = av
        self.au = au 
        self.asig = asig
        self.gamma = gamma

        

    def HiddenLayer(self):

        # Description : Takes in the state vector at a given time step and computes the output vector for the next layer

        output = np.zeros( (self.h,1) )

        
        for i in range(self.h):
            phi_j = np.exp( - np.linalg.norm( self.X - self.mu[:,i]  )**2 /( 2*self.sigma[0][i]**2 )  )
            output[i] =  phi_j

        self.output = output
    
    def OutputLayer(self):

        # Description : Takes in output from Hiddenlayer and computes Ki,Kp and Kd values

        self.K = self.w.dot(self.output)

        # print(self.K)
        self.Vprev = self.V
        self.V = self.v.dot(self.output)
    
    def Update(self,y_ref,yt_0,yt_1,yt_2,yt_3):

        # Update Params for next episode

        del_TD = 0.5 * ( y_ref - yt_0 )**2 + self.gamma*self.V - self.Vprev

        # Update w matrix 
        self.w[0] = self.w[0] - self.aw *  del_TD*(yt_1 - yt_2)*self.output.T  
        self.w[1] = self.w[1] + self.aw *  del_TD*self.X[0,0]*self.output.T 
        self.w[2] = self.w[2] + self.aw *  del_TD*(yt_1 - 2*yt_2 + yt_3)*self.output.T 

        # Updating the v value
        v_prev = self.v
        self.v = self.v + self.av * del_TD * self.output.T

        # Updating the centers and widths of hidden layers

        # print("Printing Shapes of Stuff")

        # print("Shape of self.au :", v_prev)

        for i in range(self.h):
            self.mu[:,i] = self.mu[:,i] + self.au*del_TD*v_prev[0][i]*self.output[i]*(self.X- self.mu[:,i])[:,0]/self.sigma[0][i]**2

        for i in range(self.h):
            self.sigma[0][i] = self.sigma[0][i] + self.asig*del_TD*del_TD*v_prev[0][i]*self.output[i]*( np.linalg.norm(self.X- self.sigma[0][i]) )/self.sigma[0][i]**3
        

        print(self.K)



        
