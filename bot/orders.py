import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        order = None  # ✅ initialize to avoid crash

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity,
                newOrderRespType="RESULT"
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC",
                newOrderRespType="RESULT"
            )

        elif order_type == "STOP":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP_MARKET",
                stopPrice=price,
                quantity=quantity,
                newOrderRespType="RESULT"
            )

        else:
            raise ValueError(f"Unsupported order type: {order_type}")

        # 🔥 Now safe
        print("\n📦 Raw API Response:", order)
        logging.info(f"Order response: {order}")

        return order

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise