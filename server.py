from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 静的ファイルの提供
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_form(name: str = ""):
    return f"""
    <html>
        <body>
            <h1>GETリクエスト</h1>
            <p>名前: {name}</p>
            <a href="/static/index.html">戻る</a>
        </body>
    </html>
    """

@app.post("/", response_class=HTMLResponse)
async def post_form(name: str = Form(...)):
    return f"""
    <html>
        <body>
            <h1>POSTリクエスト</h1>
            <p>名前: {name}</p>
            <a href="/static/index.html">戻る</a>
        </body>
    </html>
    """

@app.post("/password", response_class=HTMLResponse)
async def post_pw_form(password: str = Form(...)):
    return f"""
    <html>
        <body>
            <h1>パスワード</h1>
            <p>あなたのパスワードは: {password} です</p>
            <a href="/static/index.html">戻る</a>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
