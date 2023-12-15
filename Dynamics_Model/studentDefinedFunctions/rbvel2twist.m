%% rbvel2twist(V_hat) is the inverse mapping of twist2rbvel. 

function V = rbvel2twist(V_hat)
    % TODO: construct the 6-vector twist V from V_hat
    V = [V_hat(1:3,4) ; skew2angvel(V_hat(1:3, 1:3))];
end
