function EOM = EOM_lag(L,q,dq,ddq,Y)
    % This function returns C matrix from Mass matrix M
    
    EOM = sym(jacobian(gradient(L,dq) , [q;dq])*[dq;ddq] - gradient(L,q)...
        - Y);
end
