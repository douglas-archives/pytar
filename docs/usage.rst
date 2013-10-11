========
Usage
========

To use Pytar in a project::

    from pytar.pytar import pytar_extract
    pytar_extract('my-tar-file.tar')

To use as a console app::

    # pytar $ACTION $TARGET
    $ pytar extract my-tar-file.tar

Another examples
----------------

Extracting to a different directory::

    # pytar $ACTION $TARGET $EXTRACT_PATH
    $ pytar extract my-tar-file.tar ../extract/path/

(The contents from `my-tar-file.tar` will be extracted to `../extract/path/` directory.)