from database.retrieve_db import create_connection


def buy_stock(stock, price, shares=1):
    conn = create_connection()
    cur = conn.cursor()
    for i in range(shares):
        cur.execute(f"INSERT INTO Portfolio (Stock, BuyPrice) VALUES ('{stock}', {price});")
    conn.commit()


def sell_stock(stock, price):
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(f"UPDATE Portfolio SET SellPrice={price} WHERE Stock='{stock}' and SellPrice is NULL;")
    conn.commit()
