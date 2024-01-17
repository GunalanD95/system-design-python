from abc import abstractmethod , ABC 


class FeeCalculationStrategy(ABC):
    
    @abstractmethod
    def calculate_fees(self):
        pass 