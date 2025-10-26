from fastapi import FastAPI
import random
import time
import aiohttp

app = FastAPI()

@app.get("/api/test")
def mock_test():
	delay = random.uniform(0.1, 0.8)
	time.sleep(delay)

	if random.random() < 0.1:
		time.sleep(3.0)

	if random.random() < 0.7:
		return {"status": "ok", "delay": delay}
	else:
		raise aiohttp.ClientResponseError(status_code=500, DETAIL={"status": "error", "delay": delay})

if __name__ == "__main__":
	import uvicorn
	uvicorn.run("mock_server:app", host="127.0.0.1", port=8000, reload=True)