function [index_a, index_b] = select_individuals(array)
    
    
    index_a = 0;
    index_b = 0;
    
    while index_a == index_b            %indices cannot be the same
        
        rand_a = rand();
        rand_b = rand();
        
        if rand_a >= array(6, 1)
            index_a = array(6, 3);
        elseif rand_a >= array(5, 1)
            index_a = array(5, 3);
        elseif rand_a >= array(4, 1)
            index_a = array(4, 3);
        elseif rand_a >= array(3, 1)
            index_a = array(3, 3);
        elseif rand_a >= array(2, 1)
            index_a = array(2, 3);
        elseif rand_a >= array(1, 1)
            index_a = array(1, 3); 
        end

        if rand_b >= array(6, 1)
            index_b = array(6, 3);
        elseif rand_b >= array(5, 1)
            index_b = array(5, 3);
        elseif rand_b >= array(4, 1)
            index_b = array(4, 3);
        elseif rand_b >= array(3, 1)
            index_b = array(3, 3);
        elseif rand_b >= array(2, 1)
            index_b = array(2, 3);
        elseif rand_b >= array(1, 1)
            index_b = array(1, 3);  
        end
        
    end

end