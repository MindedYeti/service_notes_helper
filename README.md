# Service Notes Helper
## Purpose
A lightweight automation tool that generates and copies pre-formatted service notes to the clipboard.
Built to eliminate repetitive typing in operational workflow.

## Current Features (MVP)

### Notes Helper (v1.0)
- Collects customer name, file no., and tracking number.
- Generates templated notes for 'New' and 'Returned'.
- Automatically copies the note to clipboard for quick pasting.

### Excel Generator (V2.0)
- Randomly generates **20-100 fake shipment records** using the Faker library.
- Each record includes:
    - Customer Name
    - File Number (Prefix + year + 6-digit ID)
    - File Type (randomly selected from preset list)
    - Tracking number (10-digit courier format)
- Exports results automatically to an Excel file 
## Next Steps
- Automate email generation with the Excel file attached.
- Add Power Automate integration for real-time workflow updates.


## Stack
- Python 3.13 | Panda | Faker | Pyperclip | VS Code | Git + GitHub

## Version History
|Version|Date|Description|
|**v1.0**|2025-11-01|Initial clipboard note generator MVP|
|**v2.0**|2025-11-02|Excel generator MVP - random dataset + Excel export|

*Latest update: Excel Generator MVP (2025-11-02)*