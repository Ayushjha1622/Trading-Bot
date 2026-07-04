class TradingBotException(Exception):
    """Base exception."""


class ConfigurationException(TradingBotException):
    """Configuration related errors."""


class AuthenticationException(TradingBotException):
    """Authentication failures."""


class APIException(TradingBotException):
    """API returned an error."""


class NetworkException(TradingBotException):
    """Network or timeout error."""