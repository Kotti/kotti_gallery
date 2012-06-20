=============
kotti_gallery
=============

This is an extension to the Kotti CMS that allows you to add image galleries to your Kotti site.

It uses `Bootstrap Carousel`_ for the gallery view.

`Find out more about Kotti`_


Setup
=====

To activate the ``kotti_gallery`` add-on in your Kotti site, you need to add an entry to the ``kotti.configurators`` setting in your Paste Deploy config.
If you don't have a ``kotti.configurators`` option, add one.
The line in your ``[app:main]`` section could then look like this::

  kotti.configurators = kotti_gallery.kotti_configure

With this, you'll be able to add galleries in your site.


Development
===========

Contributions to ``kotti_gallery`` are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

Note that all development is done on the ``develop`` branch and ``master`` is reserved for "production-ready state".
Therefore make sure to always base your work on the current state of the ``develop`` branch.

This follows the highly recommended `A successful Git branching model`_ pattern, which is implemented by the excellent `gitflow`_ git extension.

Testing
-------

``kotti_gallery`` has 100% test coverage.
Please make sure that you add tests for new features and that all tests pass before submitting pull requests.
Running the test suite is as easy as running ``py.test`` from the source directory.


.. _Bootstrap Carousel: http://twitter.github.com/bootstrap/javascript.html#carousel
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti
.. _`plone.scale`: http://pypi.python.org/pypi/plone.scale/1.2.2
.. _Github repository: https://github.com/disko/kotti_image_gallery
.. _gitflow: https://github.com/nvie/gitflow
.. _A successful Git branching model: http://nvie.com/posts/a-successful-git-branching-model/
