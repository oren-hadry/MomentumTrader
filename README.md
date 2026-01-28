## MomentumTrader

### TL;DR
A conservative, risk-aware **market-making** trading system written in Python.  
The strategy is deliberately **non-aggressive**: it does not chase price moves, reduces fees and execution costs, limits directional exposure, and remains relatively passive compared to common industry approaches — while still achieving consistent profitability.

---

## Overview

This repository contains a **demonstration / proof‑of‑concept project** showcasing the design and implementation of a conservative algorithmic trading system.

The system was run on the **OKX exchange**, trading a **single BTC‑USDT market**, with the explicit goal of **risk reduction and stability** rather than maximizing directional exposure or outperforming the underlying asset.

The project focuses on **engineering judgment** in trading systems: how execution constraints, throttling, and position sizing materially affect risk and behavior in real market conditions.

---

## The Problem

Many algorithmic trading systems implicitly rely on **market-taking behavior**: chasing price movements, reacting aggressively to momentum, and paying higher fees in exchange for immediacy.

While effective in certain regimes, these approaches typically:
- increase transaction costs and fees,
- amplify exposure to short-term price fluctuations,
- raise execution and adverse selection risk,
- tightly couple performance to market direction.

This project explores an alternative approach: a **passive, market-making execution model** that deliberately avoids chasing the market, reduces costs, and limits exposure — aiming for steady profitability through discipline rather than aggressiveness.

---

## Strategy Characteristics

Key properties of the implemented approach:

- Operates primarily as a **market maker**, not a market taker
- Does **not chase price movements** or momentum extremes
- Conservative position sizing with strict exposure limits
- Reduced fees and transaction costs through passive order placement
- Explicit throttling during extreme momentum and unstable conditions
- Execution-first design (prioritizes risk reduction over opportunity capture)
- Intentionally avoids large directional bets

Relative to common industry strategies, the system is **significantly more passive**, trading less frequently and accepting lower market participation in exchange for reduced risk and volatility — while still maintaining attractive profitability.

---

## Results Summary

The system was run continuously and evaluated over a **six-month period**, using real market data from the OKX exchange. Over this timeframe, the strategy demonstrated **stable and promising results**, validating the core design assumptions around passive execution, reduced exposure, and disciplined risk management.

## Results Summary

The system was evaluated on real market data from OKX.

Key observations:
- Strategy volatility is **significantly lower** than BTC price volatility
- Drawdowns are limited and controlled
- Profitability is driven by **execution discipline**, not directional exposure

The graphs illustrate how this design behaves under historical data for engineering insight, not to claim competitive edge or investment value. It is a systems engineering demonstration, not a production or investment strategy.

### Cumulative PnL (%) vs BTC

![Cumulative PnL % vs BTC](assets/cumulative_pnl_percent_vs_btc.png)

The strategy delivers positive absolute returns with materially lower variance than BTC itself. During strong directional moves, it intentionally underperforms the benchmark, reflecting its conservative design.

### Cumulative PnL (USD)

![Cumulative PnL (USD)](assets/cumulative_pnl_usd.png)

The cumulative PnL curve shows steady, incremental profit generation with limited drawdowns, supporting the hypothesis of reduced market‑direction dependency.

---

## Architecture

The system is structured around a single trading loop with clear separation of concerns between strategy logic, execution, state management, and external exchange interaction.

```
┌────────────────────────────────────────────────────────────────────────────┐
│                              TradingBot                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         Trade Logic Loop                            │   │
│  │  1. Fetch price → 2. Calculate momentum → 3. Check extreme momentum │   │
│  │  │  4. Check order status → 5. Place new orders → 6. Sleep & repeat │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└───────────────┬─────────────────────────┬───────────────────────┬──────────┘
                │                         │                       │
                ▼                         ▼                       ▼
┌───────────────────────┐   ┌─────────────────────┐   ┌───────────────────────┐
│    ExchangeClient     │   │    WalletManager    │   │       Loggers         │
│    (Abstract Base)    │   │                     │   │                       │
├───────────────────────┤   ├─────────────────────┤   ├───────────────────────┤
│ • get_price()         │   │ • check_order_size()│   │ • Logger (app.log)    │
│ • place_order()       │   │ • update_executed   │   │ • PriceLogger         │
│ • check_order_status()│   │   _order()          │   │ • OrderLogger         │
│ • cancel_order()      │   │ • Balance tracking  │   │                       │
│ • get_account_balance │   │                     │   │                       │
└───────────┬───────────┘   └─────────────────────┘   └───────────────────────┘
            │
            ▼
┌───────────────────────┐
│      OKXClient        │
│   (Implementation)    │
├───────────────────────┤
│ • API authentication  │
│ • Request signing     │
│ • Rate limit handling │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│      APIClient        │
├───────────────────────┤
│ • HTTP session        │
│ • Retry logic         │
│ • Error handling      │
└───────────┬───────────┘
            │
            ▼
    ┌───────────────┐
    │   OKX API     │
    └───────────────┘
```

---

## What This Project Is NOT

- Not a production‑ready trading bot
- Not an optimized or profit‑maximizing strategy
- Not a multi‑asset or high‑frequency system

The emphasis is on **risk‑aware system design and execution discipline**, not financial performance claims.

---

## Intended Audience

This project is intended for:
- Engineers evaluating system design and execution trade‑offs
- Technical interview discussions
- Demonstration of disciplined decision‑making under uncertainty

It should be read as a **systems engineering exercise**, not an investment product.

---

## Disclaimer

This project is for educational and demonstration purposes only. Cryptocurrency trading involves significant risk of loss. Use at your own risk.

