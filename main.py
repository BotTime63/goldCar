import json
import random
import os


def shuffle_json_media(filename):
    # 1. Check if the file exists
    if not os.path.exists(filename):
        print(f"Error: Could not find {filename}")
        return

    # 2. Read the current links
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            links = json.load(f)

        if not isinstance(links, list):
            print("Error: JSON format is not a list of links.")
            return

        print(f"Loaded {len(links)} links.")
    except Exception as e:
        print(f"Failed to read JSON: {e}")
        return

    # 3. Create a backup just in case
    backup_name = f"backup_{filename}"
    with open(backup_name, 'w', encoding='utf-8') as f:
        json.dump(links, f, indent=2)
    print(f"Backup created: {backup_name}")

    # 4. Shuffle the links
    random.shuffle(links)

    # 5. Save the shuffled links back to the file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            # indent=2 makes it pretty/readable
            json.dump(links, f, indent=2)
        print(f"Success! {filename} has been randomized.")
    except Exception as e:
        print(f"Failed to save JSON: {e}")


if __name__ == "__main__":
    # Ensure this matches your filename exactly
    shuffle_json_media("mediaNEW.json")