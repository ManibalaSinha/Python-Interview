import copy
original = [[2,1], [3,4]]
shallow = copy.copy(original)
shallow[0][0]=23
print(original)
print(shallow)
deep=copy.deepcopy(original)
deep[0][0]=99
print(original)
print(deep)