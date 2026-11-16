"""Shared fixtures. TODO: spark session fixture (scope='session'), gold DataFrame, silver tables, metrics spec."""
import pytest


@pytest.fixture(scope="session")
def spark():
    # TODO: from src.spark_session import get_spark; yield; stop
    pytest.skip("TODO: implement spark fixture")
