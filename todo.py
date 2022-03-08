import csv
#print out instructions for user

print("press 1 to enter task, 2 to list task and 3 to delete task")
#prompt useri for task
option = input("enter command: ")
#save task for user
if option == "1":
    file = open("task.csv", "a")

    task = input("daily_activities: ")
    time = input("time: ")

    writer = csv.writer(file)
    writer.writerow([task, time])
    file.close()
            
    
#list task for user
elif option == "2":
    file = open("task.csv", "r")
    csv_reader = csv.reader(file)
    lists_from_csv =[]
    for row in csv_reader:
        lists_from_csv.append(row)
        
    print(lists_from_csv)
elif option == "3":
    file = open("task.csv", "r")
    csv_reader = csv.reader(file)
    lists_from_csv =[]
    for row in csv_reader:
        lists_from_csv.append(row)
        
    confirm = input("clear all task or one task?: ")
    if confirm == "all":
        file.clear
        print(lists_from_csv)
    elif confirm == ("one") or ("1"):
        print(lists_from_csv)
        remove = input("enter task to remove: ")
        if remove in lists_from_csv:
            lists_from_csv.remove(remove)
        print(lists_from_csv)