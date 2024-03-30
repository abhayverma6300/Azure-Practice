# Azure Cognitive Services Implementations

## Overview
This repository contains implementations of various Azure Cognitive Services including Custom Vision, Optical Character Recognition (OCR), Form Recognizer, and Language services such as Named Entity Recognition (NER), Text Analytics, and Conversation Language Understanding (CLU). The implementations are provided in Flask, Django, and FastAPI frameworks for each service.

## Directory Structure

### Custom Vision (CV)
- `.CV_env`: Environment directory for Custom Vision service.
- `Obj_Det`: Implementation of object detection using Custom Vision.
- `OCR_Django`: OCR implementation using Custom Vision with Django framework.
- `OCR_Fast`: OCR implementation using Custom Vision with FastAPI framework.
- `OCR_flask`: OCR implementation using Custom Vision with Flask framework.

### Form Recognizer (Form Recognizer)
- `Django_env`: Environment directory for Form Recognizer service with Django framework.
- `FastAPI`: Implementation of Form Recognizer with FastAPI framework.
- `FR_flask`: Implementation of Form Recognizer with Flask framework.

### Language Services (Language)
- `.lang_env`: Environment directory for Language services.
- `CLU_Django`: Implementation of Conversation Language Understanding with Django framework.
- `CLU_FastAPI`: Implementation of Conversation Language Understanding with FastAPI framework.
- `CLU_Flask`: Implementation of Conversation Language Understanding with Flask framework.
- `Lang_Django`: Implementation of Language services with Django framework.
- `Lang_FastAPI`: Implementation of Language services with FastAPI framework.
- `Lang_Flask`: Implementation of Language services with Flask framework.
- `NER_Django`: Implementation of Named Entity Recognition with Django framework.
- `NER_FastAPI`: Implementation of Named Entity Recognition with FastAPI framework.
- `NER_Flask`: Implementation of Named Entity Recognition with Flask framework.
- `abc.txt`: Sample text file.
- `xyz.txt`: Another sample text file.

## Dependencies
- Python 3.x
- Libraries: Flask, Django, FastAPI, Azure SDKs for Cognitive Services

## Setup
1. Clone the repository:

    ```
    git clone https://github.com/abhayverma6300/Azure-Practice.git
    cd Azure-Practice
    ```

2. Install the required dependencies using `pip` and the provided `requirements.txt` file:

    ```
    pip install -r requirements.txt
    ```
3. Set up environment variables for authentication keys and endpoints.

## Usage
1. Choose the service and framework combination according to your requirements.
2. Run the corresponding application file for the chosen framework.

## License
This project is licensed under the [MIT License](LICENSE).

## Additional Information
- Experiment with different Azure Cognitive Services and frameworks to suit specific use cases.
- Refer to the documentation of each service for detailed usage and configuration instructions.
- Ensure proper authentication and endpoint configuration for seamless integration with Azure services.
