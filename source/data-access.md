---
myst:
  html_meta:
    description lang=en: This page explains how to access Earth Data Hub datasets using open standards such as Xarray and Zarr, including environment setup, API key authentication, protected datasets, quotas, and local caching, plus the STAC catalogue API and direct Zarr access over HTTPS.
---

# {edh-octicon}`download` Data Access

{ .lead }
Learn how to access data and optimise your workflows.

(environment-setup)=

## Environment setup

```{admonition} Pure open standards. Zero vendor lock-in.
---
class: note
---
Earth Data Hub is built entirely on open standards. Our datasets are cloud-optimised Zarr stores, meaning you can stream them directly over HTTP using any language or library you already know.
```

While you can use any language, we recommend **Python combined with [Xarray](https://docs.xarray.dev/en/stable/)** for the best experience.

Install the required packages for this quick start by running this command in your terminal:

````{tab-set}
---
class: outline
---
~~~{tab-item} {iconify}`vscode-icons:file-type-pypi` pip
```bash
pip install xarray "zarr>3" dask aiohttp
```
~~~

~~~{tab-item} {iconify}`vscode-icons:file-type-uv` uv
```bash
uv add xarray "zarr>3" dask aiohttp
```
~~~

~~~{tab-item} {iconify}`vscode-icons:file-type-conda` conda
```bash
conda install -c conda-forge xarray "zarr>3" dask aiohttp
```
~~~
````

## Try a public dataset

Let's verify your environment. We have provided a **public test dataset** that you can access instantly, with **no accounts or passwords required**. It is the perfect place to test your setup before exploring the wider catalogue.

Run the following in your Python console:

```{code-block} pycon
---
substitutions:
---
>>> import xarray as xr

>>> xr.open_dataset(
...     "https://|datastore_internal_host|/public/test-dataset-v1.zarr",
...     chunks={},  # Tells Xarray to load data on-demand
...     engine="zarr",
... )
<xarray.Dataset> Size: 4GB
Dimensions:               (latitude: 720, longitude: 1440,
                           age_band_lower_bound: 14, year: 71)
Coordinates:
  * latitude              (latitude) float64 6kB 90.0 89.75 ... -89.5 -89.75
  * longitude             (longitude) float64 12kB 0.0 0.25 0.5 ... 359.5 359.8
  * age_band_lower_bound  (age_band_lower_bound) int64 112B 0 5 10 ... 55 60 65
  * year                  (year) int64 568B 1950 1951 1952 ... 2018 2019 2020
Data variables:
    demographic_totals    (latitude, longitude, age_band_lower_bound, year) float32 4GB dask.array<chunksize=(180, 180, 14, 2), meta=np.ndarray>

```

And just like that, you are connected! The output above shows an Xarray `Dataset` representing the data you are accessing. To access the rest of our catalogue, you will need to **set up authentication**.

(set-up-your-api-key)=

## Set up your API key

To access our full suite of datasets, you will need a free **API Key**.

1. **Register an account** on the {edh_url_with_camefrom}`DestinE Platform </login>`.
1. Visit the {edh_url}`API keys management section </quota-api-keys#my-personal-access-tokens>`.
1. **Copy your default API key** (or generate a new one).

```{admonition} Climate DT requires upgraded access.
---
class: warning
---
Some datasets, including the **Destination Earth Climate Adaptation Digital Twin (Climate DT)** collection, require additional permissions. See [](upgraded-access).
```

(protected-datasets)=

## Access protected datasets

Most datasets in the Earth Data Hub catalogue require your API key. Here are two ways to configure authentication:

### Option 1: Key in the URL

The quickest way to test protected data is to include your API key directly as the password in the dataset URL:

```{code-block} python
---
substitutions:
---
import xarray as xr

# Replace <your API key> with your actual key
xr.open_dataset(
    "https://edh:<your API key>@|datastore_internal_host||private_test_dataset_path|",
    chunks={},
    engine="zarr",
)
```

### Option 2: Using .netrc (Recommended)

For everyday use, we recommend **storing your API key in a hidden `.netrc` file**. This allows your Python scripts to authenticate automatically in the background without exposing your keys.

If you don't have it already, **create a file** in your home directory:

- **macOS/Linux:** `~/.netrc`
- **Windows:** `C:\Users\<username>\_netrc`

Then, **add the following lines** to the `.netrc` file:

```{code-block} text
---
substitutions:
---
machine |datastore_internal_host|
  password <your API key>

machine |datastore_host|
  password <your API key>
```

```{note}
Earth Data Hub uses multiple endpoints, so your `.netrc` file needs an entry for each one. You can retrieve your `.netrc` file directly from your {edh_url}`EDH account settings </quota-api-keys#my-personal-access-tokens>` using the {{ info_icon }} button.
```

Now, you can load protected datasets cleanly by enabling environment trust (`trust_env=True`):

```{code-block} python
---
emphasize-lines: 5
substitutions:
---
import xarray as xr

xr.open_dataset(
    "https://|datastore_internal_host||private_test_dataset_path|",
    storage_options={"client_kwargs": {"trust_env": True}},  # Auto-detect your .netrc
    chunks={},
    engine="zarr",
)
```

```{admonition} Set it up once, use it everywhere.
---
class: tip
---
Direct authentication is fine for a quick test, but using a `.netrc` file is the recommended approach. It keeps your API key out of your code, helps prevent accidental commits, and makes your scripts easier to share.
```

(upgraded-access)=

## Upgraded access

Some datasets, including the Destination Earth Climate Adaptation Digital Twin ({edh_url}`Climate DT </collections/climate-dt-2>`) collection, require upgraded access. You can easily recognise these datasets in the catalogue by their {bdg-restricted}`Restricted` badge.

For example, if you try to access a Climate DT dataset without the required permissions, your request will fail with `HTTP 403 Forbidden`.

Visit the [**Destination Earth User Access Upgrade**](https://platform.destine.eu/access-policy-upgrade/) page to check your eligibility and learn how to apply for upgraded access.

(quotas)=

## Quotas

Earth Data Hub datasets are divided into small blocks of data called **chunks**, so you only retrieve the parts of the data you need. To learn more about how chunks are organised, see [](chunking-schemes).

When you stream data on demand, each chunk is retrieved through an HTTP request behind the scenes. To keep the service fair and reliable for everyone, each user has a **monthly quota of 500,000 requests**.

That may sound like a lot, and for most workflows, it is. But if you need to access large amounts of data, the key is to **stream only the data you need** and avoid downloading the same chunks repeatedly. To reduce unnecessary requests, see [](cache-data-locally).

```{note}
Your quota resets at midnight on the **first day of each month**. You can {edh_url}`check your quota usage </quota-api-keys#quota>` at any time.
```

(cache-data-locally)=

## Cache data locally

Accessing the same dataset multiple times? **Local caching** makes repeated reads much faster and avoids downloading the same chunks again, saving both time and quota.

Before running the example, replace **`URL`** with your dataset URL and **`CACHE_STORAGE`** with your preferred cache directory.

```{code-block} python
---
emphasize-lines: 10-15
substitutions:
---
import xarray as xr

# Replace with the Earth Data Hub dataset URL you'd like to access
URL = "https://|datastore_internal_host||private_test_dataset_path|"

# Replace with the local directory you'd like to use for caching
CACHE_STORAGE = "./edh_cache/"

ds = xr.open_dataset(
    f"asyncwrapper::simplecache::{URL}",
    storage_options={
        "https": {"client_kwargs": {"trust_env": True}},
        "simplecache": {"cache_storage": CACHE_STORAGE},
        "asyncwrapper": {"asynchronous": True},
    },
    chunks={},
    engine="zarr",
)
```

Behind the scenes, caching is handled by the **fsspec** library. The `simplecache` backend is a great default for most workflows, while other caching backends provide additional features such as customisable cache expiration and size limits.

To learn more about available caching options, see the [fsspec documentation](https://filesystem-spec.readthedocs.io/en/latest/features.html#caching-files-locally).

## API reference

Under the hood, Earth Data Hub is just two open interfaces: a **STAC catalogue** to find data, and **Zarr over HTTPS** to read it. No SDK required. If your tool can make a web request, it can use Earth Data Hub.

### STAC catalogue

[STAC](https://stacspec.org/) (SpatioTemporal Asset Catalog) is a standard, searchable catalogue of Earth data. Every collection and dataset you see in the Earth Data Hub catalogue is also available as STAC metadata, starting from a single root URL: <code>{{ stac_api_url }}</code>

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

For the full list of endpoints and query parameters, see the {edh_url}`interactive STAC API documentation </api/stac/v1/api.html>`.

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

### Zarr over HTTPS

A Zarr dataset is simply a **folder of small files** on the web: a few JSON files describing the data, plus the data itself split into chunks. Each of those files has its own URL, so a plain HTTPS request is all it takes to read one.

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

For protected datasets, add your API key to the request:

```{code-block} bash
---
substitutions:
---
# Using your API key directly
curl -u edh:<your API key> https://|datastore_internal_host||private_test_dataset_path|/zarr.json

# Using your API key (with bearer auth)
curl https://|datastore_internal_host||private_test_dataset_path|/zarr.json -H "Authorization: Bearer <your API key>"

# Using your .netrc file
curl --netrc https://|datastore_internal_host||private_test_dataset_path|/zarr.json
```

```{note}
Every request counts towards your monthly quota, whichever tool you use. See [](quotas).
```
