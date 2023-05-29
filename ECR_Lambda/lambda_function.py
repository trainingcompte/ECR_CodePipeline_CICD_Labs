import json 
import base64
import cv2

def decode(encoded_img):
    aux_path = '/tmp/tmp.png'
    with open(aux_path,"wb") as f:
        f.write(base64.b64decode(encoded_img))
        f.close()
    out = cv2.imread(aux_path)
    return out

def encode(img):
    aux_path = '/tmp/tmp.png'
    cv2.imwrite(aux_path,img)
    with open(aux_path, 'rb') as f:
        code = base64.b64encode(f.read())
        f.close()
    return code.decode('utf-8')


def lambda_handler(event, context):
    img = decode(event['body'])
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_image = encode(gray_img)


    return {
        'statusCode': 200,
        'body': gray_image,
        'isBase64Encoded': True,
        'headers': {'content-type': 'image/png'}
    }