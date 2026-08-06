# {octicon}`download` Data Access

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
>>> import xarray as xr

>>> xr.open_dataset(
...     "https://data.earthdatahub.destine.eu/public/test-dataset-v0.zarr",
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

## Set up your API key

To access our full suite of datasets, you will need a free **API Key**.

1. **Register an account** on the [DestinE Platform](https://platform.destine.eu/).
1. **Visit your [Earth Data Hub account settings](https://earthdatahub.destine.eu/quota-api-keys#my-personal-access-tokens)**.
1. **Copy your default API key** (or generate a new one).

```{admonition} Climate DT requires upgraded access.
---
class: warning
---
Datasets in our **Destination Earth Climate Adaptation Digital Twin (Climate DT)** collection require additional permissions. If you need access, follow the [Destination Earth User Access Upgrade](https://platform.destine.eu/access-policy-upgrade/) process.
```

## Access protected datasets

Most datasets in the Earth Data Hub catalogue require your API key. Here are two ways to configure authentication:

### Option 1: Key in the URL

The quickest way to test protected data is to include your API key directly as the password in the dataset URL:

```python
import xarray as xr

# Replace <your API key> with your actual key
xr.open_dataset(
    "https://edh:<your API key>@data.earthdatahub.destine.eu/private/test-dataset-v0.zarr",
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

```text
machine data.earthdatahub.destine.eu
  password <your API key>

machine api.earthdatahub.destine.eu
  password <your API key>
```

Now, you can load protected datasets cleanly by enabling environment trust (`trust_env=True`):

```{code-block} python
---
emphasize-lines: 5
---
import xarray as xr

xr.open_dataset(
    "https://data.earthdatahub.destine.eu/private/test-dataset-v0.zarr",
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

## Cache data locally

Accessing the same dataset multiple times? **Local caching** makes repeated reads much faster and avoids downloading the same chunks again, saving both time and quota.

Before running the example, replace **`URL`** with your dataset URL and **`CACHE_STORAGE`** with your preferred cache directory.

```{code-block} python
---
emphasize-lines: 10-15
---
import xarray as xr

# Replace with the Earth Data Hub dataset URL you'd like to access
URL = "https://data.earthdatahub.destine.eu/private/test-dataset-v0.zarr"

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
