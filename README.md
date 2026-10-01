# EDH Docs

Source code for the Earth Data Hub documentation, built with [Sphinx](https://www.sphinx-doc.org/).
It uses the [Shibuya](https://shibuya.lepture.com/) theme and supports Markdown pages through [MyST](https://mystmd.org/).

Run quality assurance checks:

```bash
make qa
```

Build the documentation locally:

```bash
make html
```

Open the generated HTML or serve it:

```bash
make serve
```

Then go to <http://localhost:8000>.

## Markdown for LLMs

Every page is also published as Markdown (`page.md` next to `page.html`), together with `llms.txt` and `llms-full.txt`, by [sphinx-llm](https://github.com/NVIDIA/sphinx-llm).
The "Copy page" and "Open in ..." buttons point to the Markdown on the production site: to try them locally, build with

```bash
make html O="-D html_baseurl=http://localhost:8000/"
```

## Custom badges

Use these roles for badges matching the Earth Data Hub webportal:

```md
{bdg-restricted}`Restricted`
{bdg-edh-keyword}`EDH keyword`
{bdg-draft}`Draft`
{bdg-deprecated}`Deprecated`
{bdg-geobrowser}`Geobrowser available`
```

## Licenses

- Documentation and other content: [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode)
- Code: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
