from re import sub,findall
import os
import time

fold_pat_sol = r'\s*[*-+]\s+'
    ## For example, if you do not want to fold the lines started
    ##  with '+ ', you can change it to r'\s*[*-]\s+'. 
fold_pat = r'(' + fold_pat_sol + r')(.*)\n'
def process(fpath): ## for future extension: rewrite as a class
    with open(fpath + '/raw.md') as f_src:
        lines = f_src.readlines()

    notMLcode = True
    for i in range(len(lines)):
        if notMLcode:
            ## reformat link [[note]] to [note](../note/), except multiline code
            lines[i] = sub(r'\[\[([^\[\]]+)\]\]', r'[\1](../\1/)', lines[i])
        ## enable folding:
        indent_level = len(findall(r'^[ \t]*', lines[i])[0])
        if i > 0 and notMLcode and indent_level > indent_level_prev:
            fold_targ = r'\1<input type="checkbox" id="fold%d">' % i
            fold_targ += r'<label for="fold%d">\2</label>\n' % i
            lines[i - 1] = sub(fold_pat, fold_targ, lines[i - 1])
        indent_level_prev = indent_level
        if len(findall(r'^\s*`{3}', lines[i])) > 0:
            notMLcode = not notMLcode

    mod_time = time.localtime(os.path.getmtime(fpath + '/raw.md'))
    with open(fpath + '/index.md', 'w') as f_targ:
        f_targ.write(time.strftime('（最后修改于 %Y-%m-%d', mod_time)
                + '，源文件共 %d 行' % len(lines)
                + '。可在[无折叠版本](raw)中进行全文搜索。）\n\n')
        f_targ.writelines(lines)

if __name__ == "__main__":
    # filenames = [fname for fname in os.listdir('dir/') if os.path.splitext(name)[1] == '.md']
    for folder in os.listdir('../contents/'):
        print(folder)
        process('../contents/' + folder)

