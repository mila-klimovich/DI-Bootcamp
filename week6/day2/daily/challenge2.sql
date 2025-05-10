-- Table for orders
CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE DEFAULT CURRENT_DATE
);

-- Table for items in an order
CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES product_orders(order_id) ON DELETE CASCADE,
    item_name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

INSERT INTO product_orders DEFAULT VALUES;  -- order_id = 1
INSERT INTO product_orders DEFAULT VALUES;  -- order_id = 2

-- Items for order 1
INSERT INTO items (order_id, item_name, price)
VALUES
(1, 'Laptop', 999.99),
(1, 'Mouse', 25.50),
(1, 'Keyboard', 45.00);

-- Items for order 2
INSERT INTO items (order_id, item_name, price)
VALUES
(2, 'Monitor', 150.00),
(2, 'HDMI Cable', 10.00);

-- Create a function that returns the total price for a given order.
CREATE FUNCTION get_order_total(p_order_id INT)
RETURNS NUMERIC AS $$
DECLARE
    total_price NUMERIC;
BEGIN
    SELECT SUM(price)
    INTO total_price
    FROM items
    WHERE order_id = p_order_id;

    RETURN COALESCE(total_price, 0);
END;
$$ LANGUAGE plpgsql;


SELECT get_order_total(1); 
SELECT get_order_total(2);  


