async function loadAds() {
  let res = await fetch("http://127.0.0.1:5000/ads")
  let data = await res.json()

  let box = document.getElementById("ads")
  box.innerHTML = ""

  data.forEach(ad => {
    box.innerHTML += `
      <div class="card">
        <h3>${ad.title}</h3>
        <p>${ad.description}</p>
      </div>
    `
  })
}

loadAds()
