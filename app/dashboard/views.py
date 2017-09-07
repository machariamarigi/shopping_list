""" Module for handling dashboard views"""

from flask import render_template, redirect, url_for, session, flash

from . import dashboard
from .forms import ShoppinglistForm, ShoppingitemForm
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
            message = store.add_shoppinglist(user_id, form.name.data)
            flash(message)
            return redirect(url_for('dashboard.dashboard_page'))
        return render_template(
            "dashboard/dashboard.html",
            add_shoppinglist=add_shoppinglist,
            form=form,
            shoppinglists=all_shoppinglist
        )
    return redirect(url_for('auth.login'))


@dashboard.route(
    '/dashboard/edit_shoppinglist/<sh_id>',
    methods=['GET', 'POST']
)
def shoppinglist_edit(sh_id):
    """Render the edit shoppinglist template on the / route"""
    if session['logged_in']:
        add_shoppinglist = False
        user_id = int(store.current_user['id'])
        single_shopping_list = store.get_shoppinglist(int(user_id), int(sh_id))
        form = ShoppinglistForm(dict=single_shopping_list)
        all_shoppinglist = store.current_user['shopping_lists']
        if form.validate_on_submit():
            for list in store.current_user['shopping_lists']:
                if list['name'] == form.name.data:
                    flash('List ' + str(form.name.data) + " already exists.")
                    break
            else:
                single_shopping_list['name'] = form.name.data
            return redirect(url_for('dashboard.dashboard_page'))
        form.name.data = single_shopping_list['name']
        return render_template(
            "dashboard/dashboard.html",
            add_shoppinglist=add_shoppinglist,
            form=form,
            shoppinglists=all_shoppinglist
        )
    return redirect(url_for('auth.login'))


@dashboard.route('/dashboard/delete/<sh_id>', methods=['GET', 'POST'])
def delete_shoppinglist(sh_id):
    """Delete shopping lists"""
    if session['logged_in']:
        user_id = int(store.current_user['id'])
        store.remove_shoppinglist(int(user_id), int(sh_id))
        return redirect(url_for('dashboard.dashboard_page'))
    return redirect(url_for('auth.login'))


@dashboard.route(
    '/dashboard/shopping_list/<id>', methods=['GET', 'POST'])
def view_shoppinglist(id):
    """Render items in a shopping list and input form"""
    if session['logged_in']:
        user_id = int(store.current_user['id'])
        view_list = store.get_shoppinglist(user_id, int(id))
        items = view_list['items']
        form = ShoppingitemForm()
        if form.validate_on_submit():
            message = store.add_shoppingitems(
                user_id,
                int(id),
                form.name.data,
                form.quantity.data
            )
            flash(message)
            return redirect(url_for('dashboard.view_shoppinglist', id=id))
        return render_template(
            'dashboard/shoppinglist.html',
            items=items,
            form=form,
            shoppinglist=view_list
        )
    return redirect(url_for('auth.login'))


@dashboard.route(
        '/dashboard/shopping_list/edit_item/<id>/<si_id>',
        methods=['GET', 'POST']
)
def edit_shoppingitem(id, si_id):
    """Edit a shopping list item"""
    if session['logged_in']:
        user_id = int(store.current_user['id'])
        item = store.get_shoppingitem(user_id, int(id), int(si_id))
        form = ShoppingitemForm(dict=item)
        current_shoppinglist = store.get_shoppinglist(user_id, int(id))
        all_items = current_shoppinglist['items']
        if form.validate_on_submit():
            for item in current_shoppinglist['items']:
                if item['name'] == form.name.data:
                    flash('Item ' + str(form.name.data) + " already exists")
                    break
            else:
                item['name'] = form.name.data
                item['quantity'] = form.quantity.data
            return redirect(url_for('dashboard.view_shoppinglist', id=id))
        form.name.data = item['name']
        form.quantity.data = item['quantity']
        return render_template(
            'dashboard/shoppinglist.html',
            items=all_items,
            form=form,
            shoppinglist=current_shoppinglist
        )
    return redirect(url_for('auth.login'))


@dashboard.route(
        '/dashboard/shopping_list/delete_item/<id>/<si_id>',
        methods=['GET', 'POST']
)
def delete_shoppingitem(id, si_id):
    """Delete a shopping list item"""
    if session['logged_in']:
        user_id = int(store.current_user['id'])
        store.remove_shoppingitem(user_id, int(id), int(si_id))
        return redirect(url_for('dashboard.view_shoppinglist', id=id))
    return redirect(url_for('auth.login'))


@dashboard.route(
        '/dashboard/shopping_list/but/<id>/<si_id>',
        methods=['GET', 'POST']
)
def buy_shoppingitem(id, si_id):
    """Mark items as bought"""
    if session['logged_in']:
        user_id = int(store.current_user['id'])
        store.buy_shoppingitem(user_id, int(id), int(si_id))
        return redirect(url_for('dashboard.view_shoppinglist', id=id))
    return redirect(url_for('auth.login'))
