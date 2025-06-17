# 📖Scraping-Bible-verses-and-their-references

This Python script scrapes Bible verses about **Jesus** from [dailyverses.net](https://dailyverses.net/jesus), extracts their references, and saves them into a CSV file.

---

## 📂 Output

- `Extracted_verses.csv` – Contains two columns:
  - `verse`: the full verse text
  - `refrence`: the verse reference (e.g., John 14:6)

---

## 🛠️ Features

- ✅ Scrapes verses across 8 pages of [dailyverses.net/jesus](https://dailyverses.net/jesus)
- ✅ Cleans HTML and handles irregularities
- ✅ Stores data in a CSV using `pandas`
- ✅ Prints “Success!” once the file is saved
