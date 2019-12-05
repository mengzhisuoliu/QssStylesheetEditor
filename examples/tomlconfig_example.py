#!usr/bin/python
# -*- coding: utf-8 -*-
"""example for TomlConfig

| author: lileilei  email: <hustlei@sina.cn>  @2019, wuhan
"""

import sys, os
currentdir = os.path.dirname(__file__)
sys.path.append(currentdir + "/..")  # test environments, if TomlConfig is installed, this not needed
from tomlconfig import TomlConfig

config = TomlConfig()
if config.read(os.path.join(currentdir, "config.toml")):
    print("config file loaded")
else:
    print("config file not loaded")

# in or not
if "general.language" in config:
    print("'general.language' is an option or section in tomlcofig.")
language = config["general.language"]
print("language content is:" + language)

size = config["general.editor.size"]
print("size:{}".format(size))
fontWeight = config["general.editor"].get("fontWeight", 2)
print("fontWeight:{}".format(fontWeight))

if "general.language" in config:  # True
    print("'general.language' is in config.")
if config.hasSec("general.editor"):  # True
    print("'general.editor' is a section in config")

config["otherSection"]={'key1':1}  # add section
config["general.theme"]="simple"  # add "theme=simple" to general
