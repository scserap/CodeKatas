from AOC_2021.day1.day1 import read_file


def get_binary_list(report):
    binary_report = []
    for line in report:
        line = line.replace('\n', '')
        bit = [int(x) for x in str(line)]
        binary_report.append(bit)
    return binary_report


def get_rate(binary_report, oxygen_or_CO2):
    line_size = len(binary_report[0])
    print('line_size ={}'.format(line_size))
    for x in range(0,line_size):
        print('bit number ={}'.format(x))
        sum_bit = 0
        for i in range(0,len(binary_report)):
            sum_bit += binary_report[i][x]
        print('sum_bit ={}'.format(sum_bit))

        if sum_bit >= (len(binary_report) / 2):
            if oxygen_or_CO2=='oxygen':
                criteria_bit = 1
            else:
                criteria_bit = 0
        else:
            if oxygen_or_CO2=='oxygen':
                criteria_bit = 0
            else:
                criteria_bit = 1

        print('criteria_bit={}'.format(criteria_bit))
        temporary_report=[]
        for line in binary_report:
            if line[x]==criteria_bit :
                temporary_report.append(line)
                print('line[{}] = {} ({})'.format(x, line[x], line))
                print('oxygen_or_CO2= {}'.format(oxygen_or_CO2))

            print('len(temporary_report)= {}'.format(len(temporary_report)))
            print('len(binary_report)= {}'.format(len(binary_report)))
        if len(temporary_report)>0: binary_report = temporary_report
    string_binary_report = [str(int_bit) for int_bit in binary_report[0]]
    rate = int(''.join(string_binary_report), 2)
    print('{} - {}'.format(oxygen_or_CO2, rate))
    return rate


def main():
    report = read_file('day3_input.txt')
    binary_report = get_binary_list(report)
    oxygen = get_rate(binary_report,'oxygen')
    CO2 = get_rate(binary_report, 'CO2')
    print('oxygen ={}'.format(oxygen))
    print('CO2 ={}'.format(CO2))
    life_support_rating = oxygen * CO2
    print('life_support_rating = {}'.format(life_support_rating))
# oxygen =1161
# CO2 =3621
# life_support_rating = 4203981


if __name__ == "__main__":
    main()
