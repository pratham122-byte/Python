"""Find array elements greater than the average (fixed copy).

Run: `python arraygreaterthanavg_fixed.py` and enter numbers separated by spaces,
or press Enter to use the sample list.
"""

from typing import List


def greater_than_average(arr: List[float]) -> List[float]:
    if not arr:
        return []
    avg = sum(arr) / len(arr)
    return [x for x in arr if x > avg]


def _parse_numbers(s: str) -> List[float]:
    parts = s.strip().split()
    nums: List[float] = []
    for p in parts:
        try:
            if '.' in p:
                nums.append(float(p))
            else:
                nums.append(int(p))
        except ValueError:
            continue
    return nums


if __name__ == '__main__':
    user = input('Enter numbers separated by space (or press Enter to use sample): ')
    if user.strip():
        arr = _parse_numbers(user)
    else:
        arr = [10, 20, 30, 40, 50]

    if not arr:
        print('No valid numbers provided.')
    else:
        avg = sum(arr) / len(arr)
        greater = greater_than_average(arr)
        print(f'Array: {arr}')
        print(f'Average: {avg}')
        print(f'Elements greater than average: {greater}')
