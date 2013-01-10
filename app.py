#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect

import settings

def init_routes(app):

    @app.route('/')
    def home():
        return render_template('home.html', menus=settings.MENUS,
                dirlinks=settings.DIRLINKS, active_page='Home')

    @app.route('/blog')
    def blog():
        return redirect('http://blog.popong.com')

    @app.route('/about')
    def about():
        return render_template('about.html', menus=settings.MENUS,
                dirlinks=settings.DIRLINKS, active_page='About')

def main():
    app = Flask(__name__)
    init_routes(app)
    app.run(**settings.SERVER_SETTINGS)
    app.add_url_rule('/favicon.ico',
            redirect_to=url_for('static', filename='images/favicon.ico'))

if __name__ == '__main__':
    main()