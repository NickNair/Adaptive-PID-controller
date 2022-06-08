% Defining the class RBF
classdef RBF<handle

    % Defining variables for the class
    properties 

        X; % Variable for state
        h; % Variable for number of hidden layers
        mu; % Variable for mean
        sigma; % Variable for variance
        K; % Variable for K values of PID
        Vprev; % Variable for previous value of value function
        V; % Variable for value of value function
        w; % Variable for Actor weight matrix
        v; % Variable for Critic weight matrix
        output; % Variable for hidden layer
        aw; % Variable for learning parameter
        av; % Variable for learning parameter
        au; % Variable for learning parameter
        asig; % Variable for learning parameter
        gamma; % Variable for discount factor in RL

    end
    methods

        % Defining the RBF constructor
        function self = RBF(aw , av , au , asig , gamma,h )

            self.X = zeros(3,1); % Initializing X
            self.h = h; % Initializing for number of hidden layers h
            self.mu = zeros(3,h); % Initializing mean (mu)
            self.sigma = ones(1,h); % Initializing variance (sigma)
            self.K = zeros(3,1); % Initializing K
            self.Vprev = 0; % Initializing previous value function
            self.V  = 0; % Initializing value function
            self.w = zeros(3,h); % Initializing w
            self.v = zeros(1,h); % Initializing v
            self.output = ones(h,1); % Initializing output
            self.aw = aw; % Initializing learning parameter aw
            self.av = av; % Initializing learning parameter av
            self.au = au; % Initializing learning parameter au
            self.asig = asig; % Initializing learning parameter asig
            self.gamma = gamma; % Initializing learning parameter gamma
            
        end

        % Defining the function for the hidden layer of the RBF 
        function self = HiddenLayer(self)

            % Looping over h hidden layers
            for i = 1:self.h 

                % Gaussian Function (Equation 26 in the paper)
                self.output(i) = exp(- (norm( self.X - self.mu(:,i) )^2 )/(2*self.sigma(i)^2) );
            end
        end

        % Defining the function for output layer of the RBF
        function self = OutputLayer(self)

            % Equation 27 in the paper
            self.K = self.w*self.output;

            % Equating previous value function value to current value function value
            self.Vprev = self.V;

            % Equation 28 in the paper
            self.V = self.v*self.output;
        end

        function self = Update(self, y_ref , Y, y1, y2 , y3 , delU )

            % TD Error (Equation 30 in the paper)
            del_TD = 0.5 * ( y_ref - Y )^2 + self.gamma*self.V - self.Vprev;

            % Finding delY/delU
            delY_delU = (Y - y1 )/delU ;

            % Finding the gradient of the weight matrix
            w_gradient = del_TD *delY_delU* ( [ (y1 - y2) ; -self.X(1) ; (y1 - 2*y2 + y3) ]*self.output');

            % Update rule for w (Equation 32 in the paper)
            self.w = self.w - self.aw * w_gradient;

            % Finding the gradient of the mean (mu) matrix
            mu_gradient = del_TD* (repmat(self.X,1,self.h) - self.mu).*(  (( self.output.*(self.v') )./( (self.sigma).^2 )')' );

            % Update rule for mean (Equation 34 in the paper)
            self.mu = self.mu + self.au*mu_gradient;

            temp = zeros(1,self.h);

            for j = 1: self.h

                temp(j) = norm( self.X - self.mu(:,j) )^2;

            end
            % Finding gradient for updating sigma (variance)
            sig_gradient =  (del_TD) * temp.* ((( self.output.*(self.v') )./( (self.sigma).^3 )')');

            % Update rule for sigma (Equation 35 in the paper)
            self.sigma = self.sigma + self.asig*sig_gradient;

            % Update rule for critic weights, value function (Equation 33 in the paper)
            self.v = self.v + self.av*del_TD*self.output';

        end
        
        % Defining function to initialize weights
        function self = initialize_weights(self,area)

            % Initialize the weights for area 1
            if area == 1
                self.w = readmatrix('w_matrix1.txt');

            % Initialize the weights for area 2
            elseif area == 2
                self.w = readmatrix('w_matrix2.txt');
            end 
        end
    end
end



