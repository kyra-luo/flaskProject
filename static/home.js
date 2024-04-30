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

document.addEventListener('DOMContentLoaded', function () {
    const textareas = document.querySelectorAll('.auto-expand');

    textareas.forEach(textarea => {
        textarea.addEventListener('input', function () {
            // Find the nearest sibling '.charCount' div to update
            let charCountDiv = this.parentNode.querySelector('.charCount');
            let maxLength = this.getAttribute('maxlength');
            let currentLength = this.value.length;
            charCountDiv.textContent = `${currentLength} / ${maxLength}`;
        });

        // Initialize the count on page load for pre-filled textareas
        let initialLength = textarea.value.length;
        let maxLength = textarea.getAttribute('maxlength');
        let charCountDiv = textarea.parentNode.querySelector('.charCount');
        charCountDiv.textContent = `${initialLength} / ${maxLength}`;
    });
});

