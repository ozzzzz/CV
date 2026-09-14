# HOWTO

## Generate pdf
To generate pdf, install [md2pdf](https://github.com/jmaupetit/md2pdf) (`uv tool install "md2pdf[cli]"`) and generate pdf from markdown file:

```bash
DYLD_LIBRARY_PATH=/opt/homebrew/lib md2pdf -i README.md -o Bogdan_Neterebskii.pdf -c style.css
```

`DYLD_LIBRARY_PATH` needed on macOS so WeasyPrint finds Homebrew's pango/gobject libs (`brew install pango gdk-pixbuf`).

## Generate graphs

Go to the `graphs` folder, install dependencies and run the [marimo](https://marimo.io/) notebook:

```bash
cd graphs
poetry install
poetry run marimo edit graphs/marimo_notebook.py
```