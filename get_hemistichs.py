import json


def main():
    with open("lines.json") as f:
        lines = json.load(f)

    with open("hemistichs.txt", "w") as f:
        for line in lines:
            if "hemistichOne" not in line or "hemistichTwo" not in line:
                continue

            f.write(line["hemistichOne"] + "\n")
            f.write(line["hemistichTwo"] + "\n")


if __name__ == "__main__":
    main()
