import numpy as np

class Critic:

    def __init__(self , aw , av , au  , gamma ,h = 3 ):

        #  Initialize all parameters

        self.X = np.zeros((3,1))
        self.h = h
        self.wh = np.zeros( (h,3) )


        # critic
        self.Vprev = 0
        self.V = 0


        # critic
        self.v = np.zeros( (1, h) )


        self.output = np.zeros( (h,1) )
        
        # Learning Rates


        # critic

        self.av = av

        # both
        self.au = au 

        # critic 
        self.gamma = gamma

        

    def HiddenLayer(self):

        # Description : Takes in the state vector at a given time step and computes the output vector for the next layer

        output = 1/(1 + np.exp(self.wh.dot(self.X)) )

        

        self.output = output
    
    def OutputLayer(self):

        # Description : Takes in output from Hiddenlayer and computes Ki,Kp and Kd values


        # critic
        self.Vprev = self.V
        self.V = self.v.dot(self.output)
    
    def Update(self,y_ref,yt_0,yt_1,yt_2,yt_3):

        # Update Params for next episode

        del_TD = 0.5 * ( y_ref - yt_0 )**2 + self.gamma*self.V - self.Vprev


        # critic

        # Updating the v value
        v_prev = self.v
        self.v = self.v + self.av * del_TD * self.output.T

        
        for i in range(self.h):
            self.wh[i,0] = self.wh[i,0] + self.au*del_TD*v_prev[0][i]*self.output[i]*( 1 - self.output[i] )*self.X[0]
            self.wh[i,1] = self.wh[i,1] + self.au*del_TD*v_prev[0][i]*self.output[i]*( 1 - self.output[i] )*self.X[1]
            self.wh[i,2] = self.wh[i,2] + self.au*del_TD*v_prev[0][i]*self.output[i]*( 1 - self.output[i] )*self.X[2]

        return v_prev
    


        
