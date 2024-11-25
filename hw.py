# Function to collect details of a group
def collect_group_details():
    # Taking input from the user for each attribute
    groupname = input("Enter the group name: ")
    sizeofthegroup = int(input("Enter the size of the group: "))
    dateofthecompetition = input("Enter the date of the competition (dd/mm/yyyy): ")
    venue = input("Enter the venue of the competition: ")
    typeofthemedal = input("Enter the type of medal (Gold/Silver/Bronze): ")

    # Returning as a tuple
    return (groupname, sizeofthegroup, dateofthecompetition, venue, typeofthemedal)

# List to store the details of all five groups
group_records = []

# Collecting details for five groups
for i in range(5):
    print(f"\nEnter details for Group {i+1}:")
    group_details = collect_group_details()
    group_records.append(group_details)

# Displaying the stored records
print("\nStored records for all five groups:")
for i, group in enumerate(group_records, 1):
    print(f"\nGroup {i}: {group}")
