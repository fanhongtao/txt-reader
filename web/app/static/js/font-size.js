$(document).ready(function() {
  $("#inc_font_size").click(function() {
    set_font_size(fontSize + 2)
  });

  $("#dec_font_size").click(function() {
    set_font_size(fontSize - 2)
  });

  $("#reset_font_size").click(function() {
    set_font_size(16)
  });

  set_font_size(fontSize);
})

const value = sessionStorage.getItem("fontSize");
let fontSize = value !== null ? parseInt(value, 10) : 16;

function set_font_size(newSize) {
  fontSize = newSize;
  textElement = document.getElementById('content');
  textElement.style.fontSize = fontSize + 'px';
  sessionStorage.setItem('fontSize', fontSize);
}
