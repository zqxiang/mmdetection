from .builder import DATASETS
from .coco import CocoDataset


@DATASETS.register_module()
class FruitsNutsDataset(CocoDataset):
    CLASSES = ("date", "fig", "hazelnut")
