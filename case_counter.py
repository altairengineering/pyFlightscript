import json

def count_training_cases(train_file_path="train.txt"):
    """
    Reads the train.txt file and counts how many training cases have been made.
    A training case is defined as a user-assistant message pair.
    """
    with open(train_file_path, "r", encoding="utf-8") as f:
        data = f.read()
        data = data.strip()
        # Remove any trailing commas before the closing bracket (common JSON error)
        if data.endswith(",]"):
            data = data[:-2] + "]"
        # Try to parse as JSON array
        try:
            messages = json.loads(data)
        except json.JSONDecodeError as e:
            # Try to recover from common issues: trailing commas, etc.
            # Remove any trailing commas before closing array
            import re
            data_fixed = re.sub(r',\s*\]', ']', data)
            try:
                messages = json.loads(data_fixed)
            except Exception as e2:
                print("Failed to parse train.txt as JSON. Please check the file format.")
                print("Original error:", e)
                print("After attempted fix:", e2)
                return 0
        if not isinstance(messages, list):
            print("train.txt does not contain a JSON array at the top level.")
            return 0

    # Count user-assistant pairs
    count = 0
    i = 0
    while i < len(messages) - 1:
        if (
            isinstance(messages[i], dict)
            and isinstance(messages[i+1], dict)
            and messages[i].get("role") == "user"
            and messages[i+1].get("role") == "assistant"
        ):
            count += 1
            i += 2
        else:
            i += 1  # Skip to next message if not a user-assistant pair

    print(f"Number of training cases: {count}")
    return count

if __name__ == "__main__":
    count_training_cases()
