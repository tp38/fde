from abc import ABC, abstractmethod

class DayResultDao(ABC):
    @abstractmethod
    def create_connection(self, url) :
        pass

    @abstractmethod
    def create_data(self, values) :
        pass

    @abstractmethod
    def update_data(self, values) :
        pass

    @abstractmethod
    def read_data(self, day) :
        pass

    @abstractmethod
    def destroy_data(self, day) :
        pass

    @abstractmethod
    def read_all_data(self) :
        pass

    @abstractmethod
    def close(self) :
        pass
