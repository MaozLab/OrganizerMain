# Organizer GUI
In the “Organizer” multi-chip system there are many possibilities to connect organ-chips. The purpose of this GUI is to provide the best way to connect the chips according to data from the user.


## Input
#### Parallel Organs Entry:
* The amount of organs to connect in parallel.
* Enter a number between 2 and 6, or leave blank for 0.

#### Serial Organs Entry:
* The amount of organs to connect in serial.
* Enter a number between 1 and 6, or leave blank for 0.
* When there is 1 serial organ, there must be at least 2 parallel organs as well.
* The sum of the parallel organs and the serial organs can not be greater than 6.

#### Setups Entry:
* The amount of setups (sub-systems).
* Enter a number between 1 and 3, default is 1.
* When there is more than 1 setup, the amount of organs can not be greater than 3.

#### Organs Entry:
* Which specific organs.
* Enter the organ letters in alphabetical order, uppercase or lowercase.
* When left blank a default option will be shown.

## Output
* To run the program, press the "Run" button, or press the RETURN key on the keyboard.
Based on the data from the entries, the program will show:
    * Which valves to close
    * Which organs are connected in parallel
    * Which organs are connected in serial
    * An illustration of the organizer
