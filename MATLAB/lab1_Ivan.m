n_bits = 10;
n_param = 1;
pop_size = 6;
max_iter = 100;

x = round(rand(pop_size, n_bits));

m = 0;

iter = 0;

ff_av_init = mean(sum(x, 2));

while m < 8 && iter < max_iter
    
    ff = sum(x, 2);

    prob = ff / sum(ff);

    parents = [];

    for i = 1:pop_size
        shot = rand(1);

        c = 0;

        for j = 1:pop_size
            c = c + prob(j);
            if shot <= c
                parents(i,:) = x(j,:);
                break;
            end
        end
    end

    pairs = parents(randperm(pop_size), :);

    for i = 1:2:((pop_size) / 2) + 2
        chom1 = pairs(i, 1:(n_bits / 2));
        pairs(i, 1:(n_bits / 2)) = pairs(i + 1, 1:(n_bits / 2));
        pairs(i + 1, 1:(n_bits / 2)) = chom1;
    end

    
    iter =iter + 1
    m = max(sum(pairs, 2))
    
    ff_av = mean(sum(x, 2));
end