$(document).ready(function() {
  $(document).keydown(function (event) {
    switch (event.keyCode) {
    case 37:
      document.getElementById("pre-page").click();
      return false;
    case 39:
      document.getElementById("next-page").click();
      return false;
    };
    return true;
  });

  $("#page-up").click(function() {
    window.scrollBy(0, -(window.innerHeight - 30))
  });

  $("#page-down").click(function() {
    window.scrollBy(0, window.innerHeight - 30)
  });
})

