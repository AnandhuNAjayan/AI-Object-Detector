import cv2

# Another Image Name = 'RDJ.jpg'
#Another image Name = ''i20_Modelpc.png''

image = cv2.imread('i20_Modelpc.png')

image = cv2.resize(image, (640, 480))

classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
    print(classNames)


thresh = 0.55

configPath = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

classIds, confs, bbox = net.detect(image, confThreshold=thresh)
print(classIds, bbox)

if len(classIds) != 0:
    for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
        cv2.rectangle(image, box, color=(0, 255, 0), thickness=5)
        cv2.putText(image, classNames[classId-1].upper(), (box[0]+10, box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)


cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
