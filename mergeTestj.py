lst1 = [{'id': 1, 'x': "one"},{'id': 2, 'x': "two", 'y': {'y1':'y1val', 'y2':'y2val'}}]
lst2 = [{'id': 2, 'x': "two", 'y': {'y1':'y1val', 'y2':'y2val'}}, {'id': 3, 'x': "three"}]

result = {x['id']:x for x in lst1 + lst2}.values()

print(lst1+lst2)

# print([x for x in lst2 if x not in lst1])

print(lst1 + [x for x in lst2 if x not in lst1])

print({x['id']:x for x in lst1 + lst2})

print(result)

print(lst1[0].values())


#############################################################################

anno1 = {
    "images": [
        {
            "id": 441,
            "dataset_id": 8,
            "category_ids": [ 1 ],
            "path": "/datasets/pa_keypoint_upper2/PA20181212_2nd_save0000.jpg",
            "width": 1440,
            "height": 1920,
            "file_name": "PA20181212_2nd_save0000.jpg",
            "annotated": "true",
            "annotating": [],
            "num_annotations": 2,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": "false",
            "is_modified": "false"
        },
        {
            "id": 442,
            "dataset_id": 8,
            "category_ids": [ 1 ],
            "path": "/datasets/pa_keypoint_upper2/PA20181212_2nd_save0000_0.jpg",
            "width": 1440,
            "height": 1920,
            "file_name": "PA20181212_2nd_save0000_0.jpg",
            "annotated": "true",
            "annotating": [],
            "num_annotations": 2,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": "false",
            "is_modified": "false"
        },
        {
            "id": 443,
            "dataset_id": 8,
            "category_ids": [ 1 ],
            "path": "/datasets/pa_keypoint_upper2/PA20181212_2nd_save0000_1.jpg",
            "width": 1300,
            "height": 1700,
            "file_name": "PA20181212_2nd_save0000_1.jpg",
            "annotated": "true",
            "annotating": [],
            "num_annotations": 4,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": "false",
            "is_modified": "false"
        }
    ],
}


anno2 = {
    "images": [
        {
            "id": 441,
            "dataset_id": 8,
            "category_ids": [ 1 ],
            "path": "/datasets/pa_keypoint_upper2/PA20181212_2nd_save0000.jpg",
            "width": 1440,
            "height": 1920,
            "file_name": "PA20181212_2nd_save0000.jpg",
            "annotated": "true",
            "annotating": [],
            "num_annotations": 2,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": "false",
            "is_modified": "false"
        },
        {
            "id": 442,
            "dataset_id": 8,
            "category_ids": [ 1 ],
            "path": "/datasets/pa_keypoint_upper2/PA20181212_2nd_save0000_0.jpg",
            "width": 1440,
            "height": 1920,
            "file_name": "PA20181212_2nd_save0000_0.jpg",
            "annotated": "true",
            "annotating": [],
            "num_annotations": 2,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": "false",
            "is_modified": "false"
        },
        {
            "id": 443,
            "dataset_id": 8,
            "category_ids": [ 1 ],
            "path": "/datasets/pa_keypoint_upper2/PA20181212_2nd_save0000_1.jpg",
            "width": 1300,
            "height": 1700,
            "file_name": "PA20181212_2nd_save0000_1.jpg",
            "annotated": "true",
            "annotating": [],
            "num_annotations": 4,
            "metadata": {},
            "milliseconds": 0,
            "events": [],
            "regenerate_thumbnail": "false",
            "is_modified": "false"
        }
    ],
}

import json
from collections import OrderedDict

def merge_two_anno_files(anno1, anno2):  

    # # check if there is same image id.
    # anno1_imgid_list = [imginfo["id"] for imginfo in anno1["images"]] # ex: [351, 352, 353, 354, ...]
    # anno2_imgid_list = [imginfo["id"] for imginfo in anno2["images"]]
    # anno1_imgid_set = set(anno1_imgid_list)
    # for i in anno2_imgid_list:
    #     if i in anno1_imgid_set:
    #         raise ValueError('two different annotation json files have the same image id!!! This should not be occured!!! j')
    
    merged_images_list = anno1["images"] + anno2["images"]
    merged_anno = {"images":merged_images_list}

    # merged_anno_as_od = json.loads(str(merged_anno), object_pairs_hook=OrderedDict)
    # print (merged_anno)
    print(json.dumps(merged_anno, indent=4))

merge_two_anno_files(anno1,anno2)

