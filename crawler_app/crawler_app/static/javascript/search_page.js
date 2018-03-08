
const BFS_LIMIT = 3;
const DFS_LIMIT = 20;
const DEPTH_STR = "Depth Level (From 1 to {num})";

$(".btn-submit").click(function(event) {
  if (this.form.checkValidity()) {
    $("input, select, .btn").css("pointer-events", "none");
    $("html").css("cursor", "wait");
  }
  return true;
});

$("#bfs-btn").click(function(event) {
  $("#depth-input").prop("placeholder", DEPTH_STR.replace("{num}", BFS_LIMIT))
      .prop("max", BFS_LIMIT);
})

$("#dfs-btn").click(function(event) {
  $("#depth-input").prop("placeholder", DEPTH_STR.replace("{num}", DFS_LIMIT))
      .prop("max", DFS_LIMIT);
})
