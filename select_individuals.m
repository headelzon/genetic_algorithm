function [selectedIndividuals] = select_individuals(sorted_fit)
    
    probability = sorted_fit/sum(sorted_fit);

    for j = 1:length(probability)
        matingVector(j,1) = sum(probability(1:j));
    end

    for j = 1:length(probability)
        matingSelector = rand;
        
        for i = 1:length(probability)
            if matingSelector < matingVector(i,1)
                selectedIndividuals(j) = i;
                break
            end
        end
    end

end