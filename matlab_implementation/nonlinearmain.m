yd = [ 2.1*ones(1,100) 3.5*ones(1,100) 2*ones(1,100) 3*ones(1,100)];
[y,x,i] = nonlinearsystem(yd);

plot(x,y)