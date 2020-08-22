# JRNY
A simple CLI tool I created to help me write my journal.

![Example](/imgs/example1.png)

## Installation
I have not yet implemented a proper installation, but you can download the code & use it in it's folder, or figure out how to install it yourself. (If you try to do that, be aware that the only dependency not included in the base Python 3 installation is the `xdg` module.)

## Usage
First, create `~/.config/jrny/config.ini`(Replace `~/.config/` with your XDG config location if necessary.)
Here is my `config.ini` as an example of the options you must set before using JRNY:

![Example](/imgs/example2.png)

`ROOT_DIRECTORY` sets the directory that your whole journal is kept inside of.

`DIRECTORY_STRUCTURE` controls how the directories that your journal entries will be stored in are generated.

`TIME_FORMAT` controls how the filenames of your journal entries are generated.

`FILE_TYPE` sets the file extension of your journal entries.

`TEXT_EDITOR` is what your journal entries will be written in.

After configuring JRNY, you can use the 2 currently implemented commands:

`jrny -s`: Display a status message. (Displays info on today's entry, as well as the amount of entries you have written, and some values from the config file.)

`jrny -w`: Write today's entry. (Creates all the needed directories and launches your text editor to edit your entry in the format you specified.)
