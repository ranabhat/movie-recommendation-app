from movie.repository.abstractrepo import MovieRecommendationRepo
from movie.domain.movie import Movie

class MemRepo(MovieRecommendationRepo):
    def __init__(self, data, genre=None):
        self.data = data
        self.genre = genre

    def list(self):
        return [Movie.from_dict(i) for i in self.data]

    def recommended_list(self):
        return [Movie.from_dict(i) for i in self.data if self.genre in i["genre"]]