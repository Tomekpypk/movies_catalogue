from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = [
        {"title": "The Great Gatsby", "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRUEtMQ3GOWnEQ8EO0WDLrLe-yL1dd_KjU-fBSxr1hKaelXM_-T",
          "description": "Nowy Jork, rok 1922. Milioner Jay Gatsby spotyka po pięciu latach swoją wielką miłość, Daisy, z którą wcześniej rozdzieliły go koleje losu.", "link": "https://www.filmweb.pl/film/Wielki+Gatsby-2013-506934"},
        {"title": "Terminal", "image": "https://i.ebayimg.com/images/g/lxMAAMXQOT5Q9Uu4/s-l640.jpg",
          "description": "Gdy Viktor Navorski, turysta z Europy Wschodniej, przylatuje do Nowego Jorku, w jego ojczyźnie ma miejsce zamach stanu. Amerykańskie władze nie uznają paszportu mężczyzny, więc miejscem przymusowego pobytu staje się dla niego hala terminalu.",
              "link": "https://www.filmweb.pl/film/Terminal-2004-106408"},
        {"title": "Terminator", "image": "https://fwcdn.pl/fpo/09/95/995/7919703.3.jpg",
          "description": "Elektroniczny morderca zostaje wysłany z przyszłości do roku 1984, by zabić matkę przyszłego lidera rewolucji. W ślad za nim rusza Kyle Reese, który ma chronić kobietę.",
              "link": "https://www.filmweb.pl/film/Terminator-1984-995"},
        {"title": "Kapitan Bomba", "image": "https://yt3.googleusercontent.com/ytc/AIf8zZQbVFgAfPD0iT2EAOrilefPRNDAUmE2KudJsKCX=s900-c-k-c0x00ffffff-no-rj",
 "description": "Produkcja może i nie ma wysokiego budżetu, za to jest średnia. Autor dał z siebie całe 30%. A skoro jest średnio, to dobrze.",
 "link": "https://www.filmweb.pl/serial/Kapitan+Bomba-2007-469752"}
    
        
    ]
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
