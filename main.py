from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
clean_reference = []
clean_verse = []
for n in range(1, 9):
    response = requests.get("https://dailyverses.net/jesus?p=" + str(n))
    soup = bs(response.content, "html.parser")

    verses = soup.find_all("span", class_ = "v2")
    for verse in verses:
        text = verse.get_text(strip=True).replace("<br/>", "")
        clean_verse.append(text)
    if n != 8:
        try:
            clean_verse.pop(25)
        except:
            print("no 25")

    reference = soup.find_all("a", class_ = "vc")
    for ref in reference:
        text = ref.get_text(strip=True)
        clean_reference.append(text)

dict_ = {
    "verse" : clean_verse,
    "refrence" : clean_reference
}
df = pd.DataFrame(dict_)
df.to_csv("Extracted_verses.csv", index = False)
print("Success!")
