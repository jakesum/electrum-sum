Electrum-SUM - Lightweight Sumcoin client
=========================================

Electrum-SUM is a port of Electrum, the Bitcoin wallet, to Sumcoin.

::

  Licence: MIT Licence
  Original Author: Thomas Voegtlin
  Port Maintainer: Tech1k
  Language: Python (>= 3.6)
  Homepage: https://electrum-sum.org/






Getting started
===============

Electrum-SUM is a pure python application. If you want to use the
Qt interface, install the Qt dependencies::

    sudo apt-get install python3-pyqt5

If you downloaded the official package (tar.gz), you can run
Electrum-SUM from its root directory without installing it on your
system; all the python dependencies are included in the 'packages'
directory. To run Electrum-SUM from its root directory, just do::

    ./run_electrum

You can also install Electrum-SUM on your system, by running this command::

    sudo apt-get install python3-setuptools
    python3 -m pip install .[fast]

This will download and install the Python dependencies used by
Electrum-SUM instead of using the 'packages' directory.
The 'fast' extra contains some optional dependencies that we think
are often useful but they are not strictly needed.

If you cloned the git repository, you need to compile extra files
before you can run Electrum-SUM. Read the next section, "Development
Version".



Development version
===================

Check out the code from GitHub::

    git clone git://github.com/Tech1k/electrum-sum.git
    cd electrum-sum

Run install (this should install dependencies)::

    python3 -m pip install .[fast]


Compile the protobuf description file::

    sudo apt-get install protobuf-compiler
    protoc --proto_path=electrum_sum --python_out=electrum_sum electrum_sum/paymentrequest.proto

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

See :code:`electrum_sum/gui/kivy/Readme.md`.
