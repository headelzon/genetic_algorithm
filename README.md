# genetic_algorithm
## Overview

In most cases the algorithm is written along the timeline:
1. Initialize population 
2. Calculate fitness of each individual
3. Continue if not every individual has maximum fitness
4. Basing on their fitness the probability of selection is calculated
5. 2 individuals are selected for mating
6. Cross over (85% probability)
7. Mutation (2% probability)
7. New population is created (with number of individuals preserved)
8. If all individuals have maximum fitness stop

## Definitions

<b>Population</b> - set of chromosomes, each representing a separate solution of a problem.

<b>Chromosome</b> (individual) - sequence of binary digits, representing a solution of a problem. Every solution must be encoded in this way for the algorithm to work.

<b>Cost function</b> or sometimes <b>fitness function</b> is the function that evaluates given solution. It takes one chromosome, decodes the information stored in the sequence of 1s and 0s, and is able to say how good is the individual. The cost function is different with each problem.

<b>Selection</b> of the chromosomes to mate is dependent on their fitness (cost), evaluated earlier by the cost function. The higher fitness of an individual, the higher the probability that it will be selected for mating.

After a set of individuals is chosen, each chromosome takes part in <b>cross-over</b>. A threshold is randomly chosen, and the chromosomes exchange part of their information with each other. This way, with each iteration, the chromosomes are getting better and better (their fitness is getting higher).

Having the population crossed-over, mutation can happen - random change of one bit in a chromosome. Chance of mutation is usually not bigger than 2%.

After the whole sequence the population is evaluated again by the cost function. If the average cost does not fulfill given requirements, the algorithm is repeated until it does.

## Problems solved by my algorithms
<ul>
<li>1-0 Knapsack Problem</li>
<li>Scheduling problem</li>
<li>Multivariable function minimization</li>
</ul>
