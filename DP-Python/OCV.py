import cv2


image = cv2.imread('./img/image.png')

if image is not None:
    print("Image loaded successfully !")
    # print(image)
    # print(image.dtype)
    # cv2.imshow("This is Image !",image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    
# else:
#     print("Failed to load image.")
    
    
# isSaved = cv2.imwrite("output.png",image)
# if isSaved:
#     print("Image Successfully !")
# else:
#     print("Faild to save an image !"    )
    
oimg = cv2.imread("output.png")
# cv2.imshow("This is Image !",oimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Dimensiotion 

# h,w,c = oimg.shape

# print(f"Height : {h}, Width : {w}, Channels : {c}")

# Gray Scale converting 

gray_scale = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("This is Image !",gray_scale)
cv2.waitKey(0)
cv2.destroyAllWindows()

    