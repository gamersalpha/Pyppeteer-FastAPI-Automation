from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from pyppeteer import launch

app = FastAPI()

class ScreenshotRequest(BaseModel):
    url: str

class ScriptRequest(BaseModel):
    url: str
    login_selector: str = ""
    password_selector: str = ""
    login: str = ""
    password: str = ""
    script: str

@app.post("/screenshot")
async def screenshot(request: ScreenshotRequest):
    try:
        browser = await launch(
            headless=True,
            args=['--no-sandbox', '--disable-gpu']
        )
        page = await browser.newPage()
        await page.goto(request.url)
        screenshot = await page.screenshot(encoding='base64')
        await browser.close()
        return {"screenshot": screenshot}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/script")
async def script(request: ScriptRequest):
    try:
        browser = await launch(
            headless=True,
            args=['--no-sandbox', '--disable-gpu']
        )
        page = await browser.newPage()
        await page.goto(request.url)

        if request.login_selector and request.login:
            await page.type(request.login_selector, request.login)
        if request.password_selector and request.password:
            await page.type(request.password_selector, request.password)

        await page.evaluate(request.script)
        html = await page.content()
        await browser.close()
        return {"html": html}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9595)
