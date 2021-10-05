
function showPage(page) {

    // Hide all of the divs:

    document.querySelectorAll('form').forEach(form => {
        form.style.display = 'none';
    });

    // Show the div provided in the argument:
    document.querySelector(`#${page}`).style.display = 'block';
}


// Wait for page to loaded
document.addEventListener('DOMContentLoaded', function() {
            var alertList = document.querySelectorAll('.alert')
        alertList.forEach(function (alert) {
        new bootstrap.Alert(alert)
        })  
    // Select all buttons
    document.querySelectorAll('a.personal').forEach(a => {

        // When a button is clicked, switch to that page
        a.onclick = function() {
            showPage(this.dataset.page);
        }
    })
})