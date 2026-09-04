# {octicon}`bug` Troubleshooting

{ .lead }
Understand common errors and how to solve them.

## Zarr v3 compatibility issues

If the dataset URL is correct but you get a `FileNotFoundError` or `NotImplementedError` when opening a dataset, your Zarr library may not support the **Zarr v3** format used by Earth Data Hub.

````{dropdown} FileNotFoundError
```python
FileNotFoundError: No such file or directory: 'https://data.earthdatahub.destine.eu/era5/era5-single-levels-atmosphere-daily-utc-v0.zarr'
```
````

````{dropdown} NotImplementedError
```python
NotImplementedError: # V3 reading and writing is experimental! To enable support, set:
ZARR_V3_EXPERIMENTAL_API=1
```
````

If you're using Python, make sure you have **zarr-python 3.0** or later installed.

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
```python
ClientResponseError: 403, message='Forbidden', url='https://api.earthdatahub.destine.eu/climate-dt-2/IFS-NEMO-SSP3-7.0-sfc-hourly-standard-v0.zarr/zarr.json'
```
````

## Exhausted quota

If you receive a `ClientResponseError: 429 Too Many Requests`, Earth Data Hub has successfully recognised your account, but you have used all of your available requests for the month.

You will need to wait for your quota to reset before accessing more data. To learn more about quotas and how to make the most of them, see [](quotas).

````{dropdown} ClientResponseError: 429 Too Many Requests
```python
ClientResponseError: 429, message='Too Many Requests', url='https://data.earthdatahub.destine.eu/era5/era5-single-levels-atmosphere-daily-utc-v0.zarr/zarr.json'
```
````
