from Flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# 데이터 예제
data = {
    "apple": {"GI": 36, "Calories": 52},
    "banana": {"GI": 51, "Calories": 89},
    "rice": {"GI": 73, "Calories": 130},
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    # 디버깅용: 요청 메서드 출력
    print(f"Received request: {request.method}")
    
    try:
        query = request.get_json().get("search")  # JSON 데이터에서 검색어 가져오기
        print(f"Search query received: {query}")  # 디버깅용: 검색어 출력
        result = data.get(query.lower())  # 소문자로 변환하여 데이터 검색
        if result:
            return jsonify({"success": True, "food": query.capitalize(), "info": result})
        else:
            return jsonify({"success": False, "food": query.capitalize()})
    except Exception as e:
        # 디버깅용: 에러 메시지 출력
        print(f"Error occurred: {e}")
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
