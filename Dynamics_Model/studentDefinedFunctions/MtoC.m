function C = MtoC(M,q,dq)
    % This function returns C matrix from Mass matrix M
    
    n = max(size(M));
    C = sym(zeros(n));

 
    for i = 1:n
        for j = 1:n
            for k= 1:n

                C(i,j) = C(i,j) + (diff(M(i,j),q(k))+diff(M(i,k),q(j))...
                    -diff(M(k,j),q(i)))*dq(k);
                
                
            end
            
        end
    end

    C = 1/2*C;

end
