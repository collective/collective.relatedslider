# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.relatedslider.testing import COLLECTIVE_RELATEDSLIDER_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that collective.relatedslider is properly installed."""

    layer = COLLECTIVE_RELATEDSLIDER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.relatedslider is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('collective.relatedslider'))

    def test_browserlayer(self):
        """Test that ICollectiveRelatedsliderLayer is registered."""
        from collective.relatedslider.interfaces import ICollectiveRelatedsliderLayer
        from plone.browserlayer import utils
        self.assertIn(ICollectiveRelatedsliderLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_RELATEDSLIDER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.relatedslider'])

    def test_product_uninstalled(self):
        """Test if collective.relatedslider is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('collective.relatedslider'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveRelatedsliderLayer is removed."""
        from collective.relatedslider.interfaces import ICollectiveRelatedsliderLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveRelatedsliderLayer, utils.registered_layers())
