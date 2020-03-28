import requests
import base64
import json
import os


# Sample image file is available at http://plates.openalpr.com/ea7the.jpg
# IMAGE_PATH = 'C:/Users/Aditi Chatterjee/Desktop/openalpr_64/samples/us-1.jpg'

# def readLicence(IMAGE_PATH,OUPUT_FILE):
def readLicence(IMAGE_PATH,OUT_PATH):
    # IMAGE_PATH = 'E:/ImageProcessing/Project_LPR/frames/'
    SECRET_KEY = 'sk_DEMODEMODEMODEMODEMODEMO'

    with open(IMAGE_PATH, 'rb') as image_file:
        img_base64 = base64.b64encode(image_file.read())

    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=1&country=us&secret_key=%s' % (SECRET_KEY)
    r = requests.post(url,data = img_base64)
    try:
        print(r.json()['results'][0]['plate'])
    except:
        print("\nNo license plate found")
    name_of_file = ("E:/ImageProcessing/Project_LPR/plates_details")

    # try:        
    #     completeName = OUT_PATH + ".json"
    # #Alter this line in any shape or form it is up to you.
    #     file1 = open(completeName , "w")

    #     file1.write(json.dumps(r.json(), indent=2))

    #     file1.close()
    # except:
    #     completeName = OUT_PATH + ".txt"
    # #Alter this line in any shape or form it is up to you.
    #     file1 = open(completeName , "w+")

    #     file1.write("No number plate found")

    #     file1.close()

    #save json to file OUPUT_FILE

    # print(json.dumps(r.json(), indent=2))
def accessImageFromLocation():
    directory = r'E:/ImageProcessing/Project_LPR/frames/'
    outdirectory = 'E:/ImageProcessing/Project_LPR/json/'
    i=0
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            i=i+1
            IMAGE_PATH = (os.path.join(directory, filename))
            img_name = "details of frame"+str(i)
            OUT_PATH=(os.path.join(outdirectory,img_name))
            # imageFile=os.path.join(directory, 'details.json')
            # readLicence(IMAGE_PATH,OUT_PATH)
            readLicence(IMAGE_PATH,OUT_PATH)

        else:
            continue
accessImageFromLocation()