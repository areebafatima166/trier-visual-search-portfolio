# R reproduction of the Python primary models (analysis/exp3_models.py)
# Same data preparation, same fixed effects, random intercept per participant, REML.
# p-values from lmerTest (Satterthwaite df); Python used Wald z. Expect small p-value differences.
suppressPackageStartupMessages({ library(readr); library(dplyr); library(lme4); library(lmerTest) })

args <- commandArgs(trailingOnly = TRUE)
src <- ifelse(length(args) >= 1, args[1], ".")

load_one <- function(f, s) {
  read_csv(file.path(src, f), show_col_types = FALSE) %>%
    mutate(sample = s, subject_id = paste0(s, "_", subject))
}
d <- bind_rows(load_one("Search_3a_agg_long.csv", "3a"),
               load_one("Search_3b_agg_long.csv", "3b")) %>%
  mutate(dp = as.integer(distractor == "present"),
         ch = as.integer(color_history == "variable"),
         bl = as.integer(color_cond_blocking == "interleaved"))

cat("Rows:", nrow(d), "| participants:", n_distinct(d$subject_id), "\n\n")

cat("=== P1 RT (primary) ===\n")
m_rt <- lmer(rt ~ dp * ch * bl + (1 | subject_id), data = d, REML = TRUE)
print(summary(m_rt)$coefficients)
cat("\n=== P2 accuracy (primary) ===\n")
m_acc <- lmer(acc ~ dp * ch * bl + (1 | subject_id), data = d, REML = TRUE)
print(summary(m_acc)$coefficients)

cat("\n=== S2 RT: random distractor slope ===\n")
s2_rt <- tryCatch(lmer(rt ~ dp * ch * bl + (1 + dp | subject_id), data = d, REML = TRUE),
                  warning = function(w) { cat("WARNING:", conditionMessage(w), "\n"); NULL })
if (!is.null(s2_rt)) print(VarCorr(s2_rt))

cat("\n=== S2 accuracy: random distractor slope ===\n")
s2_acc <- tryCatch(lmer(acc ~ dp * ch * bl + (1 + dp | subject_id), data = d, REML = TRUE),
                   warning = function(w) { cat("WARNING:", conditionMessage(w), "\n"); NULL })
if (!is.null(s2_acc)) print(VarCorr(s2_acc))
