def get_interval(array: list) -> list:
    """
    Get intervals.
    :param array:
    :return:
    """

    return list(zip(array[::2], array[1::2]))


def filter_intervals(array: list, lesson: list) -> list:
    """
    Filter incoming arrays if it is out of lessons time.
    :param array:
    :param lesson:
    :return:
    """

    start_lesson, end_lesson = lesson[0], lesson[1]
    filtered_array = []
    for start, end in array:
        if (start < start_lesson and end < start_lesson) or start > end_lesson:
            continue
        if start < start_lesson < end < end_lesson:
            filtered_array.append((start_lesson, end))
            continue
        if start < start_lesson < end and end > end_lesson:
            filtered_array.append((start_lesson, end_lesson))
            continue
        if start > start_lesson < end and end > end_lesson:
            filtered_array.append((start, end_lesson))
        else:
            filtered_array.append((start, end))
    return filtered_array


def appearance(pupils_intervals, tutors_intervals) -> int:
    """
    Find crossed intervals and calculate sum.
    :param pupils_intervals:
    :param tutors_intervals:
    :return:
    """

    pupils_index, tutors_index = 0, 0
    crossed_intervals = []
    while (pupils_index < len(pupils_intervals) and
            tutors_index < len(tutors_intervals)):
        pupil_in, pupil_out = (pupils_intervals[pupils_index][0],
                               pupils_intervals[pupils_index][1])
        tutor_in, tutor_out = (tutors_intervals[tutors_index][0],
                               tutors_intervals[tutors_index][1])
        if tutor_out >= pupil_in and pupil_out >= tutor_in:
            crossed_intervals.append(
                [max(pupil_in, tutor_in), min(pupil_out, tutor_out)]
            )
        if tutor_out < pupil_out:
            tutors_index += 1
        else:
            pupils_index += 1
    return sum([end - start for start, end in crossed_intervals])


def main(intervals):
    pupils_intervals = get_interval(intervals['pupil'])
    tutors_intervals = get_interval(intervals['tutor'])
    filtered_pupils_intervals = filter_intervals(pupils_intervals, intervals[
        'lesson'])
    filtered_tutors_intervals = filter_intervals(tutors_intervals, intervals[
        'lesson'])
    return appearance(filtered_pupils_intervals, filtered_tutors_intervals)


if __name__ == '__main__':
    """
    2 - ой тест падает, не понял как фильтровать эти интервалы, если это 
    таймлайн то в данных даны данные 2-х учеников, т. к. 
    1594704564, 1594705150, 1594704581, 1594704582 (вышел в 5150 и как-то 
    зашел в 4581)
    """

    tests = [
        {'data': {'lesson': [1594663200, 1594666800],
                  'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                            1594663396, 1594666472],
                  'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
         'answer': 3117
         },
        {'data': {'lesson': [1594702800, 1594706400],
                  'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                            1594704512, 1594704513, 1594704564, 1594705150,
                            1594704581, 1594704582, 1594704734, 1594705009,
                            1594705095, 1594705096, 1594705106, 1594706480,
                            1594705158, 1594705773, 1594705849, 1594706480,
                            1594706500, 1594706875, 1594706502, 1594706503,
                            1594706524, 1594706524, 1594706579, 1594706641],
                  'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                            1594705149, 1594706463]},
         'answer': 3577
         },
        {'data': {'lesson': [1594692000, 1594695600],
                  'pupil': [1594692033, 1594696347],
                  'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
         'answer': 3565
         },
    ]

    for i, test in enumerate(tests):
        test_answer = main(test['data'])
        assert test_answer == test[
            'answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
