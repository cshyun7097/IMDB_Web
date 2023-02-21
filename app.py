from flask import Flask, render_template, Response, request, redirect
import pymysql

conn = pymysql.connect(host = '127.0.0.1', user = 'root', password = '1234', db = 'imdb', charset='utf8')
cur = conn.cursor()
cur.execute('SELECT * from movie')
movielist = cur.fetchall()
cur.execute('SELECT * from tvshow')
tvshowlist = cur.fetchall()
cur.execute('SELECT * from game')
gamelist = cur.fetchall()
cur.execute('SELECT * from podcast')
podcastlist = cur.fetchall()
cur.execute('SELECT * from musicvideo')
musicvideolist = cur.fetchall()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/movie')
def movie():
    return render_template('movie.html', movielist = movielist)

@app.route('/podcast')
def podcast():
    return render_template('podcast.html', podcastlist = podcastlist)

@app.route('/game')
def game():
    return render_template('game.html', gamelist = gamelist)

@app.route('/tvshow')
def tvshow():
    return render_template('tvshow.html', tvshowlist = tvshowlist)

@app.route('/musicvideo')
def musicvideo():
    return render_template('musicvideo.html', musicvideolist = musicvideolist)

@app.route('/gaming')
def gaming():
    return render_template('gaming.html')

if __name__ == '__main__':
    app.run()