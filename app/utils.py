import json
import os


def save_output(data, filename):

    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    path = f"outputs/{filename}.json"

    with open(path, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

    return path