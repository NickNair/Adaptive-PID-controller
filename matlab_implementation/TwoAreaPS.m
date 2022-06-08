% Defining class TwoAreaPS
classdef TwoAreaPS<handle

    % Defining the variables for the class
    properties

        yt_a1; % Defining variable yt for output of area 1 
        yt_a2; % Defining variable yt for output of area 2
        Xprev; % Defining variable for previous value of X
        X; % Defining variable X
        Y; % Defining variable Y
        Tg; % Defining variable for governor time constant
        Tp; % Defining variable for plant time constant
        Tt; % Defining variable for turbine time constant
        Kp; % Defining variable for PID parameter Kp
        T12; % Defining variable for tie line power constant
        a12; % Defining variable for a12
        R; % Defining variable for regulation
        beta1; % Defining variable for frequency bias constant of area 1
        beta2; % Defining variable for frequency bias constant of area 2
        T; % Defining variable for time step
        A; % Defining variable for state space model matrix A
        B; % Defining variable for state space model matrix B
        C; % Defining variable for state space model matrix C
        Ad; % Defining variable for discretization parameter 
        Bd; % Defining variable for discretization parameter 

    end
    methods
        function self = TwoAreaPS( Tg, Tp, Tt, Kp, T12, a12, R, T, beta1, beta2,  yt_a1, yt_a2)

            self.yt_a1 = yt_a1; % Initializing variable for previous output value
            self.yt_a2 = yt_a2; % Initializing variable for previous output value
            self.Xprev = zeros( 7,1); % Initializing variable for input
            self.X= zeros( 7,1); % Initializing variable for input
            self.Y = zeros( 5,1 ); % Initializing variable for output
            self.Tg = Tg; % Initializing variable for governor time constant
            self.Tp = Tp ; % Initializing variable for plant time constant
            self.Tt = Tt ; % Initializing variable for turbine time constant
            self.Kp = Kp; % Initializing variable for PID parameter Kp
            self.T12 = T12 ; % Initializing variable for tie line power constant
            self.a12 = a12; % Initializing variable for a12
            self.R = R ; % Initializing variable for regulation
        
            self.beta1 = beta1; % Initializing variable for frequency bias constant of area 1
            self.beta2 = beta2; % Initializing variable for frequency bias constant of area 2
        
            self.T = T;
        
            self.CalcDiscreteCoef();
        end

        function self = CalcDiscreteCoef(self)
            Tg = self.Tg;
            Tp = self.Tp;
            Tt = self.Tt;
            Kp = self.Kp;
            T12 = self.T12 ;
            a12 = self.a12;
            R = self.R ;
            
            % Defining state space model matrix A
            self.A  = [ -1/Tp Kp/Tp  0  -Kp/Tp  0  0  0  ;
                        0  -1/Tt  1/Tt  0  0 0  0  ; 
                        -1/(R*Tg)  0  -1/Tg  0  0 0 0 ; 
                        2*pi*T12  0  0  0  -2*pi*T12  0 0 ; 
                        0  0  0  -Kp*a12/Tp  -1/Tp  Kp/Tp  0 ;  
                        0   0 0 0 0  -1/Tt 1/Tt ; 
                        0   0 0 0 -1/(R*Tg)  1/Tg  -1/Tg  ];
               
            % Defining state space model matrix B
            self.B = [ 0 0 -Kp/Tp  0 ;
                       0 0 0 0 ;
                      1/Tg 0  0 0 ;
                       0 0 0 0 ;
                       0 0 0 0 ;
                       0 0 0 0 ;
                       0 1/Tg 0 -Kp/Tp ] ;
    
            % Defining state space model matrix C
            self.C = [ self.beta1  0  0 1  0 0  0 ;
                       0  0 0 1 self.beta2  0  0 ; 
                       0  0 0 1 0 0 0 ; 
                       1  0 0 0 0 0 0 ;
                       0  0 0 0 1 0 0 ]    ;

            % Calculating system matrix for discrete time (eq 8 in the paper)
            self.Ad = expm(self.A*self.T);
    
            % Calculating input matrix for discrete time (eq 9 in the paper)
            self.Bd = inv(self.A)*(self.Ad - eye(7) )*self.B;

        end
    
        % Defining function output
        function self = Output(self,Ut)

            % Updating previous values for area 1
            self.yt_a1 = [self.Y(1) self.yt_a1(1) self.yt_a1(2)];

            % Updating previous values for area 2
            self.yt_a2 = [self.Y(2) self.yt_a2(1) self.yt_a2(2)];

            % System equation (Equation 4 in the paper)
            self.X = self.Ad*self.Xprev +self.Bd*Ut;

            % Output equation (Equation 5 in the paper)
            self.Y = self.C*self.Xprev;

            % Updating previous values for X 
            self.Xprev = self.X;

        end
        
    end
end