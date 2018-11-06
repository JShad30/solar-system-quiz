$(document).ready(function() {
    $("#begin-quiz").on("click", function() {
        $("#quiz-intro").addClass("not-active");
		$("#question-1").addClass("active");
	});
	$("#question-1").on("click", function() {
        $("#question-1").addClass("not-active");
		$("#question-1").addClass("active");
	});
});