from copy import copy
from mimetypes import init
from cv2 import drawMatches
import torch.nn as nn
import copy
class BaseModule(nn.Module):
    def __init__(self, init_cfg=None) -> None:
        super(BaseModule, self).__init__()
        self._is_init=False
        self.init_cfg=copy.deepcopy(init_cfg)
drawMatches