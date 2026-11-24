from flask import Flask, render_template, request, abort

app = Flask(__name__)


def calcular_promedio(n1, n2, n3):
    return round((n1 + n2 + n3) / 3, 1)


def estado_aprobacion(promedio, asistencia):
    if promedio >= 40 and asistencia >= 75:
        return "APROBADO"
    return "REPROBADO"


def nombre_mas_largo(nombres):
    return max(nombres, key=len)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    promedio = None
    estado = None

    if request.method == "POST":
        try:
            n1 = float(request.form["nota1"])
            n2 = float(request.form["nota2"])
            n3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])
        except (KeyError, ValueError):
            abort(400, "Debes ingresar valores numéricos en todos los campos.")

        for nota in (n1, n2, n3):
            if not 10 <= nota <= 70:
                abort(400, "Las notas deben estar entre 10 y 70.")
        if not 0 <= asistencia <= 100:
            abort(400, "La asistencia debe estar entre 0 y 100.")

        promedio = calcular_promedio(n1, n2, n3)
        estado = estado_aprobacion(promedio, asistencia)

    return render_template("ejercicio1.html", promedio=promedio, estado=estado)


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mayor = None
    cantidad = None

    if request.method == "POST":
        nombres = [
            request.form.get("nombre1", "").strip(),
            request.form.get("nombre2", "").strip(),
            request.form.get("nombre3", "").strip(),
        ]

        if "" in nombres:
            abort(400, "Debes ingresar los tres nombres.")
        if len({n.lower() for n in nombres}) < 3:
            abort(400, "Los tres nombres deben ser diferentes.")

        mayor = nombre_mas_largo(nombres)
        cantidad = len(mayor)

    return render_template("ejercicio2.html", mayor=mayor, cantidad=cantidad)


@app.errorhandler(400)
def error_400(e):
    return render_template("error.html", mensaje=e.description), 400


if __name__ == "__main__":
    app.run(debug=True)