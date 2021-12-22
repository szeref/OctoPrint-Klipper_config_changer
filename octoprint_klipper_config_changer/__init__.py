# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin
import os
import shutil

class Klipper_config_changerPlugin(octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.AssetPlugin,
                       octoprint.plugin.SettingsPlugin):

    def get_settings_defaults(self):
        with open(os.path.expanduser('~/printer.cfg')) as f:
            tool = f.readline()
        tool = tool.replace("#", "")
        return dict(tool=tool)

    def on_settings_save(self, data):
        octoprint.plugin.SettingsPlugin.on_settings_save(self, data)
        shutil.copy(os.path.expanduser('~/printer_' + self._settings.get(["tool"]) + '.cfg'), os.path.expanduser('~/printer.cfg'))
        self._printer.commands("RESTART")

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(
            js=["js/utils.js"]
        )

__plugin_name__ = "Klipper config changer"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = Klipper_config_changerPlugin()
