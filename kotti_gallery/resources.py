# -*- coding: utf-8 -*-

from kotti.resources import Content
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from kotti_gallery import _


class Gallery(Content):

    id = Column(Integer, ForeignKey('contents.id'), primary_key=True)

    type_info = Content.type_info.copy(
        name=u'Gallery',
        title=_(u'Gallery'),
        add_view=u'add_gallery',
        addable_to=[u'Document'],
        selectable_default_views=[
            ("span12", _("1 Column")),
            ("span6", _("2 Columns")),
            ("span4", _("3 Columns")),
            ("span3", _("4 Columns")),
            ("span2", _("6 Columns")),
            ("span1", _("12 Columns")),
        ]
    )
