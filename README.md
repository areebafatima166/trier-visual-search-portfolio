![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23912671.svg)](https://doi.org/10.5281/zenodo.23912671)
# Colour History and Distractor Effects in Interleaved and Blocked Visual Search

Secondary analysis of Experiment 3 from Adam, Patel, Rangan & Serences (2021), *Journal of Cognition*, DOI 10.5334/joc.182.

This is an independent reanalysis of published open data. It is not the original experiment, and the original authors' findings are not claimed as the author's own.

## Status
- Primary models run in Python (statsmodels) and reproduced in R (lme4, lmerTest); estimates agree to two decimals.
- RT is in milliseconds (inferred from value range); each cell is the mean of responded trials of at least 200 ms, correct and incorrect together.
- Accuracy is computed over all trials and is not filtered in the same way as RT.
- The random-slope sensitivity model is singular in both implementations and is not reported as a robustness check.
- Post hoc exclusion of two pilot participants leaves RT conclusions unchanged; the accuracy effect is sample-dependent.

## What's in this repo?
- analysis/ — Python code for primary models (exp3_models.py)
- r/ — R script for reproduction of primary models
- results/ — Model outputs
- requirements.txt — Python dependencies

## Reproduce
Place Search_3a_agg_long.csv and Search_3b_agg_long.csv (from OSF project u7wvy) in data/raw/, then run:

Python:
    pip install -r requirements.txt
    python analysis/exp3_models.py

R:
    Open and run the R script in r/

Original data: https://osf.io/u7wvy/

## Citation
If you use this code, please cite:

> Fatima, A. (2026). Colour History and Distractor Effects in Interleaved and Blocked Visual Search: Secondary Analysis of Experiment 3 (Version v1.0) [Computer software]. Zenodo. https://doi.org/10.5281/zenodo.23912671

## License
MIT License
