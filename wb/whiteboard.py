import re

def count_words(input_string):
    new_dict = {}
    str_split = re.findall(r"[\w]+", input_string.lower())
    for elem in str_split:
        new_dict[elem] = new_dict.get(elem, 0) + 1
    return new_dict
    
print(count_words("That's my maitre'd, Mr. Anderson!"))