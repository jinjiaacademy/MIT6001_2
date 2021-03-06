def craps_sim(hands_per_game, num_games):
    '''Assumes hands_per_game and num_games are ints > 0
    Play num_games games of hands_per_game hands; print results'''
    games = []

    # Play num_games games
    for t in range(num_games):
        c = Craps_game()
        for i in range(hands_per_game):
            c.play_hand()
        games.append(c)

    # Produce statistics for each game
    p_ROI_per_game, dp_ROI_per_game = [], []
    for g in games:
        wins, losses = g.pass_results()
        p_ROI_per_game.append((wins-losses)/float(hands_per_game))
        wins, losses, pushes = g.dp_results()
        dp_ROI_per_game.append((wins-losses)/float(hands_per_game))

    # Produce and print summary statistics
    mean_ROI = str(round((100*sum(p_ROI_per_game)/num_games), 4)) + '%'
    sigma = str(round(100*np.std(p_ROI_per_game), 4)) + '%'
    print('Pass:', 'Mean ROI =', mean_ROI, 'Std. Dev. =', sigma)
    mean_ROI = str(round((100*sum(dp_ROI_per_game)/num_games), 4)) + '%'
    sigma = str(round(100*np.std(dp_ROI_per_game), 4)) + '%'
    print('Don\'t pass:', 'Mean ROI =', mean_ROI, 'Std Dev =', sigma)
