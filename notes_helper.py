# Date/Time function imported to Python
from datetime import date
# pyperclip is imported to enable copying to clipboard
import pyperclip
# pulls today's date
today_og = date.today()
# changes date format to dd mmm yy
today = today_og.strftime("%d %b %Y")
customer = input("Customer's name: ")
file_no = input("File number: ")
tracking_no = input("Tracking number: ")
note_type = input("New/Return :")
if note_type.lower() == "new":
    # print statement is stored in a variable
    new_mail_note = (f"New mail sent to {customer}\nTracking number: {tracking_no}\nDate: {today}")
    print(new_mail_note)
    # copy to clipboard
    pyperclip.copy(new_mail_note)
elif note_type.lower() == "return":
    # print statement is stored in a variable
    return_mail_note = (f"Item Returned \nTracking number: {tracking_no} \nDate: {today}.")
    print(return_mail_note)
    # copy to clipboard
    pyperclip.copy(return_mail_note)
else:
    print("Invalid input. Please enter 'new' or 'return'.")
