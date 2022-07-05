def find_key_index(array, key='0'):
    return array.find(key)


def is_crossed(x1, y1, x2, y2, x3, y3, x4, y4):
    if (x1, y1, x2, y2) == (x3, y3, x4, y4):
        return True
    if x2 >= x4 or x3 >= x1 or y2 <= y3 or y4 <= y1:
        return False
    return True


def get_area(x1, y1, x2, y2, x3, y3, x4, y4):
    if is_crossed(x1, y1, x2, y2, x3, y3, x4, y4):
        right = min(x1, x4)
        top = min(y2, y4)
        left = max(x2, x3)
        bottom = max(y1, y3)
        return abs((left - right) * (top - bottom))
    raise ValueError('There is no crossed area')


if __name__ == '__main__':
    assert find_key_index('') == -1
    assert find_key_index('1') == -1
    assert find_key_index('0') == 0
    assert find_key_index('10000') == 1

    assert is_crossed(1, 1, 2, 2, 3, 3, 4, 4) is False
    assert is_crossed(2, 1, 1, 2, 0.5, 1.5, 1.5, 2.5) is True
    assert is_crossed(4, 1, 3, 4, 2, 2, 4, 3) is True
    assert is_crossed(4, 1, 3, 4, 3, 2, 5, 3) is True
    assert is_crossed(3, 0, 0, 3, 1, 0, 2, 3) is True
    assert is_crossed(4, 0, 1, 3, 2, 1, 3, 2) is True
    assert is_crossed(4, 0, 1, 3, 2, 2, 4, 3) is True
    assert is_crossed(2, 1, 1, 2, 1, 2, 2, 3) is False
    assert is_crossed(2, 1, 1, 2, 2, 1, 3, 2) is False
    assert is_crossed(2, 1, 1, 2, 2, 1, 1, 2) is True
    assert is_crossed(2, -3, 1, -0.5, 1, -2, 3, -1) is True
    assert is_crossed(-1, -3, -2, -1, -1.75, -2, -1, 0) is True

    assert get_area(2, 1, 1, 2, 1, 1, 2, 3) == 1
    assert get_area(2, 0, 1, 1, 1.5, 0, 3, 1) == 0.5
    assert get_area(2, 1, 1, 4, 0, 2, 2, 3) == 1
