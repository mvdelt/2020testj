
import numpy as np
from abc import ABCMeta, abstractmethod
from typing import Callable, TypeVar
import torch


class Transform(metaclass=ABCMeta):
    """
    Base class for implementations of __deterministic__ transformations for
    image and other data structures. "Deterministic" requires that the output of
    all methods of this class are deterministic w.r.t their input arguments. In
    training, there should be a higher-level policy that generates (likely with
    random variations) these transform ops. Each transform op may handle several
    data types, e.g.: image, coordinates, segmentation, bounding boxes. Some of
    them have a default implementation, but can be overwritten if the default
    isn't appropriate. The implementation of each method may choose to modify
    its input data in-place for efficient transformation.
    """

    def _set_attributes(self, params: list = None): # i. 오타임. 타입이 list 대신 dict 여야함. 근데, 파이썬의 타입힌트는 아무 강제성이 없어서, 이렇게해놓고도 걍 딕셔너리 넣어도 잘 작동함.
        """
        Set attributes from the input list of parameters.

        Args:
            params (list): list of parameters.   # i. 설명도 오타. list대신 dict여야함.
        """

        if params:
            for k, v in params.items():
                if k != "self" and not k.startswith("_"):
                    setattr(self, k, v)

    # @abstractmethod
    # def apply_image(self, img: np.ndarray):
    #     """
    #     Apply the transform on an image.

    #     Args:
    #         img (ndarray): of shape NxHxWxC, or HxWxC or HxW. The array can be
    #             of type uint8 in range [0, 255], or floating point in range
    #             [0, 1] or [0, 255].
    #     Returns:
    #         ndarray: image after apply the transformation.
    #     """
    #     pass

    # @abstractmethod
    # def apply_coords(self, coords: np.ndarray):
    #     """
    #     Apply the transform on coordinates.

    #     Args:
    #         coords (ndarray): floating point array of shape Nx2. Each row is (x, y).

    #     Returns:
    #         ndarray: coordinates after apply the transformation.

    #     Note:
    #         The coordinates are not pixel indices. Coordinates on an image of
    #         shape (H, W) are in range [0, W] or [0, H].
    #     """

    #     pass

    # def apply_segmentation(self, segmentation: np.ndarray) -> np.ndarray:
    #     """
    #     Apply the transform on a full-image segmentation.
    #     By default will just perform "apply_image".

    #     Args:
    #         segmentation (ndarray): of shape HxW. The array should have integer
    #         or bool dtype.

    #     Returns:
    #         ndarray: segmentation after apply the transformation.
    #     """
    #     return self.apply_image(segmentation)

    # def apply_box(self, box: np.ndarray) -> np.ndarray:
    #     """
    #     Apply the transform on an axis-aligned box.
    #     By default will transform the corner points and use their
    #     minimum/maximum to create a new axis-aligned box.
    #     Note that this default may change the size of your box, e.g. in
    #     rotations.

    #     Args:
    #         box (ndarray): Nx4 floating point array of XYXY format in absolute
    #             coordinates.
    #     Returns:
    #         ndarray: box after apply the transformation.

    #     Note:
    #         The coordinates are not pixel indices. Coordinates on an image of
    #         shape (H, W) are in range [0, W] or [0, H].
    #     """
    #     # Indexes of converting (x0, y0, x1, y1) box into 4 coordinates of
    #     # ([x0, y0], [x1, y0], [x0, y1], [x1, y1]).
    #     idxs = np.array([(0, 1), (2, 1), (0, 3), (2, 3)]).flatten()
    #     coords = np.asarray(box).reshape(-1, 4)[:, idxs].reshape(-1, 2)
    #     coords = self.apply_coords(coords).reshape((-1, 4, 2))
    #     minxy = coords.min(axis=1)
    #     maxxy = coords.max(axis=1)
    #     trans_boxes = np.concatenate((minxy, maxxy), axis=1)
    #     return trans_boxes

    # def apply_polygons(self, polygons: list) -> list:
    #     """
    #     Apply the transform on a list of polygons, each represented by a Nx2
    #     array.
    #     By default will just transform all the points.

    #     Args:
    #         polygon (list[ndarray]): each is a Nx2 floating point array of
    #             (x, y) format in absolute coordinates.
    #     Returns:
    #         list[ndarray]: polygon after apply the transformation.

    #     Note:
    #         The coordinates are not pixel indices. Coordinates on an image of
    #         shape (H, W) are in range [0, W] or [0, H].
    #     """
    #     return [self.apply_coords(p) for p in polygons]

    # @classmethod
    # def register_type(cls, data_type: str, func: Callable):
    #     """
    #     Register the given function as a handler that this transform will use
    #     for a specific data type.

    #     Args:
    #         data_type (str): the name of the data type (e.g., box)
    #         func (callable): takes a transform and a data, returns the
    #             transformed data.

    #     Examples:

    #     .. code-block:: python

    #         def func(flip_transform, voxel_data):
    #             return transformed_voxel_data
    #         HFlipTransform.register_type("voxel", func)

    #         # ...
    #         transform = HFlipTransform(...)
    #         transform.apply_voxel(voxel_data)  # func will be called
    #     """
    #     assert callable(
    #         func
    #     ), "You can only register a callable to a Transform. Got {} instead.".format(
    #         func
    #     )
    #     argspec = inspect.getfullargspec(func)
    #     assert len(argspec.args) == 2, (
    #         "You can only register a function that takes two positional "
    #         "arguments to a Transform! Got a function with spec {}".format(
    #             str(argspec)
    #         )
    #     )
    #     setattr(cls, "apply_" + data_type, func)


