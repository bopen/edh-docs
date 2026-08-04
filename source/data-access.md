# {octicon}`download` Data Access

{ .lead }
Stream data efficiently with code examples, tools, and best practices.

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
