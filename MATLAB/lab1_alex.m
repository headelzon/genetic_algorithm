clear all;
clc;

% define boundary conditions
nparam = 1;
popsize = 20;
nelemen = 10;
% initialize population
P = round(rand(popsize, nelemen));

iterations = 0;

fit_init = sum(P, 2); %determine fitness of each individual
av_init = mean(fit_init);

% while(1)
    fit = sum(P, 2); 
    av = mean(fit_init);
    [B,I] = sort(fit); % B - fitness sorted, I - corresponding indices

    % mating probability vector
    prob = B/sum(B);

    for j = 1:length(prob)
        matingVector(j,1) = sum(prob(1:j));
    end

    for j = 1:popsize
        matingSelector = rand;
        
        for i = 1:length(prob)
            if matingSelector < matingVector(i,1)
                selectedIndividual(j) = i;
                break
            end
        end
    end

    % cross selected individuals

    i = popsize;
   
    while i - 1 > 0
        crossPoint = round(rand*nelemen);

        Indi1 = [P(I(selectedIndividual(i)), 1:crossPoint) P(I(selectedIndividual(i-1)), crossPoint+1:nelemen)];
        Indi2 = [P(I(selectedIndividual(i-1)), 1:crossPoint) P(I(selectedIndividual(i)), crossPoint+1:nelemen)];

        newP(popsize + 1 - i, :) = Indi1;
        newP(popsize + 2 - i, :) = Indi2;

        i = i - 2; % population size must be even for algorithm to work properly
    end

    P
    P = newP
    fit = sum(P, 2);
    av2 = mean(fit);
    
    iterations = iterations + 1;
    
    if all(fit == fit(1)) == 1
        fit
        av2
        P
        iterations
        % break
    end
% end