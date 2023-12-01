from django.shortcuts import render
import tensorflow as tf

# Image Transformations
from PIL import Image
import numpy as np
import cv2

def preprocess_uploaded_image(uploaded_image):
    try:
        # Open and read the uploaded image using PIL
        image = Image.open(uploaded_image)

        # Resize the image to (32, 32)
        image = image.resize((32, 32))

        # Convert the image to grayscale
        gray_image = image.convert('L')

        # Convert the grayscale image to a NumPy array
        gray_image_array = np.array(gray_image)

        # Reshape the grayscale image to (32, 32, 1)
        final_image = gray_image_array.reshape((32, 32, 1))

        # Add an extra dimension to match batch format (optional)
        final_image = np.expand_dims(final_image, axis=0)

        return final_image

    except Exception as e:
        return None





# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def Alzehimer(request):
    classes=['MildDemented','ModerateDemented','NonDemented','VeryMildDemented']    
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_image = request.FILES['image']
        processed_image = preprocess_uploaded_image(uploaded_image)
        if processed_image is not None:
                
                # Load your machine learning model
            model = tf.keras.models.load_model(r"Alzehimers_prediction\Mini_Project")

                # Make predictions using the processed image
            predictions = model.predict(processed_image)
            Output=classes[np.argmax(predictions)]
            print(Output)
            return render(request,'Alzehimer.html',{'Output':Output,'Probability':np.max(predictions)*100})
    else:
        return render(request,'Alzehimer.html',{'Output':'Enter The Image','Probability':0})