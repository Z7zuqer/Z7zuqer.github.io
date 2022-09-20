sta, end = 1, 128
for idx in range(sta, end):
    print('<img src="./regis_res/warped/x/axial{:04d}.png" id="wx{}" '
          'class="w3-border w3-padding" style="width: 320px; top: 780px; right: 55%; '
          'position: absolute; display: none" title="Registration Results">'.format(idx, idx-sta))
    print(
        '<img src="./regis_res/warped/y/coronal{:04d}.png" id="wy{}" '
        'class="w3-border w3-padding" style="width: 320px; top: 780px; right: 10%; '
        'position: absolute; display: none" title="Registration Results">'.format(
            idx, idx - sta))
    print(
        '<img src="./regis_res/warped/z/sagittal{:04d}.png" id="wz{}" '
        'class="w3-border w3-padding" style="width: 320px; top: 780px; right: -35%; '
        'position: absolute; display: none" title="Registration Results">'.format(
            idx, idx - sta))

