from abc import ABC, abstractmethod

class MonthResultDao(ABC):
    @abstractmethod
    def create_connection(self, url) :
        pass

    @abstractmethod
    def get_days(self, year, month) :
        pass

    @abstractmethod
    def get_ca(self, year, month) :
        pass

    @abstractmethod
    def get_hours(self, year, month) :
        pass

    @abstractmethod
    def get_hsup(self, year, month) :
        pass

    @abstractmethod
    def get_prime(self, year, month, seuil) :
        pass
