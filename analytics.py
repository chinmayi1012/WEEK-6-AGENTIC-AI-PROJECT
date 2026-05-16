def calculate_bmi(weight, height):
    return weight / (height ** 2)


def wellness_score(sleep, water, exercise):
    score = (sleep * 10) + (water * 5) + (exercise * 15)
    return score
@app.get("/about")
def about():
    return {"project": "Agentic AI Backend"}