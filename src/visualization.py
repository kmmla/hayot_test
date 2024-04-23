import matplotlib.pyplot as plt

def picture(img, title):
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.show()

def histograms(features, title):
    plt.hist(features, bins=20)
    plt.title(title)
    plt.show()

def visualize(images, features):
    # Tuple unpacking to access multiple images and features
    for i, (img, feat) in enumerate(zip(images, features)):
        picture(img, f"Picture {i+1}")
        histograms(feat, f"Histogram {i+1}")