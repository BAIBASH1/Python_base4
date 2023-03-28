from PIL import Image


def crop_middle(image):
    middle_crop_image = \
        image.crop((int(count_pixel / 2), 0, int(image.width - count_pixel / 2), image.height))
    return middle_crop_image


def crop_left(image):
    left_crop_image = image.crop((count_pixel, 0, image.width, image.height))
    joined_image = Image.blend(left_crop_image, crop_middle(image), 0.5)
    return joined_image


def crop_right(image):
    right_crop_image = image.crop((0, 0, image.width - count_pixel, image.height))
    joined_image = Image.blend(right_crop_image, crop_middle(image), 0.5)
    return joined_image

if __name__ == '__main__':
    import_image = Image.open('image.jpg')
    red, green, blue = import_image.split()
    count_pixel = 60

<<<<<<< HEAD
    new_avatar = Image.merge("RGB", (crop_left(red), crop_middle(green), crop_right(blue)))
    new_avatar.save('full_new_avatar.jpg')
    new_avatar.thumbnail((80, 80))
    new_avatar.save('80x80_new_avatar.jpg')
=======
import_image = Image.open('image.jpg')
(red, green, blue) = import_image.split()
count_pixel = 60

new_avatar = Image.merge("RGB", (crop_left(red), crop_middle(green), crop_right(blue)))
new_avatar.save('full_new_avatar.jpg')
new_avatar.thumbnail((80, 80))
new_avatar.save('80x80_new_avatar.jpg')
>>>>>>> c64a07e596c149ccb774c9539a036e7b506b7182
