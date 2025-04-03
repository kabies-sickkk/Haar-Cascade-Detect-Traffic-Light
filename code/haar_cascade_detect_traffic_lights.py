import cv2
import serial
import time 
source = "red_dec.jpg"
tx = source.split('_')[0]
ser = serial.Serial("COM3",9600) #hãy thay chân COM tương ứng với thiết bị 
time.sleep(2) # thời gian để arduino khởi động
# Load ảnh
img = cv2.imread(source)

# Load Haar Cascade cho việc nhận diện vật thể
detector = cv2.CascadeClassifier('lights_det.xml')

# Chuyển đổi ảnh sang ảnh xám để tăng tốc độ xử lý
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Nhận diện vật thể trong ảnh
objects = detector.detectMultiScale(gray, scaleFactor=1.01, minNeighbors=4, minSize=(30, 30))

# Vẽ khung hình chữ nhật xung quanh các vật thể được nhận diện
for (x, y, w, h) in objects:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img,str(tx), (x+10,y+25),cv2.FONT_HERSHEY_SIMPLEX, 1,(0,0,255),2)
if tx == "red":
    print(tx)
    ser.write(b'1') #gửi tín hiệu 1 để bật led đỏ
elif tx == "yellow":
    print(tx)
    ser.write(b'2')# gửi tín hiệu 2 để bật led vàng
elif tx == "green":
    print(tx)
    ser.write(b'3')# gửi tín hiệu 3 để bật led xanh lá
else:
    ser.write(b'0')# gửi 0 để tắt toàn bộ led
    print("not detect")
# Hiển thị ảnh với khung hình chữ nhật đã được vẽ
cv2.imshow("Detected Objects", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
ser.write(b'0')
