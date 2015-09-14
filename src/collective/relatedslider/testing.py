# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.relatedslider


class CollectiveRelatedsliderLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.relatedslider)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.relatedslider:default')


COLLECTIVE_RELATEDSLIDER_FIXTURE = CollectiveRelatedsliderLayer()


COLLECTIVE_RELATEDSLIDER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_RELATEDSLIDER_FIXTURE,),
    name='CollectiveRelatedsliderLayer:IntegrationTesting'
)


COLLECTIVE_RELATEDSLIDER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_RELATEDSLIDER_FIXTURE,),
    name='CollectiveRelatedsliderLayer:FunctionalTesting'
)


COLLECTIVE_RELATEDSLIDER_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_RELATEDSLIDER_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveRelatedsliderLayer:AcceptanceTesting'
)
