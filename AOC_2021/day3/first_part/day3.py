from AOC_2021.day1.day1 import read_file


def get_binary_list(report):
    binary_report = []
    for line in report:
        line = line.replace('\n', '')
        bit = [int(x) for x in str(line)]
        binary_report.append(bit)
    return binary_report


def get_rate(binary_report, gamma_or_epsilon):

    report_size = len(binary_report)
    line_size = len(binary_report[0])
    print('line_size ={}'.format(line_size))
    print('report_size ={}'.format(report_size))
    sum_bits = []
    gamma_binary = []
    for x in range(0,line_size):
        sum_bit = 0
        for i in range(0,report_size):

            sum_bit += binary_report[i][x]
        sum_bits.append(sum_bit)
        print(sum_bits)
    for sum_bit in sum_bits:
        if sum_bit>(report_size/2):
            if gamma_or_epsilon == 'gamma':
                gamma_binary.append('1')
            else:
                gamma_binary.append('0')
        else:
            if gamma_or_epsilon == 'gamma':
                gamma_binary.append('0')
            else:
                gamma_binary.append('1')

    gamma_rate = int(''.join(gamma_binary),2)
    return gamma_rate


def main():
    report = read_file('first_part/day3_input.txt')
    binary_report = get_binary_list(report)
    gamma = get_rate(binary_report,'gamma')
    epsilon = get_rate(binary_report, 'epsilon')
    print(print('gamma ={}'.format(gamma)))
    print(print('epsilon ={}'.format(epsilon)))
    power_consumption = gamma * epsilon
    print('Result = {}'.format(power_consumption))


if __name__ == "__main__":
    main()
