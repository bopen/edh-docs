# EDH Docs

Earth Data Hub documentation built with Sphinx.
It uses the Shibuya theme and supports Markdown pages through MyST.

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

## Custom badges

Use these roles for badges matching the Earth Data Hub webportal:

```md
{bdg-restricted}`Restricted`
{bdg-edh-keyword}`EDH keyword`
{bdg-draft}`Draft`
{bdg-deprecated}`Deprecated`
{bdg-geobrowser}`Geobrowser available`
```
