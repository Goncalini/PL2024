import re
import sys

def replacertitle(match):
    counter = len(match.group(1))
    replace = f'<h{counter}>{match.group(2)}</h{counter}>'
    return replace

def replacerlist(match):
    items = f'<ol>{match.group(1)}\n</ol>'
    return items

def markdown_to_html(markdown):
    # Título
    markdown = re.sub(r'^(#+)\s+(.*)$', replacertitle, markdown, flags=re.MULTILINE)
    
    # Bold
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    
    # Itálico
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)
    
    # Lista numerada
    markdown = re.sub(r'^(\d+\.)\s*(.*)$', r'<li>\2</li>', markdown, flags=re.MULTILINE)
    #markdown = f'<ol>\n{markdown}\n</ol>'

    # Imagem
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)

    # Link
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

    return markdown

def markdown_to_html_list(markdown):
    # Lista numerada
    markdown = re.sub(r'^(\d+\.)\s*(.*)$', r'<li>\2</li>', markdown, flags=re.MULTILINE)

    return markdown

def main(md_file):
    with open(md_file, 'r') as f:
        with open('convertedfile.html', 'w') as arq:
            in_list = False
            for line in f:
                if line[0].isdigit() and line[1] == '.':
                    if not in_list:
                        arq.write('<ol>\n')
                        in_list = True
                    html_line = markdown_to_html_list(line.strip())
                else:
                    if in_list:
                        arq.write('</ol>\n')
                        in_list = False
                    html_line = markdown_to_html(line.strip())
                arq.write(html_line + '\n')
            if in_list:
                arq.write('</ol>\n')


if __name__ == "__main__":
    main(sys.argv[1])
