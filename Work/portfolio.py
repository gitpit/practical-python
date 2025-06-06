# #

class Portfolio:
    def __init__(self,holdings) -> None:
        self.holdings = holdings
    
    def __iter__(self):
        return self.holdings.__iter__()
    def __len__(self):
        return len(self.holdings)
    def __contains__(self,name):
        return any([s.name==name for s in self.holdings])
    @property
    def total_cost(self):
        return sum([s.cost for s in self.holdings])
