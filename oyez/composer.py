from pathlib import Path

import jinja2

from .entities import ReleaseLog


class Composer:
    def compose(self, release: ReleaseLog) -> str:
        raise NotImplementedError


class RestructureTextWriter(Composer):
    def __init__(self, path: Path) -> None:
        self._path = path

    def compose(self, release: ReleaseLog) -> str:
        pass
