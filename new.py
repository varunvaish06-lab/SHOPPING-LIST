shopping_list = []
FILENAME = "simple_shopping_list.txt"

def clear_screen():
    """Simulates clearing the console screen."""
    print("\n" * 50)

def display_header():
    """Displays the main program header."""
    print("=" * 70)
    print(" " * 20 + "SIMPLE SHOPPING LIST ADDER")
    print("=" * 70)

def load_from_file(filename):
    """Loads previous items from a file for continuity (simple text file format)."""
    loaded_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                
                parts = line.strip().split('|')
                if len(parts) >= 2:
                    item = {
                        "name": parts[0],
                        "quantity": parts[1]
                    }
                    loaded_list.append(item)
    except FileNotFoundError:
        
        pass
    except Exception as e:
        print(f"\n[WARNING] Could not load previous list. Starting fresh. Error: {e}")
    return loaded_list

def save_to_file(shopping_list, filename):
    """Saves the current list to a file."""
    try:
        with open(filename, 'w') as file:
            for item in shopping_list:
                
                line = f"{item['name']}|{item['quantity']}\n"
                file.write(line)
        return True
    except Exception:
        return False

def add_item(shopping_list):
    """
    Prompts the user to add a new item (name and quantity).
    Handles updating quantity if the item already exists.
    """
    print("\n" + "-" * 70)
    print("ADD NEW ITEM")
    print("-" * 70)
    
    name = input("Enter item name: ").strip()
    
    if not name:
        print("\n[ERROR] Item name cannot be empty!")
        return False 
    
    
    for item in shopping_list:
        if item["name"].lower() == name.lower():
            print(f"\n[WARNING] '{name}' already exists in your list!")
            quantity = input(f"Enter additional quantity (current: {item['quantity']}): ").strip()
            
            try:
                
                current_qty = int(item['quantity']) if item['quantity'].isdigit() else 0
                new_qty_added = int(quantity) if quantity.isdigit() else 0
                item["quantity"] = str(current_qty + new_qty_added)
                print(f"\n[SUCCESS] Quantity updated for '{name}'. New total: {item['quantity']}!")
            except ValueError:
                print("\n[ERROR] Invalid quantity entered. Item not updated.")

            return True
    
    
    quantity = input("Enter quantity (default: 1): ").strip()
    if not quantity or not quantity.isdigit() or int(quantity) <= 0:
        quantity = "1"
    
    item = {
        "name": name,
        "quantity": quantity
    }
    
    shopping_list.append(item)
    print(f"\n[SUCCESS] '{name}' (x{quantity}) added to your shopping list!")
    return True 

def main():
    """The main program loop."""
    
    
    global shopping_list
    shopping_list = load_from_file(FILENAME)
    
    if shopping_list:
        print(f"\n[INFO] Loaded {len(shopping_list)} item(s) from previous session.")
        input("Press Enter to start adding items...")

    while True:
        clear_screen()
        display_header()

        
        if shopping_list:
            print("\n" + "-" * 70)
            print("CURRENT LIST:")
            print("-" * 70)
            print(f"{'Item':<30} {'Quantity':<10}")
            print("-" * 40)
            
            
            sorted_list = sorted(shopping_list, key=lambda x: x['name'].lower())
            for item in sorted_list:
                print(f"{item['name']:<30} {item['quantity']:<10}")
            print("-" * 40)
        else:
            print("\nYour list is empty. Time to add some items!")
            
        
        add_item(shopping_list)
        
        
        choice = input("\nAdd another item? (y/n, default 'y'): ").strip().lower()
        if choice == 'n':
            break

    
    if save_to_file(shopping_list, FILENAME):
        print("\n[SUCCESS] Shopping list saved successfully!")
    else:
        print("\n[ERROR] Could not save file! Your changes might be lost.")
        
    print("Thank you for using the Simple Shopping List Adder. Goodbye! 👋")

if __name__ == "__main__":
    main()