from itertools import combinations
from itertools import permutations
from openpyxl import load_workbook

loc_variable = "D://Reverie-20210804T085618Z-001//Reverie//Selenium//variable.xls"
loc_react_test_case = "D://Reverie-20210804T085618Z-001//Reverie//Selenium//react test cases.xls"

wb = xlrd.open_workbook(loc_variable)
sheet_variable = wb.sheet_by_index(0)

attributes = ["gender", "article", "season"]

templates_with_two_attribute = permutations(attributes, 2)

templates_with_three_attribute = permutations(attributes, 3)
templates_with_four_attribute = permutations(attributes, 4)
templates_with_five_attribute = permutations(attributes, 5)
templates_with_six_attribute = permutations(attributes, 6)
templates_with_seven_attribute = permutations(attributes, 7)

# Print the obtained permutations
count = 0
for i in list(templates_with_two_attribute):
	print (i)
	count = count + 1

print(count)
