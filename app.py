from flask import Flask, render_template, url_for, request, redirect
from projects import Project
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/projects/", methods=['GET', 'POST'])
def projects():
    projects = Project.getAllProjects()
    if request.method=='GET':
        return render_template('projects.html', projects=projects)
        
    return render_template('projects.html')

@app.route("/resume/")
def resume():
    return render_template('resume.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/form/", methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        title = request.args.get('title')
        status = request.args.get('status')
        if status == 'EDIT':
            projects = Project.getAllProjects()
            chosen_project = {}
            for project in projects:
                if project['title'] == title:
                    chosen_project = project
            return render_template('form.html', status='EDIT', project=chosen_project)
        elif status=='ADD-PROJECT':
            return render_template('form.html', project=None, status='ADD-PROJECT')
        elif status=='DEL-PROJECT':
            return render_template('form.html', project=title, status='DEL-PROJECT')
        else:
            return render_template('form.html')
    if request.method == 'POST':
        status = request.args.get('status')
        if status == 'EDIT':
            title = request.args.get('title')
            affiliation = request.form['affiliation']
            timeline = request.form['timeline']
            link = request.form['link']
            description = request.form['description']
            imgName = request.form['imgName']
            Project.updateProject(title, description, affiliation, imgName, timeline, link)
            return redirect(url_for('projects'))
        elif status == 'ADD-PROJECT':
            title = request.form['title']
            print(title)
            affiliation = request.form['affiliation']
            print(affiliation)
            timeline = request.form['timeline']
            print(timeline)
            link = request.form['link']
            print(link)
            description = request.form['description']
            print(description)
            imgName = request.form['imgName']
            print(imgName)
            Project.addProject(title, description, affiliation, imgName, timeline, link)
            return redirect(url_for('projects'))
        
@app.route('/projects/delete', methods=['GET', 'POST'])
def delete():
    if request.method=='GET':
        title = request.args.get('title')
        if title:
            projects = Project.getAllProjects()
            chosen_project = {}
            for project in projects:
                if project['title'] == title:
                    chosen_project = project
            return render_template('confirmation.html', project=chosen_project, title=title)
    elif request.method == 'POST':
        title = request.args.get('title')
        Project.delProject(title)        
        return redirect(url_for('projects'))

if __name__ == '__main__':
    Project.getAllProjects()