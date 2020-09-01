from pathlib import Path

from jinja2 import Template

from .entities import ReleaseLog


class Writer:
    def write(self, release: ReleaseLog) -> None:
        raise NotImplementedError


class TemplateWriter(Writer):
    def __init__(self, path: Path, template: str) -> None:
        self._path = path
        with open(template, "r") as f:
            self._template = Template(f.read(), trim_blocks=True)

    def write(self, release: ReleaseLog) -> None:
        rendered_template = self._template.render(
            package = release.package,
            log_date = release.log_date,
            changes = release.changes
        )
        self.prepend(rendered_template)

    def prepend(self, content: str) -> None:
        try:
            with open(self._path, "r") as f:
                existing_content = f.read()
        except FileNotFoundError:
            existing_content = ""
        with open(self._path, "w") as f:
            f.write(content)
            f.write(existing_content)

    def append(self, content: str) -> None:
        with open(self._path, "w+") as f:
            f.write(content)
