# Colour History and Distractor Effects in Interleaved and Blocked Visual Search

Secondary analysis of Experiment 3 from Adam, Patel, Rangan & Serences (2021), *Journal of Cognition*, DOI 10.5334/joc.182.

This is an independent reanalysis of published open data. It is not the original experiment, and the original authors' findings are not claimed as the author's own.

## Status
- Primary models run in Python (statsmodels) and reproduced in R (lme4, lmerTest); estimates agree to two decimals.
- RT is in milliseconds (inferred from value range); each cell is the mean of responded trials of at least 200 ms, correct and incorrect together.
- Accuracy is computed over all trials and is not filtered in the same way as RT.
- The random-slope sensitivity model is singular in both implementations and is not reported as a robustness check.
- Post hoc exclusion of two pilot participants leaves RT conclusions unchanged; the accuracy effect is sample-dependent.

## Reproduce
Place `Search_3a_agg_long.csv` and `Search_3b_agg_long.csv` (from OSF project u7wvy) in `data/raw/`, then run:
