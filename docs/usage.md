# Usage

## Configure
> Prepare your aliases data

Do this whenever you want to pull in the latest changes to your aliases. These are used for the CLI and web apps.

```sh
$ make parse
```

## Run

### View CLI output

```sh
$ make cli
```

Or for scrollable output:

```sh
$ make cli-scroll
```

### Start dynamic CLI app

```sh
$ make live
```

### Start server locally

Start a Python server to serve the static assets, including the JSON data containing your aliases.

```sh
$ make serve
```

Then open the webapp in your browser:

- http://localhost:8000/
