import xgboost as xgb
#123123
def train_xgb(X_tr, y_tr, X_va, y_va, params):
    dtr, dva = xgb.DMatrix(X_tr, label=y_tr), xgb.DMatrix(X_va, label=y_va)
    booster = xgb.train(params, dtr, num_boost_round=200,
                        evals=[(dva, "val")], early_stopping_rounds=20)
    return booster
