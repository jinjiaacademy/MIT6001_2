
def build_ROC(model, test_set, label, title, plot = True):
    xVals, yVals = [], []
    for p in np.arange(0, 1, 0.01):
        true_pos, false_pos, true_neg, false_neg =\
                             apply_model(model, test_set, label, p)
        xVals.append(1.0 - specificity(true_neg, false_pos))
        yVals.append(sensitivity(true_pos, false_neg))
    auroc = skm.auc(xVals, yVals)
    if plot:
        plt.plot(xVals, yVals)
        plt.plot([0,1], [0,1,], '--')
        plt.title(title +  ' (AUROC = ' +
                  str(round(auroc, 3)) + ')')
        plt.xlabel('1 - Specificity')
        plt.ylabel('Sensitivity')
    return auroc

build_ROC(model, test, 'M', 'ROC for Predicting Gender')
