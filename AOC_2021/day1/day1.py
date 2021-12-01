def read_file(file_name):
    with open(file_name) as f:
        lines = f.readlines()
    return lines


def get_sum_measurements(measurements,measurement_number,number_of_measurements_to_sum ):
    sum_measurements = 0
    print('number_of_measurements_to_sum={}'.format(number_of_measurements_to_sum))
    for i in range(0,number_of_measurements_to_sum):
        sum_measurements += int(measurements[measurement_number-i])
        print('sum_measurements={}'.format(sum_measurements))
    return sum_measurements


def is_increased(measurements, measurement_number, number_of_measurements_to_sum):
    current = get_sum_measurements(measurements,measurement_number,number_of_measurements_to_sum)
    previous = get_sum_measurements(measurements,measurement_number-1,number_of_measurements_to_sum)
    is_measurement_increased = False
    if current>previous:
        is_measurement_increased = True
    print('{measurement_number}. Check, {current} > {previous} = {is_measurement_increased}'.format(
        measurement_number=measurement_number,
        current=current,
        previous=previous,
        is_measurement_increased=is_measurement_increased
    ))
    # if is_measurement_increased:
    #     print(1)
    # else :
    #     print(0)
    return is_measurement_increased


def get_how_many_times_increased(measurements, number_of_measurements_to_sum):
    how_many_times_increased = 0
    for x in range(number_of_measurements_to_sum, len(measurements)):
        print('x={}'.format(x))
        if is_increased(measurements, x, number_of_measurements_to_sum):
            how_many_times_increased += 1
    return how_many_times_increased


def main():
    measurements = read_file('day1/day1_source.txt')
    how_many_times_increased_1 = get_how_many_times_increased(measurements, 1)
    how_many_times_increased_3 = get_how_many_times_increased(measurements, 3)
    print('It Increased {} times (Every single row)'.format(how_many_times_increased_1))
    print('It Increased {} times (3 rows)'.format(how_many_times_increased_3))


if __name__ == "__main__":
    main()
