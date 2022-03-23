from abc import ABCMeta, abstractmethod

class MovieRecommendationRepo(metaclass=ABCMeta):

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def recommended_list(self):
        pass
