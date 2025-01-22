import numpy as np
from copy import deepcopy
from typing import List

# ***************************************
# Helper Functions for readable code
# *************************v*************

def randi(**kwargs):
    ''' draws random int (0 or 1) ( or in 'min'-'max' range if specified in kwargs) '''
    dim = ('dim' in kwargs) and kwargs['dim'] or 1
    min_val = ('min' in kwargs) and kwargs['min'] or 0
    max_val = ('max' in kwargs) and kwargs['max'] or 1
    choice = np.random.randint(min_val, max_val)
    return choice

def randf(**kwargs):
    ''' draws random float in [0;1] (or in 'min'-'max' range if specified in kwargs) '''
    dim = ('dim' in kwargs) and kwargs['dim'] or 1
    min_val = ('min' in kwargs) and kwargs['min'] or 0
    max_val = ('max' in kwargs) and kwargs['max'] or 1
    choice = np.random.random_sample()
    return (max_val - min_val) * choice + min_val

def rando(option1, option2, chance=0.5):
    ''' returns one of the options depending on the chance '''
    if randb(chance):
        return option1
    else:
        return option2

def randb(chance=0.5):
    return randf() < chance

# ***************************************
# Various selection methods
# *************************v*************

def select_by_cutoff(pop, size):
    ''' select all individuals of population until cut-off '''
    return pop[0:size]
    
def select_by_graceful_cutoff(pop, size, age_grace_period:int=5):
    ''' select all individuals of population until cut-off, but retain 
        all individuals younger than the grace-period age '''
    new_pop = []
    for individual in pop:
        if individual.age >= 1 and individual.age <= age_grace_period:
            new_pop.append(individual)
    for new_individual in new_pop:
        pop.remove(new_individual) 
    new_pop += pop
    return new_pop[0:size]
    
def select_by_roulette(pop, size):
    ''' select individuals of population with probability proportional to
        their fitness '''
    new_pop = []
    while len(new_pop) < size:
        if len(new_pop) > 1:
            if new_pop[-1] in pop:
                pop.remove(new_pop[-1])
        total_fitness = sum([individual.get_fitness() for individual in pop])
        ball = randf() * total_fitness
        current_fitness  = 0
        for individual in pop:
            current_fitness += individual.get_fitness()
            if ball < current_fitness:
                new_pop.append(individual)
                break
    return new_pop
    
def select_by_walk(pop, size, walk_rate:float=0.5):
    ''' select individuals of population if random draw is smaller than
        some probability-rate (like walking a probabilistic tree structure) '''
    new_pop = []
    while len(new_pop) < size:
        if len(new_pop) > 1:
            if new_pop[-1] in pop:
                pop.remove(new_pop[-1])
        for individual in pop:
            if randf() < walk_rate:
                new_pop.append(individual)
                break
    return new_pop

# ******************************************
# Individual / Population template classes
# *************************v****************

class Individual:
    next_id = 0
    def __init__(self, problem_instance, genome=None, **kwargs):
        self.args = kwargs
        self.problem_instance = problem_instance
        self.genome = genome or problem_instance.generate()
        self.fitness = None
        self.id = Individual.next_id
        self.age = 0
        Individual.next_id += 1

    def clone(self):#->Individual
        new_individual = type(self)(self.problem_instance, deepcopy(self.genome), **self.args)
        return new_individual
    
    def mutate(self):#->Individual
        new_individual = type(self)(self.problem_instance, self.problem_instance.mutate(self.genome), **self.args)
        return new_individual
    
    def recombine(self, other):#->Individual
        new_individual = type(self)(self.problem_instance, self.problem_instance.recombine(self.genome, other.genome), **self.args)
        return new_individual
    
    def evaluate(self, population) -> float:
        self.fitness = self.compute_fitness(population)
        return self.fitness

    def get_fitness(self)-> float:
        return self.fitness

    def compute_fitness(self, population) -> float:
        return self.compute_problem_fitness()

    def compute_problem_fitness(self) -> float:
        return self.problem_instance.evaluate(self.genome)
    
    def to_str(self) -> str:
        result = ''
        result += '<' + str(self.__class__.__name__) 
        result += ' ' + str(self.genome)
        result += '\t@' + str(round(self.compute_problem_fitness(), 5)) 
        result += '>'
        return result
    
    def __str__(self) -> str:
        return self.to_str()

