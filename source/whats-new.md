---
myst:
  html_meta:
    description lang=en: This page highlights recent updates and changes to the platform.
---

# {edh-octicon}`megaphone` What's new

{ .lead }
Stay up to date with the latest Earth Data Hub changes.

(copernicus-dem-v1)=

## Copernicus DEM version 1 (2026-10-16)

Version 1 of the global Copernicus DEM datasets, **GLO-30** and **GLO-90**, is now available. The elevation values are unchanged, but the stores are now north-up Zarr v3 with a declared CRS, so they work directly with GDAL. Version 0 remains available to existing users until the end of 2026.

### Breaking changes

- Latitudes run from north to south (north-up); version 0 was south-up.
- The Zarr format is v3 instead of v2.
- GLO-30 only: the duplicated 180° meridian column is gone, and longitudes span `[-180, 180)`.

### Bug fixes

- The `EPSG:9518` compound CRS (WGS 84 + EGM2008 height) is declared in both CF and GDAL form; version 0 of GLO-90 declared none.

### Performance

- GLO-30 chunks are 0.5° × 1° instead of 1° × 1°, so small-window reads download less data.

(copernicus-dem-v1-migration)=

### Migrating from version 0

1. Use zarr-python 3 (`pip install "zarr>=3"`) or GDAL 3.8 or newer.

1. Replace `-v0.zarr` with `-v1.zarr` in the store URLs.

1. Reverse latitude slices: the bounds now go from north to south. A slice in the old order returns an empty selection, _silently_:

   ```python
   rome = ds.dsm.sel(lat=slice(41.8, 42.0), lon=slice(12.4, 12.6))  # v0 south-up
   rome = ds.dsm.sel(lat=slice(42.0, 41.8), lon=slice(12.4, 12.6))  # v1 north-up
   ```

1. Review code that relies on array positions: row 0 is now the northern edge, and GLO-30 has one fewer longitude column.
