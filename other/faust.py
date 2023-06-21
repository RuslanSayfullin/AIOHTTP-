import faust

app = faust.App('myapp', broker='kafka://localhost')

class Order(faust.Record):
    account_id: str
    product_id: str
    price: float
    quantity: int

order_topic = app.topic('orders', value_type=Order)

@app.agent(order_topic)
async def process_order(orders):
    async for order in orders:
        total = order.price * order.quantity
        print(f'Order total for {order.account_id}: {total}')
