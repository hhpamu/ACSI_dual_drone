function R = rotationMatrix(q, axis)
    % This function returns the rotation matrix for a given axis (x, y, or z) 
    % and rotation angle q.

    % Calculate rotation matrix based on axis
    switch axis
        case 'x'
            R = [1, 0, 0;
                 0, cos(q), -sin(q);
                 0, sin(q), cos(q)];
        case 'y'
            R = [cos(q), 0, sin(q);
                 0, 1, 0;
                 -sin(q), 0, cos(q)];
        case 'z'
            R = [cos(q), -sin(q), 0;
                 sin(q), cos(q), 0;
                 0, 0, 1];
        otherwise
            error('Invalid axis. Choose from x, y, or z.');
    end
end
