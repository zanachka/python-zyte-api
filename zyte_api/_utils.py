import aiohttp
from aiohttp import TCPConnector

from .constants import API_TIMEOUT

# 120 seconds is probably too long, but we are concerned about the case with
# many concurrent requests and some processing logic running in the same reactor,
# thus, saturating the CPU. This will make timeouts more likely.
_AIO_API_TIMEOUT = aiohttp.ClientTimeout(total=API_TIMEOUT + 120)


def create_session(connection_pool_size=100, **kwargs) -> aiohttp.ClientSession:
    """Create a session with parameters suited for Zyte API"""
    kwargs.setdefault("timeout", _AIO_API_TIMEOUT)
    if "connector" not in kwargs:
        kwargs["connector"] = TCPConnector(limit=connection_pool_size, force_close=True)
    return aiohttp.ClientSession(**kwargs)