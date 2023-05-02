import Universe as uni
import os
import time

begin = time.time()

if __name__ == '__main__':

    new_uni = uni.create_mat(40, 40)
    new_neig = uni.get_neighbors(new_uni)
    clear = lambda: os.system('cls')
    rate = 1 / 5

    while True:
        time.sleep(rate - ((time.time() - begin) % rate))
        new_uni, new_neig, new_disp, = uni.dead_alive(new_uni, new_neig)
        clear()
        print(new_disp)
