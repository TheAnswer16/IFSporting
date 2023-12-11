

const colappses = document.querySelectorAll(".collapse-header");

for (c of colappses) {
    c.addEventListener("click", toggleInfo) 
}

function toggleInfo(){
    const id = this.getAttribute("id");

    document.querySelector(`#collapse-body-${id}`).classList.toggle("hidden")
}
