# HOWTO

## Generate pdf
To generate pdf, install [md2pdf](https://github.com/jmaupetit/md2pdf) and generate pdf from markdown file:

```bash
md2pdf --css style.css README.md Bogdan_Neterebskii.pdf
```

## Generate graphs

Go to the `graphs` folder, install dependencies and run the [marimo](https://marimo.io/) notebook:

```bash
cd graphs
poetry install
poetry run marimo edit graphs/marimo_notebook.py
```