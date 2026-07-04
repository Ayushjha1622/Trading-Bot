import hashlib
import hmac
import time
from urllib.parse import urlencode

from core.config import settings


class BinanceAuth:
    @staticmethod
    def generate_signature(params: dict) -> str:
        query_string = urlencode(params)

        return hmac.new(
            settings.secret_key.encode("utf-8"),
            query_string.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()

    @staticmethod
    def sign(params: dict) -> dict:
        signed = params.copy()
        signed["timestamp"] = int(time.time() * 1000)
        signed["signature"] = BinanceAuth.generate_signature(
            {k: v for k, v in signed.items() if k != "signature"}
        )
        return signed

    @staticmethod
    def headers() -> dict:
        return {
            "X-MBX-APIKEY": settings.api_key,
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
        }