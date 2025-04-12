from flask import Flask, request, jsonify
import requests
from lxml import etree

app = Flask(__name__)

@app.route("/parse", methods=["GET"])
def parse_sec_filing():
    sec_url = request.args.get("url")
    if not sec_url:
        return jsonify({"error": "Missing SEC filing URL"}), 400

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(sec_url, headers=headers, timeout=10)
        parser = etree.HTMLParser(recover=True)
        tree = etree.fromstring(resp.content, parser=parser)

        extracted = {
            "Filing URL": sec_url,
            "Revenue": "Not found",
            "Gross Profit": "Not found",
            "SG&A": "Not found",
            "Net Income": "Not found"
        }

        for elem in tree.xpath("//*[starts-with(name(), 'ix:nonfraction')]"):
            name = elem.attrib.get("name", "").lower()
            value = elem.text.strip() if elem.text else ""
            if "revenues" in name and extracted["Revenue"] == "Not found":
                extracted["Revenue"] = value
            elif "grossprofit" in name and extracted["Gross Profit"] == "Not found":
                extracted["Gross Profit"] = value
            elif "sellinggeneralandadministrativeexpense" in name and extracted["SG&A"] == "Not found":
                extracted["SG&A"] = value
            elif "netincomeloss" in name and extracted["Net Income"] == "Not found":
                extracted["Net Income"] = value

        return jsonify(extracted)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
