import hashlib
import hmac
from typing import Dict


def generate_signature(params: Dict[str, str], secret_key: str) -> str:
    query_string = "&".join(f"{key}={value}" for key, value in sorted(params.items()))
    return hmac.new(secret_key.encode(), query_string.encode(), hashlib.sha256).hexdigest()
