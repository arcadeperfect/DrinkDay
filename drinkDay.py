from dd_matrix_image import message, image_loader
import multiprocessing as mp





img1 = './resources/static_images/drink.png'
img2 = './resources/static_images/dontDrink.png'




print(img1)

if __name__ == '__main__':

    queue = mp.Queue()
    process = image_loader(queue)
    process.start()
    queue.put(message(img1,2))