from flask import Flask, request, render_template

from yt_dlp import YoutubeDL

app = Flask(__name__)

def get_video_link(youtube_video_id):
    options = {
        'quiet': True,
        'forceurl': True,
        'skip_download': True,
        'format': 'best'
    }

    with YoutubeDL(options) as yd:

        youtube_video_file_url = yd.extract_info(
            youtube_video_id,
            download=False
        )['url']

    return youtube_video_file_url


@app.route('/')
def index():

    youtube_video_id = request.args.get('v')
    youtube_video_file_url = get_video_link(youtube_video_id)

    return render_template('index.html', video_url=youtube_video_file_url)

if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
