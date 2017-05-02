#!/usr/bin/env python
#string compression algorithm O()
def compression(str_raw):
    tokens = []
    count = 1
    result = str()
    final_str = str()
    for alphabet in str_raw:
        tokens.append(alphabet)
    init_comparator = tokens[0]
    for item in tokens[1:len(str_raw)]:
        if item == init_comparator:
            count +=1
        else:
            result = result+init_comparator+str(count)
            init_comparator = item
            count = 1
    final_str = result+init_comparator+str(count)
    if len(str_raw) <= len(final_str):
        return str_raw
    else:
        return final_str

str_raw = raw_input('Enter a string: ')
print compression(str_raw)
