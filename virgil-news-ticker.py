import obspython as obs
import codecs

# ----------------------------------------------------------------- #
# Austin Tinkel
# https://austin-tinkel.com
# https://twitter.com/AustinTinkel
# Some code taken from Revenkroz's Random Text at 
# https://obsproject.com/forum/resources/random-text.1542/ and 
# https://obsproject.com/wiki/Getting-Started-With-OBS-Scripting
# ----------------------------------------------------------------- #

DEFAULT_PATH = "C:\\"

# Object for storing info
class Storage:
    _props_ = None
    _settings_ = None
    lines = []
    source_name = ""
    file_name = ""
    spaces = 0
    interstitial = ""

def assemble_string():
    output = ""
    for line in Storage.lines:
        output += line.strip() + ((" " * (Storage.spaces // 2)) + Storage.interstitial + (" " * (Storage.spaces // 2)))
    return output

def script_description():
    return "A script that is meant to be used with a Text source with a Scroll filter to emulate a news ticker."

# get the sources
def populate_list_property_with_source_names(list_property):
    sources = obs.obs_enum_sources()
    obs.obs_property_list_clear(list_property)
    obs.obs_property_list_add_string(list_property, "", "")
    for source in sources:
        name = obs.obs_source_get_name(source)
        obs.obs_property_list_add_string(list_property, name, name)
    obs.source_list_release(sources)

# default values for script settings
def script_defaults(settings):
    obs.obs_data_set_default_string(settings, "source_name", "")
    obs.obs_data_set_default_string(settings, "source_file", "")
    obs.obs_data_set_default_int(settings, "spaces", 25)
    obs.obs_data_set_default_string(settings, "interstitial", "")

# script settings
def script_properties():
    props = obs.obs_properties_create()
    Storage._props_ = props

    # Source Name text box
    list_property = obs.obs_properties_add_list(props, "source_name", "Source name", obs.OBS_COMBO_TYPE_LIST, obs.OBS_COMBO_FORMAT_STRING)
    populate_list_property_with_source_names(list_property)
    # Source File file picker
    obs.obs_properties_add_path(props, "file_name", "Source File", obs.OBS_PATH_FILE, "Text Files (*.txt)", DEFAULT_PATH)
    # Spaces text box
    obs.obs_properties_add_int_slider(props, "spaces", "Spaces", 0, 200, 5)
    # Interstitial text box
    obs.obs_properties_add_text(props, "interstitial", "Interstitial Character", obs.OBS_TEXT_DEFAULT)
    # Update button
    obs.obs_properties_add_button(props, "button", "Update", on_get_update_click)
    # Refresh sources button
    obs.obs_properties_add_button(props, "button", "Refresh list of sources", lambda props,prop: True if populate_list_property_with_source_names(list_property) else True)

    return props

def script_update(settings):
    Storage._settings_ = settings

    Storage.source_name = obs.obs_data_get_string(settings, "source_name")
    Storage.file_name = obs.obs_data_get_string(settings, "file_name")
    Storage.spaces = obs.obs_data_get_int(settings, "spaces")
    Storage.interstitial = obs.obs_data_get_string(settings, "interstitial")

    update_file()

def on_get_update_click(props, prop):
    update_file()
    update_text()

def update_text():
    source = obs.obs_get_source_by_name(Storage.source_name)
    if source is not None:
        settings = obs.obs_data_create()

    text = assemble_string()

    # set text element
    obs.obs_data_set_string(settings, "text", text)
    obs.obs_source_update(source, settings)
    obs.obs_data_release(settings)
    obs.obs_source_release(source)

def update_file():
    if Storage.file_name is not "":
        # open file and create a list out of the lines
        Storage.lines = codecs.open(Storage.file_name, "r", "utf-8").readlines()