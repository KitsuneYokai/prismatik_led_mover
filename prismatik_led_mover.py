"""
Prismatik (https://github.com/psieg/Lightpack) LED mover by KitsuneYokai
"""

import configparser
import os


# CHANGE THESE VALUES
# PRO TIP:  You can rearrange one LED in the Prismatik setup gui from the side where its not alignt right,
#           to the first led thats shown, to get the right number for the X and Y Axis
#           Prismatik -> Settings -> Device -> Run configuration wizard

x_new = 100  # how much pixel to move the LED on the X axis
x_operation = "+"  # + or -
y_new = 100  # how much pixel to move the LED on the Y axis
y_operation = "+"  # + or -


# load Lightpack.ini file
config = configparser.ConfigParser()
config.optionxform = str
config.read(os.path.join(os.path.dirname(__file__), "Lightpack.ini"))

# for each section in the config file look for the "Position" key
for section in config.sections():
    for key, value in config.items(section):
        if key == "Position":
            # remove the @Point() from the value
            val_remove_text1 = value.replace("@Point(", "")
            val_remove_text2 = val_remove_text1.replace(")", "")
            # create a dict of the x and y values from the value
            xy_dict = val_remove_text2.split(" ")
            print(xy_dict)
            # calculate the new x and y values
            x_final = f"{int(xy_dict[0])} {x_operation} {int(x_new)}"
            y_final = f"{int(xy_dict[1])} {y_operation} {int(y_new)}"
            new = "@Point(" + str(eval(x_final)) + " " + str(eval(y_final)) + ")"
            print(new)
            # replace the old values with the new ones
            config.set(section, key, new)

# write the new config.ini file
with open(os.path.join(os.path.dirname(__file__), "Lightpack.ini"), "w") as configfile:
    config.write(configfile)
