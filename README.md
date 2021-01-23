# ML_preprocessing

This repository holds some scripts and python notebooks that have helped me to preprocess Image data for ML training.

### extract_frames.py

This script takes a video file as input and saves 1 frame per `n` frames. `--n` is a user input. Depending on the number of images required, this number can be tweaked. The default value has been set to `10`.

#### Running 
```
python3 extract_frames <path-to-video> <path-to-output-folder> --n <N>
```

### Preprocessing data
Open the preprocessing.ipynb file. This file contains code and documentation on usage.
