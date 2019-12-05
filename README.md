# TomlConfig
Toml configparser made (stupidly) simple for python.

# install

~~~shell
pip install TomlConfig
~~~

# Usage

If the toml config file "config.toml" exist with content:

~~~
[general]
language = 'en'

[general.editor]
size = 12
font = 'arial'
~~~

Use the TomlConfig parse it as following:

~~~python
from tomlconfig import TomlConfig

# read config file
config = TomlConfig("config.toml")

# get item
language = config["general.language"] # "en"
size = config["general.editor.size"]  # 12

# in operation
"general.language" in  config  # True

# set or add item
config["general.editor.font"] = "Roman" # set font=Roman in toml
config["server.name"] = 'server1' # add a new item
config["newSection"] = {"k1":1} # add a new config section

# list item operation
config.insertToChild("general.editor.font", 0, "Arial") # change font from str to list and insert item
config.appendToChild("general.editor.font", "SimSun") # font=["Arial", "Roman", "SimSun"]
# same as config["general.editor.file"].append("SimSun")
~~~
