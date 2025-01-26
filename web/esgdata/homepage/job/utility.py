import os


class Util:
    
    @classmethod    
    def excel_to_image(cls,excel_path, sheet_name, output_image):
        import pyautogui
        import openpyxl
        import time
        from PIL import ImageGrab
        import os
        import win32com.client as win32
        from pywinauto import Application


        excel = win32.Dispatch("Excel.Application")
        excel.Visible = True
    
        # Open the workbook in read-only mode
        workbook = excel.Workbooks.Open(excel_path, ReadOnly=True)
        app = Application().connect(path="EXCEL.EXE")
        window = app.top_window()
        window.maximize()  # Maximize the Excel window

        window.set_focus()
        # Wait for Excel to open
        time.sleep(3)  # Adjust if needed
        rect = window.rectangle()
        print(f"Window Rectangle: {rect}")
    
        # Take a screenshot of only the Excel window
        screenshot = ImageGrab.grab(bbox=(rect.left, rect.top, rect.right, rect.bottom))
        screenshot.save(output_image)
    
        print(f"Screenshot saved as {output_image}")
    
        # Close the workbook and quit Excel
        workbook.Close(False)  # Close without saving changes
        excel.Quit()
