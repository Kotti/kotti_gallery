# -*- coding: utf-8 -*-

from kotti.resources import Content
from kotti.util import _
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer


class Gallery(Content):

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(name=u'Gallery',
                                       title=_(u'Gallery'),
                                       add_view=u'add_gallery',
                                       addable_to=[u'Document'], )
