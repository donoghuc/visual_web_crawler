
$(".btn-submit").click(function(event) {
  if (this.form.checkValidity()) {
    $("input, select, .btn").css("pointer-events", "none");
    $("html").css("cursor", "wait");
  }
  return true;
});
