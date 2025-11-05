#calling faker pkg
from faker import Faker
import random
import pandas as pd
from datetime import date

#pulling today's date from date time
today_og = date.today()
#changing the format of the date
today = today_og.strftime("%d-%m-%Y")

#defining the save path for the excel
save_path = fr"E:\10_Month_Plan\Service_Notes_Helper\Reports\TrackingSheet_{today}.xlsx"

#generating random number of items for each file
count = random.randint(20, 100)

#random file types to generate
all_file_types = ["New Order", "Return", "Cancellation", "Upgrade", "Payment Due", "Renewal"]

# generator object
fake = Faker()

#empty list to store each item
name_list = []

# creating sets to check for uniqueness
used_file_nos = set()
used_tracking_nos = set()

# compiling as a function to prevent changing multiple parts in the while loop
def make_file_no():
    prefix = "CSN"
    year = random.randint(2005, 2025)
    generate_no = random.randint(1,999999)
    # combining diff aspects of file no with 6 no padding
    new_file_no = f"{prefix}-{year}-{generate_no:06}"
    return new_file_no

#compiling as a function to prevent changing multiple parts in the while loop
def make_tracking_no():
     # creating a random tracking number
    tracking_no_random = random.randint(1,9999999999)
    new_tracking_no = f"WC{tracking_no_random:010}"
    return new_tracking_no

#loop count times
for name in range(count):
    #generating a random name using Faker's person provider
    add_name = fake.name()
    
    #Generating a random file type
    file_type = random.choice(all_file_types)
   
    #checking for uniqueness in file no
    file_no = make_file_no()
    while file_no in used_file_nos:
        file_no = make_file_no()
    used_file_nos.add(file_no)

    #checking for uniqueness in tracking no
    tracking_no = make_tracking_no()
    while tracking_no in used_tracking_nos:
        tracking_no = make_tracking_no()
    used_tracking_nos.add(tracking_no)

    # creating each list inside dictionary
    record = {"Customer": add_name, "FileNumber": file_no, "FileType": file_type, "TrackingNumber": tracking_no}
    #adding random name to list
    name_list.append(record)
# How many records for the day
total_records = len(name_list)
print(f"Total Records: {total_records}")
print(f"Excel file saved to: {save_path}")
# Creating excel file
df = pd.DataFrame(name_list)
df.to_excel(save_path, index=False)