# Cagil Gumus Blog

Currently using a forked version of `Pelican-Cid` theme. Reason: Change fonts and geometry of text etc.

WARNING: Remember to upload the source changes to `main` branch! `make github` doesn't do that!

## Installation 

### Using Makefile
```bash
# Checkout Pelican-Cid git submodule as the main theme
git submodule update --init --recursive
make env
make RELATIVE=1 devserver # for local development
make publish # to generate artifacts for GitHub Pages
make github # use ghp-import to upload changes to gh-pages
```

## Tips and Tricks 

* use `Status: draft` to mark posts that are not ready

Here is the website: https://cagil-gumus.github.io/