
$(".btn-submit").click(function(event) {
  $("input, select, .btn").css("pointer-events", "none");
  $("html").css("cursor", "wait");
  return true;
});
