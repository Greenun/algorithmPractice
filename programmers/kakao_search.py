def solution(word, pages):
    import re
    url_filter = re.compile(r'<meta property="og:url" content="(.*)"/>')
    body_filter  = re.compile(r'<body>(.*)</body>', re.DOTALL)
    link_filter = re.compile(r'<a href="(.*)">')
    word_filter = re.compile(f'[a-zA-Z]*{word.lower()}[a-zA-Z]*')
    
    page_links = list()
    external_links = list()
    basic_score = list()
    for page in pages:
        page_links.append(url_filter.search(page).group(1))
        external_links.append(link_filter.findall(page))    
        body = body_filter.search(page).group(1).lower()
        words = word_filter.findall(body)
        count = 0
        # 4 6 8 10 17
        for w in words:
            if w == word.lower():
                count += 1
        basic_score.append(count)
    final_scores = list()
    for i, link in enumerate(page_links):
        score = basic_score[i]
        temp = 0
        for j, external in enumerate(external_links):
            if link in external:
                temp += basic_score[j] / len(external)
        score += temp
        final_scores.append(score)
    return final_scores.index(max(final_scores))
        