# importing Faker pkg
from faker import Faker
import random
import pandas as pd
from datetime import date
today_og = date.today()
today = today_og.strftime("%d-%m-%Y")
save_path = fr"E:\10_Month_Plan\Service_Notes_Helper\Reports\TrackingSheet_{today}.xlsx"
# any value range btwn
count = random.randint(20, 100)
prefix = "CSN"
all_file_types = ["New Order", "Return", "Cancellation", "Upgrade", "Payment Due", "Renewal"]
# generator object
fake = Faker()
#empty list
name_list = []
#loop count times
for name in range(count):
    #generating a random name using Faker's person provider
    add_name = fake.name()
    # creating a random file number
    year = random.randint(2005, 2025)
    unique_no = random.randint(1,999999)
    # combining diff aspects of file no with 6 no padding
    file_no = f"{prefix}-{year}-{unique_no:06}"
    # picking a file type randomly
    file_type = random.choice(all_file_types)
    # creating a random tracking number
    tracking_no_random = random.randint(1,9999999999)
    tracking_no = f"WC{tracking_no_random:010}"
    # creating each list inside dictionary
    record = {"Customer": add_name, "FileNumber": file_no, "FileType": file_type, "TrackingNumber": tracking_no}
    #adding random name to list
    name_list.append(record)
# How many records for the day
total_records = len(name_list)
print(f"Total Records: {total_records}")
print(f"Excel filed saved to: {save_path}")
# Creating excel file
df = pd.DataFrame(name_list)
df.to_excel(save_path, index=False)