import cv2
import numpy as np
import face_recognition

def img_comparision(path1, path2):
	image1 = cv2.imread(path1)
	if image1 is None:
	    print ("Could not read first image output")
	    exit()

	image2 = cv2.imread(path2)
	if image2 is None:
	    print ("Could not read second image output")
	    exit()

	encoding1 = face_recognition.face_encodings(image1)
	encoding2 = face_recognition.face_encodings(image2)

	name = "Not similar"
	compare = face_recognition.compare_faces(encoding1,encoding2[0],tolerance=0.7)
	face_dist = face_recognition.face_distance(encoding1,encoding2[0])
	best_match_index = np.argmin(face_dist)
	print (compare)
	print (face_dist)
	print (best_match_index)
	if compare[best_match_index]:
		name = "similar"

	print (name)

path1="test_images/srk1.jpg"
path2="test_images/duplicatesrk.jpg"
img_comparision(path1,path2)