import torch

from torchvision.models import resnet18
from torchvision.transforms import Normalize, ToTensor

import imageio
import cv2

# img = imageio.imread('https://www.google.com/search?q=cockorel&tbm=isch&ved=2ahUKEwjSzNjc77TtAhWWxCoKHYohAI4Q2-cCegQIABAA&oq=cockorel&gs_lcp=CgNpbWcQAzoECAAQQzoFCAAQsQM6BAgjECc6BwgjEOoCECc6BwgAELEDEEM6AggAOgQIABAeUOIjWMFQYLZYaAFwAHgBgAFBiAHHBpIBAjE2mAEAoAEBqgELZ3dzLXdpei1pbWewAQrAAQE&sclient=img&ei=uXTKX5KMKZaJqwGKw4DwCA&bih=986&biw=2048#imgrc=9Hfk7g8DEJ4OBM')
# img = imageio.imread('https://sun9-32.userapi.com/impf/c848536/v848536355/5aecb/3RG9xhg2Rak.jpg?size=2560x1920&quality=96&proxy=1&sign=dd676d3a4d2df20fe1822d921b219b58&type=album')
img = imageio.imread('https://cdn.insidesport.co/wp-content/uploads/2020/10/07193932/fifa.jpg')


img = cv2.resize(img, (256, 256), interpolation=cv2.INTER_LANCZOS4)
img = ToTensor()(img)
img = Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])(img)
img = img.unsqueeze(0)

model = resnet18(pretrained=True).eval()

res = model(img)
res = torch.softmax(res, dim=1)

prob, image_class = torch.max(res, dim=1)
prob = prob.item()
image_class = image_class.item()

imagenet_num_classes = 1000
with open('imagenet.txt', 'r') as file_in:
    classes_words = file_in.read().splitlines()

classes_num2word = dict(zip(range(imagenet_num_classes), classes_words))

print(prob, classes_num2word[image_class])
