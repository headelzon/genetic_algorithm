clear all;
clc;

n_param = 1;    % number of parameters in chromosome
n_elem = 10;    % number of bits in each paramter
population = 6; % size of populaton

x = randi([0 1], [population n_elem])    % population 6 rows, 10 columns, values 0 or 1

ff_init = sum(x, 2)                % cost of population
ff_total_init = sum(ff_init);            % sum of fitnesses
average_ff_init = mean(ff_init)    % average fitness

ff = ff_init;
ff_total = ff_total_init;

iterations = 0;

while all(ff == ff(1)) == 0

    prob = ff/ff_total;         % probability of selection

    [prob, A] = sort(prob);
    probabilities = [prob, A]; %probabilities(1,2) - 1 row, 2 col

    C = [];
    min = 0;

    for n=1:6
        C = [C; min, min+prob(n)];
        min = min + prob(n);
    end

    C = [C, A]; 
    % matrix C with selection intervals (columns 1 and 2 which take into consideration
    % selection probability, and the 3rd column contains indices of corresponding individuals

    [a, b] = select_individuals(C); % select individuals a and b for mating

    x = mate(x, a, b);              % mate individuals a and b to form new population x from previous pop x

    ff = sum(x, 2);
    ff_total = sum(ff)
    
    iterations = iterations + 1;
end

ff
average_ff = mean(ff)
