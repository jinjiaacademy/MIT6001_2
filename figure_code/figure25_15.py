def add_labels(examples, label_file):
    df = pd.read_csv(label_file, comment='#')
    df = df.set_index('Name')
    for e in examples:
        if e.get_name() in df.index:
            e.set_label(df.loc[e.get_name()]['Diet'])


def check_diet(cluster):
    herbivores, carnivores, omnivores = 0, 0, 0
    for m in cluster.members():
        if m.get_label() == 0:
            herbivores += 1
        elif m.get_label() == 1:
            carnivores += 1
        else:
            omnivores += 1
    print(' ', herbivores, 'herbivores,', carnivores, 'carnivores,',
          omnivores, 'omnivores\n')


def test_teeth_diet(features_file, labels_file, num_clusters,
                    num_trials, scale_method=None):
    def print_clustering(clustering):
        for c in clustering:
            names = ''
            for p in c.members():
                names += p.get_name() + ', '
            print(names[:-2])
            check_diet(c)
    species_dict = read_mammal_data(features_file, scale_method)
    examples = build_mammal_examples(species_dict)
    add_labels(examples, labels_file)
    print_clustering(try_k_means(examples, num_clusters, num_trials))
