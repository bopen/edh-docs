# EDH Docs

Earth Data Hub documentation built with Sphinx.
It uses the Shibuya theme and supports Markdown pages through MyST.

Run quality assurance checks:

```bash
uv run pre-commit run --all
```

Build the documentation locally:

```bash
uv run make html
```

Open the generated HTML or serve it:

```bash
uv run python -m http.server 8000 --directory build/html
```

Then go to <http://localhost:8000>.
