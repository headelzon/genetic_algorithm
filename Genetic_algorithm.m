clear all;
clc;

n_param = 1;    % number of parameters in chromosome
n_elem = 10;    % number of bits in each paramter
population = 6; % size of populaton

x = randi([0 1], [6 10])    % population 6 rows, 10 columns, values 0 or 1

ff = sum(x, 2)              % cost of population
av1 = mean(ff)
sum_fitness = sum(ff)


ff_total = sum(ff); 
prop = ff/ff_total;         % probability of selection

% prop = sort(prop)
[prop, A] = sort(prop)
B = [prop, A]

%B(1,2) - 1 row, 2 col

C = [];
min = 0;

for n=1:6
    C = [C; min, min+prop(n)];
    min = min + prop(n);
end

B
C

% generate two random numbers between 0 and 1

elem_choice1 = rand()
elem_choice2 = rand()
index_choice1 = 0;
index_choice2 = 0;

% TODO chosen indices can't be the same

if (elem_choice1 > C(1,1) && elem_choice1 < C(1,2))
    index_choice1 = 1;
elseif (elem_choice1 > C(2,1) && elem_choice1 < C(2,2))
        index_choice1 = 2;
elseif (elem_choice1 > C(3,1) && elem_choice1 < C(3,2))
        index_choice1 = 3;
elseif (elem_choice1 > C(4,1) && elem_choice1 < C(4,2))
        index_choice1 = 4;
elseif (elem_choice1 > C(5,1) && elem_choice1 < C(5,2))
        index_choice1 = 5;
elseif (elem_choice1 > C(6,1) && elem_choice1 < C(6,2))
        index_choice1 = 6;
end

if (elem_choice2 > C(1,1) && elem_choice2 < C(1,2))
    index_choice2 = 1;
elseif (elem_choice2 > C(2,1) && elem_choice2 < C(2,2))
        index_choice2 = 2;
elseif (elem_choice2 > C(3,1) && elem_choice2 < C(3,2))
        index_choice2 = 3;
elseif (elem_choice2 > C(4,1) && elem_choice2 < C(4,2))
        index_choice2 = 4;
elseif (elem_choice2 > C(5,1) && elem_choice2 < C(5,2))
        index_choice2 = 5;
elseif (elem_choice2 > C(6,1) && elem_choice2 < C(6,2))
        index_choice2 = 6;
end

index_choice1 % mating element 1 (its index)
index_choice2 % mating element 2

mating_point = randi([1 6])

x
[x(index_choice2, 1:mating_point), x(index_choice2, 1:mating_point)] = deal(x(index_choice2, 1:mating_point), x(index_choice1, 1:mating_point));
x

av1
ff = sum(x, 2)
av2 = mean(ff)
sum_fitness = sum(ff)
