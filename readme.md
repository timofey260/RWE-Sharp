# RWE#: Grand sequel to RWE+

```
   ___ _      ______  ____ 
  / _ \ | /| / / __/_/ / /_
 / , _/ |/ |/ / _//_  . __/
/_/|_||__/|__/___/_    __/ 
                  /_/_/    

RWE# - timofey26, atom and lang0s 

```

RWE#(ar-we-e sharp) is custom Level editor for Rain World(2017) and second iteration of RWE+

Main features from RWE+:
* Better UI(in all the ways, the pyside 6 is awesome)
* Modular design(windows go brrrr)
* Modding support
* Better Performance
* Better linux and mac ports(hopefully)

# Screenshots

todo

# Quickstart

To use RWE#, you can either download release version from [releases page](https://github.com/timofey260/RWE-Sharp/releases) or Run/Build from source(see below)

Note: Mac users would need to build [Drizzle](https://github.com/SlimeCubed/Drizzle) from [source](https://github.com/SlimeCubed/Drizzle) and put it inside RWE#'s drizzle folder

## Download Release

1. Go to the [Releases page](https://github.com/timofey260/RWE-Sharp/releases) and download latest release for your system(if there is no build for your system, build from source)
2. Unpack the downloaded archive to wherever you want(RWE# must have access to folders)
3. Run RWE#'s binary/executable

## Run from source

To run from source you must have python installed with venv package(install it with pip or your distro-specific analog)

1. Clone the repo(Either [download source code](https://github.com/timofey260/RWE-Sharp/archive/refs/heads/master.zip) or use `git clone` as showed below):
```shell
git clone https://github.com/timofey260/RWE-Sharp/
cd RWE-Sharp
```
I recommend using git since it allows for easy updating of rwe#

2. Create [Virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments):
```shell
python -m venv init .venv
```

After that make sure you [initiate all environment variables of shell](https://docs.python.org/3/library/venv.html#how-venvs-work)(so that you would use venv's commands instead of default ones):

For example Bash users should use this:
```shell
source .venv/bin/activate
```

3. Install all required packages:
```shell
pip install -r requirements.txt
```

4. Run RWE#:
```shell
python main.py
```

## Building from source

1. Do steps 1-3 in **Run from source** installation
2. Install Pyinstaller package:
```shell
pip install pyinstaller
```
3. Build(you might need to reinitiate environment variables):
```shell
pyinstaller -F main.py
```
Note: `-F` compiles your source code into one file instead of many, and i'd recommend leaving it in

Note: when you build with pyinstaller and share your build somewhere, make sure to also include ./files directory with your build(check how RWE# builds look)

# Modding

RWE# was developed with modding in mind

If you want to make your own mod for RWE#, i'd recommend checking RWE#'s wiki and api for more information
