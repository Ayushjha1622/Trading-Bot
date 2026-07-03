# Trading Bot

A Python-based trading bot for Binance Futures trading with command-line interface and REST API support.

## Features

- **Binance Futures Integration**: Connect to Binance Futures API (testnet and mainnet)
- **Order Management**: Place, cancel, and monitor orders
- **Position Tracking**: Real-time position monitoring
- **Account Management**: View account balance and positions
- **Logging**: Comprehensive logging for debugging and monitoring
- **Configuration Management**: Environment-based configuration with validation

## Project Structure

```
trading_bot/
├── app/
│   ├── __init__.py
│   ├── cli.py              # Command-line interface
│   ├── config.py           # Configuration management
│   ├── client.py           # Binance API client
│   ├── orders.py           # Order management logic
│   ├── validators.py       # Input validation
│   ├── logger.py           # Logging setup
│   ├── exceptions.py       # Custom exceptions
│   ├── models.py           # Data models
│   └── utils.py            # Utility functions
├── logs/                   # Application logs
├── tests/                  # Test files
├── pyproject.toml         # Project configuration
├── uv.lock                # Dependency lock file
├── README.md              # This file
├── .env                   # Environment variables
├── .env.example           # Example environment file
├── .gitignore             # Git ignore rules
└── main.py                # Entry point
```

## Requirements

- Python 3.8+
- pip or uv package manager

## Installation

### Using uv (Recommended)

```bash
# Install uv if not already installed
pip install uv

# Install dependencies
uv pip install -e .
```

### Using pip

```bash
# Install dependencies
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file based on `.env.example`:

```bash
cp .env.example .env
```

2. Add your Binance API credentials to `.env`:

```env
BINANCE_API_KEY=your_api_key_here
BINANCE_SECRET_KEY=your_secret_key_here
BINANCE_BASE_URL=https://testnet.binancefuture.com
LOG_LEVEL=INFO
```

**Important**: Never commit `.env` file to version control!

## Usage

### Command-Line Interface

```bash
# View help
python main.py --help

# Example commands
python main.py order place --symbol BTCUSDT --side BUY --type MARKET --quantity 0.1
python main.py order cancel --order-id 12345
python main.py position list
python main.py account info
```

### As a Python Module

```python
from app.config import settings
from app.client import BinanceClient

client = BinanceClient(
    api_key=settings.api_key,
    secret_key=settings.secret_key,
    base_url=settings.base_url
)

# Place an order
order = client.place_order(
    symbol="BTCUSDT",
    side="BUY",
    type="MARKET",
    quantity=0.1
)
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app
```

## Logging

Logs are stored in the `logs/` directory. Log level can be configured via the `LOG_LEVEL` environment variable (DEBUG, INFO, WARNING, ERROR, CRITICAL).

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `BINANCE_API_KEY` | Yes | - | Your Binance API key |
| `BINANCE_SECRET_KEY` | Yes | - | Your Binance secret key |
| `BINANCE_BASE_URL` | No | `https://testnet.binancefuture.com` | Binance API base URL |
| `LOG_LEVEL` | No | `INFO` | Logging level |

## Error Handling

The application validates configuration on startup and will fail fast with clear error messages if required credentials are missing.

## License

MIT

## Security Notes

⚠️ **Never commit `.env` file or API keys to version control**
- Use `.env.example` as a template for required variables
- Set appropriate API key permissions on Binance
- Consider using testnet for development and testing
