import importlib

from .entities import Package


class PackageInformation:
    def package_info(self) -> Package:
        raise NotImplementedError


class PythonPackage(PackageInformation):
    def __init__(self, package_name: str):
        self.package_name = package_name

    def package_info(self) -> Package:
        package = importlib.import_module(self.package_name)

        return Package(self.package_name, package.__version__)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(package_name={repr(self.package_name)})"


class ConfiguredPackage(PackageInformation):
    def __init__(self, package_name: str, package_version: str) -> None:
        self.package_name = package_name
        self.package_version = package_version

    def package_info(self) -> Package:
        return Package(self.package_name, self.package_version)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(package_name={repr(self.package_name)}, "
            f"package_version={repr(self.package_version)})"
        )
