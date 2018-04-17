# ga_kp.py
# GENETIC ALGORITHM FOR THE 0/1 KNAPSACK PROBLEM
# ORTEGA VICTORIANO IVAN

import math
import random
import functools

knapsack_capacity = 20
w = [2,3,4,4,5,10,12,1,3]
v = [3,3,3,5,6,7,7,5,5]
# Chromosomes must be the same length than the number of items
L_chromosome=len(w)
N_chains=2**L_chromosome
crossover_point=L_chromosome//2

#Number of chromosomes
N_chromosomes=10
#probability of mutation
prob_m=0.7

# Initial population
F0=[]
fitness_values=[]


# This function generates a random chromosome.
def random_chromosome():
    
    chromosome=[]
    
    for i in range(0,L_chromosome):
        if random.random()<0.1:
            chromosome.append(0)
        else:
            chromosome.append(1)

    return chromosome


# Initialize a random population
for i in range(0,N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)


# This function evaluates a chromosome in order to
# get the total value according to the items that
# it is using.
def f(chromosome):
    global w,v
    i = 0
    total_value = 0
    for c in chromosome:
        if c == 1:
            total_value += v[i]
        i += 1
    return total_value


# This function gets the total weight according to
# the items that a chromosome has.
def get_weight(chromosome):
    global w
    i = 0
    total_weight = 0
    for c in chromosome:
        if c == 1:
            total_weight += w[i]
        i += 1
    return total_weight


# This function gets the fitness of a chromosome
# according to its value and its weight.
def fitness_fucntion(chromosome):

    total_weight = get_weight(chromosome)
    fitness = f(chromosome)

    if total_weight > knapsack_capacity: 
        while total_weight > knapsack_capacity:
            l = len(chromosome)
            for i in range(0,l):
                if chromosome[i] == 1:
                    chromosome[i] ^= 1
                    break
            total_weight = get_weight(chromosome)
        fitness = f(chromosome)
        return fitness
    else:
        return fitness


# This function gets the fitness values of each individual in 
# the population.
def evaluate_chromosomes():
    
    global F0,knapsack_capacity

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
            acc += 0.01
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
        
        # Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            o1[int(round(random.random()*(L_chromosome-1)))]^=1
        if random.random() < prob_m:
            o2[int(round(random.random()*(L_chromosome-1)))]^=1
        
        # The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

    # The generation replaces the old one
    F0[:]=F1[:]

if __name__ == '__main__':
    it_max = 200
    while it_max > 0:
        F0.sort(key=functools.cmp_to_key(compare_chromosomes))
        evaluate_chromosomes()
        nextgeneration()
        it_max -= 1