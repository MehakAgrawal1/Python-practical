#Q3.Write a python program to Check for Key in Dictionary Value list.
test_dict = {'Simply' : [{'CS' : 5}, {'Python' : 6}], 'for' : 2, 'CS' : 3} 
 
print("The original dictionary is : " + str(test_dict)) 
 
key = "Python"
res = any(key in ele for ele in test_dict['Simply'])
 
print("Is key present in nested dictionary list ?  : " + str(res)) 
