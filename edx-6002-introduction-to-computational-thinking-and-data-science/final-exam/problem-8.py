import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
numSteps = 200

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP
    global MAXRABBITPOP
    max_rabbit_pop = MAXRABBITPOP
    for rabbit in range(CURRENTRABBITPOP):
        if random.random() >= (CURRENTRABBITPOP/max_rabbit_pop):
            CURRENTRABBITPOP += 1
    
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP
    global MAXRABBITPOP
    max_rabbit_pop = MAXRABBITPOP
    
    for fox in range(CURRENTFOXPOP):
        if random.random() <= (CURRENTRABBITPOP/max_rabbit_pop) and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() <= 1/3:
                CURRENTFOXPOP += 1
        else:
            if random.random() <= 0.1 and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbit_populations = []
    fox_populations = []
    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)
    return (rabbit_populations, fox_populations)

rabbit_vals, fox_vals = runSimulation(numSteps)
x_vals = [i for i in range(numSteps)]
pylab.figure()
pylab.plot(x_vals, rabbit_vals, label='Rabbit Population')
pylab.plot(x_vals, fox_vals, label='Fox Population')
pylab.legend()
pylab.xlabel('Time Steps')
pylab.ylabel('Population')
pylab.title('Rabbit and Fox Population Over Time')
pylab.show()

rabbit_coeff = pylab.polyfit(range(len(rabbit_vals)), rabbit_vals, 2)
fox_coeff = pylab.polyfit(range(len(fox_vals)), fox_vals, 2)

rabbit_pred = pylab.polyval(rabbit_coeff, range(len(rabbit_vals)))
fox_pred = pylab.polyval(fox_coeff, range(len(fox_vals)))

pylab.figure()
pylab.plot(range(len(rabbit_vals)), rabbit_pred, label='Rabbit Population')
pylab.plot(range(len(fox_vals)), fox_pred, label='Fox Population')
pylab.legend()
pylab.xlabel('Time Steps')
pylab.ylabel('Population')
pylab.title('Predicted Rabbit and Fox Population Over Time')
pylab.show()


