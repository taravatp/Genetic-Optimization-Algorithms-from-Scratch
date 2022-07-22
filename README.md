# Genetic-Optimization-Algorithms-from-Scratch

In this project, I exprimented with the functionality of genetic algorithm and particle swarm optimization algorithm on the following functions: Sphere, Bent Cigar, Rastrigins and Ackley. All the algorithms are implemented from scratch with python.

# Designing a Basic Genetic Algorithm:
1. Each chromosome consists of 30 genes.
2. Each gene is a real valued number in a specified boundary.
3. Calculated the fitness of each chromose based on the value of our target function (Sphere, Bent Cigar, Rastrigins or Ackley).
4. Chose parents based on the Roulette-wheel method.
5. Applyed one point crossover.
6. Applyed mutation by changing the value of a gene to a valid number by a specified probabilty.

# Results of the Basic Genetic Algorithm:
**According to the following results, it is ovbvious that the genetic algorithm does not converge on multi-modal functions (Rastrigins and Ackley). The reason is that it gets stuck in local optimas of the multi-modal functions.**

<p float="left">
  <img src="https://github.com/taravatp/Genetic-Optimization-Algorithms-from-Scratch/blob/main/Results/sphere_basic_genetic.png" width="48%%" />
  <img src="https://github.com/taravatp/Genetic-Optimization-Algorithms-from-Scratch/blob/main/Results/bentcigar_basic_genetic.png" width="48%%" /> 
</p>
<p float="left">
  <img src="https://github.com/taravatp/Genetic-Optimization-Algorithms-from-Scratch/blob/main/Results/rastrigins_basic_genetic.png" width="48%%" />
  <img src="https://github.com/taravatp/Genetic-Optimization-Algorithms-from-Scratch/blob/main/Results/ackley_basic_genetic.png" width="48%%" /> 
</p>

# Results of the Particle Swarm Optimization Algorithm:
**In order to solve the aformentioned problem of the genetic algorithm, I implemented the particle swarm optimization algorithm. The following results demonstrate that PSO works well on both unimodal and multi-modal functions.**

<p float="left">
  <img src="https://github.com/taravatp/Genetic-Optimization-Algorithms-from-Scratch/blob/main/Results/sphere_PSO.png" width="48%" />
  <img src="https://github.com/taravatp/Genetic-Optimization-Algorithms-from-Scratch/blob/main/Results/bentcigar_PSO.png" width="48%" /> 
</p>
<p float="left">
  <img src="https://github.com/taravatp/Genetic-Optimization-Algorithms-from-Scratch/blob/main/Results/rastrigins_PSO.png" width="48%" />
  <img src="https://github.com/taravatp/Genetic-Optimization-Algorithms-from-Scratch/blob/main/Results/ackley_PSO.png" width="48%" /> 
</p>
