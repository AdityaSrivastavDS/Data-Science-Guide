#Way-1 to import user defined module
import module
print(module.sum(20,30))
print(module.mul(43,6))

#way-2 to use user defined module
#we can also import a single function also that we created in our module
from module import sum
print(sum(20,230))

#way-3 to use user definned module
#we can use alias also to use our created module like we have done below
import module as md
print(md.mul(2,6))