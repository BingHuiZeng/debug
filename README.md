# Install
python setup.py develop

# Useage
## debug_line

debug_line output the debug information of the input variable and the line of the code where the variable is defined.

Add code like this:
```python
from debug import debug_line

print("batch_dict",debug_line(batch_dict))
```

Output:
```txt
 batch_dict   {
    "frame_id": "(3,)",
    "calib": [<pcdet.utils.calibration_kitti.Calibration object at 0x7f441010ac40>,<pcdet.utils.calibration_kitti.Calibration object at 0x7f441028acd0>,<pcdet.utils.calibration_kitti.Calibration object at 0x7f441028a5b0>
    ],
    "gt_boxes": "torch.Size([3, 30, 8])",
    "lidar_points": "torch.Size([80188, 5])",
    "radar_points": "torch.Size([3350, 9])",
    "image_paths": "(3, 1)",
    "lidar2camera": "torch.Size([3, 1, 4, 4])",
    "lidar2image": "torch.Size([3, 1, 5, 4])",
    "camera_intrinsics": "torch.Size([3, 1, 5, 4])",
    "camera_imgs": "torch.Size([3, 1, 3, 256, 704])",
    "ori_shape": "(3, 2)",
    "img_process_infos": "(3, 1, 4)",
    "lidar_aug_matrix": "torch.Size([3, 4, 4])",
    "use_lead_xyz": "torch.Size([3])",
    "lidar_voxels": "torch.Size([6916, 32, 4])",
    "lidar_voxel_coords": "torch.Size([6916, 4])",
    "lidar_voxel_num_points": "torch.Size([6916])",
    "radar_voxels": "torch.Size([1617, 32, 8])",
    "radar_voxel_coords": "torch.Size([1617, 4])",
    "radar_voxel_num_points": "torch.Size([1617])",
    "img_aug_matrix": "torch.Size([3, 1, 4, 4])",
    "image_shape": "torch.Size([3, 2])",
    "fog_intensity": "torch.Size([3])",
    "batch_size": 3,
    "raw_radar_points": "torch.Size([3350, 8])",
    "lidar_pillar_features": "torch.Size([6916, 64])",
    "radar_pillar_features": "torch.Size([1617, 64])",
    "lidar_spatial_features": "torch.Size([3, 64, 320, 320])",
    "radar_spatial_features": "torch.Size([3, 64, 320, 320])",
    "spatial_features": "torch.Size([3, 128, 320, 320])",
    "image_features": [
        "torch.Size([3, 192, 32, 88])",
        "torch.Size([3, 384, 16, 44])",
        "torch.Size([3, 768, 8, 22])"
    ],
] /home/name/project/XXX/tools/../pcdet/datasets/processor/point_feature_encoder.py:30


```

## debug_path
debug_path output the debug information of the code path.

Add code like this:
```python
from debug import debug_path
print("debug_path",debug_path())
```

Output:
```txt
debug_path /home/name/project/XXX/tools/../pcdet/datasets/processor/point_feature_encoder.py:56
/home/name/project/XXX/tools/../pcdet/datasets/processor/point_feature_encoder.py:31
/home/name/project/XXX/tools/../pcdet/models/detectors/voxel_rcnn_ssl.py:798
/home/name/project/XXX/tools/../pcdet/models/detectors/voxel_rcnn_ssl.py:105
/home/name/project/XXX/tools/../pcdet/models/__init__.py:44
/home/name/project/XXX/tools/train_utils/train_utils_ssl.py:62
/home/name/project/XXX/tools/train_utils/train_utils_ssl.py:170
train.py:167
train.py:243
```


