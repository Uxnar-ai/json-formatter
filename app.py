#!/usr/bin/env python3.12
# jsonfmt —— 粘贴 JSON 一键排版/压缩/查错，纯前端算，不经服务器
import os

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("page.html")


@app.get("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("JSONFMT_PORT", "8870")), debug=False)
