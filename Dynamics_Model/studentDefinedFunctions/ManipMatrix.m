function M = ManipMatrix(m, I)
    % This function returns the manipulator mass matrix for a given mass
    % and moment of inertia amount x y and z

    % Calculate ManipMatrix
    M = [ eye(3)*m zeros(3,3)
    zeros(3,3)   diag(I)];

end
