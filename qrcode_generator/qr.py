import qrcode as qr
import cv2

# # Generate and save the QR code
# img = qr.make("https://www.linkedin.com/in/debasis-sahoo-5a7866249/")
# img.save("Debasis_Sahoo__LinkedIN.png", scale=8)

# # Read the QR code using opencv
# img = cv2.imread("Debasis_Sahoo__LinkedIN.png")
# decoded_objects = cv2.QRCodeDetector().detectAndDecode(img)

# # Print the decoded data
# decoded_data = decoded_objects[0]
# print(decoded_data)




# the previous one is my qrcode 
n=input("Enter your link or text here for making qr code :  ")
var=qr.make(n)
var.save("myqrcode.png",scale=10)

var=cv2.imread("myqrcode.png")
decoded_objects = cv2.QRCodeDetector().detectAndDecode(var)
decoded_data = decoded_objects[0]
print(decoded_data)
print("your qr code is ready:  ")
