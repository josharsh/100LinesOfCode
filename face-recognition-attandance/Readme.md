# Face Recognition Attendance System

## Libraries used:-
	a. OpenCV -> For accessing camera and changing format of image from BGR to RGB
	b. Numpy -> For finding minimum face distance (if are multiple faces)
	c. Face_Recognition -> For finding encodings of face, face_distance and also to compare faces
	d. OS -> For directing to the images folder
	e. DateTime -> For marking the attendance at which time the candidate appeared in the camera

## How it works
 
In this project first we need to provide one sample image (the name of image should be the name of the person who's image is being uploaded) for
identification and then the encoding function will calculate it's features and after that if that person comes in frame of camera then his/her
attendance will be marked and also his/her name will be shown below their face (in live camera).


