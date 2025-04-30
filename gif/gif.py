import imageio.v3 as iio


filenames = ['kermit1.jpg', 'kermit2.jpg'] #ukuran harus sama
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('kkkkkk.gif', images, duration = 0.5, loop = 0)