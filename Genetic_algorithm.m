clear all;
clc;

n_param = 1;    % number of parameters in chromosome
n_elem = 10;    % number of bits in each paramter
population = 20; % size of populaton

if rem(population, 2) ~= 0
    warning('Population size should be even');
end

x = randi([0 1], [population n_elem]);    % population, values 0 or 1

ff_init = sum(x, 2);                % cost of population
ff_total_init = sum(ff_init);       % sum of fitnesses
average_ff_init = mean(ff_init);    % average fitness

ff = ff_init;
iterations = 0;

while all(ff == ff(1)) == 0

    [B,I] = sort(ff); % B - fitness sorted, I - corresponding indices
    
    selectedIndividuals = select_individuals(B);
    
    new_x = mate(selectedIndividuals, x, I, population);
    
    x = new_x;
    
    ff = sum(x, 2);
    ff_total = sum(ff);
    
    iterations = iterations + 1;
    
end

ff;
average_ff = mean(ff)
