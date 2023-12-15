%% twist2rbvel(V) maps the 6-vector twist V to the 4x4 rigid body velocity matrix in homogeneous coordinates V_hat

function V_hat=twist2rbvel(V)
    % TODO: construct the 4x4 rigid body velocity matrix in homogeneous
    % coordinates V_hat from V
    V_hat = [[angvel2skew(V(4:6)) V(1:3)]
            [zeros(1,3)              0 ]];
end