# ga_coin.py
# GENETIC ALGORITHM FOR THE MINIMUM CHANGE PROBLEM
# ORTEGA VICTORIANO IVAN

import math
import random
import functools

d = [1,3,5,6,8,7]
N = 129

# Chromosomes must be the same length than the number of coin denominations
L_chromosome=len(d)
N_chains=2**L_chromosome
crossover_point=L_chromosome//2

#Number of chromosomes
N_chromosomes=10
#probability of mutation
prob_m=0.5

# Initial population
F0=[]
fitness_values=[]


# This function generates a random chromosome.
def random_chromosome():
    
    chromosome=[]
    
    # Generate chromosomes with random integer numbers
    # between 0 and N
    for i in range(0,L_chromosome):
        if random.random()<0.5:
            chromosome.append(random.randint(0,N//2))
        else:
            chromosome.append(random.randint((N//2)+1,N))
            
    return chromosome


# Initialize a random population
for i in range(0,N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)


# This function evaluates a chromosome in order to
# get the total value according to the coins used.
def f(chromosome):
    global d
    i = 0
    total_value = 0
    for c in chromosome:
        total_value += d[i]*c
        i += 1
    return total_value


# This function gets the fitness of a chromosome
# according to its value and its number of coins.
def fitness_fucntion(chromosome):

    global N

    # Gamma is the penalty factor
    gamma = 0.01

    number_of_coins = sum(chromosome)
    fitness = f(chromosome)

    if fitness <= N:
        return fitness-number_of_coins*gamma

    else:
    	while fitness > N:
    		
    		l = len(chromosome)
    		
    		for i in range(0,l):
    			if chromosome[i] >= 1:
    				chromosome[i] -= 1
    				break
    		fitness = f(chromosome)
    	number_of_coins = sum(chromosome)

    	return fitness-number_of_coins*gamma


# This function gets the fitness values of each individual in 
# the population.
def evaluate_chromosomes():
    
    global F0

    for p in range(N_chromosomes):
        fitness_values[p]=fitness_fucntion(F0[p])
        

# This function compares the fitness between two chromosomes.
def compare_chromosomes(chromosome1,chromosome2):
    fvc1=fitness_fucntion(chromosome1)
    fvc2=fitness_fucntion(chromosome2)
    if fvc1 > fvc2:
        return -1
    elif fvc1 == fvc2:
        return 0
    else:
        return 1


suma=float(N_chromosomes*(N_chromosomes+1))/2.

Lwheel=N_chromosomes*10

# Roulette wheel function.
def create_wheel():
    global F0,fitness_values
    maxv=max(fitness_values)
    acc=0
    for p in range(N_chromosomes):
        if maxv == fitness_values[p]:
            acc += 0.0001
        else:
            acc+=maxv-fitness_values[p]
    fraction=[]

    for p in range(N_chromosomes):
        fraction.append( float(maxv-fitness_values[p])/acc)
        if fraction[-1]<=1.0/Lwheel:
            fraction[-1]=1.0/Lwheel

    fraction[0]-=(sum(fraction)-1.0)/2
    fraction[1]-=(sum(fraction)-1.0)/2

    wheel=[]

    pc=0

    for f in fraction:
        Np=int(f*Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc+=1

    return wheel
        
F1=F0[:]
gen_num = 0

def nextgeneration():
    
    global gen_num

    F0.sort(key=functools.cmp_to_key(compare_chromosomes))
    print('Generation ',gen_num)
    gen_num += 1
    print ("Best solution so far:")
    print ("f(",F0[0],")= ", f(F0[0]))
                                                                    
    # Elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]
    for i in range(0,(N_chromosomes-2)//2):
        roulette=create_wheel()
        # Two parents are selected
        p1=random.choice(roulette)
        p2=random.choice(roulette)
        # Two descendants are generated
        o1=F0[p1][0:crossover_point]
        o1.extend(F0[p2][crossover_point:L_chromosome])
        o2=F0[p2][0:crossover_point]
        o2.extend(F0[p1][crossover_point:L_chromosome])
        
        prob_sum = 0.5
        # Individuals always mutate, but it depends of a random number
        rnd_num = int(round(random.random()*(L_chromosome-1)))
        if random.random() < prob_m:
        	if random.random() <= prob_sum:
        		o1[rnd_num]+=1
        	else:
        		o1[rnd_num] = abs(o1[rnd_num]-1)

        rnd_num = int(round(random.random()*(L_chromosome-1)))
        if random.random() < prob_m:
        	if random.random() < prob_sum:
        		o2[rnd_num]+=1
        	else:
        		o2[rnd_num] = abs(o2[rnd_num]-1)
        
        # The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

    # The generation replaces the old one
    F0[:]=F1[:]

if __name__ == '__main__':
    it_max = 5000
    while it_max > 0:
        F0.sort(key=functools.cmp_to_key(compare_chromosomes))
        evaluate_chromosomes()
        nextgeneration()
        it_max -= 1
