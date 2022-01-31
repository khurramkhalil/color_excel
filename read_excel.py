import pandas as pd
import numpy as np
from styleframe import StyleFrame, utils


# only select cells whose character have red font, else np.nan
def only_cells_with_red_text(cell):
    return cell if cell.style.font_color in {utils.colors.red, 'FFFF0000'} else np.nan
    # return cell if not (cell.style.font_color in {utils.colors.red, 'FFFF0000'}) else np.nan


# Only select cells whose background is red, else np.nan
def only_cells_with_red_background(cell):
    return cell if cell.style.bg_color in {utils.colors.red, 'FFFF0000'} else np.nan
    # return cell if not (cell.style.bg_color in {utils.colors.red, 'FFFF0000'}) else np.nan


# Get all the sheets from the Excel file.
sheet_names = pd.ExcelFile('test_excel.xlsx').sheet_names

# Iterate through Excel sheets one by one
for sheet in sheet_names:
    # read current sheet from the Excel file
    sff = StyleFrame.read_excel('test_excel.xlsx', sheet_name=sheet, read_style=True, use_openpyxl_styles=False)

    # call both functions one by one on all sheets and print the results
    sf_1 = StyleFrame(sff.applymap(only_cells_with_red_text).dropna(axis=0, how='all'))
    print(sf_1)
    sf_2 = StyleFrame(sff.applymap(only_cells_with_red_background).dropna(axis=0, how='all'))
    print(sf_2)
