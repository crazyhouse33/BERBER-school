import string
import random
import sys    
    
class Data:
        
    def generate_data(size):
        data = ""
        for x in range(size):
            data += random.choice(string.hexdigits)
        return data

    data = generate_data(1000)
    print(sys.getsizeof(data))
    print(data)
