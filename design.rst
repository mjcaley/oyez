Components
==========

Change
------

Represents a single change.  Has an identifier, a description, and an optional hyperlink.

Change
    __init__(identifier, description, hyperlink=None)

    @property identifier -> string?

    @property description -> string

    @property hyperlink -> Optional[string]

Reader
------

Reads from a source.  Produces a collection of Change instances representing the changes contained in the source.

Reader
    read() -> Collection[Change]


Implementation of Reader that reads a directory for files of changes (mimicing towncrier).

DirectoryReader(Reader)
    __init__(path)


Implementation of Reader that reads from a local git repository.

GitReader(Reader)


Implementation of Reader that reads from a GitHub repository.  Can interpret pull requests, releases, and issues.

GitHubReader(Reader)
    __init__(url)


Writer
------

Writes to a change log in a particular format.

Writer
    write(Collection[Change])


PackageInfo
-----------

Determines package name, version, and date.

PackageInfo
    @property name

    @property version

    @property date


Implements information defined in the configuration file.

ConfigPackageInfo(PackageInfo)


Implements information pulled from the PythonPackage.  Imports and gets __version__.

PythonPackageInfo(PackageInfo)
    __init__(package_name)


Composer
--------

Collects package information (including name, version, and date), and Collection[Change].

Composer
    __init__(Reader, Writer, PackageInfo)

    read()

    write()

    @property version

    @property name

    @property date
