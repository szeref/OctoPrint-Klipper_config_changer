$(function() {
    function KlipperConfigChangerViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];

        // Open settings link
        self.openKlipperConfigChangerSettings = function () {
		$("a#navbar_show_settings").click();
      		$("li#settings_plugin_klipper_config_changer_link a").click();
    	}; 

    }

    // This is how our plugin registers itself with the application, by adding some configuration
    // information to the global variable OCTOPRINT_VIEWMODELS
    OCTOPRINT_VIEWMODELS.push([
        // This is the constructor to call for instantiating the plugin
        KlipperConfigChangerViewModel,

        // This is a list of dependencies to inject into the plugin, the order which you request
        // here is the order in which the dependencies will be injected into your view model upon
        // instantiation via the parameters argument
        ["settingsViewModel"],

        // Finally, this is the list of selectors for all elements we want this view model to be bound to.
        ["#navbar_plugin_klipper_config_changer"]
    ]);
});
