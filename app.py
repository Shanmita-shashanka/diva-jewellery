from flask import Flask, render_template, request
app = Flask(__name__)
products = [
    {
        "name": "Silver Deer Heart Necklace",
        "price": 2999,
        "image": "https://www.giva.co/cdn/shop/files/PD096_1.jpg?v=1712924838&width=713"
    },
    {
        "name": "Silver Hearts Whisper Bracelet",
        "price": 3499,
        "image": "https://www.giva.co/cdn/shop/files/BR01423_1_bfc33158-4136-4815-990b-a7497c4d2bc9.jpg?v=1768544341&width=713"
    },
    {
        "name": "Silver Zircon Beachy Waves Ring",
        "price": 1999,
        "image": "https://www.giva.co/cdn/shop/files/R0636_1_1.jpg?v=1715151725&width=713"
    },
    {
        "name": "Silver Leaf Centrepiece Bracelet",
        "price": 3599,
        "image": "https://www.giva.co/cdn/shop/products/BR0482_1.jpg?v=1743510112&width=713"
    },
    {
        "name": "Silver Minimal Heart Bracelet",
        "price": 3999,
        "image": "https://www.giva.co/cdn/shop/products/BR0479_1-min.jpg?v=1671715686&width=713"
    },
    {
        "name": "Oxidised Silver Moon Heart Pendant with Link Chain",
        "price": 3499,
        "image": "https://www.giva.co/cdn/shop/products/PD01296_1.jpg?v=1662644120&width=713"
    },
    {
        "name": "Silver Zircon Layered Ring",
        "price": 2499,
        "image": "https://www.giva.co/cdn/shop/files/R054_1_b37f3b0b-0f56-42c8-954a-98ee4a1ab53b.jpg?v=1715601912&width=713"
    },
    {
        "name": "Silver Flowery Snowflake Studs",
        "price": 1999,
        "image": "https://www.giva.co/cdn/shop/files/ER0582_1_7e551a23-43aa-4b92-bea8-16cad78154f9.jpg?v=1712925439&width=713"
    },
    {
        "name": "Silver Zircon Twinkling Hoop Earrings",
        "price": 1799,
        "image": "https://www.giva.co/cdn/shop/files/ER0289_1_a956bac2-9843-4d2b-9252-a1c8974bb03e.jpg?v=1730788360&width=713"
    },
    {
        "name": "Silver Falling Dew Pendant With Link Chain",
        "price": 3299,
        "image": "https://www.giva.co/cdn/shop/files/PD0133_1_eb3247c2-5b1b-4de4-adb5-67fbcedaa87e.jpg?v=1747894019&width=713"
    },
    {
        "name": "Silver Graceful Waves Bracelet",
        "price": 4099,
        "image": "https://www.giva.co/cdn/shop/files/BR0699_1.jpg?v=1696593415&width=713"
    },
    {
        "name": "Silver Zircon Ferns Bracelet",
        "price": 1999,
        "image": "https://www.giva.co/cdn/shop/files/BR0694_1.jpg?v=1737613391&width=713"
    }

]
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template("shop.html", products=products)


app.run(debug=True)

@app.route("/cart/<int:id>")
def cart(id):
    selected_product = products[id]
    return render_template("cart.html", products=[selected_product])

@app.route("/checkout/<int:id>", methods=["GET", "POST"])
def checkout(id):
    selected_product = products[id]

    if request.method == "POST":
        name = request.form.get("name")

        return render_template(
            "success.html",
            name=name,
            product=selected_product   # ✅ now it works
        )

    return render_template("checkout.html", product=selected_product)