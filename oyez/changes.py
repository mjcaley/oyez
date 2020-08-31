from pathlib import Path
from typing import Dict, List, Mapping

from .entities import Change


class Changes:
    def __init__(self, category_table: Mapping[str, str]) -> None:
        self.category_table = category_table

    def write(self, changes: Mapping[str, Change]) -> None:
        raise NotImplementedError

    def read(self) -> Mapping[str, List[Change]]:
        raise NotImplementedError


class TownCrierChangesReader(Changes):
    def __init__(self, path: Path, category_table: Mapping[str, str]):
        self._path = path
        super().__init__(category_table=category_table)

    def write(self, changes: Mapping[str, List[Change]]) -> None:
        for category, change in changes.items():
            path = self._path / Path(".".join([change.identifier, category]))
            with open(path, "w") as file:
                file.write(change.description)

    def read(self) -> Dict[str, List[Change]]:
        result: Dict[str, List[Change]] = {}

        for file in self._path.iterdir():
            identifier, _, category = file.name.rpartition(".")
            if category in self.category_table:
                with open(file, "r") as f:
                    content = f.read()
                changes = result.get(category, [])
                changes.append(Change(identifier, content))
                result[category] = changes

        return result
