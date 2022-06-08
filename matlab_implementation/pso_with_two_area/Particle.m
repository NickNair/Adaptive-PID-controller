classdef Particle
    properties
        fitness;
        dim;
        minx;
        maxx;
        position;
        velocity;
        best_part_pos;
        best_part_fitnessVal;
        rnd;
    end
    methods
        function self = Particle(dim, minx, maxx)
            rng('default')
            self.rnd = rand();
 
            self.position = zeros(1,dim);
         
            self.velocity = zeros(1,dim);
         
            self.best_part_pos = zeros(1,dim);
         
            for i = 1:dim
                self.position(i) = ((maxx - minx) * self.rnd + minx);
                self.velocity(i) = ((maxx - minx) * self.rnd + minx);
             
                self.fitness = system_with_pid(self.position) ;
                
                self.best_part_pos = self.position;
                self.best_part_fitnessVal = self.fitness ;
            end
        end
        
    end
end



