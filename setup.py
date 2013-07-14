"""
Flask-DebuggerLink
-------------

Flask extension that exposes debugger on additional url.
"""
from setuptools import setup


setup(
    name='Flask-DebuggerLink',
    version='0.1',
    url='http://jaworski.me/flask-debuggerlink/',
    license='BSD',
    author='Marcin Jaworski',
    author_email='marcin@jaworski.me',
    description='Exposes debugger on separate url',
    long_description=__doc__,
    py_modules=['flask_debuggerlink'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'blinker',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
