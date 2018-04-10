# File ag_ackley.py
# Example of GA for the Ackley Function
# Dr. Jorge Luis Rosas Trigueros
# Modified by: Ortega Victoriano Ivan

from tkinter import *
import math
import random
import functools
import numpy as np

L_chromosome=8 	
N_chains=2**L_chromosome

#Lower and upper limits of search space in the Ackley Function
a=-32.768
b=32.768

crossover_point=L_chromosome//2	# 

# This function generates a random chromosome
def random_chromosome():
    chromosome=[]
    for i in range(0,L_chromosome):
        if random.random()<0.1:
            chromosome.append(0)
        else:
            chromosome.append(1)

    return chromosome

#Number of chromosomes
N_chromosomes=10

#probability of mutation
prob_m=0.5

# Original Population (Genetic Notation)
F0=[]
fitness_values=[]

# Generate a random pupulation
for i in range(0,N_chromosomes):
    F0.append(random_chromosome())
    fitness_values.append(0)	# Initialize the fitness values

# Binary decodification
def decode_chromosome(chromosome):
    global L_chromosome,N_chains,a,b
    value=0
    for p in range(L_chromosome):
        value+=(2**p)*chromosome[-1-p]

    return a+(b-a)*float(value)/(N_chains-1)

# N-Dimensional Ackley Function
def ackley(*X):
	dim = len(X)
	sum1 = np.sqrt((1/dim)*sum([x**2 for x in X]))
	cosine_term = sum([np.cos(2*np.pi*x) for x in X])
	return -20*np.exp(-0.2*sum1)-np.exp((1/dim)*cosine_term)+np.e+20


def evaluate_chromosomes():
    global F0

    for p in range(N_chromosomes):
        v=decode_chromosome(F0[p])
        fitness_values[p]=ackley(v) # The fitness is the value in the search space evaluated in the function
        

def compare_chromosomes(chromosome1,chromosome2):
    vc1=decode_chromosome(chromosome1)
    vc2=decode_chromosome(chromosome2)
    fvc1=ackley(vc1)
    fvc2=ackley(vc2)
    if fvc1 > fvc2:
        return 1
    elif fvc1 == fvc2:
        return 0
    else: #fvg1<fvg2
        return -1


suma=float(N_chromosomes*(N_chromosomes+1))/2.

Lwheel=N_chromosomes*10

# Common criteria to select the individuals in
# the genetic operations. The probability to choose
# an individual depends on its aptitude.
def create_wheel():
    global F0,fitness_values
    
    maxv=max(fitness_values)
    acc=0
    for p in range(N_chromosomes):
        acc+=maxv-fitness_values[p]
    fraction=[]
    for p in range(N_chromosomes):
        fraction.append( float(maxv-fitness_values[p])/acc)
        if fraction[-1]<=1.0/Lwheel:
            fraction[-1]=1.0/Lwheel
    #print fraction
    fraction[0]-=(sum(fraction)-1.0)/2
    fraction[1]-=(sum(fraction)-1.0)/2
    #print fraction

    wheel=[]

    pc=0

    for f in fraction:
        Np=int(f*Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc+=1

    return wheel

# The descendants    
F1=F0[:] 

n = 0
def nextgeneration():
    global n
    print (n)
    n += 1
    w.delete(ALL)
    F0.sort(key=functools.cmp_to_key(compare_chromosomes))
    print ("Best solution so far:")
    print ("ackley(",decode_chromosome(F0[0]),")= ", ackley(decode_chromosome(F0[0])))
                                                                    
    #elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]
    for i in range(0,(N_chromosomes-2)//2):
        roulette=create_wheel()
        #Two parents are selected
        p1=random.choice(roulette)
        p2=random.choice(roulette)
        #Two descendants are generated
        o1=F0[p1][0:crossover_point]
        o1.extend(F0[p2][crossover_point:L_chromosome])
        o2=F0[p2][0:crossover_point]
        o2.extend(F0[p1][crossover_point:L_chromosome])
        #Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            o1[int(round(random.random()*(L_chromosome-1)))]^=1
        if random.random() < prob_m:
            o2[int(round(random.random()*(L_chromosome-1)))]^=1
        #The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

    graph_f()
    graph_population(F0,w,s,s,xo,yo,'red')
    graph_population(F1,w,s,s*0.5,xo,yo,'green')
    #The generation replaces the old one
    F0[:]=F1[:]



#visualization
master = Tk()

xmax=400
ymax=400

xo=200
yo=200

s=10

w = Canvas(master, width=xmax, height=ymax)
w.pack()

            
button1 = Button(master, text="Next Generation", command=nextgeneration)
button1.pack()

N=2000


def graph_f():

	# Recommended interval for the Ackley Function
    xini=-32.768
    xfin=32.768

    dx=(xfin-xini)/N

    xold=xini
    yold=ackley(xold)
    for i in range(1,N):
        xnew=xini+i*dx
        ynew=ackley(xnew)
        w.create_line(xo+xold*s,yo-yold*s,xo+xnew*s,yo-ynew*s)
        xold=xnew
        yold=ynew

def graph_population(F,mycanvas,escalax,escalay,xcentro,ycentro,color):
    for chromosome in F:
        x=decode_chromosome(chromosome)
        mycanvas.create_line(xcentro+x*escalax,ycentro-10*escalay,xcentro+x*escalax, ycentro+10*escalay,fill=color)


graph_f()
graph_population(F0,w,s,s,xo,yo,'red')
F0.sort(key=functools.cmp_to_key(compare_chromosomes))
evaluate_chromosomes()



mainloop()
