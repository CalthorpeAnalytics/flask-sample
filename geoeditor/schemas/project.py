from typing import Optional, ClassVar, Type
from dataclasses import field

import marshmallow

from geoeditor.extensions import dataclass


@dataclass
class Project:
    id: int = field(metadata={"metadata": {"dump_only": True}})
    name: Optional[str]

    Schema: ClassVar[Type[marshmallow.Schema]]
