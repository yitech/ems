import pytest

# Configure pytest-asyncio default scope to avoid deprecation warning
def pytest_configure(config):
    config.addinivalue_line(
        "asyncio_default_fixture_loop_scope", "function"
    )

@pytest.fixture(scope="function")
def sample_data():
    return {
        "symbol": "AAPL",
        "price": 150.0,
        "volume": 1000
    }