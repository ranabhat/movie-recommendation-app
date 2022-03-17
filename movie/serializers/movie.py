import json

class MovieJsonEncoder(json.JSONEncoder):
    def default(self, o):
        try:
            to_serialize = {
                "id": str(o.id),
                "name": o.name,
                "genre": o.genre
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
