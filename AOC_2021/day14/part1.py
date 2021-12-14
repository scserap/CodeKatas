from datetime import datetime

from AOC_2021.day1.day1 import read_file
import numpy as np



def apply_rules_to_template(template,rules):
    new_text = ''
    for i in range(len(template)-1):
        temp_chars = template[i:i + 2]
        if new_text == '': new_text = template[i:i+1]
        if len(np.where(rules[:,0]==temp_chars)[0])>0:
            new_text += rules[np.where(rules[:,0]==temp_chars)[0][0]][1]
        else:
            new_text += temp_chars
    # print(new_text)
    return new_text


def main():
    print(datetime.now())
    dataset = read_file('test_dataset.txt')
    rules = []
    template = ''
    for row in dataset:
        row = row.replace('\n', '')
        if template=='':
            template = row
        else:
            if len(row)>0:
                row = row.split(' -> ')
                rules.append([row[0],row[1]+row[0][1]])

    rules = np.array(rules)
    # print(rules)
    for k in range(10):
        # print(k)
        template = apply_rules_to_template(template,rules)
    template = np.array(list(template))
    unique, counts = np.unique(template, return_counts=True)
    result = max(counts)-min(counts)
    print('the quantity of the most common element and subtract the quantity of the least common element is {}'.format(result))
    print(datetime.now())

if __name__ == "__main__":
    main()
#
# Template:     NNCB
# After step 1: NCNBCHB
#               NCNBCHB
# After step 2: NBCCNBBBCBHCB
#               NBCCNBBBCBHCB
# After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
#               NBBBCNCCNBBNBNBBCHBHHBCHB
# After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB
#               NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB