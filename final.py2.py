inventory = []
categories = set()

while True:
    item_name = input("Enter item name: ")
    category = input("Enter category: ").strip().lower()
    quantity = int(input("Enter quantity: "))
    
    inventory.append({"name": item_name, "category": category, "quantity": quantity})
    categories.add(category)
    
    choice = input("Do you want to add more items? (y/n): ").strip().lower()
    if choice == 'n':
        break
    print()

print("\n" + "============" + " INVENTORY SUMMARY " + "============")
print()

total_different_items = len(inventory)
item_names = [item["name"] for item in inventory]

if total_different_items > 1:
    names_str = ", ".join(item_names[:-1]) + ", and " + item_names[-1]
elif total_different_items == 1:
    names_str = item_names[0]
else:
    names_str = ""

print(f"Total Different Items: {total_different_items}")
print(f"Explanation: You entered {total_different_items} different items: {names_str}.")
print()

total_quantity = sum(item["quantity"] for item in inventory)
quantities_str = " + ".join(str(item["quantity"]) for item in inventory)
print(f"Total Quantity in Stock: {total_quantity}")
print(f"Explanation: Sum of all quantities: {quantities_str} = {total_quantity}")
print()

avg_quantity = total_quantity / total_different_items if total_different_items > 0 else 0
print(f"Average Quantity per Item: {avg_quantity}")
print(f"Explanation: Average = {total_quantity} total / {total_different_items} items")
print()

most_stocked = max(inventory, key=lambda x: x["quantity"])
print(f"Most Stocked Item: {most_stocked['name']} ({most_stocked['quantity']} units)")
print(f"Explanation: {most_stocked['name']} has the highest quantity among all items.")
print()

least_stocked = min(inventory, key=lambda x: x["quantity"])
print(f"Least Stocked Item: {least_stocked['name']} ({least_stocked['quantity']} units)")
print(f"Explanation: {least_stocked['name']} has the lowest quantity.")
print()

print("--------------------------------------------------")
print(f"Unique Categories in Inventory: {categories}")
print("Explanation: Categories are taken from user input and converted to lowercase.")
print("No duplicates are shown here.")
print()
print("--------------------------------------------------")
print()
print("📦 Items Sorted by Quantity (High to Low):")
print()

sorted_inventory = sorted(inventory, key=lambda x: x["quantity"], reverse=True)
for i, item in enumerate(sorted_inventory, 1):
    print(f"{i}. {item['name']} - {item['quantity']} units")

print()
print("Explanation: Items are sorted using the quantity field from highest to lowest.")
print()
print("--------------------------------------------------")
print()
print("📁 Categories in Alphabetical Order:")
print()

sorted_categories = sorted(list(categories))
for i, cat in enumerate(sorted_categories, 1):
    print(f"{i}. {cat}")

print()
print("Explanation: The set of unique categories was sorted alphabetically for display.")
print()
print("============ END OF REPORT ============")