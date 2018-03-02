
$(".btn-submit").click(function(event) {
  if (this.parentElement.checkValidity()) {
    $("input, select, .btn").css("pointer-events", "none");
    $("html").css("cursor", "wait");
  }
  return true;
});
