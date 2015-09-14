from plone.app.contenttypes.behaviors.collection import ICollection
from plone.app.layout.viewlets.content import ContentRelatedItems
from plone.app.layout.viewlets import ViewletBase


class RelatedSliderViewlet(ViewletBase):
    """Viewlet for displaying a slider of related items"""
    related_content = []

    def update(self):
        slider_type = self.context.slider_type
        if slider_type == u'criteria':
            self.related_content = ICollection(self.context).results()
        elif slider_type == u'related':
            self.related_content = [o.to_object for o in
                                    self.context.relatedItems
                                    if not o.isBroken()]


class RelatedViewlet(ContentRelatedItems):
    """Override the related viewlet to skip rendering if the related
    slider is enabled"""

    def related_items(self):
        slider_type = self.context.slider_type
        if slider_type == u'related':
            return []
        return super(RelatedViewlet, self).related_items()
