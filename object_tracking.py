import cv2

prototxt = "goturn.prototxt"
model = "goturn.caffemodel"

tracker = cv2.TrackerGOTURN_create()

video_path = "car.mp4" 
video = cv2.VideoCapture(video_path)

output_path = "output.mp4"
fps = int(video.get(cv2.CAP_PROP_FPS))
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

ret, frame = video.read()
#bbox = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
bbox = (857, 258, 121, 97)
tracker.init(frame, bbox)

while True:
    ret, frame = video.read()
    if not ret:
        break

    ret, bbox = tracker.update(frame)

    if ret:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)

        # blur
        x, y, w, h = [int(i) for i in bbox]
        roi = frame[y:y+h, x:x+w]
        roi_blurred = cv2.blur(roi, (25, 25))
        frame[y:y+h, x:x+w] = roi_blurred

    out.write(frame)
    cv2.imshow("Tracker Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()
