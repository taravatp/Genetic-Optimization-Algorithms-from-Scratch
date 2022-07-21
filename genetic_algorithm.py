import copy
import math

import numpy as np
import matplotlib.pyplot as plt


class Chromosome:
    def __init__(self, cost_func, num_genes=30):
        self.cost_func = cost_func
        self.num_genes = num_genes
        self.lower_bound = self.get_bounds()[0]
        self.upper_bound = self.get_bounds()[1]
        self.chromosome = self.get_chromosome()

    def get_bounds(self):
        if self.cost_func == 'sphere':
            return [-5.12, 5.12]
        elif self.cost_func == 'bentcigar':
            return [-100, 100]
        elif self.cost_func == 'rastrigins':
            return [-5.12, 5.12]
        elif self.cost_func == 'ackley':
            return [-32.7, 32.7]
        else:
            print('you have entered an invalid cost function')
            breakpoint()

    def get_chromosome(self):
        chromosome = np.random.uniform(self.lower_bound, self.upper_bound, self.num_genes)
        return chromosome

    def set_chromosome(self, chromosome):
        self.chromosome = chromosome

    def get_cost_value(self):
        if self.cost_func == 'sphere':
            return self.sphere()
        elif self.cost_func == 'bentcigar':
            return self.bentcigar()
        elif self.cost_func == 'rastrigins':
            return self.rastrigins()
        elif self.cost_func == 'ackley':
            return self.ackley()
        else:
            print('you have entered an invalid cost function')
            breakpoint()

    def sphere(self):
        cost = sum(self.chromosome ** 2)
        return abs(cost)

    def bentcigar(self):
        cost = (self.chromosome[0] ** 2) + (10 ** 6) * np.sum(self.chromosome[1:] ** 2)
        return abs(cost)

    def rastrigins(self):
        cost = np.sum(self.chromosome ** 2 + 10 * np.cos(2 * math.pi * self.chromosome) + 10)
        return abs(cost)

    def ackley(self):
        n = self.chromosome.shape[0]
        cost = -20 * np.exp(-.2 * np.sqrt(np.sum(self.chromosome ** 2) / n)) - np.exp(
            np.sum(np.cos(2 * math.pi * self.chromosome)) / n) + 20 + np.exp(1)
        return abs(cost)


def initialization():
    solutions = []
    for n in range(Npopulation):
        solutions.append(Chromosome(cost_function))
    return solutions


def roulette_wheel(population):
    fitness = []
    chromosome_probabilities = []

    for p in population:
        fitness.append(1 / (1 + p.get_cost_value()))

    sum_fitness = sum(fitness)
    for fit in fitness:
        chromosome_probabilities.append(fit / sum_fitness)

    chromosome_cumulative_probabilities = np.cumsum(np.array(chromosome_probabilities))
    pointer_value = sum(chromosome_probabilities) * np.random.rand()
    index = np.argwhere(pointer_value <= chromosome_cumulative_probabilities)

    return population[int(index[0])]


def corssover(parent1, parent2):
    child1 = Chromosome(cost_function)
    child2 = Chromosome(cost_function)

    split_point = int(np.random.randint(0, parent1.chromosome.shape))
    child1_chromosome = np.concatenate((parent1.chromosome[0: split_point], parent2.chromosome[split_point:]))
    child1.set_chromosome(child1_chromosome)

    child2_chromosome = np.concatenate((parent2.chromosome[0: split_point], parent1.chromosome[split_point:]))
    child2.set_chromosome(child2_chromosome)

    return child1, child2


def mutate(solution, mu):
    sol = copy.deepcopy(solution)
    flag = np.random.rand(*solution.chromosome.shape) <= mu
    ind = np.argwhere(flag)
    sol.chromosome[ind] = np.random.uniform(solution.lower_bound, solution.upper_bound)
    return sol


def best_solution(population):
    best_cost = math.inf
    for sol in population:
        if sol.get_cost_value() < best_cost:
            best_cost = sol.get_cost_value()
    return best_cost


# some parameters
num_iter = 30  # number of times that we are going to run the algorithm
num_generations = 300  # number of generations that we are going to produce in each iteration
Npopulation = 50  # Number of population
cost_function = input('enter one of the following cost functions:\n1-sphere\n2-bentcigar\n3-rastrigins\n4-ackley\n')

average_cost = 0
for i in range(num_iter):
    generations = []
    best_solution_per_generation = []
    init_population = initialization()
    generations.append(init_population)

    for j in range(num_generations):
        current_population = generations[-1]
        new_population = []
        for k in range(Npopulation // 2):
            p1 = roulette_wheel(current_population)
            p2 = roulette_wheel(current_population)
            child1, child2 = corssover(p1, p2)
            child1 = mutate(child1, 0.2)
            child2 = mutate(child2, 0.2)
            new_population.append(child1)
            new_population.append(child2)
        generations.append(new_population)

        best = best_solution(current_population)
        best_solution_per_generation.append(best)
    print(f'best solution in iteration {i}: {best}')
    average_cost += best

print('average cost:', average_cost / num_iter)
plt.plot(best_solution_per_generation)
plt.title(f'{cost_function} function over generation')
plt.xlabel('generations')
plt.ylabel('best solution')
plt.show()
