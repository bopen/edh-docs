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

## Custom badges

Use these roles for badges matching the Earth Data Hub webportal:

```md
{bdg-restricted}`Restricted`
{bdg-edh-keyword}`EDH keyword`
{bdg-draft}`Draft`
{bdg-deprecated}`Deprecated`
{bdg-geobrowser}`Geobrowser available`
```

## Required envars to properly build the documentation

- `READTHEDOCS_CANONICAL_URL`:\
  Root of the documentation site
  (can be also a root absolute path)
- `BASE_URL`:\
  external full URL to the EDH portal
- `DATASTORE_INTERNAL_HOST`:\
  Main EDH access domain (by default `data.earthdatahub.destine.eu`)
- `DATASTORE_HOST`:\
  Alternative EDH access URL (required for restricted datasets, by default `api.earthdatahub.destine.eu`)
- `DOCUMENTATION_PORTAL`:\
  Public URL to the documentation portal (by default `https://earthdatahub.destine.eu/docs`)

## Licenses

- Documentation and other content: [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode)
- Code: [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
