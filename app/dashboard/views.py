""" Module for handling dashboard views"""

from flask import render_template, flash, redirect, url_for, session

from . import dashboard
from .forms import ShoppinglistForm
from app import store


@dashboard.route('/dashboard', methods=['GET', 'POST'])
def dashboard_page():
    """Render the dashboard template on the / route"""
    if session['logged_in']:
        add_shoppinglist = True
        form = ShoppinglistForm()
        all_shoppinglist = store.current_user['shopping_lists']
        if form.validate_on_submit():
            user_id = int(store.current_user['id'])
            store.add_shoppinglist(user_id, form.name.data)
            return redirect(url_for('dashboard.dashboard_page'))
        return render_template(
            "dashboard/dashboard.html",
            add_shoppinglist=add_shoppinglist,
            form=form,
            shoppinglists=all_shoppinglist
        )


@dashboard.route('/dashboard/edit_shoppinglist/<sh_id>', methods=['GET', 'POST'])
def shoppinglist_edit(sh_id):
    """Render the edit shoppinglist template on the / route"""
    if session['logged_in']:
        add_shoppinglist = False
        user_id = int(store.current_user['id'])
        single_shopping_list = store.get_shoppinglist(int(user_id), int(sh_id))
        form = ShoppinglistForm(dict=single_shopping_list)
        all_shoppinglist = store.current_user['shopping_lists']
        if form.validate_on_submit():
            single_shopping_list['name'] = form.name.data
            return redirect(url_for('dashboard.dashboard_page'))
        form.name.data = single_shopping_list['name']
        return render_template(
            "dashboard/dashboard.html",
            add_shoppinglist=add_shoppinglist,
            form=form,
            shoppinglists=all_shoppinglist
        )


@dashboard.route('/dashboard/delete/<sh_id>', methods=['GET', 'POST'])
def delete_shoppinglist(sh_id):
    if session['logged_in']:
        user_id = int(store.current_user['id'])
        store.remove_shoppinglist(int(user_id), int(sh_id))
        return redirect(url_for('dashboard.dashboard_page'))
        return render_template(title="Delete Shoppinglist Item")
