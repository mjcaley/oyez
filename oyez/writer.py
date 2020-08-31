from pathlib import Path

from .entities import ReleaseLog


class Writer:
    def write(self, release: ReleaseLog) -> None:
        raise NotImplementedError


class RestructureTextWriter(Writer):
    def __init__(self, path: Path) -> None:
        self._path = path

    def write(self, release: ReleaseLog) -> None:
        pass
