#!/usr/bin/env python
from distutils.core import setup, Extension

ds1302 = Extension('ds1302',
				   sources = ['python.c'],
				   libraries = ['python3.9', 'wiringPi', 'm', 'crypt', 'rt'],
				   extra_compile_args = ['-std=c99'],
			   )

setup(name='rpi_rtc',
	  version="0.1",
	  description='Python library for handling DS1302 RTC with Raspberry Pi',
	  ext_modules=[ds1302],
	  py_modules=['rpi_time', 'hwclock'],
)
