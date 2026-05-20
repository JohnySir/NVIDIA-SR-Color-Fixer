import cv2
import os
import random
import time
import sys

# Enable ANSI colors on Windows
if sys.platform == "win32":
    os.system('')

# 1. Create a folder for the fixed images so we don't overwrite the originals
output_folder = "Fixed_Photos"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 2. Get a list of all files in the current folder
files = os.listdir(".")

captions = [
    "🎨 Untwisting the color rainbow...",
    "🌊 Painting the sky blue again (literally)...",
    "🤫 Telling the pixels to stop being dramatic...",
    "🔄 Swapping red for blue because NVIDIA forgot how rainbows work...",
    "🏎️ Making sure your blue car doesn't look like a rusty orange...",
    "✨ De-rusting your blue photos...",
    "💆 Pixel massage in progress...",
    "🛠️ Fixing NVIDIA's 'creative' color choices...",
    "🧼 Calming down the angry orange pixels...",
    "☕ Cozy color correction incoming. Sit back and relax...",
    "📖 Teaching the red channel some manners...",
    "💎 Returning the blue to its rightful owner...",
    "🙃 Un-flipping the script...",
    "🌈 Putting the RGB back in... well, RGB...",
    "🎭 Sorting out the color identity crisis...",
    "🏡 Making the colors feel at home again...",
    "🍵 Brewing a cup of tea while the pixels settle...",
    "🦋 Turning that rusty orange back into a crisp blue...",
    "🧠 Pixels are finally going to therapy...",
    "🌍 Making the world look right again, one pixel at a time..."
]

# ANSI Color codes for a rainbow effect
COLORS = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']

# Pick a random caption and "animate" the typing with rainbow colors
caption = random.choice(captions)
for i, char in enumerate(caption):
    color = COLORS[i % len(COLORS)]
    sys.stdout.write(f"{color}{char}\033[0m")
    sys.stdout.flush()
    time.sleep(0.01)
print("\n")

for filename in files:
    # Only look for image files
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        print(f"Processing: {filename}")
        
        # Load the image
        img = cv2.imread(filename)
        
        if img is not None:
            # This swaps the Red and Blue channels back to where they belong
            # In OpenCV, this is essentially flipping BGR to RGB
            fixed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Save it into the 'Fixed_Photos' folder
            cv2.imwrite(os.path.join(output_folder, filename), fixed_img)
        else:
            print(f"Skipping {filename} - couldn't read the file.")

print("\n\033[92m✅ All done! Check the 'Fixed_Photos' folder.\033[0m")
