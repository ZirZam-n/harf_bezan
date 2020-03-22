var converter = new showdown.Converter();

[].forEach.call(document.getElementsByClassName('post-text'),
    (e) => e.innerHTML = converter.makeHtml(e.innerHTML.trim()));

editor = document.getElementById('editor');
preview_box = document.getElementById('preview');

function show_preview() {
    preview_box.innerHTML = converter.makeHtml(editor.value.trim());
}

if (editor && preview_box)
    editor.addEventListener('keyup', show_preview);

$(document).ready( function() {
    $("input[type='text'], textarea").attr('spellcheck',false);
});
