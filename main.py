from pandas import DataFrame

# получаем из файлика строчки и записываем их в список
def get_data(path):
    try:
        f = open(file=path, mode='r')
        arr = [x.strip('\n') for x in f]
    except FileNotFoundError:
        return 'ERROR! Path isn\'t correct'
    return arr

# берем список, символ разделения и количество столбцов.
# Разделяем строчку по сепаратору и запихиваем каждую подстроку в свой массив, который будет значением словаря
def separate_string(list, sep_sign, rows):
    dict = {a:[] for a in rows}
    try:
        for i in range(len(rows)):
            arr = []
            for string in list:
                arr.append(string.split(sep=sep_sign, maxsplit=len(rows))[i])
            dict[rows[i]] = arr
    except IndexError:
        return 'Separate sybol or amount input rows is incorrect'
    return dict

# добавляем словарь в датафрейм и создаем ексель таблицу
def fill_excel_table(dict, excel_name, sheet_name='by sotonoche'):
    try:
        df = DataFrame(dict)
        df.to_excel(f'./{excel_name}.xlsx', sheet_name=sheet_name, index=False)
    except Exception as e:
        return e

try:
    file_path = input('Введите путь до файла: ')
    separator = input('Введите разделитель: ')
    rows = [x for x in input('Введите названия колонок через пробел: ').split()]
    name_ex = input('Введите название файла: ')
    if file_path == '' or separator == '' or name_ex == '':
        raise Exception('Строчка пуста, а должно быть значение')
except Exception as e:
    print(e)

arr = get_data(path=file_path)
dict = separate_string(list=arr, sep_sign=separator, rows=rows)
fill_excel_table(dict=dict, excel_name=name_ex)
