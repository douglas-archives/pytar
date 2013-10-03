====================
(Experimental) Pytar
====================
Cause I'll never remember a valid tar command.

.. image:: https://badge.fury.io/py/pytar.png
    :target: http://badge.fury.io/py/pytar
    
.. image:: https://travis-ci.org/douglasmiranda/pytar.png?branch=master
        :target: https://travis-ci.org/douglasmiranda/pytar

.. image:: https://coveralls.io/repos/douglasmiranda/pytar/badge.png?branch=master
        :target: https://coveralls.io/r/douglasmiranda/pytar?branch=master

.. image:: https://pypip.in/d/pytar/badge.png
        :target: https://crate.io/packages/pytar?version=latest

Boom!

.. image:: http://imgs.xkcd.com/comics/tar.png

I don't know if its a good or bad idea, but I'm doing anyway.

* Free software: BSD license
* Documentation: http://pytar.rtfd.org.

Features
--------

Well, for now:

* Extracting tar files without having to remember those commands.

    .. code-block:: bash

        # pytar $ACTION $TARGET
        $ pytar extract my-tar-file.tar

Install
--------

* Using PIP.

    .. code-block:: bash

        $ pip install pytar --pre

See `--pre flag <http://www.pip-installer.org/en/latest/usage.html#install-pre>`_ on PIP documentation.