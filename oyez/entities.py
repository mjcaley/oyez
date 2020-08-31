from datetime import date
from typing import List, Mapping, Optional


class Change:
    def __init__(
        self,
        identifier: str,
        description: str,
        hyperlink: Optional[str] = None,
    ):
        self._identifier = identifier
        self._description = description
        self._hyperlink = hyperlink

    @property
    def identifier(self):
        return self._identifier

    @property
    def description(self):
        return self._description

    @property
    def hyperlink(self):
        return self._hyperlink

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"identifier={repr(self.identifier)}, "
            f"description={repr(self.description)}, "
            f"hyperlink={repr(self.hyperlink)})"
        )


class Category:
    def __init__(self, name: str, display_name: str):
        self._name = name
        self._display_name = display_name

    @property
    def name(self) -> str:
        return self._name

    @property
    def display_name(self) -> str:
        return self._display_name

    def __hash__(self):
        return hash(self.name)


class Package:
    def __init__(self, name: str, version: str) -> None:
        self._name = name
        self._version = version

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version


class ReleaseLog:
    def __init__(
        self,
        package: Package,
        changes: Mapping[Category, List[Change]],
        log_date: date = date.today(),
    ) -> None:
        self._package = package
        self._changes = changes
        self._log_date = log_date

    @property
    def package(self) -> Package:
        return self._package

    @property
    def changes(self) -> Mapping[Category, List[Change]]:
        return self._changes

    @property
    def log_date(self) -> date:
        return self._log_date
