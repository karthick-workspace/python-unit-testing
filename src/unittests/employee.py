from dataclasses import dataclass, asdict


@dataclass
class Employee:
    name: str = None
    id: int = None
    dept: str = None
    status: str = "Active"

    @classmethod
    def from_dict(cls, dict_input):
        return Employee(**dict_input)

    def to_dict(self):
        return asdict(self)
