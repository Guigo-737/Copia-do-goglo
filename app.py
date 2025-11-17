from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/advanced")
def advanced_search():
    return render_template("advanced_search.html")

@app.route("/search")
def search():
    q = request.args.get("q")
    return f"Você pesquisou por: {q}"

@app.route("/search_advanced")
def search_advanced():
    all_words = request.args.get("all")
    exact = request.args.get("exact")
    any_word = request.args.get("any")
    none = request.args.get("none")
    
    return f"""
        <h2>Resultados da Pesquisa Avançada</h2>
        <p><b>Com todas as palavras:</b> {all_words}</p>
        <p><b>Com frases exatas:</b> {exact}</p>
        <p><b>Com qualquer palavra:</b> {any_word}</p>
        <p><b>Sem palavras:</b> {none}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
