# {octicon}`rocket` Getting Started

```{attention}
This page is not intended for the documentation. It serves as a guideline for defining the content of the portal’s [Getting Started](https://earthdatahub.destine.eu/getting-started) section.
```

{ .lead }
Get up and running with Earth Data Hub in just a few minutes.

## 1. Set up your environment

For the best experience, we recommend using **Python** with **Xarray**.

To install the required packages, run this command in your terminal:

```bash
pip install xarray "zarr>3" dask aiohttp
```

## 2. Open your first dataset

To access a dataset, you only need **two things**: its URL and your [personal API key](https://earthdatahub.destine.eu/quota-api-keys#my-personal-access-tokens).

Every dataset in the [EDH Catalogue](https://earthdatahub.destine.eu/catalogue) includes a ready-to-use code snippet like the one below.

If you're signed in to the Earth Data Hub, click the {octicon}`eye` icon in the snippet to automatically insert your API key. Then copy, paste, and run the snippet.

```python
import xarray as xr

xr.open_dataset(
    # Replace <YOUR_API_KEY> with your API key
    "https://edh:<YOUR_API_KEY>@data.earthdatahub.destine.eu/private/test-dataset-v0.zarr",
    chunks={},
    engine="zarr",
)
```

That's it. You now have an Xarray `Dataset` ready to stream data directly into your workflows.

## 3. Go further

You're ready to start crunching data.

Before diving in, we recommend exploring the [](data-access) section in the EDH documentation. You'll find practical examples, performance tips, and best practices, including how to:

- Access restricted datasets (e.g., Climate DT)
- Store your API key securely in a `.netrc` file
- Speed up repeated reads with local caching
- And much more

```{admonition} Avoid downloading entire datasets.
---
class: caution
---
Earth Data Hub is designed for **on-demand streaming**. Avoid downloading entire datasets: many are massive, and you may exceed your quota before getting useful results.
```
