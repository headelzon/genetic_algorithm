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
average_ff_init = mean(ff_init)     % average fitness

ff_av_array = average_ff_init;
ff_max_array = max(ff_init);

ff = ff_init;
iterations = 0;
iter_array = iterations;

% while all(ff == ff(1)) == 0
while iterations < 70
% while mean(ff) ~= 10
    
    [B,I] = sort(ff); % B - fitness sorted, I - corresponding indices
    
    selectedIndividuals = select_individuals(B);
    
    new_x = mate(selectedIndividuals, x, I, population);
    
    x = new_x;
    
    ff = sum(x, 2);
    ff_total = sum(ff);
    
    iterations = iterations + 1;
    
    ff_av_array = [ff_av_array mean(ff)];
    ff_max_array = [ff_max_array max(ff)];
    iter_array = [iter_array iterations];
    
end

ff;
average_ff = mean(ff)

figure(1)
subplot(2, 1, 1)
stem(iter_array, ff_av_array, 'r', 'filled', 'LineStyle', 'none')
xlabel('Iterations')
ylabel('Average fitness of population')
subplot(2, 1, 2)
stem(iter_array, ff_max_array, 'r', 'filled', 'LineStyle', 'none')
xlabel('Iterations')
ylabel('Maximum fitness in population')