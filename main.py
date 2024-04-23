from src.image_processing import preprocess_images, extract_features
from src.similarity import calculate_similarity, save_results
from src.visualization import visualize

input_folder = "data/input/"

image1, image2 = preprocess_images(input_folder + 'image1.webp', input_folder + 'image2.jpg')
if image1 is not None and image2 is not None:
    print("Upload completed")
else:
    print("Upload failed")
    exit()


features1, features2 = extract_features(image1, image2)

similarity_res = calculate_similarity(features1, features2)
similarity_percentage = (similarity_res + 1) / 2 * 100
print("Similarity: %.2f%%" % similarity_percentage)

save_results('image1.webp', 'image2.jpg', features1, features2, similarity_percentage)



visualize((image1, image2), (features1, features2))
