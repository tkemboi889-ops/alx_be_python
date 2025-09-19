task=input("Enter a task description:")
priority=input("Enter the task priority(high,medium,low):")
time_bound=input("Is it time bound(yes or no):")
match priority:
    case "high"|"medium"|"low":
     if time_bound=="yes":
        print("Reminder: is a high priority task that requires emmediate attention today!:")
     elif time_bound=="no":
        print("Note:is a low priority task consider completing it when you have a free time:")
        
     else:
        print("time bound not identified:")
    case _:
        print("your priority is not recognized")