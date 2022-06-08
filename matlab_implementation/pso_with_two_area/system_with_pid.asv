function fitness = system_with_pid(k_values)
    PL1 = 0;
    PL2 = 0;
    import RBF.*
    
    
    ut1 = [];
    ut2 = [];
    pl1 = []; 
    pl2 = [];
    ACE1 = []; 
    ACE2 = [];
    time = [];
    
    Tg = 0.08;
    Tp = 20;
    Tt = 0.3;
    Kp = 120;
    T12 = 0.545/(2*pi);
    a12 = -1;
    R = 5;
    T = 1/80;
    dt = 1/80;
    beta1 = 0.425;
    beta2 = 0.425;
    
    
    System = TwoAreaPS( Tg, Tp, Tt, Kp, T12, a12, R, T, beta1, beta2,  [0,0,0],[0,0,0] );
    
    KP1 = k_values(1);
    KI1 = k_values(2);
    KD1 = k_values(3);
    
    KP2 = k_values(4);
    KI2 = k_values(5);
    KD2 = k_values(6);
    
    
    
    ut_1 = 0;
    ut_2 = 0;
    
    t = 200;
    
    y = [];
    x = [];
    
    for i = 1:t/dt
        e_t_a1 = 0 - System.yt_a1(1);
        del_y_a1 =  System.yt_a1(1) - System.yt_a1(2);
        del2_y_a1 = System.yt_a1(1) - 2*System.yt_a1(2) + System.yt_a1(3);
    
        e_t_a2 = 0 - System.yt_a2(1);
        del_y_a2 =  System.yt_a2(1) - System.yt_a2(2);
        del2_y_a2 = System.yt_a2(1) - 2*System.yt_a2(2) + System.yt_a2(3);
    
        ut_1 = ut_1 + KI1*e_t_a1 - KP1*del_y_a1 - KD1*del2_y_a1;
    
        ut_2 = ut_2 + KI2*e_t_a2 - KP2*del_y_a2 - KD2*del2_y_a2;
    
        ut1 = [ut1 ut_1];
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
    
        Ut = [ ut_1 ; ut_2 ; PL1 ; PL2 ];
    
        System.Output(Ut);
        performance_index = [];
        performance_index = [performance_index, dt*(i*dt)*( abs(System.Y(1)) + abs(System.Y(2)))];
    end

    fitness = sum(performance_index);
end