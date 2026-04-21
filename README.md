# 🚀 Binance Futures Trading Bot (Python CLI)

This project is a small trading bot that I built using Python to understand how trading systems interact with real-world APIs.

It works with the Binance Futures Testnet and allows placing different types of orders directly from the command line. The main focus was to keep the code clean, modular, and easy to understand while handling errors properly.

---

## ✨ What it can do

* Place MARKET orders (instant execution)
* Place LIMIT orders (custom price)
* Place STOP orders (conditional trigger)
* Supports both BUY and SELL
* Simple command-line interface
* Basic input validation
* Logs API requests and errors

---

## 🛠️ Tech used

* Python 3
* python-binance
* argparse
* logging

---

## 📁 Project Structure

trading_bot/

├── bot/
│   ├── client.py        # Handles Binance API connection
│   ├── orders.py        # Contains order logic
│   ├── validators.py    # Validates user input
│   └── logging_config.py

├── cli.py               # Entry point (CLI)
├── requirements.txt
└── README.md

---

## ⚙️ Setup

1. Clone the repo:

```id="c1"
git clone https://github.com/abhitiwari12/binance-trading-bot.git
cd binance-trading-bot
```

2. Install dependencies:

```id="c2"
pip install -r requirements.txt
```

3. Create a `.env` file and add your API keys:

```id="c3"
API_KEY=your_api_key
API_SECRET=your_api_secret
```

---

## ▶️ How to run

### MARKET Order

```id="c4"
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```id="c5"
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

### STOP Order

```id="c6"
python cli.py --symbol BTCUSDT --side BUY --type STOP --quantity 0.002 --price 80000
```

---

## 📌 Example Output

```
Order Summary:
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

Order Placed Successfully
Order ID: 13058570368
Status: FILLED
```

---

## 🧠 What I learned

* How to work with external APIs (Binance)
* Handling real-time order execution
* Structuring Python projects properly
* Writing cleaner and more modular code
* Debugging API errors and edge cases

---

## 🚧 Future ideas

* Add a simple UI (maybe Streamlit)
* Try basic trading strategies (RSI/MACD)
* Add live price tracking
* Improve logging and analytics

---

## ⚠️ Note

This project uses Binance Testnet, so no real money is involved.
It’s just for learning and experimentation.

---

## 👨‍💻 Author

Abhi Tiwari
