import duckdb

con = duckdb.connect(database=":memory:")

duck_db_optimisations = [
    "INSTALL spatial",
    "LOAD spatial",
    "PRAGMA memory_limit='2GB'",
    "SET threads = 2",
    "SET default_order = 'ASCENDING'",
    "PRAGMA enable_progress_bar"
]

for command in duck_db_optimisations:
    con.execute(f"{command};")

sql_query = """
    CREATE TABLE maplayers AS SELECT *,ST_GeomFromText(geom) AS the_geom 
     FROM read_parquet('tran_facilities_exp_point.parquet');

"""
index_sql = "CREATE INDEX maplayersidx ON maplayers USING RTREE (geom) WITH (max_node_capacity = 16);"

describe_layer_types_sql = "DESCRIBE SELECT * FROM 'tran_facilities_exp_point.parquet';"
metadata_sql = "SELECT * FROM parquet_metadata('tran_facilities_exp_point.parquet');"

con.execute(describe_layer_types_sql)
con.sql(sql_query)
con.sql(index_sql)

con.execute("COPY maplayers TO 'maplayers.parquet' (FORMAT 'PARQUET');")
con.close()
