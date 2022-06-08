clear
clc
num_particles = 50;           % Size of the swarm " no of birds "
max_iter = 50;                    % Maximum number of "birds steps"
dim = 6;                % Dimension of the problem

c2 = 1.49445;          % PSO parameter C1
c1 = 1.49445;        % PSO parameter C2
w = 0.729;           % pso momentum or inertia
fitness = zeros(num_particles,max_iter);

                                       %-----------------------------%
                                       %    initialize the parameter %
                                       %-----------------------------%

R1 = rand(dim, num_particles);
R2 = rand(dim, num_particles);
current_fitness = zeros(num_particles,1);

                                 %------------------------------------------------%
                                 % Initializing swarm and velocities and position %
                                 %------------------------------------------------%

current_position = 10 * (rand(dim, num_particles)-0.5);
velocity = 0.3 * randn(dim, num_particles) ;
local_best_position  = current_position ;


                                 %-------------------------------------------%
                                 %     Evaluate initial population           %
                                 %-------------------------------------------%

for i = 1 : num_particles
    current_fitness(i) = system_with_pid(current_position(:,i));
end


local_best_fitness  = current_fitness ;
[global_best_fitness,g] = min(local_best_fitness) ;

for i = 1 : num_particles
    global_best_position(:,i) = local_best_position(:,g) ;
end
%                                                %-------------------%
%                                                %  VELOCITY UPDATE  %
%                                                %-------------------%
% 
% velocity = w *velocity + c1*(R1.*(local_best_position-current_position)) + c2*(R2.*(global_best_position-current_position));
% 
%                                                %------------------%
%                                                %   SWARMUPDATE    %
%                                                %------------------%
% 
% 
% current_position = current_position + velocity ;

                                               %------------------------%
                                               %  evaluate a new swarm   %
                                               %------------------------%
iter = 0 ;        % Iterations’counter
while  ( iter < max_iter )
    if mod(iter,10)==0 && iter>1 
%         fprintf('Iter = %d', iter);
%         fprintf('Best fitness = %.7f', current_global_best_fitness);
        disp(iter);
        disp(current_global_best_fitness);
    end
    iter = iter + 1;
    
    for i = 1 : num_particles
        current_fitness(i) = system_with_pid(current_position(:,i)) ;
    end
    
    
    for i = 1 : num_particles
        if current_fitness(i) < local_best_fitness(i)
            local_best_fitness(i)  = current_fitness(i);
            local_best_position(:,i) = current_position(:,i)   ;
        end
        fitness(i,iter) = local_best_fitness(i);
    end
    
    
    [current_global_best_fitness,g] = min(local_best_fitness);
    
    
    if current_global_best_fitness < global_best_fitness
        global_best_fitness = current_global_best_fitness;
    
        for i = 1 : num_particles
            global_best_position(:,i) = local_best_position(:,g);
        end
    
    end
    
    
    velocity = w *velocity + c1*(R1.*(local_best_position-current_position)) + c2*(R2.*(global_best_position-current_position));
    current_position = current_position + velocity;


    


end % end of while loop its mean the end of all step that the birds move it


xx = fitness(:,max_iter);
% disp(current_global_best_fitness);
disp(xx);
[Y,I] = min(xx);
% disp(Y);
disp(current_position(:,I));

%