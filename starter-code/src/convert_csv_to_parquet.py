"""Task 1: CSV -> Parquet ingestion.

TODO: implement convert_csv_to_parquet() so that:
  - each Silver CSV export is read with an EXPLICIT schema (no inferSchema)
  - output is Parquet, Snappy-compressed, partitioned by billing_month where applicable
  - row counts match the source and the schema matches the Silver data dictionary
  - conversion throughput (rows/sec, seconds) is recorded for the Task 12 benchmark
"""

from pyspark.sql import DataFrame, SparkSession

from . import config


def get_schema(table_name: str):
    """TODO: return the explicit StructType for the table (per Silver data dictionary)."""
    raise NotImplementedError


def convert_csv_to_parquet(spark: SparkSession, table_name: str, csv_path, out_path) -> dict:
    """TODO: convert one table; return {table, rows_in, rows_out, seconds, rows_per_sec}."""
    raise NotImplementedError


def verify_conversion(spark: SparkSession, csv_path, parquet_path) -> bool:
    """TODO: confirm row count + schema parity with the source."""
    raise NotImplementedError


def main():
    """TODO: loop over billing_accounts, plan_catalog, invoices."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
