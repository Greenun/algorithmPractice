# meta tag나 a태그에서 뭔가 함정 부분이 있었나봄..;;
def solution(word, pages):
    import re
    # url_filter = re.compile(r'<meta property="og:url" content="(.*)"/>')
    # body_filter  = re.compile(r'<body>(.*)</body>', re.DOTALL)
    # link_filter = re.compile(r'<a href="(.*)">')
    url_filter = re.compile(r'<meta(.+?)/>')
    link_filter = re.compile(r'<a(.+?)>')
    detail_link = re.compile(r'"(.*)"')
    word_filter = re.compile(f'[a-z]*{word.lower()}[a-z]*')
    
    page_links = list()
    external_links = list()
    basic_score = list()
    for page in pages:
        page = page.lower()
        page_links.append(detail_link.search(url_filter.search(page).group(1).split(' ')[2]).group(1))
        external_links.append([detail_link.search(l).group(1) for l in link_filter.findall(page)])    
        # body = body_filter.search(page).group(1)
        # words = [w for w in word_filter.findall(body) if w == word.lower()]
        # words_count = re.sub(r'[^a-z]+', '.', page).split('.').count(word.lower())
        words = [w for w in word_filter.findall(page) if w == word.lower()]
        basic_score.append(len(words))
        # basic_score.append(words_count)
    
    final_scores = list()
    for i, link in enumerate(page_links):
        score = float(basic_score[i])
        temp = 0.0
        for j, external in enumerate(external_links):
            if i == j: continue
            if link in external:
                temp += basic_score[j] / len(external)
        score += temp
        final_scores.append(score)    
    
    return final_scores.index(max(final_scores))