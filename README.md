# Overview of the Project
The Simple Shopping List Adder is a console-based Python application designed to help users quickly create and manage a basic shopping list. The application provides persistence by saving the list to a simple text file (simple_shopping_list.txt) between sessions. Its core functionality revolves around adding new items and managing quantities, automatically updating the quantity of an item if it's already present in the list.

# ✨ Features
List Persistence: Automatically loads the previous list from simple_shopping_list.txt when the program starts and saves the updated list when the program exits.

 Quantity Management: If a user attempts to add an item that already exists, the program prompts for an additional quantity and adds it to the current total, effectively preventing duplicate entries.

 Structured Display: Presents the current shopping list in a clear, formatted, and alphabetically sorted table for easy reading.

 Simple Data Structure: Each item is stored internally as a Python dictionary containing the item's name and quantity.

 User Interaction: Uses a continuous loop for adding multiple items and clears the console screen between interactions for a cleaner user experience.

# 🛠️ Technologies/Tools Used
Category	Technology/Tool	Purpose
Language	Python 3	Core language for application logic and scripting.
Data Structure	Dictionary (Python dict)	Used to represent individual list items (Name/Quantity pairs).
Persistence	Built-in open()	Used for reading from and writing to the persistent text file (.txt).
Environment	Command Line/Console	The primary interface for running and interacting with the application.

Export to Sheets

# 🚀 Steps to Install & Run the Project
This is a single-file Python script, requiring no external libraries, making installation very simple.

1. Save the Code
Create a new file named shopping_list.py.

Paste the entire provided Python code into this file.

2. Run the Application
Open your terminal or command prompt.

Navigate to the directory where you saved shopping_list.py.

Execute the script using the Python interpreter:

Bash

python shopping_list.py
3. Interaction
The program will guide you through the process:

It displays the current list (or an empty message).

It then prompts you to Enter item name.

After the name, it asks for the quantity (defaults to 1 if left blank).

After each item addition, it asks: Add another item? (y/n). Type n to save your list and exit, or y (or press Enter) to continue adding items.

# ✅ Instructions for Testing
Run the program and perform the following test cases to verify core functionality:

Test Case	Steps	Expected Result
First Item Addition	
1. Run the program.


2. Add "Milk" with quantity "2".


3. Enter 'n' to quit.

"[SUCCESS] 'Milk' (x2) added..." message appears.


The file simple_shopping_list.txt is created containing `Milk

Quantity Update	
1. Re-run the program (Milk x2 is loaded).


2. Try to add "Milk" again with additional quantity "1".

[WARNING] message appears, prompting for additional quantity.


[SUCCESS] message confirms New total: 3.

Empty Quantity Input	
1. Add "Bread".


2. When prompted for quantity, just press Enter.

The quantity defaults to 1.


The list shows "Bread x1".

Persistence Check	
1. Ensure the list contains items (e.g., Milk x3, Bread x1).


2. Enter 'n' to quit.


3. Re-run the program.

[INFO] message confirms the number of items loaded from the previous session.


The CURRENT LIST displays all items correctly.

Input Case Insensitivity	
1. List contains "APPLES" (all caps).


2. Try to add "apples" (lowercase) with quantity "1".

The item "APPLES" in the list has its quantity updated, confirming that item names are matched regardless of casing.

Export to Sheets

If you want to enhance your project, you might consider adding a menu system to include functions like deleting or editing items!
