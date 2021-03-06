def any_prob(num_trials):
    any_month_48 = 0
    for trial in range(num_trials):
        months = [0]*12
        for i in range(446):
            months[random.randint(0, 11)] += 1
        if max(months) >= 48:
            any_month_48 += 1
    print('Probability of at least 48 births in some month =',
          round(any_month_48/num_trials, 4))
