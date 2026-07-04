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

    def get(self, endpoint: str, **kwargs):
        try:
            logger.info(f"GET {endpoint}")

            response = self.client.get(endpoint, **kwargs)

            logger.info(f"Response Status : {response.status_code}")

            response.raise_for_status()

            return response.json()
        except httpx.TimeoutException as exc:
            logger.exception(exc)
            raise NetworkException("Request timed out.") from exc
        except httpx.HTTPStatusError as exc:
            logger.exception(exc)
            raise APIException(exc.response.text) from exc

    def post(self, endpoint: str, **kwargs):
        try:
            logger.info(f"POST {endpoint}")

            response = self.client.post(endpoint, **kwargs)

            logger.info(f"Response Status : {response.status_code}")

            response.raise_for_status()

            return response.json()
        except httpx.TimeoutException as exc:
            logger.exception(exc)
            raise NetworkException("Request timed out.") from exc
        except httpx.HTTPStatusError as exc:
            logger.exception(exc)
            raise APIException(exc.response.text) from exc

    def delete(self, endpoint: str, **kwargs):
        try:
            logger.info(f"DELETE {endpoint}")

            response = self.client.delete(endpoint, **kwargs)

            logger.info(f"Response Status : {response.status_code}")

            response.raise_for_status()

            return response.json()
        except httpx.TimeoutException as exc:
            logger.exception(exc)
            raise NetworkException("Request timed out.") from exc
        except httpx.HTTPStatusError as exc:
            logger.exception(exc)
            raise APIException(exc.response.text) from exc