#!/usr/bin/env python
# vim:fileencoding=UTF-8:ts=4:sw=4:sta:et:sts=4:ai
from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__ = 'GPL v3'
__copyright__ = '2011, Hakan Tandogan <hakan@gurkensalat.com>'
__docformat__ = 'restructuredtext en'

from calibre.gui2.metadata.config import ConfigWidget as DefaultConfigWidget
from calibre.utils.config import JSONConfig

STORE_NAME = 'Options'

DEFAULT_STORE_VALUES = {
}

# This is where all preferences for this plugin will be stored
plugin_prefs = JSONConfig('plugins/Perrypedia')

# Set defaults
plugin_prefs.defaults[STORE_NAME] = DEFAULT_STORE_VALUES

class ConfigWidget(DefaultConfigWidget):

    def __init__(self, plugin):
        DefaultConfigWidget.__init__(self, plugin)


    def save_settings(self):
        new_prefs = {}

        plugin_prefs[STORE_NAME] = new_prefs
