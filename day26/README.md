# Image Classifier for Mood Detection

This TensorFlow-based image classifier is designed to detect a person's mood from an image, classifying them as either happy or sad. The model has been trained on a dataset containing labeled images of individuals expressing happiness and sadness.

## Accuracy Graph
![training_accuracy_graph](https://github.com/Akash-nath29/image-classifier/assets/100131577/782f8aa9-b661-4b9f-8dc9-fa3a1b6dbf7e)
## Data Loss Graph
![training_data_loss_graph](https://github.com/Akash-nath29/image-classifier/assets/100131577/50d83b86-c895-481a-bb09-3127acebb7b7)


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Akash-nath29/image-classifier.git
   ```

2. Navigate to the project directory:

   ```bash
   cd image-classifier
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure you have the necessary dependencies installed (see Installation).
2. Place the image(s) you want to classify in the `images` directory.
3. Run the classifier script:

   ```bash
   python classify.py
   ```

   This script will analyze the images in the `images` directory and print the predicted mood for each image.

## Model Details

- The model architecture is based on deep neural networks (DNNs), specifically designed for image classification tasks.
- It utilizes the TensorFlow framework for building and training the model.
- The model achieves accuracy comparable to state-of-the-art methods for mood detection in images.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
