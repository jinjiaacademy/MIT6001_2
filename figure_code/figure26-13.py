true_pos, false_pos, true_neg, false_neg = 0, 0, 0, 0
for e in test_set:
    age = e.get_age()
    time = e.get_time()
    if (abs(time - np.polyval(m_model, age)) <
            abs(time - np.polyval(f_model, age))):
        if e.get_label() = 'M':
            true_pos += 1
        else:
            false_pos += 1
    else:
        if e.get_label() == 'F':
            true_neg += 1
        else:
            false_neg += 1
get_stats(true_pos, false_pos, true_neg, false_neg)
