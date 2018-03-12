#!/usr/bin/env python

from distutils.core import setup

setup(name="lsprofcalltree",
      version="0.0.6",
      description="lsprof output which is readable by kcachegrind",
      author="David Allouche, Jp Calderone, Itamar Shtull-Trauring and Johan Dahlin",
      url="http://people.gnome.org/~johan/lsprofcalltree.py",
      py_modules=["lsprofcalltree"],
     )
