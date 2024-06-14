from blog_app import create_app, db
import base64

app = create_app()

if __name__ == '__main__':
    app.run(debug=False)

@app.cli.command('create-db')
def create_db(): 
    db.create_all()
    print("All dbs created successfully")

