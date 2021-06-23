from flask import Flask, redirect, request

from  youtube_dl import YoutubeDL

app = Flask(__name__)

@app.route('/')
def index():

    options = {
        'quiet': True,
        'forceurl': True,
        'skip_download': True,
        'format': 'best'
    }

    with YoutubeDL(options) as yd:

        youtube_video_id = request.args.get('v')

        youtube_video_file_url = yd.extract_info(
            youtube_video_id,
            download=False
        )['url']

        return redirect(youtube_video_file_url)

if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
