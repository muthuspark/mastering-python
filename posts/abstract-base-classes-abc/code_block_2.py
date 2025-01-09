from abc import ABC, abstractmethod, abstractproperty

class DataProcessor(ABC):
    @abstractproperty
    def data(self):
        pass

    @abstractmethod
    def process(self):
        pass

class CSVProcessor(DataProcessor):
    def __init__(self, filename):
        self._data = self._load_csv(filename)

    def _load_csv(self, filename):
      #Simulate loading data from CSV
      return ["data1","data2"]

    @property
    def data(self):
        return self._data

    def process(self):
        # Process the CSV data
        print("Processing CSV data:", self.data)
