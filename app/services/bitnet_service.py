from collections import Counter

def summarize_scene(objects: list):
    # It takes in a list of detected dictionaries and tells us what and how many entities it detected.

    if not objects:
        return "No objects detected."

    # Extract object labels
    labels = [obj["label"] for obj in objects]

    counts = Counter(labels)

    # Logic for the plain english expression, if it's more than one it adds an s
    parts = []
    for label, count in counts.items():
        if count > 1:
            parts.append(f"{count} {label}s")
        else:
            parts.append(f"{count} {label}")

    # Join all detections into a summary sentence
    if len(parts) == 1:
        summary = parts[0]
    elif len(parts) == 2:
        summary = " and ".join(parts)
    else:
        summary = ", ".join(parts[:-1]) + f", and {parts[-1]}"

    return f"Detected {summary}."
