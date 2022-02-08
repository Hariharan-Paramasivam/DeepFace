import os
from deepface import DeepFace


def dir_files(path):
    local_dir = path
    files = []
    for image_name in os.listdir(f'{local_dir}'):
        files.append(local_dir + '/' + image_name)
    return files


# print(dir_files(r'./local'))


local_path = r'./local'
global_path = r'./global'


def predict(img_path):
    models = ["VGG-Face", "Facenet", "Facenet512", "OpenFace", "DeepFace", "DeepID", "ArcFace", "Dlib"]
    New_Face, User = True, False

    for image_name in dir_files(local_path):
        result_1 = DeepFace.verify(img1_path=img_path, img2_path=image_name,
                                   model_name=models[0], enforce_detection=False,detector_backend='mtcnn')
        
        print(image_name)
        if result_1['verified']:
            New_Face = False
            User = True
            break
    if User:
        for image_name in dir_files(global_path):
                result_2 = DeepFace.verify(img1_path=img_path, img2_path=image_name,
                                           model_name=models[0], enforce_detection=False,detector_backend='mtcnn')
                print(image_name)
                if result_2['verified']:
                    User = False
                    break

            
    if New_Face:
        return 0
    elif User:
        return 1
    elif not User:
        return 2
    #return New_Face, User


#print(predict('Local/1.jpg'))