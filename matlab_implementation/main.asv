% Load disturbance for Area 1
PL1 = 0;
% Load disturbance for Area 2
PL2 = 0;

% Importing RBF Class
import RBF.*

% Defining an object (nn1) of the class RBF

nn1 = RBF( 0.13,0.21,0.25,0.9,0.98, 3);

% Defining an object (nn2) of the class RBF
nn2 = RBF( 0.13,0.21,0.25,0.9,0.98, 3);

% Defining and initializing variables
ut1 = []; % Variable for control signal for area 1
ut2 = []; % Variable for control signal for area 2
pl1 = []; % Variable for load disturbance for area 1
pl2 = []; % Variable for load disturbance for area 2
ACE1 = []; % Variable for area control error for area 1
ACE2 = []; % Variable for area control error for area 2
TieLine = []; % Variable for TieLine Power
Freq1 =[]; % Variable for Frequency change for area 2
Freq2 = [];% Variable for Frequency change  for area 2
time = []; % Variable for time 
K = [];

Tg = 0.08; % Initializing variable for governor time constant
Tp = 20; % Initializing variable for plant time constant 
Tt = 0.3; % Initializing variable for Turbine time constant 
Kp = 120; % Initializing variable for PID parameter Kp
T12 = 0.545/(2*pi); % Initializing variable for Tie line power constant 
a12 = -1; % Initializing variable a12
R = 5; % Initializing variable for Regulation 
T = 1/80; % Initializing Time step
dt = 1/80; % Initializing Time step
beta1 = 0.425; % Initializing variable for Frequency bias constant of area 1
beta2 = 0.425; % Initializing variable for Frequency bias constant of area 2

% Defining object System for the class TwoAreaPS
System = TwoAreaPS( Tg, Tp, Tt, Kp, T12, a12, R, T, beta1, beta2,  [0,0,0],[0,0,0] );

% Initializing Ki
Ki = 0 ;
% Initializing Kd
Kd = 0 ;
% Initializing Kp
Kp = 0 ;

% Initializing weights
nn1.initialize_weights(1);
nn2.initialize_weights(2);

% Initializing control signals
ut_1 = 0;
ut_2 = 0;

% Duration of run
t = 200;

% Output variable
y = [];

for i = 1:t/dt

    % Finding error signal e_t for area 1
    e_t_a1 = 0 - System.yt_a1(1);

    % Finding derivative of the output (delta y) for area 1
    del_y_a1 =  System.yt_a1(1) - System.yt_a1(2);

    % Finding second derivate of the output (delta square y) for area 1
    del2_y_a1 = System.yt_a1(1) - 2*System.yt_a1(2) + System.yt_a1(3);

    % Defining the state X for area 1 controller
    nn1.X = [ e_t_a1 ; -del_y_a1 ;  -del2_y_a1];

    % Calling HiddenLayer function using object nn1
    nn1.HiddenLayer();

    % Calling OutputLayer function using object nn1
    nn1.OutputLayer();

    % Finding error signal e_t for area 2
    e_t_a2 = 0 - System.yt_a2(1);

    % Finding derivative of the output (delta y) for area 2
    del_y_a2 =  System.yt_a2(1) - System.yt_a2(2);

    % Finding second derivate of the output (delta square y) for area 2
    del2_y_a2 = System.yt_a2(1) - 2*System.yt_a2(2) + System.yt_a2(3);

    % Defining the state X for area 2 controller
    nn2.X = [ e_t_a2 ; -del_y_a2 ; -del2_y_a2];

    % Calling HiddenLayer function using object nn2
    nn2.HiddenLayer();

    % Calling OutputLayer function using object nn2
    nn2.OutputLayer();

    % Control signal (Equation 22 in the paper) for area 1
    ut_1 = ut_1 + (nn1.K(2)*e_t_a1 - nn1.K(1)*del_y_a1 - nn1.K(3)*del2_y_a1);

    % Control signal (Equation 22 in the paper) for area 2
    ut_2 = ut_2 + (nn2.K(2)*e_t_a2 - nn2.K(1)*del_y_a2 - nn2.K(3)*del2_y_a2);

    % Calculating delU1
    delU1 =  (nn1.K(2)*e_t_a1 - nn1.K(1)*del_y_a1 - nn1.K(3)*del2_y_a1);

    
    K = [K nn1.K(3)];
    % Calculating delU2
    delU2 = (nn2.K(2)*e_t_a2 - nn2.K(1)*del_y_a2 - nn2.K(3)*del2_y_a2);


    % Defining control signal ut1 for area 1
    ut1 = [ut1 ut_1];

    % Defining control signal ut2 for area 2
    ut2 = [ut2 ut_2];
    
    % Load disturbances
    if (i*dt >=40 && i*dt <= 80)
        PL1 = 0.003;
    elseif( i*dt > 80 && i*dt <= 120)
        PL1 = 0.006;
    elseif( i*dt > 120 && i*dt <= 160)
        PL1 = 0.009;
    else
        PL1 =  0;
    end
        
    PL2 =  0;

    pl1 = [pl1 PL1];
    pl2 = [pl2 PL2];
    
    % Defining control signal Ut
    Ut = [ ut_1 ; ut_2 ; PL1 ; PL2 ];

    System.Output(Ut);
    
    % Calling Update function using the object nn1 for area 1
    nn1.Update(0 ,System.Y(1), System.yt_a1(1), System.yt_a1(2), System.yt_a1(3),delU1+1);

    % Calling Update function using the object nn2 for area 2
    nn2.Update(0 ,System.Y(2), System.yt_a2(1), System.yt_a2(2), System.yt_a2(3),delU2+1 );

    % Defining ACE for area 1
    ACE1 = [ACE1 System.Y(1)];

    % Defining ACE for area 2
    ACE2 = [ACE2 System.Y(2)];

    % Defining Tie Line Power
    TieLine = [ TieLine System.Y(3)];

    % Defining Frequency Change for area 1
    Freq1 = [ Freq1 System.Y(4)];

    % Defining Frequency Change for area 2
    Freq2 = [ Freq2 System.Y(5)];

    % Defining variable time for our time period
    time = [time i*dt];
    
    % Metrics calculations

    %Integral time absolute error(eq 38 in paper)
    ITAE = [];
    ITAE = [ITAE dt*(i*dt)*( abs(System.Y(1)) + abs(System.Y(2)))];

    % Integral time squared error(eq 36 in paper)
    ITSE = [];
    ITSE = [ITSE dt*(i*dt)*( System.Y(1)^2 + System.Y(2)^2 )];

    % Integral absolute error(eq 37 in paper)
    IAE = [];
    IAE = [IAE dt*( abs(System.Y(1)) + abs(System.Y(2)) ) ];

    % Integral Square error(eq 39 in paper)
    ISE = [];
    ISE = [ISE dt*( System.Y(1)^2 + System.Y(2)^2 ) ];

