from datetime import datetime, date

today = date.today()
print(today)
reminder = {}

print("Welcome to the To DO List\nHere you can add your daily task with their time.")

choice = "y"

while choice == "y":
    task = input("Please enter the task: ")
    date = input("Set date(YYYY-MM-DD): ")

    try:
        user_date = datetime.strptime(date , "%Y-%m-%d").date() #.date will extract the date part

        if user_date < today:
            print("Cannot set the date in past!")
            date = input("Please enter the date in present or future(YYYY-MM-DD): ")
        elif user_date >= today:
            reminder[task] = user_date
            delta = user_date - today
            print(f"Your task: {task}.")
            print("You have {} to complete the task".format(delta.days))
    except:
        print("Invalid format")

    choice = input("Do you want to enter another task?(y/n): ")
    choice = choice.lower()

print("Here is your lists of tasks!")

def display_list():
    print()
    for tasks , date_str in sorted(reminder.items() , key=lambda x: x[1]):
        rem_days = (date_str - today).days
        print(f"Task: {tasks}.")
        print(f"Last date: {date_str}")
        print(f"Total days remaining: {rem_days}.\n")
        print()

display_list()

delete = "y"

while delete == "y":
    del_choice = input("Do you want to delete any task?(y/n): ")
    if del_choice == "y":
        task_to_del = input("Enter the task to delete: ")
        if task_to_del in reminder:
            del reminder[task_to_del]
            print("Task deleted.\n")
            print("Updated list")
            print()
            display_list()




