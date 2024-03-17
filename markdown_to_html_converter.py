import argparse
import markdown

# parserとargumentを作成
parser = argparse.ArgumentParser(description="Convert Markdown to HTML.")
parser.add_argument('command')
parser.add_argument('inputfile')
parser.add_argument('outputfile')

# 引数を解析
args = parser.parse_args()

# commandがmarkdownでない場合はエラーを出す
if args.command.lower() != 'markdown':
    raise ValueError("Invalid command. The command should be 'markdown'.")

with open(args.inputfile, 'r') as f:
    md_text = f.read()

html_text = markdown.markdown(md_text)

with open(args.outputfile, 'w') as f:
    f.write(html_text)