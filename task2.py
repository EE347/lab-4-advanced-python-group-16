import random


class RandomNumberGenerator():
    
    def __init__(self, seed, lower_bound, upper_bound):
        random.seed(seed)
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        
    def random_int(self):
        return random.randint(self.lower_bound, self.upper_bound)
    

    def random_float(self):
        # The lower bound plus a random float from 0 to 1 multiplied by the range from lower to upper
        # if the float is 1 it returns upper bound and if the float is 0 is the lower bound
        return self.lower_bound + random.random()*(self.upper_bound-self.lower_bound)
    
    
if __name__ == '__main__':
    random_number_generator = RandomNumberGenerator(seed=10, lower_bound=0, upper_bound=100)
    print(random_number_generator.random_int())
    print(random_number_generator.random_float())
    