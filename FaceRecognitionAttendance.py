import face_recognition
import cv2
import numpy as np
# A CSV (comma-separated values) file is a text file that has a 
# specific format which allows data to be saved in a table structured format.
import csv
# import datetime as datetime
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# load known faces

harrys_image = face_recognition.load_image_file("HarryImage.jpeg")
# The [0] indexing is used assuming there is only one face in each image.

harry_encoding = face_recognition.face_encodings(harrys_image)[0]

rohans_image = face_recognition.load_image_file("Rohan.jpg")
rohan_encoding = face_recognition.face_encodings(rohans_image)[0]

known_face_encodings = [harry_encoding, rohan_encoding]
# The resulting face encodings are stored in the known_face_encodings list.

known_face_names = ["Harry", "Rohan"]

#  List of expected students

students = known_face_names.copy()

face_locations = []
face_encodings = []


#  Get the current date and time

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

# This line opens a file with the name specified by the current_date variable, followed by the ".csv" extension. 
# The file is opened in write mode ("w") and the "+" mode allows both reading and writing. 
# The newline="" argument is used to handle newline characters in CSV files.

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while (video_capture.isOpened()):
    _, frame = video_capture.read() # reading the frames
    small_frame = cv2.resize(frame, (0 , 0) , fx=0.25, fy=0.25) #resing the frames
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)   #converted the color to rgb

    # Recognising faces
    # face_locations: This variable stores the output of the face_recognition.face_locations() function call. 
    # It will contain a list of tuples, where each tuple represents the coordinates of a detected face. 
    # The coordinates are in the format (top, right, bottom, left)
    face_locations = face_recognition.face_locations(rgb_small_frame)

    # passing the location of the face which we found in rgb_small_frame after resizing which after gets encoded
    # and get stored in face_encodings
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    # will iterate all the faces that is present in face_encodings
    for face_encoding in face_encodings:
        # matches will store a list of true or false
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        # face.distance will check how much similarities do both the encoded results have
        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
    
        best_match_index = np.argmin(face_distance)

        if (matches[best_match_index]):
            name = known_face_names[best_match_index]

        # Add the text if a person is present

        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            BottomLeftCornerOfText = (10,100)
            fontScale = 1.5 # how much bigger we want
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2
            cv2.putText(frame, name + "Present", BottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])
    
    
    cv2.imshow("Attendance", frame)
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
f.close()
