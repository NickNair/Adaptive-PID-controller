% Load Disturbance for area 1
PL1 = 0;
% Load Disturbance for area 2
PL2 = 0;

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


Tg = 0.08; % Initializing variable for governor time constant
Tp = 20; % Initializing variable for plant time constant 
Tt = 0.3; % Initializing variable for Turbine time constant 
Kp = 120; % Initliazing PID parameter K
T12 = 0.545/(2*pi); % Initializing variable for Tie line power constant 
a12 = -1; 
R = 5; % Initializing variable for Regulation 
T = 1/80; 
dt = 1/80;
beta1 = 0.425; % Initializing variable for Frequency bias constant of area 1
beta2 = 0.425; % Initializing variable for Frequency bias constant of area 2

% Defining object System for the class TwoAreaPS
System = TwoAreaPS( Tg, Tp, Tt, Kp, T12, a12, R, T, beta1, beta2,  [0,0,0],[0,0,0] );


KP1 = 1.723845;
KI1 = 0.014555;
KD1 = 17.936909;

KP2 = 0.106744;
KI2 = 0.006323;
KD2 = 15.023620;

ut_1 = 0;
ut_2 = 0;

t = 200;

y = [];
x = [];

for i = 1:t/dt
    % Finding error signal e_t for area 1
    e_t_a1 = 0 - System.yt_a1(1);
    % Finding derivative of the output (delta y) for area 1
    del_y_a1 =  System.yt_a1(1) - System.yt_a1(2);
    % Finding double derivate of the output (delta square y) for area 1
    del2_y_a1 = System.yt_a1(1) - 2*System.yt_a1(2) + System.yt_a1(3);

    % Controller definition (Equation 22 in the paper) for area 1
    ut_1 = ut_1 + (KI1*e_t_a1 - KP1*del_y_a1 - KD1*del2_y_a1);
     % Controller definition (Equation 22 in the paper) for area 2
    ut_2 = ut_2 + (KI2*e_t_a2 - KP2*del_y_a2 - KD2*del2_y_a2);

    % Defining control signal ut1 for area 1
    ut1 = [ut1 ut_1];
    % Defining control signal ut2 for area 2
    ut2 = [ut2 ut_2];
    
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
    
    ITAE = [];
    ITAE = [ITAE, dt*(i*dt)*( abs(System.Y(1)) + abs(System.Y(2)))];

    ISTE = [];
    ISTE = [ISTE, dt*(i*dt)*( System.Y(1)^2 + System.Y(2)^2 )];

    IAE = [];
    IAE = [IAE, dt*( abs(System.Y(1)) + abs(System.Y(2)) ) ];

    ISE = [];
    ISE = [ISE, dt*( System.Y(1)^2 + System.Y(2)^2 ) ];
end

fprintf('IAE is');
disp(sum(IAE));
fprintf('ISE is');
disp(sum(ISE));
fprintf('ISTE is');
disp(sum(ISTE));
fprintf('ITAE is');
disp(sum(ITAE));

figure(1);
subplot(2,1,1);
plot(time,pl1 );
title(' Area 1 Load vs Time')
xlabel('Time(s)')
ylabel('Load (pu)')
subplot(2,1,2);
plot(time, pl2);
title('Area 2 Load vs Time')
xlabel('Time(s)')
ylabel('Load (pu)')

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

figure(3);
subplot(2,1,1);
plot(time, ACE1);
title(' Area 1 ACE vs Time for PSO Tuned PID')
xlabel('Time(s)')
ylabel('ACE (pu)')
subplot(2,1,2);
plot(time, ACE2);
title('Area 2 ACE vs Time for PSO Tuned PID')
xlabel('Time(s)')
ylabel('ACE (pu)')

ACE1_pso  = ACE1;
ACE2_pso = ACE2;