end

% Displaying metrics values
fprintf('IAE is');
disp(sum(IAE));
fprintf('ISE is');
disp(sum(ISE));
fprintf('ITSE is');
disp(sum(ITSE));
fprintf('ITAE is');
disp(sum(ITAE));

% disp(K);

writematrix(ACE1,"ACE1.txt");
writematrix(ACE2,"ACE2.txt");
writematrix(time,"time.txt");

% plotting load graph
figure(1);
plot(time,pl1 ,time,pl2);
title(' Area 1 and Area 2 Load vs Time')
xlabel('Time(s)')
ylabel('Load (pu)')

legend('Area 1', 'Area 2')

% ylabel('Load (pu)')
% subplot(2,1,2);
% plot(time, pl2);
% title('Area 2 Load vs Time')
% xlabel('Time(s)')

% plotting control signal graph
figure(2);
subplot(2,1,1);
plot(time,ut1 );
title(' Area 1 Control Signal vs Time')
xlabel('Time(s)')
ylabel('Control Signal (pu)')
subplot(2,1,2);
plot(time, ut2);
title('Area 2 Control Signal  vs Time')
xlabel('Time(s)')
ylabel('Control Signal (pu)')

% plotting ACE graph
figure(3);
subplot(2,1,1);
plot(time, ACE1);
title(' Area 1 ACE vs Time for Adaptive PID')
xlabel('Time(s)')
ylabel('ACE (pu)')
subplot(2,1,2);
plot(time, ACE2);
title('Area 2 ACE vs Time Adaptive PID')
xlabel('Time(s)')
ylabel('ACE (pu)')

figure(4);
plot(time,K);
title(' Area 1 and Area 2 Load vs Time')
xlabel('Time(s)')
ylabel('Load (pu)')

% legend('Area 1', 'Area 2')

figure(4);
subplot(2,1,1);
plot(time, Freq1);
title(' Area 1 Frequency Change vs Time')
xlabel('Time(s)')
ylabel('Frequency Change (pu)')
subplot(2,1,2);
plot(time, Freq2);
title('Area 2 Frequency Change vs Time')
xlabel('Time(s)')
ylabel('Frequency Change (pu)')

figure(5);
plot(time, TieLine);
title('Tie Line Power vs Time')
xlabel('Time(s)')
ylabel('Tie Line Power (pu)')

