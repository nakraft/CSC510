## Installing a Python distribution for the Group 36's Lua software 

This document gives the instructions to install a system that loads and summarizes csv data.  

### All systems (Linux, Mac OS X, and Windows)

1. Create virtual enviornment and activate using python 3.10. (Need some help? Visit [here](https://docs.python.org/3/library/venv.html).)

```
$ python3 -m venv lua_venv
$ source lua_venv/bin/activate
```

2. Install requirements. 

```
(lua_venv) $ pip3 install -r requirements.txt
```

3. Clone the repository. 

```
(lua_venv) $ git clone git@github.com:nakraft/CSC510.git
```

## User Guide 

You can run the software after installation with the following core commands: 

- From within the root of the repository, all test suites can be run with: 

```
(lua_venv) $ python3 -m Code.lua
```

- To run with custom parameters or a unique dataset, try inserting the arguments: 

```
(lua_venv) $ python3 -h Code.lua 
```

- For more details, visit the help page from within the terminal: 

```
(lua_venv) $ python3 -h Code.lua 
```

## Advanced details

### Dependencies

The following libraries are required:

  * GDAL 3.5.1
  * numpy 1.23.2
  * protobuf 4.21.5
