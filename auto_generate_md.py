import os

base_ffhq = './results/ffhq'
base_ade20k = './results/ade20k'
qulaity_level = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

ade20k_files = os.listdir(base_ade20k)
ade20k_img_index = list(set([int(item.split('_')[0]) for item in ade20k_files]))

with open('./web_show_ade20k_results.html', 'a') as f:
    for idx, img_index in enumerate(ade20k_img_index):
        f.write('<tr>\n')
        f.write('<td>{}</td>\n'.format(idx))
        for idx_Q, Q in enumerate(qulaity_level):
            if idx_Q == 0:
                f.write(
                    '<td><img src= "./results/ade20k/{:06d}_%20%20{}.jpg" width="170" border="0"></td>\n'.format(img_index, Q-10))
            else:
                f.write(
                    '<td><img src= "./results/ade20k/{:06d}_%20{}.jpg" width="170" border="0"></td>\n'.format(img_index, Q-10))
        f.write('</tr>\n'.format(idx))

with open('./web_show_ffhq_results.html', 'a') as f:
    img_num = 20
    for idx in range(img_num):
        f.write('<tr>\n')
        f.write('<td>{}</td>\n'.format(idx))
        for idx_Q, Q in enumerate(qulaity_level):
            f.write('<td><img src= "./results/ffhq/3001/{:03d}/{:06d}.png" width="170" border="0"></td>\n'.format(Q, idx))
        f.write('</tr>\n'.format(idx))

