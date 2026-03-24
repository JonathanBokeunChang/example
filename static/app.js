const button = document.getElementById("buttonid")
const count = document.getElementById("cookiecountid")

async function loadScore() {
    const response = await fetch("/score")
    const scoreText = await response.text()
    count.textContent = scoreText
}

async function clickCookie() {
    const response = await fetch("/click", { method: "POST" })
    const scoreText = await response.text()
    count.textContent = scoreText
}

button.addEventListener("click", clickCookie)

loadScore()
