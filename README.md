# SEC XBRL Parser

A lightweight Flask API that parses real SEC 10-K HTML filings using inline XBRL (`<ix:nonfraction>` tags) and extracts Revenue, Gross Profit, SG&A, and Net Income.

## 📦 Usage

### Local

```
pip install -r requirements.txt
python main.py
```

Then open:

```
http://localhost:8080/parse?url=https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm
```

### Render Deployment

1. Create a new Web Service on Render
2. Point it to this repo (or upload manually)
3. Use the free plan
4. Build command: `pip install -r requirements.txt`
5. Start command: `python main.py`

## 🧠 GPT Integration

Use a GET Action that hits:

```
/parse?url=https://SEC-FILING-LINK
```
