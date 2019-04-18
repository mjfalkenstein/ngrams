import logging
import sys
import time


def compute_ngrams(input_string: str = '', n: int = 0) -> dict:
    """Compute all n-grams for the given string up to a max length
    Return a dict that maps the ngram string to a list. The mapping is always of format
        ngram -> [count, ngram_len_in_words].
    This helps sorting and output formatting later

    Keyword arguments:
    input_string -- the input string to be parsed. Assumes words are separated by ' ' (default '')
    n -- the max length for the n-grams output in words (default 0)
    """
    try:
        n = int(n)
    except ValueError:
        logging.exception('Max ngram length must be an integer, exiting...')
        sys.exit(1)

    # Turn the input string into a list, delineated by spaces
    input_string_list = input_string.split(' ')
    output_dict = {}

    # For all of the words in the input string...
    for i in range(0, len(input_string_list)):

        # For each value from 1 to n...
        for j in range(1, n + 1):
            
            # Build the ngram
            g = ' '.join(input_string_list[i: i + j])

            # filter out empty strings and only enter n-grams for the current iteration
            if g and g != ' ' and len(g.split(' ')) == j:
                # Insert the new ngram into the dict. If it's already there, increment the count
                output_dict.setdefault(g, [0, j])
                output_dict[g][0] += 1
    return output_dict


def read_input_from_file(filepath: str = '') -> str:
    """Read in data from given file as a string on one line.

    Keyword arguments:
    filepath -- the path to the input data relative to this file (default '')
    """
    try:

        # Read in input file as a string and put it all on one line.
        # This makes the ngram calculations later on a little simpler.
        # In the future, it might be desirable to calculate n-grams for each line.
        with open(filepath) as file:
            file_data = file.read()
            file_data = file_data.replace('\n', ' ')
            return file_data
    except FileNotFoundError:
        logging.exception('Unable to find or open file: %s' % filepath)
        sys.exit(1)


def format_output(ngrams: dict = None) -> str:
    """Formats the given dictionary of n-grams for readable output.
    See 'n-grams' function for exact data formatting

    Keyword arguments:
    n-grams -- the dictionary describing all found n-grams (default None)
    """
    if not ngrams:
        return ''

    # Sort the ngrams dictionary first alphabetically by key, then by the length of the ngram itself
    # Including the ngram length in the dictionary means we can skip re-calculating it in this step
    sorted_ngrams = sorted(ngrams.items(), key=lambda x: x[0])
    sorted_ngrams = sorted(sorted_ngrams, key=lambda x: x[1][1])

    # Build the output string to the exercise specifications, dropping the ngram length
    output_str = ''
    for entry in sorted_ngrams:
        output_str += entry[0] + ' ' + str(entry[1][0]) + '\n'
    return output_str.strip()


def main(args):

    # Check that CLI args are present. Any args after max_ngram_length are ignored
    if len(args) < 3:
        logging.error('Input file not specified. Correct CLI usage is: '
                      'python3 ngrams.py <path/to/input/file> <max_ngram_length>')
        sys.exit(1)
    file_data = read_input_from_file(args[1])
    if not file_data:
        logging.error('Input file is empty, exiting...')
        sys.exit(1)
    else:
        ngrams_data = compute_ngrams(file_data, args[2])
        print(format_output(ngrams_data))


if __name__ == "__main__":
    start_time = time.time()
    logging.basicConfig(level=logging.ERROR)
    main(sys.argv)
    print('--- process finished in %s seconds ---' % (time.time() - start_time))
