import os

from setuptools import find_packages
from setuptools import setup

version = '0.2.2'

here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    TODO = open(os.path.join(here, 'TODO.rst')).read()
except IOError:
    TODO = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''

install_requires = [
    'Babel',
    'Kotti>=0.8dev',
    'js.bootstrap_image_gallery',
    'lingua>=1.3',

]
tests_require = [
    'pytest',
    'WebTest',
    'wsgi_intercept',
    'zope.testbrowser',
]

setup(
    name='kotti_gallery',
    version=version,
    description='Add an image gallery to your Kotti site',
    long_description=README + '\n\n' + TODO + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pylons',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'License :: Repoze Public License',
    ],
    keywords='image gallery bootstrap kotti cms pylons pyramid',
    author='Andreas Kaiser',
    author_email='disko@binary-punks.com',
    url='https://github.com/disko/kotti_gallery',
    license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'testing': tests_require,
    },
    message_extractors={
        'kotti_gallery': [
            ('**.py', 'lingua_python', None),
            ('**.zcml', 'lingua_xml', None),
            ('**.pt', 'lingua_xml', None),
        ],
    },
    entry_points={
        'fanstatic.libraries': [
            'kotti_gallery = kotti_gallery.fanstatic:library',
        ],
    },
)
