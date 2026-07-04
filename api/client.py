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
        try:
            logger.info("%s %s", method, endpoint)

            response = self.client.request(
                method=method,
                url=endpoint,
                **kwargs,
            )

            logger.info("Response Status: %s", response.status_code)

            response.raise_for_status()

            return response.json()

        except httpx.TimeoutException as exc:
            logger.exception("Request timed out")
            raise NetworkException("Request timed out") from exc

        except httpx.HTTPStatusError as exc:
            logger.exception("HTTP error")
            raise APIException(exc.response.text) from exc

    def get(self, endpoint: str, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)