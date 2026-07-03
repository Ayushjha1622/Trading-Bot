class TradingBotError(Exception):
    """Base exception for the application."""


class ConfigurationError(TradingBotError):
    pass


class AuthenticationError(TradingBotError):
    pass


class BinanceAPIError(TradingBotError):
    pass


class ValidationError(TradingBotError):
    pass