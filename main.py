import os

excuse = "I didn't fail—I merely completed a successful demo of what not to do."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(excuse)

print(excuse)
print(f"length: {len(excuse)}")
