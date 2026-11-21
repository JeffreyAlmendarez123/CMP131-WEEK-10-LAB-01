#Jeffrey ALmendarez
#cmp131
#week10-lab01



def get_employees():
    num=int(input("Enter the numbers of employees:"))
    while num<1:
        num=int(input("Please enter atleast 1"))
    return num

def days_absent(num_employees):
    total=0
    for i in range(1, num_employees + 1):
        days=int(input(f"Days missed by employee{i}:"))
        while days < 0:
            days=int(input("Error, Please enter an amount {i}:"))
        total+=days
    return total

def average_day(num_employees, total_days):
    return total_days / num_employees

def main():
    employees = get_employees()
    total = days_absent(employees)
    average=average_day(employees, total)
    print(f"average day absent:{average:.2f}")
main()
