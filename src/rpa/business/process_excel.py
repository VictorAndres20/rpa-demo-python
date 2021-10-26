# Tests for rpa framework by
# https://rpaframework.org/
import time
from RPA.Desktop import Desktop
from RPA.Excel.Files import Files


def open_file_excel():
    desktop = Desktop()
    lib = Files()
    path = '/home/viti/RPA-ingerman/rpa-solutions/labs/Jak/cartera.xlsx'
    list_dict = []
    lib.open_workbook(path)
    try:
        list_dict = lib.read_worksheet('Octubre26')
    finally:
        lib.close_workbook()
    if len(list_dict) == 0:
        print('No se encontraron datos en el excel')
    else:
        list_dict.pop(0)
        try:
            desktop.click(f"image:/home/viti/Pictures/D&D_Cartera.png")
        except Exception as e:
            print(str(e))
            try:
                desktop.click(f"image:/home/viti/Pictures/D&D_Cartera2.png")
            except Exception as e:
                print(str(e))
                print('no se encontro la aplicacion')
        for i in list_dict:
            print(i)
            if (i['I'] == 'x' or i['I'] == 'X') and (i['H'] == '' or i['H'] is None):
                desktop.move_mouse("image:/home/viti/Pictures/ColumnB.png")
                desktop.move_mouse("offset:0,17")
                desktop.click()
                desktop.type_text(i['E'])
                desktop.press_keys("enter")
                desktop.type_text(str(i['D']))
                desktop.press_keys("enter")
                if i['B'] == 'x' or i['B'] == 'X':
                    desktop.type_text('01')
                elif i['C'] == 'x' or i['C'] == 'X':
                    desktop.type_text('02')
                desktop.press_keys("enter")
                desktop.type_text(str(i['F']))
                desktop.press_keys("enter")
                desktop.type_text(str(i['A']))
                desktop.press_keys("enter")
                desktop.type_text(str(i['G']))
                desktop.press_keys("enter")
            else:
                print('No se procesa')

