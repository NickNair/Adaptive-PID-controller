import numpy as np

class NeuralNetwork:

    def __init__(self , aw , av , au  , gamma ,h = 3 ):

        #  Initialize all parameters

        self.X = np.zeros((3,1))
        self.h = h
        self.wh = np.zeros( (h,3) )

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
        self.gamma = gamma

        

    def HiddenLayer(self):

        # Description : Takes in the state vector at a given time step and computes the output vector for the next layer

        output = 1/(1 + np.exp(self.wh.dot(self.X)) )

        

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
            self.wh[i,0] = self.wh[i,0] + self.au*del_TD*v_prev[0][i]*self.output[i]*( 1 - self.output[i] )*self.X[0]
            self.wh[i,1] = self.wh[i,1] + self.au*del_TD*v_prev[0][i]*self.output[i]*( 1 - self.output[i] )*self.X[1]
            self.wh[i,2] = self.wh[i,2] + self.au*del_TD*v_prev[0][i]*self.output[i]*( 1 - self.output[i] )*self.X[2]

        # print(self.K)



        
