==============================================================================
collective.relatedslider
==============================================================================

This is a Plone addon that adds a behavior and viewlet for displaying related
content in a scrollable slider at the bottom of the content area.  It can use
either the relatedItems behavior or collection behavior applied to the content
for determining the related items.



Installation
------------

Install collective.relatedslider by adding it to your buildout::

   [buildout]

    ...

    eggs =
        collective.relatedslider


and then running "bin/buildout"

Install the add-on from the add-ons control panel, and then use the "Dexterity
Types" control panel to add the "Related Slider" behavior to your types.  Any
types using this behavior will also need to have either the "Related Items"
behavior or the "Collection" behavior applied as well.

When editing content with the behavior applied you should see a drop down to
select where the slider items come from (either collection criteria or related
items, depending on the applied behaviors).  If you use Related Items as the
source for slider items, the normal related items viewlet will be hidden from
view.


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.relatedslider/issues
- Source Code: https://github.com/collective/collective.relatedslider


Support
-------

This add-on was developed by Jazkarta, Inc.

If you are having issues, please let us know.
I can be reached at: alecpm@gmail.com


License
-------

The project is licensed under the GPLv2.
