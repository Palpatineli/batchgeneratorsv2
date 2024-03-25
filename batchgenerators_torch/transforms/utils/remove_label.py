from typing import Union, Tuple, List

import torch

from batchgenerators_torch.transforms.base.basic_transform import SegOnlyTransform


class RemoveLabelTansform(SegOnlyTransform):
    def __init__(self, label_value: int, set_to: int, segmentation_channels: Union[int, Tuple[int, ...], List[int]] = None):
        if not isinstance(segmentation_channels, (list, tuple)) and segmentation_channels is not None:
            segmentation_channels = [segmentation_channels]
        self.segmentation_channels = segmentation_channels
        self.label_value = label_value
        self.set_to = set_to
        super().__init__()

    def get_parameters(self, **data_dict) -> dict:
        return {}

    def _apply_to_segmentation(self, segmentation: torch.Tensor, **params) -> torch.Tensor:
        if self.segmentation_channels is None:
            channels = list(range(segmentation.shape[0]))
        else:
            channels = self.segmentation_channels
        for s in channels:
            segmentation[s][segmentation[s] == self.label_value] = self.set_to
        return segmentation
