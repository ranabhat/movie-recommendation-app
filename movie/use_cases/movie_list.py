from movie.repository.abstractrepo import MovieRecommendationRepo

class MovieRecommendationUsecase:
    def __init__(self, repo_object:MovieRecommendationRepo):
        self.repo_object = repo_object
    
    def movie_list_use_case(self):
        return self.repo_object.list()

    def movie_recommended_use_case(self):
        return self.repo_object.recommended_list()

# def movie_list_use_case(repo): 
#     return repo.list()

