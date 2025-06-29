# Image Classification with Azure Custom Vision

This project demonstrates how to use Azure Custom Vision Prediction API to classify images and annotate them using Python.

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Create a virtual environment**  
   ```
   py -3 -m venv venv
   ```
   Activate it:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On Unix or MacOS:
     ```
     source venv/bin/activate
     ```

3. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables**  
   Create a `.env` file in the project root with the following content:
   ```
   PREDICTION_KEY=your_azure_prediction_key
   ENDPOINT=your_azure_endpoint
   PROJECT_ID=your_custom_vision_project_id
   PUBLISHED_NAME=your_published_model_name
   IMAGE_PATH=path_to_your_test_image.jpg
   ```

5. **Prepare input image**  
   Place your test image at the path specified in `IMAGE_PATH`.

## Usage

Run the main script:
```
python main.py
```

- The script will classify the image, annotate it with the top prediction, and save the result to `data/predicted/pil_annotated.jpg`.
- The prediction and output path will be printed to the console.

## Requirements

- Python 3.7+
- Azure Custom Vision Prediction Key and Endpoint
- Published Custom Vision Model

## License

This project is for educational purposes.
