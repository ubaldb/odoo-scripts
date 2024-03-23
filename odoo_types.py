from __future__ import annotations

import msgspec

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List


class Field(msgspec.Struct):
    name: str
    desc: str


class Model(msgspec.Struct):
    name: str
    model: str
    fields: List[Field] = list()
