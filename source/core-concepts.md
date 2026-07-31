---
description: Understand the key concepts behind Earth Data Hub and how it makes massive datasets easy to discover and use.
---

# {octicon}`light-bulb` Core Concepts

{ .lead }
Understand the key concepts behind Earth Data Hub and how it makes massive datasets easy to discover and use.

## Built on ARCO

Earth Data Hub is built on **ARCO** (**A**nalysis-**R**eady **C**loud-**O**ptimised) data. Our solution combines proven, cutting-edge technologies to make massive datasets fast, accessible, and analysis-ready.

```{list-table} The three core ingredients
---
widths: 10 10 30
header-rows: 1
---
*   - Ingredient
    - Technology
    - Purpose
*   - Object Storage
    - [DestinE Platform (OVHcloud)](https://platform.destine.eu/faq/what-cloud-resources-are-available/)
    - Cloud object storage designed for scalable access.
*   - Data format
    - [Zarr](https://zarr.dev/)
    - Stores data as small chunks that can be streamed on demand.
*   - Catalogue
    - [STAC](https://stacspec.org/)
    - Makes datasets easy to discover using a standard catalogue.
```

Traditional Earth data workflows often mean downloading large files, even when you only need a small part of the data. Earth Data Hub replaces heavy downloads with **direct cloud streaming**, delivering only the data you need, when you need it.

## Simplified access

Earth Data Hub is designed to fit into your existing workflows, not replace them. That's why we rely on open standards and familiar tools, so you don't have to learn new technologies or install bespoke software just to access Earth data.

To access any dataset, you only need two things:

```{grid} 2
---
gutter: 2
padding: 0
class-row: surface
---
~~~{grid-item-card} {octicon}`key` API key

Your credentials for authenticating access to protected datasets.
~~~

~~~{grid-item-card} {octicon}`link` Dataset URL

The address of any dataset in the catalogue.
~~~
```

Use your API key and dataset URL with your favourite programming languages and libraries, or build your own tools.

## Chunking schemes

Zarr stores datasets as small chunks that can be streamed on demand. The size and arrangement of these chunks have a major impact on performance.

These two extreme chunking schemes optimise for opposite use cases:

```{grid} 2
---
gutter: 2
padding: 0
class-row: surface
---
~~~{grid-item-card} {octicon}`stack` Map-optimised

Best for viewing maps, loading large regions, and comparing snapshots in time.
~~~

~~~{grid-item-card} {octicon}`graph` Time series-optimised

Best for analysing how variables change over time at specific locations.
~~~
```

No single chunking scheme fits every use case. We optimise each dataset for its most common access patterns and, when needed, publish multiple versions for different workflows.

```{hint}
The [Climate DT](https://earthdatahub.destine.eu/collections/climate-dt-2) high-resolution datasets are available with both map-optimised and time series-optimised chunking, so you can choose the version that best fits your workflow.
```

## Webinars

```{youtube} JV5g9XWBWfI
---
width: 100%
---
```
