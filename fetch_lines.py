import json

import requests


def main():
    url = "https://transcribe.akvan.dev/api/transcribed-lines"

    params = {
        "start-vol": 2,
        "start-pg": 117,
        "start-line": 1,
        "end-vol": 2,
        "end-pg": 199,
        "end-line": 5,
        "editor": "tsb",
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    with open("lines.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(data)} JSON objects to lines.json")


if __name__ == "__main__":
    main()
