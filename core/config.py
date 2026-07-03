from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application configuration.
    Automatically loads values from the .env file.
    """

    # -----------------------
    # Application
    # -----------------------

    app_name: str = "Trading Bot"
    version: str = "1.0.0"

    # -----------------------
    # Binance
    # -----------------------

    api_key: str = Field(..., alias="BINANCE_API_KEY")
    secret_key: str = Field(..., alias="BINANCE_SECRET_KEY")

    base_url: str = Field(
        "https://testnet.binancefuture.com",
        alias="BINANCE_BASE_URL",
    )

    # -----------------------
    # Logging
    # -----------------------

    log_level: str = Field("INFO", alias="LOG_LEVEL")

    log_file: str = Field(
        "logs/trading.log",
        alias="LOG_FILE",
    )

    # -----------------------
    # HTTP
    # -----------------------

    timeout: int = Field(
        10,
        alias="TIMEOUT",
    )

    # -----------------------
    # Pydantic Configuration
    # -----------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )


settings = Settings()