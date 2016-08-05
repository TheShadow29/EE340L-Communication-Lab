#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/arktheshadow/ARK-Linux/Programming/CommunicationLab/lab2/gr-fullfft/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/arktheshadow/ARK-Linux/Programming/CommunicationLab/lab2/gr-fullfft/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/arktheshadow/ARK-Linux/Programming/CommunicationLab/lab2/gr-fullfft/build/swig:$PYTHONPATH
/usr/bin/python2 /home/arktheshadow/ARK-Linux/Programming/CommunicationLab/lab2/gr-fullfft/python/qa_dft_py_fc.py 
