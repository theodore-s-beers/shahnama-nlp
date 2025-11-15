import json


def main():
    with open("lines.json", "r", encoding="utf-8") as f:
        lines = json.load(f)

    with open("hemistichs.txt", "w", encoding="utf-8") as f:
        for line in lines:
            if "hemistichOne" not in line:
                continue

            assert "hemistichTwo" in line

            f.write(line["hemistichOne"] + "\n")
            f.write(line["hemistichTwo"] + "\n")


if __name__ == "__main__":
    main()
