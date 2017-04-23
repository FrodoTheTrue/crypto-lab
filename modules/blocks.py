import os


def generate_blocks(primes_file, blocks_file, block_size, primes_in_line):  # noqa
    block_file_path = os.path.dirname(blocks_file)

    if not os.path.exists(block_file_path):
        os.makedirs(block_file_path)

    with open(primes_file, 'r') as f_primes:
        with open(blocks_file, 'w') as f_block:
            blocks_counter = 1
            stop_counter = 1

            first_time = True
            new_line = False

            for line in f_primes:
                line = line.split(' ')

                if len(line) < primes_in_line:  # Если чисел не хватает, то не рискуем
                    break

                numbers = [int(num) for num in line]

                i = 0

                while True:
                    if i + 1 == primes_in_line:  # Здесь понимаем, что нужно взять следующую строку
                        new_line = True
                        break

                    if stop_counter == block_size:  # Этот блок здесь, чтобы не создавались лишние переносы строк
                        f_block.write('\n')
                        blocks_counter += 1
                        stop_counter = 1
                        first_time = True

                    if new_line:  # По особому обрабатываем новую строку с числами
                        current_num = next_num  # noqa
                        next_num = numbers[i]
                        new_line = False
                    else:
                        current_num = numbers[i]
                        next_num = numbers[i + 1]
                        i += 1

                    distance = next_num - current_num

                    distance = distance / 2 if distance == 1 else distance // 2

                    if first_time:
                        f_block.write('{} {}'.format(current_num, distance))
                        first_time = False
                    elif stop_counter + 1 != block_size:  # Последнее число в блоке писать нет смысла
                        f_block.write(' {}'.format(distance))

                    stop_counter += 1


def split(blocks_file, blocks_in_file, block_size, path):
    if not os.path.exists(path):
        os.makedirs(path)

    files_counter = 1
    blocks_counter = 0

    need_new_file = True

    with open(blocks_file, 'r') as f_blocks:
        for block in f_blocks:

            if len(block.split(' ')) < block_size - 1:  # Если последний блок неполный, то стоп
                break

            if need_new_file:
                f = open('{}/{}.txt'.format(path, files_counter), 'w')
                need_new_file = False

            f.write(block)

            blocks_counter += 1

            if blocks_counter == blocks_in_file:
                f.close()

                files_counter += 1
                blocks_counter = 0
                need_new_file = True


def generate_files_blocks(primes_file, blocks_file, block_size, primes_in_line, split_path):
    generate_blocks(primes_file, blocks_file, block_size, primes_in_line)
    split(blocks_file, 1, block_size, split_path)
