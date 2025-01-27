from flask import Flask, request, jsonify
from docgen.docgen import generate_docs
from qna.qna import answer_question

app = Flask(__name__)

@app.route("/generate_docs", methods=["POST"])
def generate_docs_route():
    code = request.json.get("code")
    docs = generate_docs(code)
    return jsonify(docs)

@app.route("/answer_question", methods=["POST"])
def answer_question_route():
    code = request.json.get("code")
    question = request.json.get("question")
    answer = answer_question(code, question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)