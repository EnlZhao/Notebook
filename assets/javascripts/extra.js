const updateScheme = e => {
    var giscus = document.querySelector(".giscus-frame");
    var a = localStorage.getItem('data-md-color-scheme');
    var theme = a === "default" ? "light" : "dark";
    giscus.contentWindow.postMessage(
        { giscus: { setConfig: { theme } } },
        "https://giscus.app"
    )
}

window.addEventListener('load', updateScheme, false);

const updateBoxFontColor = e => {
    var a = localStorage.getItem('data-md-color-scheme');
    if (a !== "default") {
        var elements = document.getElementsByClassName('box');
        for (var i in elements) {
            elements[i].style.color = "white";
        }
    }
}

(() => {
    var p = localStorage.getItem("data-md-color-primary");
    if (p) {
        document.body.setAttribute('data-md-color-primary', p);
    }
    var a = localStorage.getItem('data-md-color-scheme');
    if (a == null) {
        a = "slate";
        localStorage.setItem("data-md-color-scheme", a);
    }
    document.body.setAttribute('data-md-color-scheme', a);
    updateBoxFontColor();
})()