(api-reference)=

## API reference

Under the hood, Earth Data Hub is just two open interfaces: a **STAC catalogue** to find data, and **Zarr over HTTPS** to read it. No SDK required. If your tool can make a web request, it can use Earth Data Hub.

(stac-api)=

### STAC catalogue

[STAC](https://stacspec.org/) (SpatioTemporal Asset Catalog) is a standard, searchable catalogue of Earth data. Every collection and dataset you see in the Earth Data Hub catalogue is also available as STAC metadata, starting from a single root URL:

```{code-block} text
---
substitutions:
---
|stac_api_url|/
```

```{admonition} One URL to discover everything.
---
class: note
---
The STAC catalogue is **public**: browsing it requires no API key. You only need your key when you read the data itself.
```

Explore the catalogue straight from your terminal:

```{code-block} bash
---
substitutions:
---
# Root catalogue
curl |stac_api_url|/

# All collections (e.g. era5, cmip6, climate-dt-2)
curl |stac_api_url|/collections

# All datasets in a collection
curl |stac_api_url|/collections/era5/items

# Search across the catalogue
curl "|stac_api_url|/search?collections=era5&limit=5"
```

In STAC, each dataset is an **item**. Its `data` asset holds the **dataset URL**, along with the exact arguments needed to open it with Xarray:

```{code-block} json
---
emphasize-lines: 3
---
"assets": {
  "data": {
    "href": "https://data.earthdatahub.destine.eu/era5/era5-land-monthly-v0.zarr",
    "roles": ["data"],
    "xarray:open_kwargs": {"chunks": {}, "engine": "zarr"},
    "xarray:storage_options": {"client_kwargs": {"trust_env": true}}
  }
}
```

#### From catalogue to dataset in Python

Install [pystac-client](https://pystac-client.readthedocs.io/) alongside the packages from [](environment-setup):

````{tab-set}
---
class: outline
---
~~~{tab-item} {iconify}`vscode-icons:file-type-pypi` pip
```bash
pip install pystac-client xarray "zarr>3" dask aiohttp
```
~~~

~~~{tab-item} {iconify}`vscode-icons:file-type-uv` uv
```bash
uv add pystac-client xarray "zarr>3" dask aiohttp
```
~~~

~~~{tab-item} {iconify}`vscode-icons:file-type-conda` conda
```bash
conda install -c conda-forge pystac-client xarray "zarr>3" dask aiohttp
```
~~~
````

Then find a dataset in the catalogue and open it, with no URLs to copy and paste. This example uses your `.netrc` file, see [](protected-datasets):

```{code-block} python
---
substitutions:
---
import pystac_client
import xarray as xr

catalog = pystac_client.Client.open("|stac_api_url|")
item = catalog.get_collection("era5").get_item("era5-land")
asset = item.assets["data"]

xr.open_dataset(
    asset.href,
    storage_options=asset.extra_fields.get("xarray:storage_options"),
    **asset.extra_fields.get("xarray:open_kwargs", {}),
)

```

(zarr-over-https)=

### Zarr over HTTPS

A Zarr dataset is simply a **folder of small files** on the web: a few JSON files describing the data, plus the data itself split into chunks. Each of those files has its own URL, so a plain HTTPS request is all it takes to read one.

```{admonition} If it speaks HTTP, it speaks Zarr.
---
class: tip
---
Xarray, `curl`, a browser, or your own code in any language: they all read the same files the same way.
```

Try it with the public test dataset:

```{code-block} bash
---
substitutions:
---
# Dataset metadata: variables, dimensions and attributes
curl https://|datastore_internal_host|/public/test-dataset-v1.zarr/zarr.json

# Variable metadata: shape, chunk shape, data type and compression
curl https://|datastore_internal_host|/public/test-dataset-v1.zarr/demographic_totals/zarr.json

# A single chunk of raw data
curl -o chunk.bin https://|datastore_internal_host|/public/test-dataset-v1.zarr/year/c/0
```

File names follow the standard [Zarr conventions](https://zarr-specs.readthedocs.io/en/latest/v3/core/index.html). To learn more about how chunks are organised, see [](chunking-schemes).

For protected datasets, let `curl` read your API key from your `.netrc` file, or pass it directly:

```{code-block} bash
---
substitutions:
---
# Using your .netrc file (recommended)
curl --netrc https://|datastore_internal_host||private_test_dataset_path|/zarr.json

# Using your API key directly
curl -u edh:<your API key> https://|datastore_internal_host||private_test_dataset_path|/zarr.json
```

```{note}
Every request counts towards your monthly quota, whichever tool you use. See [](quotas).
```
