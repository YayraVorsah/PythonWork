#import modules          # without the extension ( each file is a module)  NOTE THAT THE "MODULES" IS AN OBJECT AND NO CAPITAL LETTERS AT THE BEINNING

#print(modules.kg_to_lbs(70))
#from modules import kg_to_lbs

#kg_to_lbs(100)

from utils import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)


# ---- OR ------
# import utils
# utils.find_max(numbers)