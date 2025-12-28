
def search_multiple_titles(filename, keywords):
    found = False
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if "<title>" in line:
                for keyword in keywords:
                    if f"<title>{keyword}</title>" in line:
                        print(f"見つかりました: {line.strip()}")
                        found = True
    if not found:
        print("どのキーワードも見つかりませんでした。")

# 実行例
keywords = ['メインページ', 'MediaWiki:Copyright', 'MediaWiki:Mainpage', '利用者:Example']
search_multiple_titles('jawiktionary-latest-pages-articles.xml', keywords)

