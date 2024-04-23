import numpy as np
import pandas as pd

def calculate_similarity(hog_features1, hog_features2):

    if hog_features1 is None or hog_features2 is None:
        raise ValueError("No features found in the image.")
    
    hog_features1 = np.array(hog_features1)
    hog_features2 = np.array(hog_features2)
    
    hog_features1_normalized = hog_features1 / np.linalg.norm(hog_features1)
    hog_features2_normalized = hog_features2 / np.linalg.norm(hog_features2)

    
    similarity = np.dot(hog_features1_normalized, hog_features2_normalized)

    return similarity

def save_results(image1, image2, features1, features2, similarity_percentage):
    # Create pandas DataFrame
    df = pd.DataFrame([[str(image1), str(image2), str(features1), str(features2), similarity_percentage]], 
                        columns = ['Image1','Image2', 'HOG_Features1', 'HOG_Features2', 'Similarity'])

    df.to_csv('data/output/results.csv', index=False)
