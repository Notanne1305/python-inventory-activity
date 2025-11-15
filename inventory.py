class InventorySystem:
    def __init__(self):
        self.item_names = []  
        self.item_prices = {}  
    
    def display_menu(self):
        """Display the main menu"""
        print("\n--- INVENTORY MENU ---")
        print("[1] Add Item")
        print("[2] Update Price")
        print("[3] Exit")
    
    def add_item(self):
        """Add a new item to inventory"""
        try:
            name = input("Enter item name: ").strip()
           
            if not name:
                print("Error: Item name cannot be empty!")
                return
            
            if name in self.item_names:
                print("Error: Item already exists in inventory!")
                return
            
            price_input = input("Enter price: ").strip()
            price = float(price_input)
            
            if price <= 0:
                print("Error: Price must be a positive number!")
                return
            
            self.item_names.append(name)
            self.item_prices[name] = price
            print("Item added successfully!")
            
        except ValueError:
            print("Error: Please enter a valid number for price!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def update_price(self):
        """Update the price of an existing item"""
        try:
            name = input("Enter item name to update: ").strip()
            
            if name not in self.item_names:
                print("Item not found in the inventory.")
                return
            
            price_input = input("Enter new price: ").strip()
            price = float(price_input)
            
            if price <= 0:
                print("Error: Price must be a positive number!")
                return
           
            self.item_prices[name] = price
            print("Price updated successfully!")
            
        except ValueError:
            print("Error: Please enter a valid number for price!")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    
    def display_inventory(self):
        """Optional: Display current inventory (for debugging)"""
        print("\nCurrent Inventory:")
        for name in self.item_names:
            print(f"  {name}: ${self.item_prices[name]}")
    
    def run(self):
        """Main program loop"""
        print("Welcome to Inventory Management System!")
        
        while True:
            try:
                self.display_menu()
                choice = input("Choice: ").strip()
                
                if choice == "1":
                    self.add_item()
                elif choice == "2":
                    self.update_price()
                elif choice == "3":
                    print("Exiting system...")
                    break
                else:
                    print("Invalid choice! Please select 1, 2, or 3.")
                    
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user. Exiting...")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    inventory_system = InventorySystem()
    inventory_system.run()