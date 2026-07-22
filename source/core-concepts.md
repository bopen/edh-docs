---
description: Understand the key concepts behind Earth Data Hub and how it makes massive datasets easy to discover and use.
---

# {octicon}`light-bulb` Core Concepts

Traditional Earth data workflows often mean downloading large files such as NetCDF and GRIB archives, even when you only need a small part of the data. Earth Data Hub replaces heavy downloads with **direct cloud streaming**, delivering only the data you need, when you need it.

## Built on ARCO

Earth Data Hub is built on **ARCO** (**A**nalysis-**R**eady **C**loud-**O**ptimised) data. Our solution builds on proven open technologies. Here are the three key ingredients that make it possible.

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
    - Reliable cloud object storage designed for scalable access.
*   - Data format
    - [Zarr](https://zarr.dev/)
    - Stores datasets as small chunks that can be streamed on demand.
*   - Catalogue
    - [STAC](https://stacspec.org/)
    - Makes datasets easy to discover using a standard catalogue.
```

## Simplified access

Earth Data Hub is designed to fit into your existing workflows, not replace them. That's why we rely on open standards and familiar tools, so you don't have to learn new technologies or install bespoke software just to access Earth data.

To access any dataset, you only need two things:

```{eval-rst}
.. grid:: 2
   :gutter: 3

   .. grid-item-card:: :octicon:`key` API key

      Your credentials for authenticating access to protected datasets.

   .. grid-item-card:: :octicon:`link` Dataset URL

      The address of any dataset in the catalogue.
```

Use your API key and dataset URL with your favourite programming languages and libraries, or build your own tools.

## Webinars

```{youtube} JV5g9XWBWfI
---
width: 100%
---
```
