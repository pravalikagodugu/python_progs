import sys

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    n = int(data)

    out_lines = []
    for i in range(n):
        out_lines.append(str(i * i))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()
