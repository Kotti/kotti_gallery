# -*- coding: utf-8 -*-

"""
Created on 2013-02-18
:author: Andreas Kaiser (disko)
"""

from __future__ import absolute_import

from fanstatic import Library
from fanstatic import Resource
from js.bootstrap_image_gallery import gallery


library = Library(
    'kotti_gallery',
    'static')
kotti_gallery = Resource(
    library,
    'kotti_gallery.css',
    minified='kotti_gallery.min.css',
    depends=[gallery, ]
    )
