---
description: Find answers to common questions and resolve issues quickly.
---

# {octicon}`question` Help & Troubleshooting

{ .lead }
Find answers to common questions and resolve issues quickly.

## FAQs

```{warning}
Work in progress.
```

## Troubleshooting

### `FileNotFoundError` or `NotImplementedError` when opening a dataset

If the dataset URL is correct but you still get one of these errors, your Zarr library may not support the **Zarr v3** format used by Earth Data Hub.

For example:

```python
FileNotFoundError: No such file or directory: 'https://data.earthdatahub.destine.eu/era5/era5-single-levels-atmosphere-daily-utc-v0.zarr'
```

```python
NotImplementedError: # V3 reading and writing is experimental! To enable support, set:
ZARR_V3_EXPERIMENTAL_API=1
```

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

To install the required Python dependencies, see [](prerequisites).
