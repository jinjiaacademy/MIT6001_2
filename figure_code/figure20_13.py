def r_squared(measured, predicted):
    '''Assumes measured a one-dimensional array of measured values
    predicted a one-dimentional array of predicted values
    Returns coefficient of determination'''
    estimated_error = ((predicted - measured)**2).sum()
    mean_of_measured = measured.sum()/len(measured)
    variability = ((measured - mean_of_measured)**2).sum()
    return 1 - estimated_error/variability
