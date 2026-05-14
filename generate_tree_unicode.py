import os

def generate_tree(startpath, exclude_dirs=('.git', '__pycache__', '.venv', 'venv', 'env', '.ipynb_checkpoints')):
    lines = []
    for root, dirs, files in os.walk(startpath):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        dirs.sort()
        files.sort()
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * (level)
        
        if level > 0:
            lines.append(f'{indent}├── {os.path.basename(root)}/')
        else:
            lines.append(f'pricing-strategy-analysis/')
            lines.append('│')
            
        subindent = '│   ' * (level + 1)
        for i, f in enumerate(files):
            if f == 'generate_tree.py' or f == 'tree_output.txt':
                continue
            if i == len(files) - 1 and not dirs:
                lines.append(f'{subindent}└── {f}')
            else:
                lines.append(f'{subindent}├── {f}')
    return '\n'.join(lines)

if __name__ == "__main__":
    with open('tree_output.txt', 'w', encoding='utf-8') as f:
        f.write(generate_tree('.'))
