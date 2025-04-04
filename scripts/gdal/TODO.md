# Instructions


These instruction assume you can use python gdal or gdal 
command directly.

## Exercise 1

1). Use gdal to open the vector layer `WC_NGI_TOPODATA_202006_fgdb`

2). Use `ogrinfo` to inspect and view the layers in the file geodatabase.

3). Use `ogrinfo` to inspect a subset of the dataset inside the fgdb.

4). What is the coordinate reference system of the layers.

5). Use `ogr2ogr` utility to convert a single table into the following formats

    * Geopackage
    * Geoparquet
    * Shapefile

6). Using the same utility as above convert the layers and transform
the Coordinate reference system to either the following:

* South African Lo19
* Pseudo Mercator (EPSG:3957)

7). Convert any layer and add a wkt representation of the geometry
as a new column.

