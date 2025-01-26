from utility import Util as u
import os

files=['Waste_generation_tracking',
       'Waste_disposal_Tracking',
       'Waste_recycle_tracking',
]


for file_name in files:
    currdirec = os.getcwd()
    parent_directory = os.path.dirname(currdirec)
    static_folder = os.path.join(parent_directory, "static/images")
    image_file_name=os.path.join(static_folder,f'{file_name}.bmp')
    full_path = os.path.join(currdirec, f'excel_templates/{file_name}.xlsx')
    u.excel_to_image(full_path,'Waste generation tracker',image_file_name)
