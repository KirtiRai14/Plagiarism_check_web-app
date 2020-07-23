import requests
from bs4 import BeautifulSoup

API_KEY = "AIzaSyBAQwx3f1ad4JSkkKZPa52nvzi7o5tbiig"
SEARCH_ENGINE_ID = "014464730682648989702:oic-deao8hq"
answers = []

def pc_check(query_in, opt1, opt2, opt3="", opt4="", opt5=""):
    disp_title, disp_snippet, disp_link = [], [], []
    query = query_in
    page = 1
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    data = requests.get(url).json()
    search_items = data.get("items")
    match_count = 0
    total_count = 1           #Stores the total number of results (whether matched or unmatched),
    result_percentage = 0     #and it has to start with 1 for proper comparison
    for i, j in enumerate(search_items, start=1):
        title = j.get("title")
        snippet = j.get("snippet")
        #html_snippet = j.get("htmlSnippet")
        link = j.get("link")
        #print("=" * 10, f"Result #{i + start - 1}", "=" * 10)
        #print("Title", title)
        #print("Description", snippet)
        #print("URL: ", link, "\n")
        if opt5 != "":
            match_count = html_to_text(link, query, opt1, opt2, match_count, opt3, opt4, opt5)
        elif opt5 == "" and opt4 != "":
            match_count = html_to_text(link, query, opt1, opt2, match_count, opt3, opt4)
        elif opt4 == "" and opt3 != "":
            match_count = html_to_text(link, query, opt1, opt2, match_count, opt3)
        else:
            match_count = html_to_text(link, query, opt1, opt2, match_count)
        if match_count == total_count:
            disp_title.append(title)
            disp_snippet.append(snippet)
            disp_link.append(link)
            #total_count += 1
        #else:
            #total_count += 1
        total_count += 1
    print("Total matched results are", match_count)
    #result_percentage = float((match_count / 10) * 100)
    result_percentage = float((match_count / (total_count-1)) * 100)
    return result_percentage, disp_title, disp_snippet, disp_link


def html_to_text(url_link, ch_query, opt1, opt2, match_count, opt3="", opt4="", opt5=""):
    res = requests.get(url_link)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)
    output = ''
    blacklist = [
        '[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script', 'style', 'a',
    ]
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    # print("&"*20+output+"&"*20)
    if opt5 != "":
        if ch_query.lower() and opt1.lower() and opt2.lower() and opt3.lower() and opt4.lower() and opt5.lower() in output.lower():
            print("Question with options is same")
            match_count += 1
    elif opt5 == "" and opt4 != "":
        if ch_query.lower() and opt1.lower() and opt2.lower() and opt3.lower() and opt4.lower() in output.lower():
            print("Question with options is same")
            match_count += 1
    elif opt4 == "" and opt3 != "":
        if ch_query.lower() and opt1.lower() and opt2.lower() and opt3.lower() in output.lower():
            print("Question with options is same")
            match_count += 1
    else:
        if ch_query.lower() and opt1.lower() and opt2.lower() in output.lower():
            print("Question with options is same")
            match_count += 1
    return match_count
