from datetime import date
from typing import List, Mapping

from .entities import Category, Change, ReleaseLog


class ChangesReader:
    def read(self) -> Mapping[Category, List[Change]]:
        raise NotImplementedError


class LogEntryWriter:
    def write(self, entry: ReleaseLog) -> None:
        raise NotImplementedError
