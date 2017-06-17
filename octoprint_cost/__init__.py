# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin

class CostPlugin(octoprint.plugin.SettingsPlugin,
                 octoprint.plugin.TemplatePlugin,
                 octoprint.plugin.AssetPlugin):

	def get_settings_defaults(self):
		return dict(
			currency="€",
                        weight="kg",
                        length="m",
                        time="h",
                        cost_per_time=1.50,
                        cost_per_length=0.08,
                        cost_per_weight=25,
                        density_of_filament=1.25,
                        check_cost=True
		)

        def get_template_configs(self):
                return [
                        dict(type="settings", custom_bindings=False),
                ]

        def get_template_vars(self):
                return dict(
                        cost_per_time=self._settings.get(["cost_per_time"]),
                        cost_per_length=self._settings.get(["cost_per_length"]),
                        cost_per_weight=self._settings.get(["cost_per_weight"]),
                        density_of_filament=self._settings.get(["density_of_filament"]),
                        currency=self._settings.get(["currency"]),
                        check_cost=self._settings.get(["check_cost"])
                )

        def get_assets(self):
                return dict(js=["js/cost.js"])

	def get_update_information(self):
		# Define the configuration for your plugin to use with the Software Update
		# Plugin here. See https://github.com/foosel/OctoPrint/wiki/Plugin:-Software-Update
		# for details.
		return dict(
			cost=dict(
				displayName="Cost Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jasiek",
				repo="OctoPrint-Cost",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jasiek/OctoPrint-Cost/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Cost Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = CostPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