class CropTransform(Transform):
    def __init__(self, x0: int, y0: int, w: int, h: int):
        """
        Args:
            x0, y0, w, h (int): crop the image(s) by img[y0:y0+h, x0:x0+w].
        """
        # super().__init__()
        print(locals())
        self._set_attributes(locals())

    # def apply_image(self, img: np.ndarray) -> np.ndarray:
    #     """
    #     Crop the image(s).

    #     Args:
    #         img (ndarray): of shape NxHxWxC, or HxWxC or HxW. The array can be
    #             of type uint8 in range [0, 255], or floating point in range
    #             [0, 1] or [0, 255].
    #     Returns:
    #         ndarray: cropped image(s).
    #     """
    #     if len(img.shape) <= 3:
    #         return img[self.y0 : self.y0 + self.h, self.x0 : self.x0 + self.w]
    #     else:
    #         return img[
    #             ..., self.y0 : self.y0 + self.h, self.x0 : self.x0 + self.w, :
    #         ]

    # def apply_coords(self, coords: np.ndarray) -> np.ndarray:
    #     """
    #     Apply crop transform on coordinates.

    #     Args:
    #         coords (ndarray): floating point array of shape Nx2. Each row is
    #             (x, y).
    #     Returns:
    #         ndarray: cropped coordinates.
    #     """
    #     coords[:, 0] -= self.x0
    #     coords[:, 1] -= self.y0
    #     return coords

    # def apply_polygons(self, polygons: list) -> list:
    #     """
    #     Apply crop transform on a list of polygons, each represented by a Nx2 array.
    #     It will crop the polygon with the box, therefore the number of points in the
    #     polygon might change.

    #     Args:
    #         polygon (list[ndarray]): each is a Nx2 floating point array of
    #             (x, y) format in absolute coordinates.
    #     Returns:
    #         ndarray: cropped polygons.
    #     """
    #     import shapely.geometry as geometry

    #     # Create a window that will be used to crop
    #     crop_box = geometry.box(
    #         self.x0, self.y0, self.x0 + self.w, self.y0 + self.h
    #     ).buffer(0.0)

    #     cropped_polygons = []

    #     for polygon in polygons:
    #         polygon = geometry.Polygon(polygon).buffer(0.0)
    #         # polygon must be valid to perform intersection.
    #         assert polygon.is_valid, polygon
    #         cropped = polygon.intersection(crop_box)
    #         if cropped.is_empty:
    #             continue
    #         if not isinstance(
    #             cropped, geometry.collection.BaseMultipartGeometry
    #         ):
    #             cropped = [cropped]
    #         # one polygon may be cropped to multiple ones
    #         for poly in cropped:
    #             # It could produce lower dimensional objects like lines or
    #             # points, which we want to ignore
    #             if not isinstance(poly, geometry.Polygon) or not poly.is_valid:
    #                 continue
    #             coords = np.asarray(poly.exterior.coords)
    #             # NOTE This process will produce an extra identical vertex at
    #             # the end. So we remove it. This is tested by
    #             # `tests/test_data_transform.py`
    #             cropped_polygons.append(coords[:-1])
    #     return [self.apply_coords(p) for p in cropped_polygons]

cropTr = CropTransform(511,1011,71,81)
print(cropTr.x0, cropTr.y0, cropTr.w, cropTr.h)
