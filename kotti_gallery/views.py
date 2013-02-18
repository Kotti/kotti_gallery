# -*- coding: utf-8 -*-

from kotti.views.edit import ContentSchema
from kotti.views.form import AddFormView
from kotti.views.form import EditFormView
from pyramid.view import view_config

from kotti_gallery import _
from kotti_gallery.fanstatic import kotti_gallery
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
        self.span = 4

    @view_config(context=Gallery, name='span1', permission='view',
                 renderer='templates/gallery-view.pt')
    def span1(self):
        self.span = 1
        return self.view()

    @view_config(context=Gallery, name='span2', permission='view',
                 renderer='templates/gallery-view.pt')
    def span2(self):
        self.span = 2
        return self.view()

    @view_config(context=Gallery, name='span3', permission='view',
                 renderer='templates/gallery-view.pt')
    def span3(self):
        self.span = 3
        return self.view()

    @view_config(context=Gallery, name='span4', permission='view',
                 renderer='templates/gallery-view.pt')
    def span4(self):
        self.span = 4
        return self.view()

    @view_config(context=Gallery, name='span6', permission='view',
                 renderer='templates/gallery-view.pt')
    def span6(self):
        self.span = 6
        return self.view()

    @view_config(context=Gallery, name='span12', permission='view',
                 renderer='templates/gallery-view.pt')
    def span12(self):
        self.span = 12
        return self.view()

    @view_config(context=Gallery,
                 name='view',
                 permission='view',
                 renderer='templates/gallery-view.pt')
    def view(self):

        kotti_gallery.need()

        images = self.context.children_with_permission(self.request)

        return {"images": images, "img_span": self.span}


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
