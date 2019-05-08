# -*- coding: utf-8 -*-

from plone.app.contenttypes.behaviors.collection import ICollection
from plone.app.layout.viewlets.content import ContentRelatedItems
from plone.app.layout.viewlets import ViewletBase


class RelatedSliderViewlet(ViewletBase):
    """Viewlet for displaying a slider of related items"""
    related_content = []
    slider_title = None

    def update(self):
        slider_type = self.context.slider_type
        self.slider_title = self.context.slider_title
        related = []
        if slider_type == u'criteria':
            related = ICollection(self.context).results()
        elif slider_type == u'related':
            related = [o.to_object for o in self.context.relatedItems
                       if not o.isBroken()]

        def getUid(obj):
            uid = getattr(obj, 'UID', None)
            if callable(uid):
                uid = uid()
            return uid

        this_uid = self.context.UID()
        self.related_content = [r for r in related if getUid(r) != this_uid]


class RelatedViewlet(ContentRelatedItems):
    """Override the related viewlet to skip rendering if the related
    slider is enabled"""

    def related_items(self):
        slider_type = self.context.slider_type
        if slider_type == u'related':
            return []
        return super(RelatedViewlet, self).related_items()
