function best_swarm_pos = pso(max_iter, n, dim, minx, maxx)
    w = 0.729;
    c1 = 1.49445;
    c2 = 1.49445;
    
    rng('default')
    rnd = rand();
    
    swarm = [];
    for i = 1:n
        swarm = [swarm, Particle(dim, minx, maxx)];
    end
    
    best_swarm_fitnessVal = Inf; 
    
    for i = 1:n 
        if swarm(i).fitness < best_swarm_fitnessVal
          best_swarm_fitnessVal = swarm(i).fitness;
          best_swarm_pos = swarm(i).position;
        end
    end


    Iter = 0;
    while Iter < max_iter
        
        for i = 1:n
        
            for k = 1:dim
                r1 = rand();   
                r2 = rand();

                
                swarm(i).velocity(k) = ((w * swarm(i).velocity(k)) + (c1 * r1 * (swarm(i).best_part_pos(k) - swarm(i).position(k))) + (c2 * r2 * (best_swarm_pos(k) -swarm(i).position(k)))) ;
                
      
                if swarm(i).velocity(k) < minx
                  swarm(i).velocity(k) = minx;
                elseif swarm(i).velocity(k) > maxx
                  swarm(i).velocity(k) = maxx;
                end
            
            
            for k = 1:dim
                swarm(i).position(k) = swarm(i).position(k) + swarm(i).velocity(k);
            end
            
            swarm(i).fitness = system_with_pid(swarm(i).position);
            
            if swarm(i).fitness < swarm(i).best_part_fitnessVal
                swarm(i).best_part_fitnessVal = swarm(i).fitness;
                swarm(i).best_part_pos = swarm(i).position;
            end
            
            if swarm(i).fitness < best_swarm_fitnessVal
                best_swarm_fitnessVal = swarm(i).fitness;
                best_swarm_pos = swarm(i).position;
            end
        
        
            end
        end
        Iter = Iter+1;
    end
end