import pandas as pd
import numpy as np
from styleframe import StyleFrame, utils


def only_cells_with_red_text(cell):
    return cell if cell.style.font_color in {utils.colors.red, 'FFFF0000'} else np.nan
    # return cell if not (cell.style.font_color in {utils.colors.red, 'FFFF0000'}) else np.nan


def only_cells_with_red_background(cell):
    return cell if cell.style.bg_color in {utils.colors.red, 'FFFF0000'} else np.nan
    # return cell if not (cell.style.bg_color in {utils.colors.red, 'FFFF0000'}) else np.nan


sheet_names = pd.ExcelFile('test_excel.xlsx').sheet_names

for sheet in sheet_names:
    sff = StyleFrame.read_excel('test_excel.xlsx', sheet_name=sheet, read_style=True, use_openpyxl_styles=False)
    sf_2 = StyleFrame(sff.applymap(only_cells_with_red_text).dropna(axis=0, how='all'))
    print(sf_2)
    sf_3 = StyleFrame(sff.applymap(only_cells_with_red_background).dropna(axis=0, how='all'))
    print(sf_3)


# sf = StyleFrame.read_excel('test_excel.xlsx', read_style=True)
# print(sf)
#
#
# sf1 = sf[[col for col in sf.columns if col.style.fill.fgColor.rgb in ('FFFFFFFF', utils.colors.white)]]
#
#

# def empty_red_background_cells(cell):
#     if cell.style.bg_color in {utils.colors.red, 'FFFF0000'}:
#         cell.value = np.nan
#     return cell
#
#
# sf_1 = StyleFrame(sff.applymap(empty_red_background_cells))
# print(sf_1)
