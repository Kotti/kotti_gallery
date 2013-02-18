kotti_gallery
=============

|build status production|

This is an extension to the Kotti CMS that allows you to add image galleries to
your Kotti site.

It uses `Bootstrap Image Gallery`_ for the gallery view.

`Find out more about Kotti`_


Setup
-----

To activate the ``kotti_gallery`` add-on in your Kotti site, you need to add an
entry to the ``kotti.configurators`` setting in your Paste Deploy config.  If
you don't have a ``kotti.configurators`` option, add one.  The line in your
``[app:main]`` section could then look like this::

    kotti.configurators = kotti_gallery.kotti_configure

With this, you'll be able to add galleries in your site.


Development
-----------

|build status master|

Contributions to ``kotti_gallery`` are highly welcome.  Just clone its
`Github repository`_ and submit your contributions as pull requests.


Testing
-------

``kotti_gallery`` has 100% test coverage.  Please make sure that you add tests
for new features and that all tests pass before submitting pull requests.
Running the test suite is as easy as running ``py.test`` from the source directory.


.. |build status production| image:: https://travis-ci.org/Kotti/kotti_gallery.png?branch=production
.. |build status master| image:: https://travis-ci.org/Kotti/kotti_gallery.png?branch=master
.. _Bootstrap Image Gallery: http://blueimp.github.com/Bootstrap-Image-Gallery/
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _Github repository: https://github.com/disko/kotti_gallery
