dict1 = {'Name':'Ramakrishna','Age':25}
dict2 = {'EmpId':1234,'Salary':5000}
dict1.update(dict2)
dict3 = dict(dict1)
print("New dictionary created from dict1 and dict2: " + str(dict3))


dict3.update({"Salary":5500})
dict3.update({"Age":26})
dict3.update({'Grade':'B1'})
print("Salary and age updated, grade added:")
print(str(dict3))
dict3.pop('Age',None)
print("Dictionary with Age removed:")
print(str(dict3))
