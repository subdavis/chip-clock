def as_digits(number, min_digits):
    """
    break a positive number into an array of digits
    1244    -> [1, 2, 4, 4]
    0       -> [0]
    -222999 -> [-222999]
    """
    n = number
    arr = []
    while n >= 10:
      arr.append(n % 10)
      n = round(n) // 10
    arr.append(round(n))
    if len(arr) < min_digits:
      for i in range(min_digits - len(arr)):
        arr.append(0)
    return list(reversed(arr))
