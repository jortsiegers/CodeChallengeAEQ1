
class ChallengeOne:
    data: list

    def __init__(self):
        self.read_input()

        self.data = self.fold_x(self.data)
        self.data = self.fold_y(self.data)
        self.data = self.fold_x(self.data)
        self.data = self.fold_y(self.data)
        self.data = self.fold_x(self.data)
        self.data = self.fold_y(self.data)
        self.data = self.fold_x(self.data)
        self.data = self.fold_y(self.data)
        self.output_data(self.data)

    def read_input(self, fn: str = 'input.txt'):
        with open(fn, 'r') as f:
            data = [list(line.replace('\n', '')) for line in f]            
        self.data = data
    
    def output_data(self, data: list, fn: str = 'output.txt'):
        with open(fn, 'w') as f:
            for row in data:
                f.write("".join(row) + '\n')
    
    ############################## YOUR CODE ##################################


    
    def fold_x(self, data: list):
        """
        Implement here your implementation of the fold x function
        """
        return nfold_x(data)

    def fold_y(self, data: list):
        """
        Implement here your implementation of the fold y function
        """
        return nfold_y(data)

        

    ###########################################################################

    
ChallengeOne()