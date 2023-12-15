function Xi = XiVector(w,p)
% This function returns the Twist for a given w and p 

w= w';
p= p';

w_x_p = -(cross(w,p));
Xi = [w_x_p ; w];

end