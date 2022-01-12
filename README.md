# ColorizationWithRegion

The code for pg2021 paper "Line Art Colorization Based on Explicit Region Segmentation"

This is a simple implementation for comparison with **Tag2Pix** ([code](https://github.com/blandocs/Tag2Pix) / [paper](http://arxiv.org/abs/1908.05840)).

Overall project refactoring and further optimization may be later.

## Usage

1. Build the environment and dataset according to **Tag2Pix**.

2. Use `python code/skeleton/line_art2skeleton.py <line art folder>` to create **skeleton maps**.

    See [DanbooRegion](https://github.com/lllyasviel/DanbooRegion) for environment.

    Some code and pretrained model are from [DanbooRegion](https://github.com/lllyasviel/DanbooRegion).

    For each **line art** folders, e.g., `keras_train`, `xdog_train`, `keras_test` or others, create a corresponding folder to place **skeleton maps**, like `keras_train_skeleton` and others.

3. Replace `loader/dataloader.py` of Tag2Pix with `code/loader/dataloader.py` to load **skeleton maps**.

    We also remove the `random_jitter` for visible test results while training.

4. For **dual-branch**, replace `network.py` and `tag2pix.py` of Tag2Pix with files in `code/dual_branch`.

5. For **direct concatenation**, replace `network.py` and `tag2pix.py` of Tag2Pix with files in `code/direct`.

6. Train the model as Tag2Pix.