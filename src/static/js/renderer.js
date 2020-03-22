var converter = new showdown.Converter();

[].forEach.call(document.getElementsByClassName('post-text'),
    (e) => e.innerHTML = converter.makeHtml(e.innerHTML.trim()));
