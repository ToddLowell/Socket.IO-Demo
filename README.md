# Socket.IO Demo

Python backend encodes image to Base64 and sends it to the JavaScript frontend.

## Frontend

```bash
$ cd Frontend/
$ npm install
$ npm run dev
```

## Backend

```bash
$ cd Backend/
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ gunicorn -k eventlet -w 1 --reload app:app
```

---

**Image Source:** https://www.wallpaperpass.com/download-botw-wallpaper-178/
