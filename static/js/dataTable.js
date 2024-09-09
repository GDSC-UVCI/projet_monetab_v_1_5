$(document).ready(function() {
    $('#table').DataTable({
            pagelength: 5,
            lengthMenu: [[3,5, 10, 25, 50, 100, -1], [3,5, 10, 25, 50, 100, "All"]],
    })
});