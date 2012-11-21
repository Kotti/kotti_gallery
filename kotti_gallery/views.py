# -*- coding: utf-8 -*-

from js.bootstrap_image_gallery import gallery
from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config

from kotti_gallery import _
from kotti_gallery.resources import Gallery


class GalleryEditForm(EditFormView):
    schema_factory = ContentSchema


class GalleryAddForm(AddFormView):

    schema_factory = ContentSchema
    add = Gallery
    item_type = _(u"Gallery")


class GalleryView(object):

    def __init__(self, context, request):

        self.context = context
        self.request = request

    @view_config(context=Gallery,
                 name='view',
                 permission='view',
                 renderer='templates/gallery-view.pt')
    def view(self):

        gallery.need()

        images = self.context.children_with_permission(self.request)

        return {"images": images}


def includeme(config):

    config.scan(__name__)

    config.add_view(
        GalleryEditForm,
        context=Gallery,
        name='edit',
        permission='edit',
        renderer='kotti:templates/edit/node.pt',
        )

    config.add_view(
        GalleryAddForm,
        name=Gallery.type_info.add_view,
        permission='add',
        renderer='kotti:templates/edit/node.pt',
        )
