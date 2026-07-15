# {octicon}`rocket` Quick Start

Get up and running with Earth Data Hub in just a few minutes.

## Prerequisites

```{admonition} No proprietary SDK is required.
---
class: note
---
Earth Data Hub is built on open standards with zero vendor lock-in.
Our datasets are cloud-optimised Zarr stores accessible over HTTP from any language or library that supports Zarr.
```

While you can connect using any language, our recommended setup uses Python and [Xarray](https://docs.xarray.dev/en/stable/).
Here is how to install the dependencies required for this quick start in your terminal:

```{code-block} bash
---
class: dark-code
---
pip install xarray "zarr>3" dask aiohttp
```

## Open a public test dataset

Start by opening the **public test dataset**—no credentials required.
It is ideal for exploring Earth Data Hub, becoming familiar with the data format, and setting up your workflows before accessing the full catalogue.

```{code-block} pycon
>>> import xarray as xr

>>> xr.open_dataset(
...     "https://data.earthdatahub.destine.eu/public/test-dataset-v0.zarr",
...     chunks={},
...     engine="zarr",
... )
<xarray.Dataset>
```

You have now opened your first Earth Data Hub dataset as an Xarray `Dataset`.
Most datasets require authentication, so the next step is to configure your API key.

## Set up your API key

To access the full Earth Data Hub catalogue, you will need a **Standard API Key**.

1. Register on the [DestinE Platform](https://platform.destine.eu/).
1. Open your [Earth Data Hub account settings](https://earthdatahub.destine.eu/account-settings#my-personal-access-tokens).
1. Copy your default API key or create a new one.

```{admonition} Climate DT datasets require upgraded access
---
class: warning
---
Datasets in the **Destination Earth Climate Adaptation Digital Twin (Climate DT)** collection require upgraded permissions
Follow the [Destination Earth User Access Upgrade](https://platform.destine.eu/access-policy-upgrade/) process to request access.
```

## Access protected datasets

Most datasets in the Earth Data Hub catalogue require authentication with your **Standard API Key**.

There are two ways to provide it:

1. **Add it to the dataset URL** — quick and convenient for testing.
1. **Configure a `.netrc` file** — recommended if you use Earth Data Hub regularly.

### Option 1: Add the API key to the URL

For a quick test, include your API key as the password in the dataset URL:

```{code-block} pycon
>>> import xarray as xr

>>> xr.open_dataset(
...     "https://edh:<your API key>@api.earthdatahub.destine.eu/private/test-dataset-v0.zarr",
...     chunks={},
...     engine="zarr",
... )
<xarray.Dataset>
```

### Option 2: Configure a `.netrc` file (recommended)

If you plan to use Earth Data Hub regularly, store your API key in a `.netrc` file. This lets your tools authenticate automatically without embedding credentials in every URL.

Create a file named:

- **macOS/Linux:** `~/.netrc`
- **Windows:** `C:\Users\<username>\_netrc`

with the following contents:

```text
machine api.earthdatahub.destine.eu
  password <your API key>
```

When using Xarray, enable `.netrc` support with `trust_env=True`:

```{code-block} pycon
>>> import xarray as xr

>>> xr.open_dataset(
...     "https://api.earthdatahub.destine.eu/private/test-dataset-v0.zarr",
...     storage_options={"client_kwargs": {"trust_env": True}},
...     chunks={},
...     engine="zarr",
... )
<xarray.Dataset>
```

```{admonition} Set it up once, use it everywhere
---
class: tip
---
For everyday use, we recommend configuring a `.netrc` file. It keeps your API key out of your code and works with any protected dataset URL from the Earth Data Hub catalogue.
```
