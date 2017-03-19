function new_population = mate(selectedIndividuals, x, I, population)

    i = population;
    nelem = size(x, 2);
    
    while i - 1 > 0
        
        crossPoint = round(rand*nelem);

        Indi1 = [x(I(selectedIndividuals(i)), 1:crossPoint) x(I(selectedIndividuals(i-1)), crossPoint+1:nelem)];
        Indi2 = [x(I(selectedIndividuals(i-1)), 1:crossPoint) x(I(selectedIndividuals(i)), crossPoint+1:nelem)];

        new_population(population + 1 - i, :) = Indi1;
        new_population(population + 2 - i, :) = Indi2;

        i = i - 2; % population size must be even for algorithm to work properly
    end

end