import time

import httpx

from core.config import settings
from core.exceptions import APIException, NetworkException
from core.logger import Logger

logger = Logger.get_logger(__name__)


class HttpClient:
    def __init__(self):
        self.client = httpx.Client(
            base_url=settings.base_url,
            timeout=settings.timeout,
        )

    def _request(self, method: str, endpoint: str, **kwargs):
        for attempt in range(3):
            try:
                logger.info("%s %s", method, endpoint)
                logger.info("Request Sent")

                response = self.client.request(
                    method=method,
                    url=endpoint,
                    **kwargs,
                )

                logger.info("Status %s", response.status_code)

                response.raise_for_status()

                return response.json()

            except httpx.TimeoutException as exc:
                logger.exception("Request timed out")
                raise NetworkException("Request timed out") from exc

            except httpx.HTTPStatusError as exc:
                logger.exception("Request failed")
                if exc.response.status_code >= 500 and attempt < 2:
                    logger.warning("Retrying request after server error (attempt %s/3)", attempt + 1)
                    time.sleep(2)
                    continue
                if exc.response.status_code >= 500:
                    raise APIException(
                        "Binance Testnet server is temporarily unavailable. Please try again."
                    ) from exc
                raise APIException(exc.response.text) from exc

    def get(self, endpoint: str, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)