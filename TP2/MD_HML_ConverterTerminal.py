import re

def replacertitle(match):
    counter = len(match.group(1))
    replace = f'<h{counter}>{match.group(2)}</h{counter}>'
    return replace

def replacerlist(match):
    items = f'<li>\{match.group(2)}</li>'
    #replace = f'<ol>\n{items}\n</ol>'
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
    markdown = re.sub(r'((?:^|\n)\d+\.\s.*(?:\n\d+\.\s.*)*)', replacerlist, markdown, flags=re.DOTALL)
    
    # Imagem
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)

    # Link
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

    return markdown

def main():
    markdown = ""
    print("Insere Texto Markdown(Se for uma lista, coloca fim na ultima linha para terminar): ")
    while True:
        line = input()
        html = markdown_to_html(line)
        if '<li>' in html:
            markdown += line + "\n"
            while True:
                line = input()
                if line.strip().lower() == "fim":
                    markdown = markdown[:-1]
                    break
                markdown += line + "\n"
            html = markdown_to_html(markdown)
            print("Texto HTML:")
            print('<ol>')
            print(html)
            print('</ol>')
            print("Insere Texto Markdown(Se for uma lista, coloca fim na ultima linha para terminar): ")
        else: 
            print("Texto HTML:")
            print(html)   
            print("Insere Texto Markdown(Se for uma lista, coloca fim na ultima linha para terminar): ")

if __name__ == '__main__':
    main()
