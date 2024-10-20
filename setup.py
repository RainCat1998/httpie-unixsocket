from setuptools import setup


setup(
    name='httpie-unixsocket',
    description='UNIX socket transport plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.0.1',
    author='RainCat1998',
    author_email='marc@marc-abramowitz.com',
    license='BSD',
    url='https://github.com/RainCat1998/httpie-unixsocket',
    py_modules=['httpie_unixsocket'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.transport.v1': [
            'httpie_unixsocket = httpie_unixsocket:UnixSocketTransportPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0',
        'requests_unixsocket @ git+https://github.com/RainCat1998/requests-unixsocket.git'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Environment :: Plugins',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
