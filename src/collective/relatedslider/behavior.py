# -*- coding: utf-8 -*-

from plone.autoform.interfaces import IFormFieldProvider
from plone.app.contenttypes.behaviors.collection import ISyndicatableCollection
from plone.app.relationfield.behavior import IRelatedItems
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
from . import _


@implementer(IVocabularyFactory)
class SliderOptionsVocabulary(object):

    def __call__(self, context):
        terms = [SimpleTerm(title=u'Disabled', value=u'disabled',
                            token='disabled')]
        if ISyndicatableCollection.providedBy(context):
            terms.append(SimpleTerm(title=u'From Criteria', value=u'criteria',
                                    token='criteria'))
        if IRelatedItems.providedBy(context):
            terms.append(SimpleTerm(title=u'From Related Items',
                                    value=u'related',
                                    token='related'))
        return SimpleVocabulary(terms)


SliderOptionsVocabularyFactory = SliderOptionsVocabulary()


@provider(IFormFieldProvider)
class IRelatedSlider(model.Schema):
    """Behavior that allows content to display related items in
    a slider"""

    slider_title = schema.TextLine(
        title=_(u'Related Slider Title'),
        description=_(u'Enter an optional title for the slider viewlet.'),
        required=False
    )

    slider_type = schema.Choice(
        title=_(u'Related Slider Type'),
        description=_(u'Select an option for what content to render in the '
                      u'slider.'),
        vocabulary='collective.relatedslider.options'
    )
