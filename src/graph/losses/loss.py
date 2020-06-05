# -*- coding: utf-8 -*-
# @Author: chengdlin2
# @Date:   2020-03-26 16:43:14
# @Last Modified by:   chengdlin2
# @Last Modified time: 2020-03-26 16:43:24
import torch

class HeatmapLoss(torch.nn.Module):
    """
    loss for detection heatmap
    """
    def __init__(self):
        super(HeatmapLoss, self).__init__()

    def forward(self, pred, gt):
        l = ((pred - gt)**2)
        l = l.mean(dim=3).mean(dim=2).mean(dim=1)
        return l ## l of dim bsize