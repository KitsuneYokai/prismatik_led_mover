
# [Prismatik](https://github.com/psieg/Lightpack) LED mover

A little script to move all the leds of an already created `Lightpack.ini` file.

## FAQ

#### What is this?

This is a little python script to move all leds of an already created Lightpack.ini

#### Why was it created?

So im using Windows + Ubuntu and im too lazy to create an own config for ubuntu, so I took the already made Windows config and pasted it inside the `$HOME/.prismatik/Profiles` folder, only to find out, that the monoitors are not alligned propperly.

#### How can i use it?

- Install the [Python](https://www.python.org/) programming language.
- Download the code.
- Copy your `Lightpack.ini` file located in your home folder `C:\Users\<username>\.Prismatik\Profiles` to the same folder of the `prismatik_led_mover.py` file.
- Open the `prismatik_led_mover.py` file in your favorite text editor ([Notepad++](https://notepad-plus-plus.org/), [VSCode](https://code.visualstudio.com/) , ...)
- Change the values from Line `14-17` to match your offset.
    | Values | Meaning  |
    | :---:   | :---: |
    | `x_new` | How much pixel the X-Axis should get moved |
    | `x_operation` | If you want to add or subtract `x_new`(left, right)|
    | `y_new` | How much pixel the Y-Axis should get moved |
    | `x_operation` | If you want to add or subtract `y_new` (up, down)|

    **PRO TIP:**

    You can rearrange one LED in the Prismatik setup gui from the side where its not alignt right,
              to the first led thats shown, to get the right number for the X and Y Axis
              Prismatik -> Settings -> Device -> Run configuration wizard
- Run the Script:

        python3 prismatik_led_mover.py

    After its done place the `Lightpack.ini` file back into your Prismatik folder, and you are good to go.

______
I hope this helped/helps someone. Have a great day ^_^
