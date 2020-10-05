from threading import Thread             #for running 2 or more programmes at same time
import face_recognition                  #library used for recognising faces
import cv2                               #computer vision library
import numpy as np                       #numpy
import pickle                            # used for importing files in a python project
from firebase import firebase            #google's database 
from picamera.array import PiRGBArray
from picamera import PiCamera
import time

def func2(namae, roku):         #values of this function is comming from face recognition results which are name and r_no which are replaced as namae and roku
    fb.put('GNITC',roku,namae)  #putting up all the data in firebase
    print(namae)
    print ('updated')



if __name__ == '__main__':
    fb = firebase.FirebaseApplication('https://kazukame-34d64.firebaseio.com/', None)   #create a firebase database and get this link from there
    video_capture = cv2.VideoCapture(0)
    video_capture.set(cv2.CAP_PROP_FPS, 2)
    with open('dataset_faces.dat', 'rb') as f:           #face encoding file is a pre-compiled python file which gives face data in program readable format
        all_face_encodings = pickle.load(f)


# Create arrays of known face encodings and their names

    face_names_ = list(all_face_encodings.keys())   #created an encoding file seperately
    face_encodings_ = np.array(list(all_face_encodings.values()))

    
# Initialize some variables
    pupil=['coo']                #random list item
    attandanc=[]                 #list of students
    ran = 0                      #random string variable for iteration
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
    # Grab a single frame of video
        ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
        if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame, number_of_times_to_upsample=2)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(face_encodings_, face_encoding,tolerance=0.55)  #you can increase tolerance for more strict criteria
                name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(face_encodings_, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = face_names_[best_match_index]
                    r_no = best_match_index

                face_names.append(name)   #creating list of students appeared in front of camera

        process_this_frame = not process_this_frame


    # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            time.sleep(0.01)
        # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            #print(name)
            
            for ran in pupil:                        #pupil is temporary list created for adding the attendance
                if name == 'Unknown':                #if unknown person appears, skip adding that one
                    break
                if name not in pupil:                # otherwise add that person in both main list(attandanc) and temporary list(pupil)
                    attandanc.append(name)       
                    pupil.append(name)               
                    Thread(target=func2(name,r_no)).start()    #initiated a thread with 2 values name and roll number 
                else:
                    break
            print(attandanc)

    # Display the resulting image
        #cv2.imshow('Video', frame)
        
    # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    


    
