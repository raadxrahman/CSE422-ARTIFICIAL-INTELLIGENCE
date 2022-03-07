import numpy as np

def fitness(population, n):
    n= []

    for i in population:
        cumulative = 0

        for j in range(len(i)):

            if i[j] == 1:
                amount = int(data[j].split()[1])
                category = data[j].split()[0]

                if category == "l":
                    cumulative -= amount
                
                elif category == "d":
                    cumulative += amount
        n.append((cumulative))
    
    return n


def select(population, fit):

    # a = [0,1,2,3,4]
    #   size = 1
    #   p = [.31, .29, 0.26, 0.14]
    
    pp = [k/np.sum(fit) for k in fit]
    a, b = np.random.choice(len(population), 2, pp)
    return population[a], population[b]


def crossover(x, y):
    idx = np.random.randint(0, len(x))
    child_chromosome = np.concatenate((x[:idx],y[idx:]))
    return child_chromosome


def mutate(child):
    mutate_idx = np.random.randint(0,len(child))
    
    # if str_list[index] == '1':
    #         str_list[index] = '0'

    if child[mutate_idx] == 1:
        child[mutate_idx] = 0

    else:
        child[mutate_idx] = 1
    
    return child


def GA(population, n, mutation_threshold = 0.3):
    iter = 2000

    for i in range(iter):
         n = fitness(population, n)
         list = []

        #  while iter < 1000:
        # fit = fitness(population,data)
        # if fit.count(0) != 0:

         for j in range(len(population)):
             x, y = select(population, n)
             child = crossover(x,y)
             random = np.random.random()

             if random < mutation_threshold:
                 child = mutate(child)
             
             if all (k == 0 for k in child):
                 list.append(child)
                 continue
             
             if fitness([child], n)[0] == 0:
                 output=""
             
                 for i in child:
                     output += str(i)
             
                 return output
             
             list.append(child)
         
         population = list
    return -1


def genetic_algorithm(filename):

    file=open(filename, "r")
    n = int(file.read(2))
    global data
    data = []
    data.append(file.readline(n))

    for x in range(1, n):
        lines = file.readline()[:-1]
        data.append(lines)

    start_population = 10 
    mutation_threshold = 0.3
    population = np.random.randint(0, 2, (start_population, n))
    print(GA(population, n, mutation_threshold))

genetic_algorithm("input1.txt")
# genetic_algorithm("input2.txt")