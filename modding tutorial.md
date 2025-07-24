# RWE# modding tutorial

so you want to add something to rwe# *huh*?

# Content

1. RWE structure
2. example/mod template
3. different parts of rwe# and rwe# structure

# RWE# structure

![basic structure of rwe#](https://media.discordapp.net/attachments/1338537809174069280/1398034604371345428/xAtLUKEeuWQAAAABJRU5ErkJggg.png?ex=6883e4af&is=6882932f&hm=a423be5559a882a630081d43bad61ed6f09cc9cf4ab2f2049cd33c7a2d8cf778&=&format=webp&quality=lossless)

*these are some squiggly lines that loosely indicate how rwe#'s systems interact with each other*

how rwe# launches:
1. application gets initiated and starts splash screen
2. splash screen loads tiles, props(and prop colors) and effects
3. application starts main window
4. main window starts manager
5. manager loads mods with mod loader
6. mods load editors, modules, uis, hotkeys, settings etc.
7. manager loads level and creates viewport for it
8. modules and selected editor initiate their graphics on level viewport

---

# How to create your first mod/mod template

first, you need to create a folder in `files/mods`

name doesn't matter as long as it has no spaces and special characters

in this folder you need to create 2 files:

* `modinfo.json` contains all metadata about your mod
* `mod.py` has the mod class
