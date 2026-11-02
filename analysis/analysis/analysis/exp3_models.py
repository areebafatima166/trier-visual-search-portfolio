"""Secondary analysis of Adam et al. (2021) Experiment 3 aggregate data.
Python/statsmodels. Reproduced in R: r/exp3_models.R."""
import sys, warnings
import pandas as pd, statsmodels.formula.api as smf
warnings.filterwarnings("ignore")
SRC = sys.argv[1]  # directory containing the two CSVs
out = []

def load(fname, sample_label):
    d = pd.read_csv(f"{SRC}/{fname}")
    d["sample"] = sample_label
    d["subject_id"] = sample_label + "_" + d["subject"].astype(str)
    return d

# Assign sample from color_cond_blocking, not the mislabelled experiment column
d = pd.concat([load("Search_3a_agg_long.csv", "3a"), load("Search_3b_agg_long.csv", "3b")], ignore_index=True)
d["blocking"] = d["color_cond_blocking"].map({"interleaved": "interleaved", "blocked": "blocked"})
d["distractor"] = d["distractor"].astype("category")
d["color_history"] = d["color_history"].astype("category")
d["blocking"] = d["blocking"].astype("category")

out.append(f"N rows: {len(d)}; subjects: {d['subject_id'].nunique()}")
out.append(f"Rows per sample: {d['sample'].value_counts().to_dict()}")
out.append("")

def fit(formula, label, data=d):
    m = smf.mixedlm(formula, data, groups=data["subject_id"]).fit(reml=True, method="lbfgs")
    out.append(f"=== {label} ===")
    out.append(f"Formula: {formula}")
    out.append(f"Converged: {m.converged}")
    tab = pd.DataFrame({"coef": m.fe_params, "se": m.bse_fe, "z": m.tvalues, "p": m.pvalues})
    tab["ci_low"] = m.fe_params - 1.96 * m.bse_fe
    tab["ci_high"] = m.fe_params + 1.96 * m.bse_fe
    out.append(tab.round(4).to_string())
    out.append("")
    return m

# Primary models
fit("rt ~ distractor * color_history * blocking", "P1 RT, primary")
fit("acc ~ distractor * color_history * blocking", "P2 accuracy, primary")

# Sensitivity S1: within each sample
for s in ["3a", "3b"]:
    sub = d[d["sample"] == s].copy()
    fit("rt ~ distractor * color_history", f"S1 RT, sample {s}", sub)
    fit("acc ~ distractor * color_history", f"S1 accuracy, sample {s}", sub)

open("results/exp3_model_results.txt", "w").write("\n".join(out))
print("\n".join(out))
