import hashlib
import hmac
from urllib.parse import urlencode

from core.config import settings


class BinanceAuth:
    @staticmethod
    def generate_signature(params: dict) -> str:
        query_string = urlencode(params)

        signature = hmac.new(
            settings.secret_key.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

        return signature