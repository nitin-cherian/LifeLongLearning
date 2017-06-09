# splitting_list_elements.py

print("""
{original_code}
json_data = ["abc", "bcd/chg", "sdf", "bvd", "wer/ewe", "sbc & osc"]
separators = ['/', '&', 'and']
title = []

for i in json_data:
    k = 0
    while k < len(separators):
        if separators[k] in i:
            t = i.split(separators[k])
            title.extend(t)
            break
        else:
            k += 1
        if k == 3:
            title.append(i)
print(title)
""")

# modified code - looks pythonic

json_data = ["abc", "bcd/chg", "sdf", "bvd", "wer/ewe", "sbc & osc"]
separators = ['/', '&', 'and']
title = []

for i in json_data:
    for separator in separators:
        if separator in i:
            t = i.split(separator)
            title.extend(t)
            break
    else:  # if any of the separators are not found in the data, just append it
        title.append(i)

title = [element.strip() for element in title]
print(title)


print("""
In the above code, for-else clause is used. If the 2nd for-loop exits without break, only then else part will be executed.
wrt to above example, if for-loop exits without break, it means in the current word there are no separators.
""")


