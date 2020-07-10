{'instances': Instances(num_instances=1, image_height=1404, image_width=1876,
                        fields=[
                            pred_boxes: Boxes(tensor([[730.4471,   34.9740, 1287.7456,  870.8266]], device='cuda:0')),
                            scores: tensor([0.9961], device='cuda:0'),
                            pred_classes: tensor([0], device='cuda:0'),
                            pred_keypoints: tensor([[[1.1186e+03, 4.0909e+02, 3.5997e-01],
                                                     [9.3111e+02, 5.2124e+02,
                                                         3.4309e-01],
                                                     [9.8193e+02, 1.4274e+02,
                                                         5.0920e-01],
                                                     [8.5400e+02, 1.7428e+02,
                                                         4.8310e-01],
                                                     [1.2080e+03, 6.4565e+02,
                                                         4.1227e-01],
                                                     [9.9946e+02, 7.2276e+02, 4.9851e-01]]], device='cuda:0'),
                            pred_keypoint_logits: tensor([[[[-0.6002, -0.3481,  0.1562,  ...,  0.1532,  0.1290,  0.1169],
                                                            [-0.8101, -0.6617, -0.3648,  ...,
                                                             0.2945,  0.1858,  0.1315],
                                                            [-1.2298, -1.2888, -1.4068,  ...,
                                                                0.5772,  0.2994,  0.1605],
                                                            ...,
                                                            [-0.6495, -0.5982, -0.4957,  ...,
                                                             1.5429,  1.8175,  1.9548],
                                                            [-0.5919, -0.7121, -0.9524,  ...,
                                                             1.2695,  1.4054,  1.4733],
                                                            [-0.5631, -0.7690, -1.1807,  ...,  1.1328,  1.1994,  1.2326]],

                                                           [[-0.1566, -0.3668, -0.7872,  ..., -1.8835, -0.9418, -0.4709],
                                                            [-0.4877, -0.7030, -1.1337,  ..., -
                                                             1.8123, -1.0598, -0.6835],
                                                            [-1.1498, -1.3754, -1.8266,  ..., -
                                                               1.6697, -1.2958, -1.1088],
                                                            ...,
                                                            [0.2780,  0.2414,  0.1681,  ..., -
                                                               3.0776, -2.4741, -2.1723],
                                                            [0.6264,  0.6244,  0.6203,  ..., -
                                                               1.5087, -0.9539, -0.6765],
                                                            [0.8006,  0.8159,  0.8465,  ..., -0.7242, -0.1938,  0.0714]],

                                                           [[-1.1328, -1.3600, -1.8142,  ..., -0.0521, -0.2990, -0.4225],
                                                            [-1.4127, -1.6767, -2.2046,  ..., -
                                                             0.1026, -0.1567, -0.1838],
                                                            [-1.9723, -2.3101, -2.9856,  ..., -
                                                               0.2035,  0.1279,  0.2937],
                                                            ...,
                                                            [-1.9207, -2.6069, -3.9794,  ..., -
                                                               2.0477, -1.9414, -1.8882],
                                                            [-1.3035, -1.8246, -2.8669,  ..., -
                                                               2.2249, -1.4579, -1.0745],
                                                            [-0.9949, -1.4335, -2.3107,  ..., -2.3134, -1.2162, -0.6676]],

                                                           [[0.4573,  0.0776, -0.6817,  ..., -0.8796, -1.3824, -1.6338],
                                                            [0.0657, -0.2848, -0.9859,  ..., -
                                                             0.9415, -1.2019, -1.3321],
                                                            [-0.7173, -1.0096, -1.5942,  ..., -
                                                               1.0652, -0.8407, -0.7285],
                                                            ...,
                                                            [-2.3823, -2.8500, -3.7852,  ..., -
                                                               2.4784, -2.2100, -2.0758],
                                                            [-1.8424, -2.0065, -2.3349,  ..., -
                                                               2.1428, -1.4356, -1.0820],
                                                            [-1.5724, -1.5848, -1.6097,  ..., -1.9750, -1.0485, -0.5852]],

                                                           [[-1.1262, -1.4927, -2.2258,  ..., -1.8752, -1.0629, -0.6568],
                                                            [-1.3311, -1.6835, -2.3882,  ..., -
                                                             1.9853, -1.1379, -0.7142],
                                                            [-1.7409, -2.0649, -2.7130,  ..., -
                                                               2.2056, -1.2878, -0.8289],
                                                            ...,
                                                            [-2.0567, -2.9528, -4.7449,  ..., -
                                                               0.6006, -0.1423,  0.0869],
                                                            [-1.2685, -1.9770, -3.3940,  ..., -
                                                               0.3704,  0.0745,  0.2969],
                                                            [-0.8744, -1.4891, -2.7185,  ..., -0.2552,  0.1829,  0.4020]],

                                                           [[-0.6498, -0.9236, -1.4713,  ..., -1.7805, -1.2213, -0.9416],
                                                            [-0.7498, -1.1267, -1.8807,  ..., -
                                                             2.2160, -1.4670, -1.0924],
                                                            [-0.9497, -1.5330, -2.6996,  ..., -
                                                               3.0870, -1.9583, -1.3939],
                                                            ...,
                                                            [1.5767,  0.7801, -0.8133,  ..., -
                                                               2.8984, -2.1551, -1.7834],
                                                            [1.5068,  1.0938,  0.2678,  ..., -
                                                               1.8912, -1.6988, -1.6026],
                                                            [1.4718,  1.2507,  0.8084,  ..., -1.3875, -1.4706, -1.5122]]]],
                                                         device='cuda:0')])}
