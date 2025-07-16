import requests
import json
import os
import time


def fetch_data(url, retries=3):
    """
    Fetch data from the given source, with optional retry attempts.
    """
    attempt = 0
    data = None

    while attempt < retries:
        try:
            response = requests.get(url, timeout=5)
            print("Status Code:", response.status_code)
            response.raise_for_status()
            data = response.json()

        except requests.exceptions.HTTPError as e:
            print("There's an HTTP Error", e)
            attempt += 1
            continue

        except requests.exceptions.RequestException as e:
            print("Request Error", e)
            attempt += 1
            time.sleep(2)
            continue

        except requests.exceptions.JSONDecodeError as e:
            print("Json Error.", e)

        else:
            print("Fetched Data Successfully.")
            break

        finally:
            print("Fetched Data")

    if data is None:
        raise Exception("Failed to fetch data after multiple attempts.")

    return data


def save_data(data, filename="data/data.json"):
    """
    Save the fetched data.
    """
    try:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    except IOError as e:
        print("File Write Error", e)

    else:
        print("Data saved successfully.")

    finally:
        print("Saved Data")


def main():
    """
    Main function to fetch JSON data from a given URL,
    and save it to a local file.
    """

    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        data = fetch_data(url)
        save_data(data)

    except Exception as e:
        print("Error.", e)

    finally:
        print("program runs")


if __name__ == "__main__":
    main()
