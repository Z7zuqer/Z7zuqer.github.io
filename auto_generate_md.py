import os

base_ffhq = './ffhq'
base_ade20k = './ade20k'
qulaity_level = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

ade20k_files = os.listdir(base_ade20k)
ade20k_img_index = list(set([int(item.split('_')[0]) for item in ade20k_files]))

with open('./README.md', 'w') as f:
    for img_index in ade20k_img_index:
        str = ''
        for idx_Q, Q in enumerate(qulaity_level):
            str += '![{:04d}_{:03d}]({}/{:06d}_ {}.jpg)\n'.format(img_index, Q, base_ade20k, img_index, Q-10)
            if idx_Q == 5:
                str+='\n'
        f.write('{}\n'.format(str))
