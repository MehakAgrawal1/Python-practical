#Q5.Write a python program to find dictionary Keys Product.
test_dict1 = {'gfg' : 6, 'is' : 4, 'best' : 7}
test_dict2 = {'gfg' : 10, 'is' : 6, 'best' : 10}
 
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))
 
res = {key: test_dict2[key] * test_dict1.get(key, 0)for key in test_dict2.keys()}
 
print("The product dictionary is : " + str(res))
