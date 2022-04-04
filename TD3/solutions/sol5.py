def objective(trial):
    xgb_params = {
        # Parameter space definition
        'n_estimators': trial.suggest_int('n_estimators', 50, 100),
        'max_depth': trial.suggest_int('max_depth', 5, 10),
        'min_child_weight': trial.suggest_int('min_child_weight', 1, 10),
        'learning_rate': trial.suggest_discrete_uniform('learning_rate', 0.01, 0.3, 0.01),
        'scale_pos_weight': trial.suggest_int('scale_pos_weight', 1, 100),
        'subsample': trial.suggest_discrete_uniform('subsample', 0.5, 1.0, 0.1),
        'colsample_bytree': trial.suggest_discrete_uniform('colsample_bytree', 0.5, 1.0, 0.1),
        'colsample_bylevel': trial.suggest_discrete_uniform('colsample_bylevel', 0.5, 1.0, 0.1),
        'gamma': trial.suggest_discrete_uniform('gamma', 0.0, 1.0, 0.1),
        'reg_lambda': trial.suggest_int('reg_lambda', 1, 100),
    }

    xgb_classifier = XGBClassifier(
        objective='binary:logistic', eval_metric='auc', use_label_encoder=False)
    xgb_classifier.set_params(**xgb_params)
    xgb_classifier.fit(X_train, Y_train, sample_weight=None)
    Y_pred = xgb_classifier.predict(X_test)
    #Y_pred = xgb_classifier.predict_proba(X_test)[:,1]
    #score = log_loss(Y_test, Y_pred)
    score = roc_auc_score(Y_test, Y_pred)
    return score


# study = optuna.create_study(direction="minimize") for the log loss scoring
study = optuna.create_study(direction="maximize")
def full_objective(trial): return objective(trial)


study.optimize(full_objective, n_trials=60, timeout=600)
xgb_params = study.best_trial.params
