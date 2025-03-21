<meta charset="UTF-8">
 <title>Trivia Time</title>
 <style>
     body {
         background-color: black;
         text-align: center;
         color: white;
         font-family: Arial, Helvetica, sans-serif;
     }
 </style>
ead>
dy>

 <h1>TRIVIA TIME</h1>
 <p>What is the meaning of life, the universe, and everything?</p>
 <img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

 <form action="/login" method="POST">
     <p><input type="text" name="nm"></p>
     <p><input type="submit" value="submit"></p>
 </form>

ody>
tml>'''

p.route("/correct")
 success():
 return f"That is correct!"

p.route("/")
 start():
 return html

p.route("/login", methods=["POST"])
 login():
     if request.form.get("nm"):
         answer = request.form.get("nm")
         if answer == "42":
