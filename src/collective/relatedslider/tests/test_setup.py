# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.relatedslider.testing import COLLECTIVE_RELATEDSLIDER_INTEGRATION_TESTING  # noqa
from collective.relatedslider.interfaces import ICollectiveRelatedSliderLayer
from Products.CMFPlone.utils import get_installer
try:
    import unittest2 as unittest
except ImportError:
    import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.relatedslider is properly installed."""

    layer = COLLECTIVE_RELATEDSLIDER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal)

    def test_product_installed(self):
        """Test if collective.relatedslider is installed with
        portal_quickinstaller."""
        self.assertTrue(self.installer.is_product_installed(
            'collective.relatedslider'
        ))

    def test_browserlayer(self):
        """Test that ICollectiveRelatedSliderLayer is registered."""
        from plone.browserlayer import utils
        self.assertIn(ICollectiveRelatedSliderLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_RELATEDSLIDER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = get_installer(self.portal)
        self.installer.uninstall_product('collective.relatedslider')

    def test_product_uninstalled(self):
        """Test if collective.relatedslider is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed(
            'collective.relatedslider')
        )

    def test_browserlayer_removed(self):
        """Test that ICollectiveRelatedSliderLayer is removed."""
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveRelatedSliderLayer,
                         utils.registered_layers())
