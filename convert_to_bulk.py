import json

with open("80b6fc97-aa38-46b1-bee8-a106d9b7cd96_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract docs from hits.hits
hits = data.get("hits", {}).get("hits", [])
bulk_lines = []

for doc in hits:
    _id = doc.get("_id")
    source = doc.get("_source", {})

    # Bulk action line
    bulk_lines.append(json.dumps({"index": {"_id": _id}}))
    # Document line
    bulk_lines.append(json.dumps(source))

# Write to new ndjson file
with open("bulk_data.json", "w", encoding="utf-8") as f:
    f.write("\n".join(bulk_lines) + "\n")

print(f"✅ Converted {len(hits)} documents into bulk.json")

