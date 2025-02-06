html_content = """
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .container {
            padding: 20px;
            border: 2px solid #ccc;
            border-radius: 10px;
            background-color: #ffffff;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        h1 {
            text-align: center;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        input[type="number"], input[type="submit"], select {
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        input[type="submit"] {
            background-color: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Kalkulator</h1>
        <form onsubmit="calculate(event)">
            <input type="number" id="num1" placeholder="Pierwsza liczba" required>
            <input type="number" id="num2" placeholder="Druga liczba (jeśli potrzebna)">
            <select id="operation">
                <option value="add">Dodaj</option>
                <option value="subtract">Odejmij</option>
                <option value="multiply">Pomnóż</option>
                <option value="divide">Podziel</option>
                <option value="power">Potęguj</option>
                <option value="sqrt">Pierwiastek kwadratowy</option>
                <option value="modulo">Reszta z dzielenia</option>
            </select>
            <input type="submit" value="Oblicz">
        </form>
        <h2 id="result"></h2>
    </div>

    <script>
        function calculate(event) {
            event.preventDefault();
            let num1 = parseFloat(document.getElementById('num1').value);
            let num2 = parseFloat(document.getElementById('num2').value);
            let operation = document.getElementById('operation').value;
            let result;

            switch (operation) {
                case 'add':
                    result = num1 + num2;
                    break;
                case 'subtract':
                    result = num1 - num2;
                    break;
                case 'multiply':
                    result = num1 * num2;
                    break;
                case 'divide':
                    result = num2 !== 0 ? num1 / num2 : 'Dzielenie przez zero!';
                    break;
                case 'power':
                    result = Math.pow(num1, num2);
                    break;
                case 'sqrt':
                    result = num1 >= 0 ? Math.sqrt(num1) : 'Nie można pierwiastkować liczby ujemnej!';
                    break;
                case 'modulo':
                    result = num1 % num2;
                    break;
                default:
                    result = 'Nieznana operacja';
            }

            document.getElementById('result').innerText = 'Wynik: ' + result;
        }
    </script>
</body>
</html>
"""

with open("kalkulator.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Strona została zapisana jako 'kalkulator.html'. Otwórz ją w przeglądarce, aby użyć kalkulatora.")
