# -*- coding: utf-8 -*-

from kotti.resources import Image
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_gallery')


def kotti_configure(settings):

    settings['pyramid.includes'] += ' kotti_gallery.views'
    settings['kotti.available_types'] += ' kotti_gallery.resources.Gallery'
    Image.type_info.addable_to.append('Gallery')
