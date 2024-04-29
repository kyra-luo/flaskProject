document.querySelectorAll('.post-toggle-reply').forEach(function (button) {
    button.addEventListener('click', function () {
        // Find the nearest sibling '.replies' div relative to the clicked button
        var repliesDiv = button.nextElementSibling;
        repliesDiv.classList.toggle('hidden');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const textareas = document.querySelectorAll('.auto-expand');

    // Function to adjust the height of a textarea
    function adjustHeight(textarea) {
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 'px';
    }

    // Attach the input event listener to each textarea
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function () {
            adjustHeight(this);
        });

        // Immediately adjust all textareas on page load
        adjustHeight(textarea);
    });

    // Attach resize event listener to the window
    window.addEventListener('resize', function () {
        textareas.forEach(textarea => {
            adjustHeight(textarea);
        });
    });
});


