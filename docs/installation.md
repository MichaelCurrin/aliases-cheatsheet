# Installation


## Project requirements

- [Python](https://www.python.org/) >= 3.10


## Install hooks

```sh
$ make hooks
```


## Install project dependencies

Required - install Poetry on your system globally. See [Gist](https://gist.github.com/MichaelCurrin/8d6c377cc46ce2ef6f94e52b4a21787d).

Then install Python packages into a virtual environment managed by Poetry:

```sh
$ make install
```

Upgrade packages when needed:

```sh
$ make upgrade
```

---

You may continue to the [Usage](usage.md) doc.
