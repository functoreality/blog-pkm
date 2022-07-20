from re import sub,findall
import os

fold_pat_sol = r'[*-+]\s+'
    ## For example, if you do not want to fold the lines started
    ##  with '+ ', you can change it to r'[*-]\s+'. 
fold_pat = r'(\s*' + fold_pat_sol + r')(.*)\n'
def process(fname):
    with open('../raw/' + fname) as f_src:
        lines = f_src.readlines()

    for i in range(len(lines)):
        ## reformat [[note]] to [note](note.md):
        lines[i] = sub(r'\[\[([^\[\]]+)\]\]', r'[\1](\1.md)', lines[i])
        ## enable folding:
        indent_level = len(findall(r'^[ \t]*', lines[i])[0])
        if i == 0:
            indent_level_prev = indent_level
            continue
        if indent_level > indent_level_prev:
            fold_targ = r'\1<input type="checkbox" id="fold%d">' % i
            fold_targ += r'<label for="fold%d">\2</label>\n' % i
            lines[i - 1] = sub(fold_pat, fold_targ, lines[i - 1])
        indent_level_prev = indent_level

    with open('../' + fname, 'w') as f_targ:
        f_targ.writelines(lines)

# filenames = [fname for fname in os.listdir('dir/') if os.path.splitext(name)[1] == '.md']
for fname in os.listdir('../raw/'):
    print(fname)
    process(fname)

