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
    - Ensures unique File Number and Tracking Number within each generated batch using sets and while-loop logic.
    - Exports results automatically to an Excel file 
## Next Steps
- Automate email generation with the Excel file attached.
- Add persistent Master ID Log to maintain uniqueness across runs.
- Add Power Automate integration for real-time workflow updates.


## Stack
- Python 3.13 | Panda | Faker | Pyperclip | VS Code | Git + GitHub

## Version History
| Version | Date | Description |
| **v1.0** | 2025-11-01 | Initial clipboard note generator MVP |
| **v2.0** | 2025-11-02 |Excel generator MVP - random dataset + Excel export |
| **v2.1** | 2025-11-04 | Added in-run uniqueness (Level 1) for File Number and Tracking Number using sets and while loops |

*Latest update: Excel Generator v2.1 - in-run uniqueness completed (2025-11-04)*