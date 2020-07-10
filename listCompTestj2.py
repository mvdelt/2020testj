
# i. anno 가 너무 길어서 내가 작성한 코드가 저~~~아래에 있음. 요 anno 딕셔너리 접어보삼. 

anno = {
    "images": [
        {
            "id": 610,
            "dataset_id": 10,
            "category_ids": [ 4 ],
            "path": "/datasets/pano_kp_uplow/imp2_0.jpg",
            "width": 1976,
            "height": 976,
            "file_name": "imp2_0.jpg",
            "annotated": False,
            "annotating": [],
            "num_annotations": 0,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": False,
            "is_modified": False
        },
        {
            "id": 628,
            "dataset_id": 10,
            "category_ids": [ 4 ],
            "path": "/datasets/pano_kp_uplow/imp2_18.jpg",
            "width": 1976,
            "height": 976,
            "file_name": "imp2_18.jpg",
            "annotated": False,
            "annotating": [],
            "num_annotations": 0,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": False,
            "is_modified": False
        },
        {
            "id": 637,
            "dataset_id": 10,
            "category_ids": [ 4 ],
            "path": "/datasets/pano_kp_uplow/imp2_27.jpg",
            "width": 1976,
            "height": 976,
            "file_name": "imp2_27.jpg",
            "annotated": False,
            "annotating": [],
            "num_annotations": 0,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": True,
            "is_modified": False
        },
        {
            "id": 710,
            "dataset_id": 10,
            "category_ids": [ 4 ],
            "path": "/datasets/pano_kp_uplow/imp2_100.jpg",
            "width": 1976,
            "height": 976,
            "file_name": "imp2_100.jpg",
            "annotated": False,
            "annotating": [],
            "num_annotations": 0,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": False,
            "is_modified": False
        },
        {
            "id": 711,
            "dataset_id": 10,
            "category_ids": [ 4 ],
            "path": "/datasets/pano_kp_uplow/imp2_101.jpg",
            "width": 1976,
            "height": 976,
            "file_name": "imp2_101.jpg",
            "annotated": False,
            "annotating": [],
            "num_annotations": 0,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": False,
            "is_modified": False
        },
        {
            "id": 713,
            "dataset_id": 10,
            "category_ids": [ 4 ],
            "path": "/datasets/pano_kp_uplow/imp2_103.jpg",
            "width": 1976,
            "height": 976,
            "file_name": "imp2_103.jpg",
            "annotated": False,
            "annotating": [],
            "num_annotations": 0,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": False,
            "is_modified": False
        }
    ],
    "categories": [
        {
            "id": 4,
            "name": "upper_imp",
            "supercategory": "implant",
            "color": "#ff8000",
            "metadata": {},
            "creator": "j",
            "keypoint_colors": [ "#ffff00", "#ff8040", "#33fff1", "#408080", "#8080ff", "#400080" ],
            "keypoints": [ "bone_right", "bone_left", "apex_right", "apex_left", "top_right", "top_left" ],
            "skeleton": [
                [ 1, 3 ],
                [ 1, 5 ],
                [ 2, 4 ],
                [ 2, 6 ]
            ]
        },
        {
            "id": 5,
            "name": "lower_imp",
            "supercategory": "implant",
            "color": "#8080ff",
            "metadata": {},
            "creator": "j",
            "keypoint_colors": [ "#ffffff", "#ff8000", "#c0c0c0", "#408080", "#ff80ff", "#8000ff" ],
            "keypoints": [ "bone_right", "bone_left", "apex_right", "apex_left", "top_right", "top_left" ],
            "skeleton": [
                [ 1, 5 ],
                [ 1, 3 ],
                [ 2, 6 ],
                [ 2, 4 ]
            ]
        }
    ],
    "annotations": [
        {
            "id": 817,
            "image_id": 610,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1129.7, 335.3, 1131.3, 327.5, 1135.6, 321.1, 1142, 316.8, 1155.1, 315.6, 1166.8, 319.3, 1174, 328.9, 1179.5, 346.3, 1179.8, 378.9, 1178.2, 386.7, 1173.9, 393.1, 1167.6, 397.3, 1157.3, 398.9, 1138.9, 395.3, 1132.6, 391, 1128.5, 384.7, 1126.9, 377, 1129.8, 335.9 ] ],
            "area": 3748,
            "bbox": [ 1127, 316, 53, 83 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#088dab",
            "keypoints": [ 1172, 370, 2, 1136, 365, 2, 1165, 328, 2, 1142, 325, 2, 1170, 389, 2, 1134, 385, 2 ],
            "metadata": {},
            "milliseconds": 71833,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612424529 },
                    "user": "j",
                    "milliseconds": 57342,
                    "tools_used": [ "Brush", "Keypoints", "Select", "Brush" ]
                },
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612538444 },
                    "user": "j",
                    "milliseconds": 9761,
                    "tools_used": [ "Select" ]
                },
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613944693 },
                    "user": "j",
                    "milliseconds": 2365,
                    "tools_used": [ "Select" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 838,
            "image_id": 628,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 601.8, 245.2, 603.9, 235.1, 609.5, 226.8, 617.7, 221.3, 627.8, 219.2, 637.5, 221.1, 645.5, 226.1, 651.1, 233.6, 657, 256.5, 657.9, 280.2, 665, 304.9, 666.5, 320.8, 664.5, 330.9, 659.1, 338.8, 635.7, 340.3, 628.1, 343.2, 622.1, 339.1, 616.5, 330.9, 606.5, 288, 605, 261.1, 601.8, 245.9 ] ],
            "area": 5934,
            "bbox": [ 602, 219, 65, 124 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#33e3d5",
            "keypoints": [ 657, 307, 2, 627, 308, 2, 642, 235, 2, 620, 237, 2, 660, 321, 2, 626, 327, 2 ],
            "metadata": {},
            "milliseconds": 45315,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613640181 },
                    "user": "j",
                    "milliseconds": 15105,
                    "tools_used": [ "Select", "Brush", "Eraser" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 839,
            "image_id": 628,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 690.9, 234.8, 693, 224.7, 698.5, 216.4, 706.8, 210.9, 716.9, 208.8, 727, 210.9, 735.3, 216.4, 740.9, 224.7, 742.9, 234.8, 744.1, 258.6, 753.3, 303.1, 753.3, 329.8, 751.3, 339.9, 747.4, 345.1, 734.6, 343.3, 722.9, 345.3, 718.4, 347.9, 709.4, 348.5, 703.4, 339.9, 701.3, 324, 697.3, 316.6, 695.9, 308.1, 694.5, 295.9, 697, 284.8, 690.9, 252.9, 690.9, 235.5 ] ],
            "area": 6893,
            "bbox": [ 691, 209, 62, 140 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#e8a553",
            "keypoints": [ 740, 314, 2, 708, 313, 2, 728, 226, 2, 703, 229, 2, 741, 327, 2, 709, 332, 2 ],
            "metadata": {},
            "milliseconds": 30424,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613655288 },
                    "user": "j",
                    "milliseconds": 7606,
                    "tools_used": [ "Select", "Eraser" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 840,
            "image_id": 628,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 760.6, 262.9, 762.6, 252.7, 768.2, 244.5, 776.5, 238.9, 786.6, 236.9, 796.7, 238.9, 805, 244.5, 810.5, 252.7, 812.6, 262.9, 812.1, 307.2, 813.5, 327.1, 811.4, 337.2, 805.9, 345.5, 797.6, 351, 787.5, 353.1, 777.2, 351, 768.9, 345.2, 763.1, 336.9, 760.1, 309.9, 760.6, 264.7 ] ],
            "area": 5404,
            "bbox": [ 760, 237, 54, 116 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#af2ecc",
            "keypoints": [ 803, 313, 2, 773, 318, 2, 799, 254, 2, 776, 255, 2, 804, 329, 2, 772, 333, 2 ],
            "metadata": {},
            "milliseconds": 19796,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613630408 },
                    "user": "j",
                    "milliseconds": 4949,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 841,
            "image_id": 628,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 811.2, 271, 813.3, 260.9, 818.8, 252.6, 827.1, 247.1, 837.2, 245, 847.3, 247.1, 855.6, 252.6, 861.2, 260.9, 863.2, 271, 862.3, 351.9, 860.2, 361.9, 853, 371.1, 845.8, 372.7, 838.1, 371.3, 831.8, 372.7, 820.9, 371.9, 817.9, 369.9, 812.4, 361.6, 810.3, 351.5, 811.2, 271.5 ] ],
            "area": 6150,
            "bbox": [ 810, 245, 53, 128 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#4550de",
            "keypoints": [ 849, 328, 2, 820, 318, 2, 846, 264, 2, 830, 264, 2, 848, 354, 2, 819, 354, 2 ],
            "metadata": {},
            "milliseconds": 19171,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613662896 },
                    "user": "j",
                    "milliseconds": 3067,
                    "tools_used": [ "Select", "Eraser" ]
                },
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613662896 },
                    "user": "j",
                    "milliseconds": 6903,
                    "tools_used": [ "Select", "Eraser" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 842,
            "image_id": 628,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 856, 264.7, 858, 254.6, 863.6, 246.3, 871.9, 240.7, 882, 238.7, 892.1, 240.7, 900.4, 246.3, 906, 254.6, 908, 264.7, 905.8, 319.1, 907.1, 341.1, 905, 351.2, 899.5, 359.5, 891.2, 365.1, 881.1, 367.1, 871, 365.1, 862.7, 359.5, 857.1, 351.2, 853.7, 322.1, 856, 266 ] ],
            "area": 6035,
            "bbox": [ 854, 239, 54, 128 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#acd932",
            "keypoints": [ 896, 337, 2, 868, 337, 2, 896, 256, 2, 872, 255, 2, 897, 345, 2, 866, 345, 2 ],
            "metadata": {},
            "milliseconds": 23802,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613619410 },
                    "user": "j",
                    "milliseconds": 7934,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 843,
            "image_id": 628,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1174.7, 252.2, 1182, 253.2, 1197.4, 259, 1204.6, 264.7, 1209.5, 272.6, 1211.2, 282, 1210.3, 290.9, 1219.5, 333.6, 1217.5, 343.7, 1211.9, 352, 1203.6, 357.5, 1186, 360.3, 1167.5, 358.3, 1159.3, 352.7, 1153.7, 344.5, 1147.5, 292.1, 1148.2, 278.2, 1151.7, 266, 1157.4, 258.8, 1165.2, 253.9 ] ],
            "area": 6252,
            "bbox": [ 1148, 252, 72, 108 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#6be44a",
            "keypoints": [ 1210, 335, 2, 1171, 338, 2, 1199, 276, 2, 1167, 277, 2, 1211, 333, 2, 1170, 336, 2 ],
            "metadata": {},
            "milliseconds": 8830,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613612913 },
                    "user": "j",
                    "milliseconds": 1766,
                    "tools_used": [ "Select" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 844,
            "image_id": 628,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1215.4, 286.5, 1217.4, 276.4, 1223, 268.1, 1231.2, 262.5, 1241.4, 260.5, 1254.4, 264, 1269, 277.3, 1278.2, 291.8, 1285.9, 310.7, 1287.3, 319.3, 1285.2, 329.5, 1279.5, 337.8, 1272.2, 343.1, 1254.4, 347.5, 1241.1, 346.8, 1234.5, 343.8, 1225.1, 333.1, 1220.9, 323, 1215.4, 287.4 ] ],
            "area": 4676,
            "bbox": [ 1215, 261, 72, 87 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#8fdb6a",
            "keypoints": [ 1273, 323, 2, 1241, 332, 2, 1258, 274, 2, 1227, 280, 2, 1274, 315, 2, 1233, 323, 2 ],
            "metadata": {},
            "milliseconds": 11860,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613610542 },
                    "user": "j",
                    "milliseconds": 2372,
                    "tools_used": [ "Select" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 845,
            "image_id": 628,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1369.1, 223.5, 1379.2, 225.6, 1387.5, 231.2, 1393.1, 239.4, 1395.1, 249.5, 1393.1, 260.7, 1392.1, 300.4, 1386.2, 323.3, 1387.6, 331.7, 1385.8, 341, 1381.1, 348.9, 1374, 354.6, 1354.8, 359.6, 1344.7, 357.5, 1336.4, 352, 1330.8, 343.7, 1328.8, 332.5, 1331.8, 318.4, 1340.1, 296.2, 1341.2, 258.6, 1342.9, 247.1, 1345.7, 238.3, 1349.6, 232.3, 1361.7, 224.6 ] ],
            "area": 6695,
            "bbox": [ 1329, 224, 66, 136 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#b068ea",
            "keypoints": [ 1377, 315, 2, 1346, 311, 2, 1381, 243, 2, 1362, 240, 2, 1378, 339, 2, 1337, 342, 2 ],
            "metadata": {},
            "milliseconds": 18928,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613614680 },
                    "user": "j",
                    "milliseconds": 4732,
                    "tools_used": [ "Select" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 846,
            "image_id": 637,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 762.7, 323.6, 772.8, 325.7, 781.1, 331.3, 786.7, 339.5, 788.7, 351.5, 785, 375.7, 788.1, 414, 786, 424.5, 780.5, 432.7, 772.2, 438.3, 762.1, 440.3, 743.4, 436.4, 735.5, 430.8, 730.2, 422.6, 728.2, 412.8, 730.8, 400, 733.7, 364.6, 739.1, 338.8, 744.7, 330.9, 752.8, 325.6 ] ],
            "area": 5744,
            "bbox": [ 728, 324, 61, 116 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#d0bd1b",
            "keypoints": [ 777, 405, 2, 743, 398, 2, 775, 341, 2, 755, 339, 2, 775, 424, 2, 740, 422, 2 ],
            "metadata": {},
            "milliseconds": 20790,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613792746 },
                    "user": "j",
                    "milliseconds": 20790,
                    "tools_used": [ "Eraser", "Keypoints", "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 823,
            "image_id": 710,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 772.6, 351.5, 780.1, 352.9, 786.4, 357, 790.7, 363, 797.1, 381.2, 800.2, 410.4, 799.4, 442, 793.1, 452.7, 787.8, 456.1, 781.5, 457.6, 767.1, 458.5, 759.3, 456.9, 752.9, 452.6, 748.6, 446.2, 747.1, 438.5, 750.2, 409.8, 751.4, 373, 754.5, 362.8, 761.8, 354.6 ] ],
            "area": 4735,
            "bbox": [ 747, 352, 53, 107 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#e514d9",
            "keypoints": [ 789, 401, 2, 760, 406, 2, 783, 362, 2, 764, 362, 2, 790, 448, 2, 759, 449, 2 ],
            "metadata": {},
            "milliseconds": 29411,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612746301 },
                    "user": "j",
                    "milliseconds": 6945,
                    "tools_used": [ "Select", "Brush" ]
                },
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612746301 },
                    "user": "j",
                    "milliseconds": 8576,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 824,
            "image_id": 710,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1169, 342.8, 1175.8, 344, 1181.6, 347.3, 1186, 352.3, 1188.5, 358.6, 1193.7, 365.3, 1200.2, 389.4, 1207.7, 428.9, 1209.7, 449.2, 1208.1, 457, 1203.9, 463.3, 1197.5, 467.6, 1189.7, 469.2, 1172.6, 468.5, 1162.8, 464.9, 1156.3, 457.2, 1154, 447.9, 1153.4, 422.9, 1148, 365.7, 1150.9, 354.2, 1158.2, 346 ] ],
            "area": 5950,
            "bbox": [ 1148, 343, 62, 126 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#2db659",
            "keypoints": [ 1199, 440, 2, 1169, 456, 2, 1178, 356, 2, 1162, 358, 2, 1200, 454, 2, 1169, 457, 2 ],
            "metadata": {},
            "milliseconds": 39470,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612738408 },
                    "user": "j",
                    "milliseconds": 7894,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 825,
            "image_id": 710,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1234.6, 332.8, 1242.4, 334.4, 1248.8, 338.6, 1253.1, 345, 1256.5, 363.8, 1256.2, 379.4, 1260.9, 398.6, 1261.9, 413.4, 1257.9, 425.9, 1248, 433.3, 1241.2, 434.3, 1219.3, 431.8, 1212.9, 427.5, 1208.7, 421.2, 1207.1, 413.4, 1213.7, 353.9, 1216.6, 344.2, 1223.8, 335.9 ] ],
            "area": 4408,
            "bbox": [ 1207, 333, 55, 101 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#158ebd",
            "keypoints": [ 1255, 415, 2, 1221, 418, 2, 1245, 346, 2, 1226, 345, 2, 1255, 420, 2, 1218, 418, 2 ],
            "metadata": {},
            "milliseconds": 22612,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612732756 },
                    "user": "j",
                    "milliseconds": 5653,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 826,
            "image_id": 710,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1263.9, 369.1, 1265.5, 361.3, 1269.8, 355, 1276.1, 350.7, 1283.9, 349.1, 1294.4, 352.1, 1300, 351.3, 1310.9, 354.6, 1318.2, 363, 1320.4, 369, 1323.4, 383.9, 1323.4, 395, 1329.3, 403, 1330.9, 410.9, 1329.4, 418.7, 1325.1, 425, 1318.7, 429.3, 1310.9, 430.9, 1297.1, 427.1, 1280.2, 428.7, 1272.4, 427.1, 1266, 422.8, 1261.7, 416.5, 1260.2, 408.7, 1263.9, 369.3 ] ],
            "area": 4583,
            "bbox": [ 1260, 349, 71, 82 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#1d199a",
            "keypoints": [ 1318, 410, 2, 1268, 410, 2, 1312, 362, 2, 1273, 360, 2, 1318, 413, 2, 1269, 410, 2 ],
            "metadata": {},
            "milliseconds": 92518,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612686498 },
                    "user": "j",
                    "milliseconds": 46259,
                    "tools_used": [ "Select", "Keypoints", "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 827,
            "image_id": 711,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 653.3, 281.1, 655, 272.5, 659.7, 265.5, 666.7, 260.8, 675.3, 259.1, 683.3, 260.6, 690, 264.7, 694.8, 270.9, 700.7, 290.5, 698.8, 308, 699.5, 334.3, 701.8, 351.2, 700.1, 359.7, 695.4, 366.7, 688.4, 371.4, 670.4, 374.3, 661.1, 372.6, 654.1, 367.8, 649.4, 360.9, 647.6, 349.6, 651.8, 318, 653.3, 281.8 ] ],
            "area": 5135,
            "bbox": [ 648, 259, 54, 115 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#7ac12d",
            "keypoints": [ 693, 287, 2, 662, 294, 2, 690, 278, 2, 665, 278, 2, 692, 358, 2, 660, 359, 2 ],
            "metadata": {},
            "milliseconds": 32515,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612856468 },
                    "user": "j",
                    "milliseconds": 7192,
                    "tools_used": [ "Select" ]
                },
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613122630 },
                    "user": "j",
                    "milliseconds": 10939,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 828,
            "image_id": 711,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 745.8, 233.4, 754.3, 235.2, 761.3, 239.9, 766, 246.9, 767.8, 256.2, 762.7, 313.7, 762.9, 354.9, 761.1, 363.6, 756.2, 370.7, 749.2, 375.5, 740.5, 377.3, 733, 376.1, 726.8, 372.8, 722, 367.8, 716.2, 350, 717.4, 319.1, 722.3, 280.4, 722.7, 256.9, 727.1, 243.8, 734.9, 236.3 ] ],
            "area": 5964,
            "bbox": [ 716, 233, 52, 144 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#32debb",
            "keypoints": [ 754, 361, 2, 728, 351, 2, 756, 247, 2, 736, 248, 2, 756, 353, 2, 729, 353, 2 ],
            "metadata": {},
            "milliseconds": 40933,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612784683 },
                    "user": "j",
                    "milliseconds": 16323,
                    "tools_used": [ "Select", "Keypoints", "Select" ]
                },
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613114344 },
                    "user": "j",
                    "milliseconds": 8287,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 829,
            "image_id": 711,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 793.6, 248.5, 802.2, 250.2, 809.2, 255, 813.9, 261.9, 815.6, 270.5, 811.9, 296.3, 813.4, 307.8, 811.1, 330, 811.5, 345.5, 809.6, 365.5, 810.7, 374.9, 809.4, 382.4, 803.7, 391.8, 796.7, 396.6, 788, 398.4, 780.9, 397.4, 770.3, 390, 762.8, 376.1, 761.8, 369.6, 766.4, 337.1, 765.6, 314.6, 771.7, 267, 775.6, 257.9, 780.4, 252.9, 786.5, 249.7 ] ],
            "area": 6350,
            "bbox": [ 762, 249, 54, 149 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#ae6aed",
            "keypoints": [ 798, 380, 2, 774, 371, 2, 804, 264, 2, 786, 264, 2, 799, 371, 2, 775, 370, 2 ],
            "metadata": {},
            "milliseconds": 84736,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612801006 },
                    "user": "j",
                    "milliseconds": 24725,
                    "tools_used": [ "Select", "Keypoints", "Select" ]
                },
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613096703 },
                    "user": "j",
                    "milliseconds": 17643,
                    "tools_used": [ "Select", "Brush", "Select" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 830,
            "image_id": 711,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 995.1, 292.1, 997.1, 282, 1002.7, 273.7, 1010.9, 268.1, 1021.1, 266.1, 1030.9, 268, 1039, 273.2, 1044.6, 281, 1047.7, 296.6, 1047.7, 314.7, 1054.2, 348.6, 1060.4, 364.3, 1063.3, 381.3, 1061.5, 400.6, 1056.6, 408.5, 1049.2, 414.2, 1031.5, 418.4, 1017.2, 416.2, 1008.9, 410.4, 1003, 402, 999.2, 390.6, 994.4, 355.9, 995.1, 292.7 ] ],
            "area": 8180,
            "bbox": [ 994, 266, 69, 152 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#31ed1c",
            "keypoints": [ 1051, 388, 2, 1021, 392, 2, 1034, 286, 2, 1014, 288, 2, 1050, 387, 2, 1020, 391, 2 ],
            "metadata": {},
            "milliseconds": 13018,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612993305 },
                    "user": "j",
                    "milliseconds": 1927,
                    "tools_used": [ "Select", "Brush" ]
                },
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613092123 },
                    "user": "j",
                    "milliseconds": 4582,
                    "tools_used": [ "Select" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 831,
            "image_id": 711,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1091.4, 234.1, 1093.5, 224, 1099, 215.7, 1107.3, 210.2, 1117.4, 208.1, 1127.5, 210.1, 1135.7, 215.6, 1141.3, 223.8, 1149.9, 258.8, 1152.5, 283.9, 1157.7, 311.3, 1168.5, 335.6, 1170.1, 344.8, 1169, 353.7, 1163.9, 367.3, 1159.2, 373, 1151.2, 378.8, 1138.9, 381.9, 1127.5, 379.8, 1119.2, 374.3, 1113.7, 366, 1109.8, 332.8, 1101.9, 297.2, 1098.7, 269.7, 1092.6, 246.3, 1091.4, 234.8 ] ],
            "area": 8760,
            "bbox": [ 1091, 208, 79, 174 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#4d1dac",
            "keypoints": [ 1157, 336, 2, 1123, 361, 2, 1131, 225, 2, 1105, 226, 2, 1154, 319, 2, 1117, 323, 2 ],
            "metadata": {},
            "milliseconds": 4096,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612992282 },
                    "user": "j",
                    "milliseconds": 1024,
                    "tools_used": [ "Select" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 832,
            "image_id": 711,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1236.4, 253.7, 1244.7, 310.4, 1249.4, 331.1, 1247.9, 343.5, 1243.6, 349.8, 1237.2, 354.1, 1219.7, 356.4, 1198.2, 354.8, 1191.9, 350.5, 1187.6, 344.1, 1186, 336.4, 1184, 303.8, 1184, 261.5, 1186, 252.5, 1194.2, 240.1, 1209.3, 233.4, 1216.4, 232.3, 1224.2, 233.9, 1230.6, 238.2, 1234.8, 244.6, 1236.4, 253 ] ],
            "area": 6662,
            "bbox": [ 1184, 232, 65, 124 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#efaf3e",
            "keypoints": [ 1236, 343, 2, 1200, 344, 2, 1223, 248, 2, 1199, 248, 2, 1235, 343, 2, 1201, 343, 2 ],
            "metadata": {},
            "milliseconds": 17373,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612960931 },
                    "user": "j",
                    "milliseconds": 5791,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 833,
            "image_id": 711,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1348, 239.5, 1355.9, 241.2, 1374.3, 252.4, 1377.8, 258.3, 1379, 265.4, 1377.1, 276, 1377.1, 325.3, 1374.2, 343.5, 1369.9, 349.8, 1363.6, 354.1, 1355.8, 355.7, 1335.3, 353, 1322.8, 348.2, 1315.4, 338.3, 1314.3, 331.8, 1322.8, 291.4, 1324.1, 269.9, 1327.3, 255.7, 1332.8, 246.4, 1340, 241.2 ] ],
            "area": 5949,
            "bbox": [ 1314, 240, 65, 116 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#bc2a79",
            "keypoints": [ 1364, 344, 2, 1327, 336, 2, 1373, 260, 2, 1342, 254, 2, 1366, 342, 2, 1326, 335, 2 ],
            "metadata": {},
            "milliseconds": 78346,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587612921759 },
                    "user": "j",
                    "milliseconds": 39173,
                    "tools_used": [ "Select", "Keypoints", "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 834,
            "image_id": 713,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 722, 274.2, 732.1, 276.3, 740.4, 281.8, 746, 290.1, 748, 300.5, 752.6, 308.3, 754.3, 320.2, 766.9, 354.6, 773.8, 387, 773.8, 401.8, 771.8, 411.9, 766.2, 420.2, 757.9, 425.8, 747.8, 427.8, 725.9, 427.8, 716.2, 426, 708.2, 420.8, 702.6, 413.2, 700, 403.8, 695.2, 359.6, 693.7, 336.2, 694.5, 304.9, 698.4, 289.4, 702.3, 283.3, 714.5, 275.3 ] ],
            "area": 9591,
            "bbox": [ 694, 274, 80, 154 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#3c0eed",
            "keypoints": [ 752, 358, 2, 716, 382, 2, 732, 290, 2, 710, 298, 2, 759, 403, 2, 719, 410, 2 ],
            "metadata": {},
            "milliseconds": 129477,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613342404 },
                    "user": "j",
                    "milliseconds": 60431,
                    "tools_used": [ "Select", "Brush" ]
                },
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613342404 },
                    "user": "j",
                    "milliseconds": 8615,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 835,
            "image_id": 713,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 781.2, 288.5, 783.3, 278.4, 788.8, 270.1, 797.1, 264.6, 807.2, 262.5, 817.3, 264.6, 825.6, 270.1, 831.2, 278.4, 834, 295.5, 834, 310.4, 832.2, 319.8, 834.8, 333.8, 834.8, 361.2, 832.4, 384.6, 827.1, 408.5, 821.4, 415.8, 813.5, 420.6, 801, 422.4, 784.8, 419.3, 776.8, 413.6, 771.4, 405.5, 769.5, 395.6, 773.4, 371.1, 774.2, 335.4, 782, 304.6, 781.2, 289.7 ] ],
            "area": 8524,
            "bbox": [ 770, 263, 65, 159 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#f368e3",
            "keypoints": [ 816, 314, 2, 793, 315, 2, 809, 282, 2, 802, 282, 2, 817, 405, 2, 781, 407, 2 ],
            "metadata": {},
            "milliseconds": 25458,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613333919 },
                    "user": "j",
                    "milliseconds": 8486,
                    "tools_used": [ "Select", "Brush", "Select" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 836,
            "image_id": 713,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1217.3, 312, 1219.3, 301.8, 1224.9, 293.6, 1233.1, 288, 1243.3, 286, 1253.4, 288, 1261.7, 293.6, 1267.2, 301.8, 1269.3, 312, 1267.4, 338.8, 1270.8, 351.8, 1269.3, 397.1, 1265.1, 415.6, 1259.5, 423.1, 1251.6, 428.2, 1233.1, 431.7, 1223, 429.7, 1214.7, 424.1, 1209.2, 415.9, 1207.1, 405.7, 1207.9, 394, 1217.3, 313.1 ] ],
            "area": 7612,
            "bbox": [ 1207, 286, 64, 146 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#f73abc",
            "keypoints": [ 1253, 394, 2, 1221, 407, 2, 1252, 307, 2, 1236, 304, 2, 1253, 410, 2, 1221, 406, 2 ],
            "metadata": {},
            "milliseconds": 26928,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613324944 },
                    "user": "j",
                    "milliseconds": 8976,
                    "tools_used": [ "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        },
        {
            "id": 837,
            "image_id": 713,
            "category_id": 4,
            "dataset_id": 10,
            "segmentation": [ [ 1333.1, 304, 1345.2, 307.6, 1362.5, 324.9, 1366.1, 337, 1366.1, 354.9, 1364.2, 370.6, 1366.1, 387, 1366.1, 408.1, 1364.3, 416.6, 1359.6, 423.6, 1352.6, 428.3, 1344.1, 430.1, 1305.8, 426.8, 1298.8, 422.1, 1294.1, 415.1, 1292.4, 406.5, 1298.6, 371.8, 1312, 319.8, 1315, 313.5, 1319.8, 308.5, 1326, 305.2 ] ],
            "area": 7448,
            "bbox": [ 1292, 304, 74, 126 ],
            "iscrowd": False,
            "isbbox": False,
            "creator": "j",
            "width": 1976,
            "height": 976,
            "color": "#734de7",
            "keypoints": [ 1349, 409, 2, 1323, 340, 2, 1351, 326, 2, 1330, 322, 2, 1348, 418, 2, 1308, 412, 2 ],
            "metadata": {},
            "milliseconds": 90234,
            "events": [
                {
                    "_cls": "SessionEvent",
                    "created_at": { "$date": 1587613279828 },
                    "user": "j",
                    "milliseconds": 45117,
                    "tools_used": [ "Select", "Keypoints", "Select", "Brush" ]
                }
            ],
            "num_keypoints": 6
        }
    ]
}

listA = [{img["id"]: img["path"]} for img in anno["images"]]
dictA = {}
for d in listA:
    dictA.update(d)

print(listA) # i. 잘 작동!
print(dictA) # i. 잘 작동!