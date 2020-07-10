
ori_ann_seg_list = [ 1129.7, 335.3, 1131.3, 327.5, 1135.6, 321.1, 1142, 316.8, 1155.1, 315.6, 1166.8, 319.3, 1174, 328.9, 1179.5, 346.3, 1179.8, 378.9, 1178.2, 386.7, 1173.9, 393.1, 1167.6, 397.3, 1157.3, 398.9, 1138.9, 395.3, 1132.6, 391, 1128.5, 384.7, 1126.9, 377, 1129.8, 335.9 ]

x_list = [v for i,v in enumerate(ori_ann_seg_list) if i%2==0]
y_list = [v for i,v in enumerate(ori_ann_seg_list) if i%2==1]

xy_list = [(x,y) for x,y in zip(x_list, y_list)]

xy_list2 = []
for x,y in zip(x_list, y_list):
    xy_list2.append(x)
    xy_list2.append(y)

xy_list2_1 = []
for i in zip(x_list, y_list):
    xy_list2_1.append(i)

# xy_list3 = [*(x,y) for x,y in zip(x_list, y_list)] # SyntaxError: iterable unpacking cannot be used in comprehension

print('x_list:',x_list)
print('y_list:',y_list)
print('xy_list:',xy_list)
print('xy_list2:',xy_list2)
print('xy_list2_1:',xy_list2_1)
# print('xy_list3:',xy_list3)
