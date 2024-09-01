from PIL import Image
import os

def generate_empty_frames(num_frames, base_filename):
    # Ensure the output directory exists
    os.makedirs('output', exist_ok=True)

    # Create a 1x1 transparent image
    img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))

    # Generate and save the frames
    for i in range(num_frames):
        filename = f"{base_filename}-{i}.png"
        filepath = os.path.join('output', filename)
        img.save(filepath, 'PNG')
        print(f"Generated: {filename}")

# Get user input
num_frames = int(300) #(input("Enter the number of frames to generate: "))
base_filename = input("Enter the base filename: ")

# Generate the frames
generate_empty_frames(num_frames, base_filename)

print("Frame generation complete.")