Electrum-BYND - Lightweight Beyondcoin client
=============================================

Electrum-BYND is a port of Electrum, the Bitcoin wallet, to Beyondcoin.

::

  Licence: MIT Licence
  Original Author: Thomas Voegtlin
  Port Maintainer: Tech1k
  Language: Python (>= 3.6)
  Homepage: https://electrum-bynd.com/






Getting started
===============

Electrum-BYND is a pure python application. If you want to use the
Qt interface, install the Qt dependencies::

    sudo apt-get install python3-pyqt5

If you downloaded the official package (tar.gz), you can run
Electrum-BYND from its root directory without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum-BYND from its root directory, just do::

    ./run_electrum

You can also install Electrum-BYND on your system, by running this command::

    sudo apt-get install python3-setuptools
    python3 -m pip install .[fast]

This will download and install the Python dependencies used by
Electrum-BYND instead of using the 'packages' directory.
The 'fast' extra contains some optional dependencies that we think
are often useful but they are not strictly needed.

If you cloned the git repository, you need to compile extra files
before you can run Electrum-BYND. Read the next section, "Development
Version".



Development version
===================

Check out the code from GitHub::

    git clone git://github.com/beyondcoin-project/electrum-bynd.git
    cd electrum-bynd

Run install (this should install dependencies)::

    python3 -m pip install .[fast]


Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    protoc --proto_path=electrum_bynd --python_out=electrum_bynd electrum_bynd/paymentrequest.proto

Create translations (optional)::

    sudo apt-get install python-requests gettext
    ./contrib/pull_locale




Creating Binaries
=================

Linux (tarball)
---------------

See :code:`contrib/build-linux/README.md`.


Linux (AppImage)
----------------

See :code:`contrib/build-linux/appimage/README.md`.


Mac OS X / macOS
----------------

See :code:`contrib/osx/README.md`.


Windows
-------

See :code:`contrib/build-wine/README.md`.


Android
-------

See :code:`electrum_bynd/gui/kivy/Readme.md`.
