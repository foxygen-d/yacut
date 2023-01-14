from flask import Flask, abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URLForm
from .models import URLMap
from .utils import check_symbols, get_unique_short_url


@app.route('/', methods=['GET', 'POST'])
def main_page_view():
    form = URLForm()
    if form.validate_on_submit():
        short = form.custom_id.data

        if URLMap.query.filter_by(short=short).first() is not None:
            flash('Такая короткая URL-ссылка уже занята!')
            return render_template('main_page.html', form=form)
        if short and not check_symbols(short):
            flash('Допустимые символы: A-z, 0-9')
            return render_template('main_page.html', form=form)

        if short is None:
            short = get_unique_short_url()

        url = URLMap(
            original=form.original_link.data, 
            short=form.custom_id.data, 
        )
        db.session.add(url)
        db.session.commit()
        return render_template('main_page.html',
                               form=form,
                               short_url=url_for('redirect_to_url_view',
                                                 short=short, _external=True))
    return render_template('main_page.html', form=form)


@app.route('/<string:short>', methods=['GET'])
def redirect_to_url_view(short):
    url = URLMap.query.filter_by(short=short).first_or_404()
    if url is None:
        abort(404)
    return redirect(url.original)
