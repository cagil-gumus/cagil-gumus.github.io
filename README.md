## Installation 

```bash
pip install "pelican[markdown]" # install the optional dependencies for Markdown
pip install ghp-import          # Makes life easier to deploy to gh-pages branch
```


## Writing Content 

* Create subfolders for the Categories and add `<blog_post>.md`.
* Render the HTML
  * `pelican content -o output -s pelicanconf.py`  w/ GitHub Pages URL
  * `pelican content -o output -s pelicanconf.py -e RELATIVE_URLS='"True"'` to render for localhost access
* `pelican --autoreload --listen &` to host http_server
* `ghp-import output -b gh-pages` to upload changes to `gh-pages` branch

## TODOs:

* Don't push raw photos. Use hosting site instead. You only have 1GB of storage
