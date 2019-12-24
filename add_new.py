import sys
from bs4 import BeautifulSoup, BeautifulStoneSoup
import requests
import os
import re


# ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾
# ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎

def replace_sup_and_sub(text):
    unicode_map = {
        #           superscript     subscript
        '0': ('\u2070', '\u2080'),
        '1': ('\u00B9', '\u2081'),
        '2': ('\u00B2', '\u2082'),
        '3': ('\u00B3', '\u2083'),
        '4': ('\u2074', '\u2084'),
        '5': ('\u2075', '\u2085'),
        '6': ('\u2076', '\u2086'),
        '7': ('\u2077', '\u2087'),
        '8': ('\u2078', '\u2088'),
        '9': ('\u2079', '\u2089'),
        'a': ('\u1d43', '\u2090'),
        'b': ('\u1d47', 'b'),
        'c': ('\u1d9c', 'c'),
        'd': ('\u1d48', 'd'),
        'e': ('\u1d49', '\u2091'),
        'f': ('\u1da0', 'f'),
        'g': ('\u1d4d', 'g'),
        'h': ('\u02b0', '\u2095'),
        'i': ('\u2071', '\u1d62'),
        'j': ('\u02b2', '\u2c7c'),
        'k': ('\u1d4f', '\u2096'),
        'l': ('\u02e1', '\u2097'),
        'm': ('\u1d50', '\u2098'),
        'n': ('\u207f', '\u2099'),
        'o': ('\u1d52', '\u2092'),
        'p': ('\u1d56', '\u209a'),
        'q': ('q', 'q'),
        'r': ('\u02b3', '\u1d63'),
        's': ('\u02e2', '\u209b'),
        't': ('\u1d57', '\u209c'),
        'u': ('\u1d58', '\u1d64'),
        'v': ('\u1d5b', '\u1d65'),
        'w': ('\u02b7', 'w'),
        'x': ('\u02e3', '\u2093'),
        'y': ('\u02b8', 'y'),
        'z': ('z', 'z'),
        'A': ('\u1d2c', 'A'),
        'B': ('\u1d2e', 'B'),
        'C': ('C', 'C'),
        'D': ('\u1d30', 'D'),
        'E': ('\u1d31', 'E'),
        'F': ('F', 'F'),
        'G': ('\u1d33', 'G'),
        'H': ('\u1d34', 'H'),
        'I': ('\u1d35', 'I'),
        'J': ('\u1d36', 'J'),
        'K': ('\u1d37', 'K'),
        'L': ('\u1d38', 'L'),
        'M': ('\u1d39', 'M'),
        'N': ('\u1d3a', 'N'),
        'O': ('\u1d3c', 'O'),
        'P': ('\u1d3e', 'P'),
        'Q': ('Q', 'Q'),
        'R': ('\u1d3f', 'R'),
        'S': ('?', '?'),
        'T': ('\u1d40', 'T'),
        'U': ('\u1d41', 'U'),
        'V': ('\u2c7d', 'V'),
        'W': ('\u1d42', 'W'),
        'X': ('X', 'X'),
        'Y': ('Y', 'Y'),
        'Z': ('Z', 'Z'),
        '+': ('\u207A', '\u208A'),
        '-': ('\u207B', '\u208B'),
        '−': ('\u207B', '\u208B'),
        '=': ('\u207C', '\u208C'),
        '(': ('\u207D', '\u208D'),
        ')': ('\u207E', '\u208E'),
        '.': ('.', '.'),
        '<': ('<', '<'),
        '>': ('>', '>'),
        '/': ('/', '/'),
        '\\': ('\\', '\\'),
    }

    def replace_sub(matchobj):
        newline = ''
        for char in matchobj.group(1):
            newline += unicode_map[char][1]
        return newline

    def replace_sup(matchobj):
        newline = ''
        for char in matchobj.group(1):
            newline += unicode_map[char][0]
        return newline

    text = re.sub(r'<sub>(.*?)</sub>', replace_sub, text)
    text = re.sub(r'<sup>(.*?)</sup>', replace_sup, text)

    return text


def get_english(num):
    url = f'https://projecteuler.net/problem={num}'
    page = requests.get(url)
    text = replace_sup_and_sub(page.text)
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.find('div', 'problem_content').get_text()
    return '\n'.join([url, text])


def get_russian(num):
    url = f'https://euler.jakumo.org/problems/view/{num}.html'
    page = requests.get(url)
    text = replace_sup_and_sub(page.text)
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.find('div', 'problemsItem').get_text()
    text = text.replace("Оригинал", "")
    return '\n'.join([url, text])


def prepare_text(in_text):
    text = in_text.replace("\n\n", "\n")
    text = text.strip()
    t_list = in_text.split('\n')
    out_text = []
    for i in t_list:
        if i.strip() == '':
            continue
        words = i.split(' ')
        new_line = "#"
        for word in words:
            if len(' '.join([new_line, word])) > 120:
                out_text.append(new_line)
                new_line = '#'
            new_line += ' ' + word
        out_text.append(new_line)

    return out_text


def make_name(n):
    return "0" * (4 - len(n)) + n


if len(sys.argv) < 2:
    exit(-1)
prob_num = sys.argv[1]

int_prob_num = int(prob_num)
min_num = make_name(str((int_prob_num - 1) // 100 * 100 + 1))
max_num = make_name(str(int_prob_num // 100 * 100 + 100))
dir_name = '_'.join([min_num, max_num])

file_name = make_name(prob_num)

try:
    os.makedirs(dir_name)
except FileExistsError:
    pass

os.makedirs(dir_name + os.path.sep + file_name)
with open(dir_name + os.path.sep + file_name + os.path.sep + file_name + ".py", "w", encoding='utf-8') as f:
    f.write('\n'.join(prepare_text(get_english(prob_num))) + '\n')
    f.write("#\n")
    f.write('\n'.join(prepare_text(get_russian(prob_num))) + '\n')
    f.write("#\n# \n\n")
    f.write('import time\n\n')
    f.write('start_time = time.time()\n\n')
    f.write('end_time = time.time()\n\n')
    f.write('print()\n')
    f.write('print(\'time:\', end_time - start_time)\n')
