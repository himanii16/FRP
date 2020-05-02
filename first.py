import cv2
import numpy as np
import face_recognition

img_path = "srk1.jpg"
image = cv2.imread(img_path)
if image is None:
    print ("Could not read image output")
    exit()

# print (np.shape (image))
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# for (x, y, w, h) in faces:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# cv2.imshow('img', image)
# cv2.waitKey()

img_path = "srk2.jpg"
image2 = cv2.imread(img_path)
if image2 is None:
    print ("Could not read image output")
    exit()

img_path = "salman.jpg"
image3 = cv2.imread(img_path)
if image3 is None:
    print ("Could not read image output")
    exit()

img_path = "duplicatesrk.jpg"
image4 = cv2.imread(img_path)
if image4 is None:
    print ("Could not read image output")
    exit()

img_path = "aamir.jpg"
image5 = cv2.imread(img_path)
if image5 is None:
    print ("Could not read image output")
    exit()

img_path = "srk3.jpg"
image6 = cv2.imread(img_path)
if image6 is None:
    print ("Could not read image output")
    exit()

encoding1 = face_recognition.face_encodings(image)
encoding2 = face_recognition.face_encodings(image2)
encoding3 = face_recognition.face_encodings(image3)
encoding4 = face_recognition.face_encodings(image4)
encoding5 = face_recognition.face_encodings(image5)
encoding6 = face_recognition.face_encodings(image6)

# print (encoding1) 
# print (encoding2)

name = "Not similar"
# print (type (encoding1))

# point to be taken care is that encoding1 i.e the first argument
# should be a list , also check that the shape in the list is matching
# with the second argument 

compare = face_recognition.compare_faces(encoding1,encoding2[0])
face_dist = face_recognition.face_distance(encoding1,encoding2[0])
best_match_index = np.argmin(face_dist)
print (compare)
print (face_dist)
print (best_match_index)
if compare[best_match_index]:
	name = "similar"

print (name)

name = "Not similar"
compare = face_recognition.compare_faces(encoding1,encoding3[0],tolerance=0.7)
face_dist = face_recognition.face_distance(encoding1,encoding3[0])
best_match_index = np.argmin(face_dist)
print (compare)
print (face_dist)
print (best_match_index)
if compare[best_match_index]:
	name = "similar"

print (name)

name = "Not similar"
compare = face_recognition.compare_faces(encoding1,encoding4[0],tolerance=0.7)
face_dist = face_recognition.face_distance(encoding1,encoding4[0])
best_match_index = np.argmin(face_dist)
print (compare)
print (face_dist)
print (best_match_index)
if compare[best_match_index]:
	name = "similar"

print (name)

name = "Not similar"
compare = face_recognition.compare_faces(encoding1,encoding5[0],tolerance=0.7)
face_dist = face_recognition.face_distance(encoding1,encoding5[0])
best_match_index = np.argmin(face_dist)
print (compare)
print (face_dist)
print (best_match_index)
if compare[best_match_index]:
	name = "similar"

print (name)

name = "Not similar"
compare = face_recognition.compare_faces(encoding1,encoding6[0],tolerance=0.7)
face_dist = face_recognition.face_distance(encoding1,encoding6[0])
best_match_index = np.argmin(face_dist)
print (compare)
print (face_dist)
print (best_match_index)
if compare[best_match_index]:
	name = "similar"

print (name)