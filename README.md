# Cagil Gumus Blog

Currently using a forked version of `Pelican-Cid` theme. Reason: Change fonts and geometry of text etc.

WARNING: Remember to upload the source changes to `main` branch! `make github` doesn't do that!

## Installation 

### Using Makefile
```bash
make env
make RELATIVE=1 devserver # for local development
make publish # to generate artifacts for GitHub Pages
make github # use ghp-import to upload changes to gh-pages
```
## Writing Content 

* Create subfolders for the Categories and add `<blog_post>.md`.
* Render the HTML
  * `pelican content -o output -s pelicanconf.py`  w/ GitHub Pages URL
  * `pelican content -o output -s pelicanconf.py -e RELATIVE_URLS='"True"'` to render for localhost access
* `pelican --autoreload --listen &` to host http_server
* `ghp-import output -b gh-pages` to upload changes to `gh-pages` branch
* `git push origin gh-pages` to publish


Here is the website: https://cagil-gumus.github.io/