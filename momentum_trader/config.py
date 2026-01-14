from dataclasses import dataclass


@dataclass
class TradingConfig:
    asset: str = "<ASSET_PAIR>"  # Trading pair symbol
    price_movement_threshold: float = "<THRESHOLD>"  # Minimum price change to trigger action
    price_resolution_minutes: int = "<MINUTES>"  # Candle interval for price data
    momentum_lookback_window_minutes: int = "<MINUTES>"  # Window for momentum calculation
    momentum_std_threshold: float = "<THRESHOLD>"  # Standard deviations for signal detection
    order_size_factor: int = "<FACTOR>"  # Base order size scaling factor
    max_order_size_multiplier: int = "<MULTIPLIER>"  # Maximum order size cap
    maker_fee_rate: float = "<RATE>"  # Fee rate for limit orders
    taker_fee_rate: float = "<RATE>"  # Fee rate for market orders
    price_validation_threshold: float = "<THRESHOLD>"  # Price sanity check multiplier
    price_adjustment_offset: float = "<OFFSET>"  # Offset for limit order pricing

    @property
    def momentum_history_window_minutes(self) -> int:
        return 2 * self.momentum_lookback_window_minutes


@dataclass
class ExchangeConfig:
    base_url: str = "https://www.okx.com"
    api_prefix: str = "/api/v5"
    initial_ban_sleep_seconds: int = "<SECONDS>"  # Wait time after rate limit hit
    request_timeout_seconds: int = "<SECONDS>"  # HTTP request timeout
    max_retries: int = "<RETRIES>"  # Maximum retry attempts
    backoff_factor: float = "<FACTOR>"  # Exponential backoff multiplier


DEFAULT_TRADING_CONFIG = TradingConfig()
DEFAULT_EXCHANGE_CONFIG = ExchangeConfig()
