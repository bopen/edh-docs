---
myst:
  html_meta:
    description lang=en: This page answers frequently asked questions about Earth Data Hub datasets, including dataset versioning, recommended versions, update schedules, and other common usage questions.
---

# {edh-octicon}`question` FAQs

{ .lead }
Find answers to common questions.

## What does the version number in the dataset URL mean?

The URL for each dataset includes a version number. For example, the `v0` at the end of the URL below indicates the dataset version:

`https://data.earthdatahub.destine.eu/era5/era5-land-v0.zarr`

Dataset versions are numbered sequentially, starting from `v0`. **A higher number indicates a more recent version.** The version number only identifies a specific version of the dataset; it does not indicate what has changed between versions or how significant the changes are.

Examples of changes between versions include:

- chunk sizes
- changes to dimensions or coordinates
- changes to dataset variables

The Earth Data Hub website always displays the URL for the **recommended version** of the dataset. We recommend using this version unless you specifically need to access an older version.

## How often are datasets updated?

Some datasets are updated regularly to include the latest data available from their original source.

The update frequency for each dataset is shown on the Earth Data Hub website in the **Update Frequency** field in the right-hand column of the dataset page.

For datasets marked as **monthly**, updates are completed **by the third week of each month**. We’re currently experimenting with more frequent updates, and some datasets marked as monthly may already be updated every two weeks.
