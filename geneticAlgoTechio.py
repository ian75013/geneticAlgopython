# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 23:14:01 2018

@author: naifos
"""

import random
import sys
#from answer import is_answer, get_mean_score
# You can redefine these functions with the ones you wrote previously.
# Another implementation is provided here.

#"from encoding import create_chromosome
#"from tools import selection, crossover, mutation
alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#"           Chromosome encoding
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def get_letter():
    return random.choice(alphabet)

def create_chromosome(size):
    # TODO: Create a chromosome as a string of the right size
    result =""
    for i in range(1,size+1) : 
        result+=get_letter()
    return result
#"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def get_answer():
    return "sYneQUanoneLMOne69ay9vt"


#"             Fitting function
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def get_score(chrom):
    key = get_answer()
    # TODO: implement the scoring function
    #  * compare the chromosome with the solution (how many character are in the correct position?)
    count=0
    universe = len(key)
    for i in range(0,universe):
        if(chrom[i]==key[i]):
            count+=1
    return count/universe

def create_population(pop_size, chrom_size):
    # use the previously defined create_chromosome(size) function
    # TODO: create the base population
    chrom=[]
    for i in range(1,pop_size):
        chrom.append(create_chromosome(chrom_size))
    
    return chrom
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
#"           Chromosome selection
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def score(chrom):
    # floating number between 0 and 1. The better the chromosome, the closer to 1
    # We coded the get_score(chrom) in the previous exercise
    return get_score(chrom)
    
def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
    # TODO: implement the selection function
    #  * Sort individuals by their fitting score
    #  * Select the best individuals
    #  * Randomly select other individuals
    Scorelist=list()
    for i in range(0,len(chromosomes_list)-1):
        Scorelist.append(score(chromosomes_list[i]))
    print(Scorelist)
    
    chromosomes_list_back = list(chromosomes_list)
    selectedchrom=list()
    
    for i in range(0,round((len(chromosomes_list_back)-1)*GRADED_RETAIN_PERCENT)):
        indexmax = Scorelist.index(max(Scorelist))
        selectedchrom.append(chromosomes_list_back[indexmax])
        chromosomes_list_back.remove(chromosomes_list_back[indexmax])
        Scorelist.remove(Scorelist[indexmax])
        
        
    for i in range(0,round((len(chromosomes_list_back)-1)*NONGRADED_RETAIN_PERCENT)):
        index = random.randrange(0,len(chromosomes_list_back))
        selectedchrom.append(chromosomes_list_back[index])
        chromosomes_list_back.remove(chromosomes_list_back[index])
        
    return selectedchrom
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#"                  Crossover
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def crossover(parent1, parent2):
    # TODO: implement the crossover function
    #  * Select half of the parent genetic material
    #  * child = half_parent1 + half_parent2
    #  * Return the new chromosome
    #  * Genes should not be moved
    #chromosome_child = ""
    #for i in range(0,round(0.5*parent1)):
    #    chromosome_child.append(parent1[i])
    #for i in range(round(0.5*parent1),round(0.5*parent1)+round(0.5*parent2)):
    #    chromosome_child.append(parent2[i])
    half_1=len(parent1)/2
    half_2=len(parent2)/2
    chromosome_child = parent1[:int(half_1)]+parent2[int(half_2):] 
    return chromosome_child
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#"                 mutation
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    
def mutation(chrom):
    # TODO: implement the mutation function
    #  * Random gene mutation : a character is replaced
    index=random.randrange(0,len(chrom))
    
    chrom_mut = list(chrom)
    chrom_mut[index] = get_letter()
    return "".join(chrom_mut)
    
def is_answer(chromosome):
    if(chromosome==get_answer()):
        return chromosome
    else:
        return None
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
#"                  Main Algorithm
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""    
def generation(population):
    
    # selection
    # use the selection(population) function created on exercise 2
    select = selection(population)
    
    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    # TODO: implement the reproduction
    while len(children) < (len(population)-len(select)):
        ## crossover
        parent1 = random.choice(population) # randomly selected
        parent2 = random.choice(population) # randomly selected
        # use the crossover(parent1, parent2) function created on exercise 2
        child = crossover(parent1, parent2)
        
        ## mutation
        # use the mutation(child) function created on exercise 2
        child = mutation(child)
        children.append(child)
    
    # return the new generation
    return select + children

def algorithm():
    chrom_size = len(get_answer())
    population_size = 10
    
    # create the base population
    population = create_population(population_size, chrom_size)
    
    answers = []
    
    # while a solution has not been found :
    while not answers:
        ## create the next generation
        # TODO: create the next generation using the generation(population) function
        population = generation(population)
        
        ## display the average score of the population (watch it improve)
        #print(get_mean_score(population), file=sys.stderr)
    
        ## check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)
                
    # TODO: print the solution
    for chromsol in answers :
        print(chromsol)
    