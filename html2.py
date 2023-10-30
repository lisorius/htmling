<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div>
        <p>ДЗ: написать функцию, которая принимает массив элементов, проходиться по каждому циклом и ставит каждому элементу случайный цвет текста</p>
    </div>
    <script>
    let arr = ["Яблоко", "Груша", "Апельсин", "Киви", "Мандарин"];

function randomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function displayArrayElements(arr) {
    for (let i = 0; i < arr.length; i++) {
        let color = randomColor();
        let element = arr[i];
        console.log(`<p style="color: ${color};">${element}</p>`);
    }
}

displayArrayElements(arr);
    </script>
</body>
</html>
