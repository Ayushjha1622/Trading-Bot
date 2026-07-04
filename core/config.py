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
        default="https://testnet.binancefuture.com",
        alias="BINANCE_BASE_URL",
    )

    # -----------------------
    # Logging
    # -----------------------

    log_level: str = Field(
        default="INFO",
        alias="LOG_LEVEL",
    )

    log_file: str = Field(
        default="logs/trading.log",
        alias="LOG_FILE",
    )

    # -----------------------
    # HTTP
    # -----------------------

    timeout: int = Field(
        default=10,
        alias="TIMEOUT",
    )

    # -----------------------
    # Pydantic Settings
    # -----------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()