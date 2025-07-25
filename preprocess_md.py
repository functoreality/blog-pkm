"""Process all blog post, generate index.md according to raw.md."""
from re import sub, findall
import os
import time

# Fold lines starting with '* ' but not '- ' or '*  '.
# to enable folding for any lines, use r'^\s*[*\-+]\s+'.
FOLD_PAT_SOL = '\\s*[*+] '
FOLD_PAT = '^(' + FOLD_PAT_SOL + ')(\\S.*)\n'


def process(post: str) -> None:  # for future extension: rewrite as a class
    """Process a single blog post: Add folds, form links, etc."""
    with open(os.path.join('contents', post, 'raw.md'),
              encoding='UTF-8') as f_src:
        lines = f_src.readlines()

    not_multiline_code = True
    for i, line_i in enumerate(lines):
        if not_multiline_code:
            # Reformat link [[note]] to [《note》](../note/), except multi-line
            # code. If you want to keep double brackets, write "[\[note]]" in
            # your raw.md.
            line_i = sub(r'\[\[([^\[\]]+)\]\]', r'[《\1》](../\1/)', line_i)
            lines[i] = line_i
        # enable folding:
        indent_level = len(findall(r'^[ \t]*', line_i)[0])
        if i > 0 and not_multiline_code and indent_level > indent_level_prev:
            fold_targ = rf'\1<input type="checkbox" name="fchk" id="fold{i}">'
            fold_targ += rf'<label for="fold{i}">\2</label>\n'
            lines[i - 1] = sub(FOLD_PAT, fold_targ, lines[i - 1])
        indent_level_prev = indent_level
        if len(findall(r'^\s*`{3}', line_i)) > 0:
            # detected begin or end of multi-line code
            not_multiline_code = not not_multiline_code

    mod_time = time.localtime(os.path.getmtime(
        os.path.join('contents', post, 'raw.md')))
    with open(os.path.join('contents', post, 'index.md'),
              'w', encoding='UTF-8') as f_targ:
        f_targ.write('---\nlayout: folded_post\ntitle: "' + post + '"\n'
                     + time.strftime('date: %Y-%m-%d +0800', mod_time)
                     + '\ncategories: jekyll update\n---\n\n')
        # + '（可在[无折叠版本](raw)中进行全文搜索）\n\n'
        # f_targ.write(time.strftime('（最后修改于 %Y-%m-%d', mod_time)
        #         + '，源文件共 %d 行' % len(lines)
        #         + '。可在[无折叠版本](raw)中进行全文搜索。）\n\n')
        f_targ.writelines(lines)


if __name__ == '__main__':
    # filenames = [fname for fname in os.listdir('dir')
    #              if os.path.splitext(fname)[1] == '.md']
    for my_post in os.listdir('contents'):
        print(my_post)
        process(my_post)
