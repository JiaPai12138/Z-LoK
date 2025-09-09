from PIL import Image, ImageOps
from os import listdir


for image in listdir('.\\Docs\\'):
    if any(text in image for text in ('.py', '_1.', '_ex', '_3d', '.gif')):
        continue

    # 打开原始图像
    original_image = Image.open(f'.\\Docs\\{image}')

    # 创建一个纯色背景图像
    background_color = (33, 33, 33)  # 白色背景
    background_image = Image.new('RGB', (940, 800), background_color)

    # 计算原始图像放置在背景图像中心的位置
    offset = ((background_image.width - original_image.width) // 2, (background_image.height - original_image.height))

    # 将原始图像粘贴到背景图像上
    background_image.paste(original_image, offset)

    # 保存合成后的图像
    background_image.save(f".\\Docs\\{image.replace('.png', '_1.png')}")
