from itertools import permutations, product
import os
from openpyxl import load_workbook
from collections import defaultdict


"""
openpyxl library documentation
https://openpyxl.readthedocs.io/en/stable/usage.html#read-an-existing-workbook
"""

MAX_CASES_FOR_TEMPLATE = 5
VARIABLES_PATH = os.path.join('data', 'variables.xlsx')
wb = load_workbook(filename=VARIABLES_PATH, data_only=True)
sheet = wb['Sheet1']

def get_template_variables(sheet):
    columns = dict()
    for firstrow in sheet:
        for column in firstrow:
            if column.value:
                columns[column.value] = column.column_letter
        break
    # Remove unwanted columns
    columns.pop('SL No')
    return columns

def get_variable_values_from_sheet(variable_name, variable_names):
    column = sheet[variable_names[variable_name]]

    # skip first cell to ignore column name
    for cell in column[1:]:
        if cell.value:
            yield cell.value


def generate_search_string(s):
    return " ".join(s)

        
def search_queries():
    variable_names = get_template_variables(sheet)
    total_variable_names = len(variable_names)

    for n in range(2, 3):
    # for n in range(2, total_variable_names+1):
        templates = permutations(variable_names, n)
        for template in templates:
            variable_values = defaultdict(lambda: False)

            # fetch variable values

            for variable_name in template:
                variable_values[variable_name] = get_variable_values_from_sheet(variable_name, variable_names)
            
            """
            produce product of two columns
            A | 1
            B | 2  ==>  A1, B1, C1, A2, B2, C2
            C |
             
            """
            list_of_arrays = (
                    (cellvalue for cellvalue in variable_column)
                        for variable_column in variable_values.values()
            )

            searches_list = product(*list_of_arrays)

            
            case_count = 0
            for search in searches_list:
                if MAX_CASES_FOR_TEMPLATE:
                    if case_count == MAX_CASES_FOR_TEMPLATE:
                        break
                    case_count += 1
                yield generate_search_string(search)


def test_search():
    # check the above function works properly by passing some known cases
    queries_should_present = {
        # 'Puma Girls',
        'Shirts Smart Casual',
        # 'Girls Puma',
        # 'ADIDAS Boys Spring',
        # 'Puma Adults-Women Boys',
        # 'Tshirts Men SCULLERS',
        # 'Fall Peter England Adults-Women'
    }
    total_search_cases = 0
    for q in search_queries():
        total_search_cases += 1

        if q in queries_should_present:
            queries_should_present.remove(q)

    print(f'Generated test cases - {total_search_cases}')
    
    if queries_should_present:
        raise AssertionError(f'some queries are not persent in the list {queries_should_present}')
    
            

if __name__ == "__main__":
    test_search()