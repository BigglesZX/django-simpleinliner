# django-simpleinliner

A simple Django app for inlining static CSS and JS files in templates. Read CSS, JS or generic files from your static directories and insert their contents into your Django templates, wrapping in appropriate HTML tags if necessary.

## Rationale

Provides a quick and easy way to inline an entire JS or CSS file from staticfiles into a template, wrapping it in appropriate tags. [`django-compressor`](https://github.com/django-compressor/django-compressor) does this but I wanted something more lightweight, and also wanted to try my hand at writing a Django extension. Some inspiration and staticfile-handling code was taken from [`django-inlinecss`](https://github.com/roverdotcom/django-inlinecss/).

## Compatibility

I've not exhaustively tested all the below combinations, however I believe this table to be accurate.

|                | Django 1.10   | 1.11 | 2.0 | 2.1 | 2.2 | 3.0 | 3.2 | 3.2 |
|---------------:|:-------------:|:----:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Python** 2.7 | ✔             | ✔    |     |     |     |     |     |     |
| 3.6            | ✔             | ✔    | ✔   | ✔   | ✔   | ✔   | ✔   | ✔   |

## Installation

```
$ pip install django-simpleinliner
```

Add `simpleinliner` to your `INSTALLED_APPS` setting.

## Usage

Load the app at the top of your template:

```
{% load simpleinliner %}
```

Call `inlinecss`, `inlinejs` or `inlinegeneric` where you want to pull in a static file:

```
{% inlinejs 'path/to/my.js' %}

{% inlinecss 'path/to/my.css' %}

{% inlinegeneric 'path/to/my.svg' %}
```

The file will be inserted into the template each time the template is rendered, keeping it up to date.

You can override the default attributes given to `<script>` and `<style>` tags generated by `simpleinliner` by including the following in your project settings:

```
SIMPLEINLINER_DEFAULT_TAG_ATTRIBUTES = {
    'script': {
        'charset': 'utf-8',
        'type': 'text/javascript',
    },
    'style': {
        'charset': 'utf-8',
        'type': 'text/css',
    },
}
```

Add or edit these as desired to change the attributes applied to these tags.

By default `simpleinliner` will silently fail (including an empty tag if using `inlinejs` or `inlinecss`) if the specified path doesn't exist. You can force it to raise an exception by setting `SIMPLEINLINER_RAISE_EXCEPTIONS` to `True` in your project settings.

## Development Installation

If working locally on the package you can install the development tools via `pip`:

```shell
$ pip install -e .[dev]
```

To lint with `flake8`:

```shell
$ flake8
```

## Credits

Since version 0.2.5 this library bundles version 1.16 of the [`html`](https://pypi.org/project/html/) library (in `html.py`), as that library does not correctly install itself in modern python/setuptools environments and cannot be correctly imported.

## Issues, Suggestions, Contributions

...are welcome on GitHub. Thanks for your interest in `simpleinliner`!
