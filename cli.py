import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_price
from bot.logging_config import setup_logger
from colorama import Fore, Style, init
import traceback

init(autoreset=True)

def main():
    setup_logger()

    print(Fore.YELLOW + "🔥 Trading Bot Started...\n")

    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_price(args.type, args.price)

        client = get_client()

        print(Fore.CYAN + "📊 Order Summary:")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        print(f"Price: {args.price}")

        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print(Fore.GREEN + "\n✅ Order Placed Successfully!")

        if order:
            print(f"Order ID: {order.get('orderId', 'N/A')}")
            print(f"Status: {order.get('status', 'N/A')}")
            print(f"Executed Qty: {order.get('executedQty', 'N/A')}")

            avg_price = order.get("avgPrice") or order.get("price")
            print(f"Avg Price: {avg_price if avg_price else 'N/A'}")
        else:
            print(Fore.YELLOW + "⚠️ No response received")

    except Exception:
        print(Fore.RED + "\n❌ Error occurred:")
        traceback.print_exc()


if __name__ == "__main__":
    main()