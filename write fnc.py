def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip()
    if data:
        year = int(data)
        print(is_leap(year))