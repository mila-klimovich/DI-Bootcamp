from menu_item import MenuItem
from menu_manager import MenuManager

item = MenuItem('Burger', 35)
item.save()
item.update('Veggie Burger', 37)
item.delete()

item2 = MenuManager.get_by_name('Beef Stew')
if item2:
    print(f"{item2.name}: {item2.price}")
else:
    print("Beef Stew not found.")

print("Listing all items...")
items = MenuManager.all_items()
print(f"Found {len(items)} items.")