function dA = diffA(A,q,dq)
    % This this function returns an A dot from a given A matrix and 
    % a given list of state vectors q. This is useful for symbolic
    % variables
    
    [r,c] = size(A);
    dA = sym(zeros(r,c));
    
    for i = 1:r
         for j = 1:c
                dA(i,j) = jacobian(A(i,j),q)*dq;
    
         end
    end
    disp(dA)
end