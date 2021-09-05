# NuitkaBS
Nuitka build system

# Why? What the reason of this project?
OK, we already have `nuitka`, and it works. It allows to build any python file
as executable or module.

## But reality is...
* The most usual case in production is microservice monolith. It means the code
base has many entry points. When you build single executable or single module,
you are doing 95% of work twice or more. If you ready to wait forever until
build complete, it's OK, but i'm not

* Some libraries with C-extensions and fallback python code work incorrect. It's
much easier to exclude these libraries from build

## Modules? Yes, but...
Yes, nuitka allow to split application code by modules. And since this moment
you have to write large number build commands -- one command for each module.
If you decided to split anything into separated module -- you have to rewrite
all commands again, adding `--nofollow-import-to=my_new_module`. If you added
any module, you have to rewrite all these commands again. And again...

## Сonclusion
NuitkaBS helps you to create really large number of build commands via simple to
read, undarstand and edit `YAML` config

# Installing
```
pip install -U nuitkabs
```

# Pre-requirements
You should know nuitka generate C-files and then compile it via `gcc` or
`clang`. So, you have to install compiler (gcc or clang), python development
headers. It will be good if you install `ccache`

# Usage
NuitkaBS is really thin wrapper over Nuitka. The first thing you have to create
`nuitkabs.yaml` file in root of your project. The most keys you see in `YAML`
config you can find in nuitka documentation. Example:

```
modules:
  models:
  views:
  starlette_app:
  ubjson:
    include-module:
      - ubjson.encoder
  starlette:
    include-module:
      - starlette.applications
      - starlette.endpoints

# =========

executables:
  my_script:
  my_daemon:

# =========

generic:
  output-dir: ../build/
  lto:
  remove-output:
  warn-unusual-code:
  follow-imports:
  plugin-enable:
    - pylint-warnings
  nofollow-import-to:
    - sqlalchemy
    - pandas
    - ujson
    - orjson
    - greenlet
```

Just compare keys and nuitka help page. They are the same.

# Compile external library
Just look the example. Find `ubjson` and `starlette` modules. Yes, there are
external libraries

# Some tricks

## List or single item
There is no difference between single item and item list:

```
generic:
  output-dir: 
    - ../build/
```

## If you have nothing to say, don't say
If you have to enumerate your modules, but you have nothing to put as value --
just let value empty

```
modules:
  models:
  views:
  starlette_app:
```