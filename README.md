# Webcam Motion Detection & Email Alert System

This project is a Python-based motion detection system that uses a webcam to capture images when motion is detected. The system then sends an email alert with the captured image as an attachment, making it ideal for basic security monitoring.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/webcam-motion-detector.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd webcam-motion-detector
    ```
3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the project:**
    ```bash
    python motion_detector.py
    ```

python motion_detector.py
The system will start monitoring using your webcam. If motion is detected, an image will be saved and an email alert will be sent.

Adjusting Contour Sensitivity
In the motion_detector.py script, the line:

python
Copy code
if cv2.contourArea(contour) < 5500:
controls the sensitivity of the motion detection based on the size of the detected contours. The value 5500 represents the area size of the object to be ignored. If you want to detect smaller objects or ignore larger ones, adjust this value accordingly.

## Example:

Smaller objects: Decrease the value.
Larger objects: Increase the value.

## Features
Real-time motion detection
Email alerts with image attachments
Adjustable contour sensitivity to filter out smaller objects
Secure password management using environment variables
Simple and configurable setup

## Project Structure
motion_detector.py: The main script responsible for detecting motion, processing contours, and sending email alerts. The sensitivity to object size can be adjusted in this file.
requirements.txt: List of Python packages required to run the project.
README.md: Documentation of the project.

## Technologies Used
Python 3.10
smtplib for sending emails
os.getenv() for environment variable management
Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes. For major changes, open an issue first to discuss what you would like to change.

## Contact
OpenCV
For questions or suggestions, you can reach me at vigneshbaskar1407@gmail.com.


## Usage

To start the motion detection system, run the following command:
```bash
