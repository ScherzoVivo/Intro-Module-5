######################################################################
# To-Do List Script -- todo.py --
# C:\Users\Alleg\Python\UW Course\Week 5\todo.py
# Assignment 5 - Working with Dictionaries and Files
# RRoot,1.1.2030,Created starter script
# DJP -- 2021-08-01 -- Initial viewing & toying around with code
# DJP -- 2021-08-02 -- Scrapped initial attempt and started over

# Note: I *really* wanted to use JSON again for this, but that would
# have been 3x in a row and it felt weird to use the same solution each time.
######################################################################
# File handler
mainList = []
count = 1

# Read file and extract current contents
fhandle = open("ToDoList.txt", "r")
for record in fhandle:
    count += 1
    recordList = record.split(",")
    mainList.append(recordList)
fhandle.close()

# Re-open file for writing (with 'append' parameter)
fhandle = open("ToDoList.txt", "w")
######################################################################
# User input
running = True
while running:
    print("""
==================================================

Main Menu:
    1) Add Record
    2) View Records
    3) Remove Record
    4) Save Point! (Save and Exit)

==================================================
    """)

    try:
        user_input = int(input("Please select an option. [1 to 4] || "))
        if user_input not in range(1, 5):
            print("Invalid Input!")
            print("Here")
            continue

    except:
        print("Invalid Input!")
        continue

    print("\n")
######################################################################
# Add records
    if user_input == 1:
        add_id = str(count)
        add_task = input("Task Name: || ")
        print("")
        due_date = str(input("Due Date: || "))

        print("""
Select a priority for the task:
    1. High Priority
    2. Medium Priority
    3. Low Priority
    4. Oops, that should be done already...
    """)

        try:
            add_priority = int(input("Enter Priority: || "))
            if add_priority not in range(5):
                print("Here")
                print("Invalid Input!")
                continue
            add_priority = str(add_priority)

        except:
            print("Invalid Input!")
            continue

        record = [add_id, add_task, due_date, add_priority + "\n"]
####################
        #Confirm input
        print(f"\n{add_id}. || {add_task} || Due: {due_date} (Priority: {add_priority})")
        correct = input("\nIs this correct? [(Y)es/(N)o] || ").lower()

        # Append record to file
        if correct in ("y", "yes"):
            mainList.append(record)
            count += 1

        # Restart loop regardless of response
        continue
######################################################################
# View Records
    if user_input == 2:
        print("==================================================")
        print("     View Records")
        print("==================================================")

        # Apply actual name to "Priority" field for display
        for row in mainList:
            priority = int(row[3])
            if priority == 1:
                priority = "High"
            elif priority == 2:
                priority = "Medium"
            elif priority == 3:
                priority = "Low"
            else:
                priority = "Oops..."

            # Display record
            print(row[0] + ". | " + row[1] + " | Due: " + row[2] \
                            + " | Priority: " + priority)
######################################################################
# Remove Record
    if user_input == 3:
        print("==================================================")
        print("     Delete Record")
        print("==================================================")

        delete_record = input("\nEnter the ID number of the record" \
                                " you wish to remove. (Or 'Exit' to return) || ")

        # Check for exit command
        if delete_record in ("exit", "Exit", "EXIT"):
            continue

        else:
            try:
                delete_record = int(delete_record)
            except:
                print("\n Invalid Input!\n")
                continue

        # Call record and assign values
        for item in mainList:
            if str(delete_record) == item[0]:
                record_id       = item[0]
                record_task     = item[1]
                record_due      = item[2]
                record_priority = item[3]

                # Apply actual name to "Priority" field for display
                priority = int(item[3])
                if priority == 1:
                    priority = "High"
                elif priority == 2:
                    priority = "Medium"
                elif priority == 3:
                    priority = "Low"
                else:
                    priority = "Oops..."
####################
        # Confirm record to be deleted
                print(f"{record_id}. -- {record_task} || Due: {record_due} -- Priority: {priority}")
                confirmation = input("\nWould you like to delete this record? (Y)es/(N)o || ").lower()

                if confirmation in ("y", "yes"):
                    mainList.pop(int(record_id) - 1)
                elif confirmation in ("n", "no"):
                    continue
                else:
                    print("Invalid Input!")
                    continue
######################################################################
# Save and exit
    if user_input == 4:
        print("==================================================")
        print("\nSaving...\n")
        for item in mainList:
            fhandle.write(item[0] + "," + item[1] + "," + item[2] + "," + item[3])
        print("Save Successful!\n")
        input("Press any key to exit...\n")
        running = False
######################################################################
# Tidy up
fhandle.close()

# todo.py
