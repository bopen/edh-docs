# {octicon}`rocket` Quick Start

## Prerequisites

```{admonition} No proprietary SDK is required.
---
class: note
---
Earth Data Hub is built on open standards with zero lock-in.
Our datasets are cloud-optimised Zarr stores accessible via HTTP using any language or library.
```

While you can connect using any language, our recommended setup uses Python and [Xarray](https://docs.xarray.dev/en/stable/).
Here is how to install the dependencies required for this quick start in your terminal:

```{code-block} bash
---
class: dark-code
---
pip install xarray "zarr>3" dask aiohttp
```

## Open a public dataset

Opening a public Earth Data Hub dataset is as simple as this:

```{code-block} pycon
>>> import xarray as xr

>>> xr.open_dataset(
...     "https://data.earthdatahub.destine.eu/public/test-dataset-v0.zarr",
...     chunks={},
...     engine="zarr",
... )
<xarray.Dataset>
```

This command opens the test dataset and displays it as an Xarray Dataset object.
Assign it to a variable, and you're ready to start exploring the data.
