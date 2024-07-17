# Truthbrush Documentation Site

## Prerequisites

### Quarto

We need to install Quarto onto the local machine. You can [download](https://quarto.org/docs/get-started/), or [install via homebrew](https://formulae.brew.sh/cask/quarto) (if you like that kind of thing):

```sh
brew install --cask quarto
```


If you use VS Code, you can also consider installing the [Quarto Extension](https://marketplace.visualstudio.com/items?itemName=quarto.quarto).


## Docs Requirements

```
pip install -r docs/requirements.txt
```



## Auto Documentation

In the ["_quarto.yml" config file](/docs/_quarto.yml), we specify in the `quartodoc` section that our site should display "references/index.qmd", which will act as the entrypoint into the package auto-documentation.

Using quartodoc to automatically generate docstring content into the "docs/references" directory:

```sh
quartodoc build --config docs/_quarto.yml --verbose
```

After the documentation pages have been generated, then we can preview and build the site.


## Building


Previewing the site (runs like a local webserver):

```sh
quarto preview docs/
```


Rendering the site (writes local HTML files to the "docs/_build" directory, which is ignored from version control):

```sh
quarto render docs/ --verbose
```


### Website Publishing

We are using the ["quarto-pages.yml" workflow configuration file](/.github/workflows/quarto-pages.yml) to deploy the site to GitHub Pages when new commits are pushed to the main branch.

In order for this to work, you first need to configure your GitHub Pages repo settings to publish via GitHub Actions.
