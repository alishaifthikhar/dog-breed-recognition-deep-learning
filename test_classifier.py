from classifier import classifier

# Test with an example image and model
image_path = "pet_images/dog_01.jpg"  # Replace with an actual image path
model_name = "vgg"  # Can be 'resnet', 'alexnet', or 'vgg'

try:
    result = classifier(image_path, model_name)
    print(f"Classifier Result: {result}")
except Exception as e:
    print(f"Error: {e}")
