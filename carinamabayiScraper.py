from bs4 import BeautifulSoup
import pandas as pd
import os

res = []

for fName in os.listdir():
    if os.path.isfile(fName) and fName.endswith(".html"):
        soup = BeautifulSoup(open(fName).read(), "html.parser")

        for tr in soup.find_all("tr"):
            td = tr.find_all("td")
            row = [tr.text.strip() for tr in td if tr.text.strip()]
            if row:
                res.append(row)

df = pd.DataFrame(res, columns=["#", "nama", "kelamin",
                                "asalBahasa", "kelaminDanAsal", "artiNama"])
print(df)
