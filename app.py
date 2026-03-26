from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-production'

data_store = []

@app.route('/')
def index():
    """Главная страница приложения"""
    return render_template('index.html', items=data_store)

@app.route('/about')
def about():
    """Страница с информацией о проекте"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Страница контактов"""
    return render_template('contact.html')

@app.route('/add', methods=['POST'])
def add_item():
    """Обработчик добавления нового элемента"""
    title = request.form.get('title')
    description = request.form.get('description')
    
    if title and description:
        item = {
            'id': len(data_store) + 1,
            'title': title,
            'description': description
        }
        data_store.append(item)
        flash('Элемент успешно добавлен', 'success')
    else:
        flash('Заполните все поля формы', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    """Обработчик удаления элемента"""
    global data_store
    data_store = [item for item in data_store if item['id'] != item_id]
    flash('Элемент удален', 'success')
    return redirect(url_for('index'))

@app.route('/api/status')
def api_status():
    """API endpoint для проверки статуса приложения"""
    return {'status': 'ok', 'items_count': len(data_store)}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)