control_mean = round(sum(control_times)/len(control_times), 2)
treatment_mean = round(sum(treatment_times)/len(treatment_times), 2)
print('Treatment_mean - control_mean =',
      round(treatment_mean - control_mean, 2), 'minutes')
two_sample_test = scipy.stats.ttest_ind(treatment_times,
                                        control_times,
                                        equal_val=False)
print('The t-statistic from two-sample test is',
      round(two_sample_test[0], 2))
print('The p-value from two-sample test is',
      round(two_sample_test[1], 2))
