function [y, x, initial_states] = nonlinearsystem(yd)
    import RBF.*
    rbf = RBF(0.13,0.21,0.25,0.9,0.98,3);
    t = 1;
    yt_1 = 0.4;
    yt_2 = 0.46;
    yt_3 = 0.42;
    initial_states = [yt_1, yt_2, yt_3];
    dt = 1/400;

    Ki = -0.07709546;
    Kd = 0.58844546;
    Kp = -0.01747239;

    ut_1 = 0;

    y = [];
    x = [];

    for i = 1:t/dt
        e_t = yd(i) - yt_1;
        del_y =  yt_1 - yt_2;
        del2_y = yt_1 - 2*yt_2 + yt_3;
        
        rbf.X = [ e_t ; -del_y ;  -del2_y];
        rbf.HiddenLayer();
        rbf.OutputLayer();

        ut_1 = ut_1 + rbf.K(2)*e_t - rbf.K(1)*del_y - rbf.K(3)*del2_y;
        disp(rbf.K);
%         [y1,y2,y3] = deal(yt_1 , yt_2, yt_3);


        [yt_1 , yt_2, yt_3] = deal(yt_1*yt_2*(yt_1 + 2.5) / ( 1 + yt_1^2 + yt_2^2 )+ ut_1 , yt_1 , yt_2) ;

        y0 = yt_1;


        rbf.Update(yd(i),y0);

        y = [y, yt_1];
        x = [x, i];
    end
    

    



end