class Population:
    def __init__(self, problem_instance, individuals=None, **kwargs):
        self.args = kwargs
        self.problem_instance = problem_instance
        self.age = 0
        self.mut_rate = self.args.get('mut', 0.1)
        self.rec_rate = self.args.get('rec', 0.3)
        self.par_rate = self.args.get('par', 0.3)
        self.selection = self.args.get('selection', select_by_cutoff)
        self.selection_args = self.args.get('selection_args', {})
        # Individuals can either be a list of previous generation individuals (which we adopt for this population)
        # or just a individual-type class, in which case we generate a new population of these class instances 
        if isinstance(individuals,list):
            self.individual_class = kwargs.get('individual_class', (len(individuals) > 0) and type(individuals[0]) or Individual)
            self.individuals = individuals
        elif isinstance(individuals,int):
            self.individual_class = kwargs.get('individual_class', Individual)
            self.individuals = self.generate_all(individuals)
        else:
            self.individuals = []
        self.size = len(self.individuals)

    def choose_mate(self, individual:Individual) -> Individual:
        return self.individuals[randi(max=int(self.par_rate * self.size))]
        
    def choose_random(self) -> Individual:
        return self.individuals[randi(max=self.size)]

    def generate(self) -> Individual:
        return self.individual_class(self.problem_instance, **self.args)
        
    def generate_all(self, size:int) -> List[Individual]:
        return [self.generate() for _ in range(size)]

    def evaluate(self):
        current_population = deepcopy(self)
        self.individuals.sort(reverse=self.problem_instance.maximizing(), key=lambda individual: individual.evaluate(current_population))
        return self
    
    def select(self, size=None):
        size = size or self.size
        self.evaluate()
        self.individuals = self.selection(self.individuals, size, **self.selection_args)
        return self
        
    def mutate(self):
        self.individuals+= [individual.mutate() for individual in self.individuals if randb(self.mut_rate)]
        return self
    
    def recombine(self):
        self.evaluate()
        self.individuals += [individual.recombine(self.choose_mate(individual)) for individual in self.individuals if randb(self.rec_rate)]
        return self
        
    def evolve(self):
        new_population = type(self)(self.problem_instance, self.individuals, **self.args)
        new_population.age = self.age + 1
        for individual in new_population.individuals:
            individual.age += 1
        new_population.recombine() # add new children to the population
        new_population.mutate()    # add new mutants to the population
        new_population.select()    # cut down population to its original size
        return new_population

    def __str__(self):
        return f"Population at t_{self.age}:\n" + "\n".join(str(i) for i in self.individuals) + "\n"

class VectorProblem:
    ''' general problem interface '''
    def maximizing(self):
        return self.objective_maximizing
    def minimizing(self):
        return not self.objective_maximizing
    def best(self):
        return None
    def best_result(self):
        return None
    def dim(self):
        return self.dimensionality
    def dims(self):
        return range(0, self.dim())


class N_Queens_Problem(VectorProblem):
    def __init__(self, dimensionality:int):
        self.dimensionality = dimensionality
        self.objective_maximizing = False
    def min(self, d:int=0) -> float:
        return 0
    def max(self, d:int=0) -> float:
        return self.dimensionality
    def check_solution(self, candidate) -> float:
        # validate solution by checking how many queen-collisions would occur, where
        # - a valid solution has 0 collisions
        # - a maximally bad solutions has n-1 collisions (e.g., all on same column as first queen)
        collisions = 0
        for row, queen_pos in enumerate(candidate):
            assert 0 <= queen_pos < len(candidate)
            # first (row) queen always fine (as long as the position-value is legal)
            if row == 0:
                pass
            # for the other n-1 rows,
            # check if other queen in same column above,
            if queen_pos in candidate[:row]:
                collisions += 1
                continue
            # diagonally to the left above,
            elif any([queen_pos-i == candidate[row-i] for i in range(1,row+1)]):
                collisions += 1
                continue 
            # # or diagonally to the right above,
            elif any([queen_pos+i == candidate[row-i] for i in range(1,row+1)]):
                collisions += 1
                continue 
        return collisions
    
    def evaluate(self, candidate:List[int]) -> int:
        # evaluate population candidate, return fitness
        return self.check_solution(candidate)
    
    def generate(self) -> List[float]:
        # generate one valid individual that conforms to the problem requirements
        return [randi(min=self.min(d), max=self.max(d)) for d in self.dims()]
    
    def mutate(self, candidate, **kwargs):
        # randomly mutate a solution by changing one row-position
        locus = randi(min=self.min(), max=self.max())
        if np.random.sample() < 0.5:
            candidate[locus] = (candidate[locus] + 1) % self.dim()
        else:
            candidate[locus] = (candidate[locus] - 1) % self.dim()
        return candidate
    
    def recombine(self, candidate1:List[float], candidate2:List[float]):
        # one-point-crossover for two parent candidates
        new_candidate = candidate1[:self.dimensionality//2] + candidate2[self.dimensionality//2:]
        return new_candidate


if __name__ == "__main__":    
    # Example EA process of 25 individuals (over 100 generations) for the 10-Queen optimization problem
    DIMS = 100
    NR_IND = 50
    GENERATIONS = 1000
    import time
    start = time.time()
    queens = N_Queens_Problem(dimensionality=DIMS)
    population = Population(queens, individuals=NR_IND)
    print(population.evaluate())
    for step in range(GENERATIONS):
        population = population.evolve()
    print(population.evaluate())
    print(f"this took: {time.time() - start} seconds")