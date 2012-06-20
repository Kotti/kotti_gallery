# -*- coding: utf-8 -*-

from kotti.resources import Image


def kotti_configure(settings):

    settings['kotti.includes'] += ' kotti_gallery.views'
    settings['kotti.available_types'] += ' kotti_gallery.resources.Gallery'
    Image.type_info.addable_to.append('Gallery')
