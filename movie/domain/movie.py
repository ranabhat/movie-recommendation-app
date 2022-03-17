import uuid
import dataclasses

@dataclasses.dataclass 
class Movie:
    id: uuid.UUID
    name: str
    genre: list[str]

    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)


