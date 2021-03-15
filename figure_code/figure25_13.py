def z_scale(vals):
    '''Assumes vals is a sequence of floats'''
    result = np.array(vals) - np.array(vals).mean()
    return (result/np.std(result)).round(4)


def linear_scale(vals):
    '''Assumes vals is a sequence of floats'''
    vals = np.array(vals)
    vals -= vals.min()
    return (vals/vals.max()).round(4)
