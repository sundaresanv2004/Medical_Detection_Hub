const formOpenBtn = document.querySelector(".form-open"),
    home = document.querySelector(".home"),
    fileInput = document.getElementById('file-input');

formOpenBtn.addEventListener("click", () => {
    if (fileInput.files.length > 0) {
        home.classList.add("show");
    }
});

// formOpenBtn.addEventListener("click", () => home.classList.add("show"));
// formCloseBtn.addEventListener("click", () => home.classList.remove("show"));