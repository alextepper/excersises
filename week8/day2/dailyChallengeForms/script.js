document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById('userForm');
    const output = document.getElementById('output');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const lastName = document.getElementById('lastName').value;

        const user = {
            name: name,
            lastName: lastName
        };

        output.textContent = JSON.stringify(user, null, 2);
    });
});
