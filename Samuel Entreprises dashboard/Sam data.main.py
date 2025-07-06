import random

def generate_data():
  """Generates 50 rows of data."""
  data = []
  for i in range(50):
    pants_start_stock = random.randint(10, 100)
    t_shirt_start_stock = random.randint(10, 100)
    shorts_start_stock = random.randint(10, 100)
    pants_stock_received = random.randint(1, 10)
    t_shirts_stock_received = random.randint(1, 10)
    shorts_stock_received = random.randint(1, 10)
    pants_sales = random.randint(1, 10)
    t_shirt_sales = random.randint(1, 10)
    shorts_sales = random.randint(1, 10)
    data.append([pants_start_stock, t_shirt_start_stock, shorts_start_stock,
                  pants_stock_received, t_shirts_stock_received, shorts_stock_received,
                  pants_sales, t_shirt_sales, shorts_sales])
  return data
print (data)


