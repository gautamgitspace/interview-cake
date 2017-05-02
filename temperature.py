from collections import Counter
temp_list = []
def insert():
    temp_reading=""
    print "Enter Temperature. Type 'DONE' when done\n"
    while temp_reading!="DONE":
        temp_reading = raw_input()
        if temp_reading=="DONE":
            print "Thank you!"
        else:
            temp_list.append(float(temp_reading))
    return temp_list
def get_max():
    maxTemp = None
    for item in temp_list:
        if maxTemp==None or maxTemp < item:
            maxTemp = item
    return maxTemp
def get_min():
    minTemp = None
    for item in temp_list:
        if minTemp==None or minTemp > item:
            minTemp = item
    return minTemp
def get_mode():
    data = Counter(temp_list)
    res = data.most_common(1)
    res_more = [x[0] for x in res]
    res_more_more = " ".join(map(str, res_more))
    return res_more_more
def get_mean():
    sum_of_temp = sum(temp_list)
    length = len(temp_list)
    return sum_of_temp/length

r1 = insert()
r2 = get_max()
r3 = get_min()
r4 = get_mean()
r5 = get_mode()
print "Here's your data: ", r1
print "Max recorded temp is: ", r2
print "Min recorded temp is: ", r3
print "Mean recorded temp is:", r4
print "Mode recorded temp is: ", r5
