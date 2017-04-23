from collections import Counter


def get_n_grams(blocks_file, num, path):
    n_grams_array = []

    with open(blocks_file, 'r') as f_block:
        for block in f_block:
            block_array = block.strip().split(' ')[1:]  # Первое число в блоке не учитываем

            for counter in range(len(block_array) - num + 1):
                n_gram = []

                for offset in range(num):
                    n_gram.append(block_array[counter + offset])  # Фиксируем все н-граммы

                n_gram = ' '.join(n_gram)
                n_grams_array.append(n_gram)

    counter = Counter(n_grams_array)

    with open('{}/{}_grams.txt'.format(path, num), 'w') as f_n_grams:
        for n_gram in sorted(counter.items(), key=lambda item: item[1], reverse=True):
            f_n_grams.write('{}\n'.format(n_gram))
