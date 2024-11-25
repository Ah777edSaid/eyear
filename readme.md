# eyear Project


## كيفية الاستخدام

1. قم بتحميل هذا المشروع من GitHub.
2. قم بتثبيت المشروع باستخدام `pip`:

   ```bash
   pip install git+https://github.com/اسم-المستخدم/اسم-المشروع.git](https://github.com/Ah777edSaid/eyear.git

3. تحميل المكتبات المطلوبة
## packages

### install packages
"""
```bash
# Commented out IPython magic to ensure Python compatibility.
# Install essential libraries only once, avoid repeated installations

# Image Enhancement with Real-ESRGAN
!pip install realesrgan

# Image Processing with OpenCV
!pip install opencv-python

# PyTorch, Torchvision, and Torchaudio (CUDA 11.8 compatible versions)
!pip install torch==1.13.1 torchvision==0.14.1 torchaudio -f https://download.pytorch.org/whl/cu118/torch_stable.html

# FastAI for high-level deep learning applications
!pip install fastai

# Hugging Face Transformers for NLP and Vision-Language Models
!pip install transformers

# Install Pillow for image processing (necessary for several image manipulations)
!pip install pillow

# Pyttsx3 for offline Text-to-Speech
!pip install pyttsx3

# Google Translate for language translation (ensure compatible version)
!pip install googletrans==4.0.0-rc1

# Playsound for audio playback
!pip install playsound

# PyAudio for audio input/output handling
!pip install pyaudio

# Google Text-to-Speech for online TTS functionality
!pip install gtts

# Pydub for audio processing (e.g., merging, splitting)
!pip install pydub ffmpeg ffmpeg-python

# Install Espeak TTS engine (optional)
!apt install -y espeak-ng

# SpeechRecognition for speech-to-text functionality
!pip install SpeechRecognition

# Tesseract OCR for extracting text from images
!apt-get install -y tesseract-ocr libtesseract-dev
!pip install pytesseract

# Pyrebase for Firebase integration
!pip install pyrebase4

# Numpy for numerical operations
!pip install numpy

# YOLOv5 setup for object detection
!git clone https://github.com/ultralytics/yolov5
# %cd yolov5
!pip install -r requirements.txt
# %cd ..

# Install additional essential libraries
!pip install ultralytics textblob pytz word2number

# Commented out IPython magic to ensure Python compatibility.
# Clone YOLOv5 repository and navigate to it
!git clone https://github.com/ultralytics/yolov5
# %cd yolov5
# Install dependencies
!pip install -r requirements.txt

!pip install pydub SpeechRecognition
!apt-get install ffmpeg
!pip install psutil

