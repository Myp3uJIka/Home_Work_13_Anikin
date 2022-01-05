from flask import Flask, request, render_template, send_from_directory
from functions import read_json, get_tags, find_tag, add_post


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


@app.route("/")  # создание декоратора для стартовой страницы
def page_index():
    return render_template('index.html', tags_list=get_tags(read_json(POST_PATH)))


@app.route("/post_by_tag")  # декоратор для поиска записей с тегами
def page_tag():
    tag = request.args.get('tag')  # присвоение query-параметра переменной
    return render_template('post_by_tag.html', content=find_tag(tag, read_json(POST_PATH)), tag=tag)


@app.route("/post", methods=["GET", "POST"])  # декоратор для отображения страницы загрузки и загруженного содержимого
def page_post_create():
    if request.method == 'GET':
        return render_template('post_form.html')  # вывод страницы добавления новой публикации при GET-запросе
    if request.method == 'POST':
        content = request.form.get('content')  # перехват содержания content-содержимого POST-запроса
        picture = request.files.get('picture')  # перехват содержания picture-содержимого POST-запроса
        if not content or not picture:  # условие при отсутствии информации в одном из полей формы
            return "Ошибка загрузки"
        path = f'{UPLOAD_FOLDER}/{picture.filename}'  # указание директории и имени файла для сохранения
        post = {  # создание записи новой публикации
            'content': content,
            'pic': f'/{path}'
        }
        picture.save(path)  # сохранение картинки
        add_post(POST_PATH, post)  # вызов функции для добавления записи в JSON-файл
        return render_template('post_uploaded.html', post=post)  # вывод страницы с информацией о новой публикации при
        # POST-запросе


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(debug=True)
