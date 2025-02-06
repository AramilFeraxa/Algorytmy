import os

html_content = '''
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Funkcje: Palindrom i Szyfrowanie Cezara</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 20px;
        }
        .container {
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
            width: 50%;
            margin: auto;
            padding: 20px;
        }
        input[type="text"] {
            width: 80%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="number"] {
            width: 20%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            margin: 5px;
            border: none;
            border-radius: 4px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #0056b3;
        }
        .content {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        #result {
            margin-top: 20px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Palindrom i Szyfrowanie Cezara</h1>
        <div class="content">
            <input type="text" id="textInput" placeholder="Wprowadź tekst">
            <br />
            <button onclick="checkPalindrome()">Sprawdź czy palindrom</button>
            <br />
            <input type="number" id="keyInput" placeholder="Klucz" min="1" max="25">
        </div>
        <br />
        <button onclick="encryptCaesar()">Zaszyfruj (Cezar)</button>
        <button onclick="decryptCaesar()">Odszyfruj (Cezar)</button>
        <div id="result"></div>
    </div>

    <script>
        function checkPalindrome() {
            const text = document.getElementById('textInput').value;
            if (text === '') {
                document.getElementById('result').innerText = 'Wprowadź tekst';
                return;
            }
            const reversed = text.split('').reverse().join('');
            const result = (text === reversed) ? "To jest palindrom" : "To nie jest palindrom";
            document.getElementById('result').innerText = result;
        }

        function encryptCaesar() {
            const text = document.getElementById('textInput').value.trim();
            const keyInput = document.getElementById('keyInput').value.trim();

            if (text === '') {
                document.getElementById('result').innerText = 'Wprowadź tekst';
                return;
            }

            if (keyInput === '' || isNaN(keyInput) || keyInput < 1 || keyInput > 25) {
                document.getElementById('result').innerText = 'Podaj klucz z zakresu 1-25';
                return;
            }

            const shift = parseInt(keyInput);
            let encrypted = '';

          for (let i = 0; i < text.length; i++) {
                let charCode = text.charCodeAt(i);
               if (charCode >= 65 && charCode <= 90) {
                   encrypted += String.fromCharCode(((charCode - 65 + shift) % 26) + 65);
              } else if (charCode >= 97 && charCode <= 122) {
                 encrypted += String.fromCharCode(((charCode - 97 + shift) % 26) + 97);
             } else {
                    encrypted += text[i];
             }
         }

            document.getElementById('result').innerText = 'Zaszyfrowany tekst: ' + encrypted;
        }

        function decryptCaesar() {
         const text = document.getElementById('textInput').value.trim();
         const keyInput = document.getElementById('keyInput').value.trim();

          if (text === '') {
             document.getElementById('result').innerText = 'Wprowadź tekst';
              return;
         }

         if (keyInput === '' || isNaN(keyInput) || keyInput < 1 || keyInput > 25) {
                document.getElementById('result').innerText = 'Podaj klucz z zakresu 1-25';
               return;
          }

         const shift = parseInt(keyInput);
         let decrypted = '';

            for (let i = 0; i < text.length; i++) {
               let charCode = text.charCodeAt(i);
             if (charCode >= 65 && charCode <= 90) {
                  decrypted += String.fromCharCode(((charCode - 65 - shift + 26) % 26) + 65);
             } else if (charCode >= 97 && charCode <= 122) {
                 decrypted += String.fromCharCode(((charCode - 97 - shift + 26) % 26) + 97);
             } else {
                 decrypted += text[i];
               }
         }

         document.getElementById('result').innerText = 'Odszyfrowany tekst: ' + decrypted;
        }
    </script>
</body>
</html>
'''

with open("generated_page.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Plik 'generated_page.html' został wygenerowany.")