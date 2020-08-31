from pathlib import Path
from typing import Mapping

import click
from dependency_injector import containers, providers

from .category_table import CategoryTable
from .changes_reader import TownCrierChangesReader
from .entities import Category


class ApplicationContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    reader = providers.Factory(
        TownCrierChangesReader, config.path.as_(Path), category_table=config.categories
    )
    # writer
    # processor


builtin_config = {
    "categories": {
        "feature": "Features",
        "bugfix": "Bug Fixes",
        "doc": "Documentation Improvements",
        "removal": "Deprecations and Removals",
        "misc": "Miscellaneous",
    }
}


def cli_config(package, version, name) -> Mapping[str, str]:
    return {
        "package": package,
        "version": version,
        "name": name,
    }


@click.command()
@click.option("--package", required=False, help="Python package to reference.")
@click.option("--version", help="Manually specify version.")
@click.option("--name", help="Override the name of the package.")
@click.option("--path", help="Path to look for change files.")
def run(package, version, name, path):
    container = ApplicationContainer()

    # Load configuration
    container.config.from_dict(builtin_config)
    # container.config.from_dict(toml_config)
    # container.config.from_dict(cli_config)

    container.config.from_dict({"path": "./test_data/"})

    cats = container.reader().read()
    print(cats)
