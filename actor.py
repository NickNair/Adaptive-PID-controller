import numpy as np

class Actor:

    def __init__(self , aw , av , au  , gamma ,h = 3 ):

        #  Initialize all parameters

        self.X = np.zeros((3,1))
        self.h = h
        self.wh = np.zeros( (h,3) )


        # actor 
        self.K =np.zeros( (3,1) )


        # actor
        self.w = np.zeros( (3, h) )
        



        self.output = np.zeros( (h,1) )
        
        # Learning Rates

        # actor
        self.aw = aw


        # both
        self.au = au 





        

    def HiddenLayer(self):

        # Description : Takes in the state vector at a given time step and computes the output vector for the next layer

        output = 1/(1 + np.exp(self.wh.dot(self.X)) )

        self.output = output
    
    def OutputLayer(self):

        # Description : Takes in output from Hiddenlayer and computes Ki,Kp and Kd values

        # actor

        self.K = self.w.dot(self.output)

        # print(self.K)
    
    
    def Update1(self,y_ref,yt_0,yt_1,yt_2,yt_3,V,Vprev):

        # Update Params for next episode


        # both 
        del_TD = 0.5 * ( y_ref - yt_0 )**2 + self.gamma*V - Vprev

        
        # actor

        # Update w matrix 
        self.w[0] = self.w[0] - self.aw *  del_TD*(yt_1 - yt_2)*self.output.T  
        self.w[1] = self.w[1] + self.aw *  del_TD*self.X[0,0]*self.output.T 
        self.w[2] = self.w[2] + self.aw *  del_TD*(yt_1 - 2*yt_2 + yt_3)*self.output.T 

        

    def Update2(self,y_ref,yt_0,yt_1,yt_2,yt_3,V,Vprev,v_prev):

        # Update Params for next episode

        del_TD = 0.5 * ( y_ref - yt_0 )**2 + self.gamma*V - Vprev
        
        for i in range(self.h):
            self.wh[i,0] = self.wh[i,0] + self.au*del_TD*v_prev[0][i]*self.output[i]*( 1 - self.output[i] )*self.X[0]
            self.wh[i,1] = self.wh[i,1] + self.au*del_TD*v_prev[0][i]*self.output[i]*( 1 - self.output[i] )*self.X[1]
            self.wh[i,2] = self.wh[i,2] + self.au*del_TD*v_prev[0][i]*self.output[i]*( 1 - self.output[i] )*self.X[2]




        
