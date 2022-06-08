% Initialization
% Parameters
clear
clc
iterations = 50;
W = 0.9;
C1 = 2.0;
C2 = 2.0;
n = 49;
% ---- initial swarm position -----
index = 1;
for i = 1 : 7
    for j = 1 : 7
        particle(index, 1, 1) = i;
        particle(index, 1, 2) = j;
        index = index + 1;
    end
end
particle(:, 4, 1) = 1000;          % best value so far
particle(:, 2, :) = 0;             % initial velocity
%% Iterations
for iter = 1 : iterations
%-- evaluating position & quality ---
        for i = 1 : n
        particle(i, 1, 1) = particle(i, 1, 1) + particle(i, 2, 1)/1.3;     %update x position
        particle(i, 1, 2) = particle(i, 1, 2) + particle(i, 2, 2)/1.3;     %update y position
        Kp = particle(i, 1, 1);
        Ki = particle(i, 1, 2);
        Gc=tf([Kp Ki],[1 0]);
        G=tf(1,[1 2 3]);
        Q=feedback(Gc*G,1);
        Z=stepinfo(Q);
        a=Z.RiseTime;
        b=Z.SettlingTime;
        % Z.Overshoot=350;
        c=Z.Overshoot;
        d=Z.Undershoot;
        % e=Z.SettlingMax;
        % alpha=0.5;
        F = min((a)+min(c)+min(b)+min(d));          % fitness evaluation
                
        if F < particle(i, 4, 1)                 % if new position is better
            particle(i, 3, 1) = particle(i, 1, 1);    % update best x,
            particle(i, 3, 2) = particle(i, 1, 2);    % best y postions
            particle(i, 4, 1) = F;               % and best value
        end
    end
    [temp, gbest] = min(particle(:, 4, 1));        % global best position
    %--- updating velocity vectors
    for i = 1 : n
        particle(i, 2, 1) = rand*W*particle(i, 2, 1) + C1*rand*(particle(i, 3, 1) - particle(i, 1, 1)) + C2*rand*(particle(gbest, 3, 1) - particle(i, 1, 1));   %x velocity component
        particle(i, 2, 2) = rand*W*particle(i, 2, 2) + C1*rand*(particle(i, 3, 2) - particle(i, 1, 2)) + C2*rand*(particle(gbest, 3, 2) - particle(i, 1, 2));   %y velocity component
    end
    %% Plotting the swarm
    disp(gbest)
    clf    
    plot(particle(:, 1, 1), particle(:, 1, 2), 'x')   
    axis([-2 10 -2 10]);
    pause(0)
    
end
disp('best value is')
disp(gbest)