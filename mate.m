function new_population = mate(population, ind_a, ind_b)
    mating_point = randi([1 size(population, 2)]);
    
    new_population = population;
    [new_population(ind_b, 1:mating_point), new_population(ind_b, 1:mating_point)] = deal(new_population(ind_b, 1:mating_point), new_population(ind_a, 1:mating_point));

end