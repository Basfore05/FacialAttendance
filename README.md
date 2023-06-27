#Face Recognition and Attendance Tracking
This is a Python script that utilizes the face_recognition library and OpenCV to perform face recognition and attendance tracking. The script captures video from a webcam, detects faces in real-time, and matches them against a set of known faces to mark attendance.

#Requirements
To run this script, you need to have the following dependencies installed:

Python 3.x
OpenCV (cv2) library
face_recognition library
numpy library
You can install the required libraries using pip with the following command:


pip install opencv-python face-recognition numpy
#Usage
Clone or download the repository to your local machine.
Make sure you have a webcam connected to your computer.
Place images of the known faces in the same directory as the script. Ensure that the images are clear and contain only one face.
Update the known_face_names list and known_face_encodings list with the names and encodings of the known faces, respectively.
Run the script using the following command:
python face_recognition_attendance.py
The script will open a window displaying the video feed from the webcam.
When a known face is detected, the person's name will be displayed on the video frame, indicating their presence.
If the detected face matches a known face and is present in the students list, the script will remove their name from the list and log their attendance in a CSV file named with the current date.
Press 'q' to quit the script.
#Output
The script generates a CSV file with the attendance records for the current date. Each row in the CSV file contains the name of the student and the timestamp when their attendance was marked.

#Limitations
The script assumes that there is only one face in each image of the known faces.
The accuracy of face recognition depends on the quality of the images provided and the lighting conditions during capture.
It is recommended to have consistent lighting and positioning of the camera for better results.
#License
This project is licensed under the MIT License.

Feel free to customize and modify the script according to your needs.

Please note that face recognition technologies may have legal and ethical considerations. Ensure that you comply with relevant laws and obtain necessary permissions before using this script for any purpose.

#Acknowledgments
The face_recognition library by Adam Geitgey: https://github.com/ageitgey/face_recognition
OpenCV: https://opencv.org/
#References
face_recognition library documentation: https://face-recognition.readthedocs.io/
OpenCV documentation: https://docs.opencv.org/
