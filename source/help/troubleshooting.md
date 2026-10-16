---
myst:
  html_meta:
    description lang=en: This page provides solutions for common Earth Data Hub issues, including Zarr v3 compatibility, restricted dataset access, exhausted quotas, API key and authorization errors, and local cache problems.
---

# {edh-octicon}`bug` Troubleshooting

{ .lead }
Understand common errors and how to solve them.

## Zarr v3 compatibility issues

If the dataset URL is correct but you get a `FileNotFoundError` or `NotImplementedError` when opening a dataset, your Zarr library may not support the **Zarr v3** format used by Earth Data Hub.

````{dropdown} FileNotFoundError
```{code-block} python
:substitutions:
FileNotFoundError: No such file or directory: 'https://|datastore_internal_host|/era5/era5-single-levels-atmosphere-daily-utc-v0.zarr'
```
````

````{dropdown} NotImplementedError
```python
NotImplementedError: # V3 reading and writing is experimental! To enable support, set:
ZARR_V3_EXPERIMENTAL_API=1
```
````

If you are using Python, make sure you have **zarr-python 3.0** or later installed.

You can check your installed version in several ways:

````{tab-set}
---
class: outline
---
~~~{tab-item} {iconify}`vscode-icons:file-type-pypi` pip
```bash
pip show zarr
```
~~~

~~~{tab-item} {iconify}`vscode-icons:file-type-uv` uv
```bash
uv tree --package zarr --depth 0
```
~~~

~~~{tab-item} {iconify}`vscode-icons:file-type-conda` conda
```bash
conda list zarr
```
~~~

~~~{tab-item} {iconify}`vscode-icons:file-type-python` python
```python
import zarr

print(f"Zarr Version: {zarr.__version__}")
```
~~~
````

To install the required Python dependencies, see [](environment-setup).

## Restricted access

If the dataset URL and API key are correct but you receive a `ClientResponseError: 403 Forbidden`, Earth Data Hub has successfully authenticated you, but your account does not have permission to access that dataset.

Some datasets, including those in the **Destination Earth Climate Adaptation Digital Twin (Climate DT)** collection, require additional permissions.

To request access, follow the instructions in [](upgraded-access).

````{dropdown} ClientResponseError: 403 Forbidden
```{code-block} python
:substitutions:
ClientResponseError: 403, message='Forbidden', url='https://|datastore_host|/climate-dt-2/IFS-NEMO-SSP3-7.0-sfc-hourly-standard-v0.zarr/zarr.json'
```
````

## Exhausted quota

If you receive a `ClientResponseError: 429 Too Many Requests`, Earth Data Hub has successfully recognised your account, but you have used all of your available requests for the month.

You will need to wait for your quota to reset before accessing more data. To learn more about quotas and how to make the most of them, see [](quotas).

````{dropdown} ClientResponseError: 429 Too Many Requests
```{code-block} python
:substitutions:
ClientResponseError: 429, message='Too Many Requests', url='https://|datastore_internal_host|/era5/era5-single-levels-atmosphere-daily-utc-v0.zarr/zarr.json'
```
````

## API key needs to be updated

If you see the error `ClientResponseError: 426 Upgrade Required`, it means that your API key cannot be used with the API domain you are currently accessing.

This can happen if you created your API key directly on the DestinE platform and are using the {{ datastore_internal_host }} domain to access the data.

You can fix this in two ways:

1. **Create a new API key** on the {edh_url}`Earth Data Hub dedicated page </quota-api-keys#my-personal-access-tokens>`, and use the new key to access the data.
1. **Keep your current API key** and use the Earth Data Hub API domain instead: <code>https://{{ datastore_host }}</code>

````{dropdown} ClientResponseError: 426 Upgrade Required
```{code-block} python
:substitutions:
ClientResponseError: 426, message='Upgrade Required', url='https://|datastore_internal_host|/era5/era5-pressure-levels-v0.zarr/zarr.json'
```
````

## Unauthorized

If you see the error `ClientResponseError: 401, message='Unauthorized'`, the two most likely scenarios are:

1. **You are adding your token directly to the URL**: in this case check that the token you use is correct and that you are using `f-string` correctly if you do.
1. **You are using a .netrc file**: in this case, besides checking the credentials in your `.netrc` file, a common error if you use Xarray / Zarr is to forget to add the `storage_options={"client_kwargs": {"trust_env": True}}` keyword argument to force the use of that identification file.

For full instructions on how to access protected datasets and configure your credentials, see the [](protected-datasets) section.

````{dropdown} ClientResponseError: 401, message='Unauthorized'
```{code-block} python
:substitutions:
ClientResponseError: 401, message='Unauthorized', url='https://|datastore_internal_host|/private/test-dataset-v0.zarr/.zattrs'
```
````

## Debugging when using the local cache

The caching mechanism explained in the [](cache-data-locally) section can sometimes make it harder to understand what went wrong.

When using the local cache, you may get a generic error such as `GroupNotFoundError`, which doesn't necessarily tell you the actual cause of the problem. For example, you might see the following error:

````{dropdown} GroupNotFoundError
```{code-block} python
:substitutions:
GroupNotFoundError: No group found in store 'asyncwrapper::simplecache::https://edh:WRONG_API_KEY@|datastore_internal_host|/private/test-dataset-v0.zarr' at path ''
```
````

If an error occurs while using the local cache, it is recommended to try the same request **without using the cache**. This can provide a more detailed error message and help identify the cause of the problem.

The following example shows the code with the cache enabled:

```{code-block} python
---
caption: Cache enabled
emphasize-lines: 4-8
substitutions:
---
import xarray as xr

xr.open_dataset(
    "asyncwrapper::simplecache::https://edh:WRONG_API_KEY@|datastore_internal_host|/private/test-dataset-v0.zarr",
    storage_options={
        "simplecache": {"cache_storage": "./edh_cache/"},
        "asyncwrapper": {"asynchronous": True},
    },
    chunks={},
    engine="zarr",
)
```

The same request without the cache looks like this:

```{code-block} python
---
caption: Cache disabled
emphasize-lines: 4
substitutions:
---
import xarray as xr

xr.open_dataset(
    "https://edh:WRONG_API_KEY@|datastore_internal_host|/private/test-dataset-v0.zarr",
    chunks={},
    engine="zarr",
)
```
