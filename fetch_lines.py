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

    with open("lines.json", "w") as f:
        f.write(response.text)

    print(f"Downloaded {len(response.text)} bytes to lines.json")


if __name__ == "__main__":
    main()
