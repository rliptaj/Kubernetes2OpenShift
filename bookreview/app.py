import connexion


BOOKS = {'1984': 50,
         'foo': 10,
         'bar': 20,
         }

def get_review(name):
    if name in BOOKS:
        return BOOKS[name]
    print(f"Cannot find book {name}")
    raise Exception("Invalid book name specified")


if __name__== '__main__':
    app = connexion.App(__name__, specification_dir='swagger/')
    app.add_api('review.yaml')
    app.run(port=8080)


 
