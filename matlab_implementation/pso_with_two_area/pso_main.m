
dim = 6;
 
num_particles = 40;
max_iter = 50;
 
 
best_position = pso(max_iter, num_particles, dim, -1, 1);
disp(best_position);
fitnessVal = system_with_pid(best_position);
disp(fitnessVal);