import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook


class Util:
    
    @classmethod    
    def excel_to_image(excel_path, sheet_name, output_image):
        # Load Excel file
        workbook = load_workbook(excel_path, data_only=True)
        sheet = workbook[sheet_name]
    
        # Read Excel sheet into a DataFrame
        data = sheet.values
        columns = next(data)  # Get the first row as column names
        df = pd.DataFrame(data, columns=columns)
    
        # Plot the DataFrame as a table
        fig, ax = plt.subplots(figsize=(10, len(df) * 0.5))  # Adjust figure size
        ax.axis('off')  # Hide the axis
        table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    
        # Adjust table properties
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.auto_set_column_width(col=list(range(len(df.columns))))
    
        # Save the figure as an image
        plt.savefig(output_image, bbox_inches='tight', dpi=300)
        plt.close()
    
        print(f"Excel sheet saved as image: {output_image}")
