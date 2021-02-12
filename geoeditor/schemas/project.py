from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class Project:
    id: int
    name: Optional[str]
