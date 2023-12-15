%% tform2adjoint(g) maps the the rigid body transformation g, 
%% in homogeneous coordinates, to the transformation adjoint matrix, Adg.

function Adg=tform2adjoint(g)
    % TODO: construct the 6x6 transformation adjoint matrix Adg from g
    Adg = [[g(1:3, 1:3)  angvel2skew(g(1:3,4))*g(1:3,1:3)]
           [zeros(3,3)                     g(1:3, 1:3)]];
end
