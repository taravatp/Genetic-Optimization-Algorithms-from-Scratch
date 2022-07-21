import copy
import math
import numpy as np
import matplotlib.pyplot as plt


class Particle:
    def __init__(self, cost_func, dims=30):

        self.cost_func = cost_func
        self.lower_bound = self.get_bounds()[0]
        self.upper_bound = self.get_bounds()[1]

        self.dims = dims
        self.current_position = np.random.uniform(self.lower_bound, self.upper_bound, self.dims)
        self.current_velocity = np.random.uniform(0, 1, self.dims)
        self.current_error = math.inf  # it is an initial value

        self.best_error = math.inf  # it is an initial value
        self.best_position = self.current_position  # it is an initial value

    def update_errors(self):
        if self.current_error < self.best_error:
            self.best_error = self.current_error
            self.best_position = self.current_position

    def update_velocity(self, best_global_position):
        w = 0.5  # constant intertia weight
        c1 = 2  # cognetive constant
        c2 = 2  # social constant

        r1 = np.random.uniform(0, 1, self.dims)
        r2 = np.random.uniform(0, 1, self.dims)
        cognitive_velocity = c1 * r1 * (self.best_position - self.current_position)
        social_velocity = c2 * r2 * (best_global_position - self.current_position)
        self.current_velocity = (w * self.current_velocity) + cognitive_velocity + social_velocity

    def update_position(self):
        self.current_position = self.current_position + self.current_velocity
        self.current_position = np.maximum(self.current_position, self.lower_bound)
        self.current_position = np.minimum(self.current_position, self.upper_bound)

    def get_cost_value(self):
        if self.cost_func == 'sphere':
            self.current_error = self.sphere()
        elif self.cost_func == 'bentcigar':
            self.current_error = self.bentcigar()
        elif self.cost_func == 'rastrigins':
            self.current_error = self.rastrigins()
        elif self.cost_func == 'ackley':
            self.current_error = self.ackley()
        else:
            print('you have entered an invalid cost function')
            breakpoint()

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

    def sphere(self):
        cost = sum(self.current_position ** 2)
        return abs(cost)

    def bentcigar(self):
        cost = (self.current_position[0] ** 2) + (10 ** 6) * np.sum(self.current_position[1:] ** 2)
        return abs(cost)

    def rastrigins(self):
        cost = np.sum(self.current_position ** 2 + 10 * np.cos(2 * math.pi * self.current_position) + 10)
        return abs(cost)

    def ackley(self):
        n = self.current_position.shape[0]
        cost = -20 * np.exp(-.2 * np.sqrt(np.sum(self.current_position ** 2) / n)) - np.exp(
            np.sum(np.cos(2 * math.pi * self.current_position)) / n) + 20 + np.exp(1)
        return abs(cost)


def initialization():
    solutions = []
    for n in range(Npopulation):
        solutions.append(Particle(cost_function))
    return solutions


# some parameters
num_iter = 30  # number of times that we are going to run the algorithm
num_steps = 300
Npopulation = 50  # Number of population
cost_function = input('enter one of the following cost functions:\n1-sphere\n2-bentcigar\n3-rastrigins\n4-ackley\n')

average_cost = 0
for i in range(num_iter):

    solutions = initialization()
    Errors_over_iterations = []

    best_global_error = math.inf
    best_global_position = None

    for j in range(num_steps):
        for sol in solutions:
            sol.get_cost_value()  # sets the cost
            sol.update_errors()
            if sol.current_error < best_global_error:
                best_global_error = sol.current_error
                best_global_position = sol.current_position
                Errors_over_iterations.append(best_global_error)

            sol.update_velocity(best_global_position)
            sol.update_position()
    average_cost += best_global_error

print('average cost:', average_cost / num_iter)
plt.plot(Errors_over_iterations)
plt.title(f'{cost_function} function over increasing steps')
plt.ylabel('error')
plt.xlabel('steps')
plt.show()
