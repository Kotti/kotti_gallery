# -*- coding: utf-8 -*-

from kotti import DBSession
from kotti.resources import Image
from kotti.views.edit import ContentSchema
from kotti.views.edit import make_generic_add
from kotti.views.edit import make_generic_edit
from pyramid.view import view_config
from resources import Gallery


class GallerySchema(ContentSchema):
    pass


class GalleryView(object):

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(context=Gallery,
                 name='view',
                 permission='view',
                 renderer='templates/gallery-view.pt')
    def view(self):

        session = DBSession()
        query = session.query(Image)\
                       .filter(Image.parent_id == self.context.id)\
                       .order_by(Image.position)
        images = query.all()

        return {"images": images}


def includeme(config):

    config.scan("kotti_gallery")

    config.add_view(make_generic_edit(GallerySchema()),
                    context=Gallery,
                    name='edit',
                    permission='edit',
                    renderer='kotti:templates/edit/node.pt', )

    config.add_view(make_generic_add(GallerySchema(), Gallery),
                    name=Gallery.type_info.add_view,
                    permission='add',
                    renderer='kotti:templates/edit/node.pt', )
