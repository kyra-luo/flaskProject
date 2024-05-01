
document.addEventListener('DOMContentLoaded', function () {
    const textarea = document.getElementById('topic');
    const countDiv = document.getElementById('topic-count');
    const maxLength = textarea.getAttribute('maxlength'); // Define the max length based on your validation rules

    // Initial update in case there's pre-filled content
    updateCharacterCount(textarea, countDiv);

    // Event listener for input
    textarea.addEventListener('input', function () {
        updateCharacterCount(textarea, countDiv);
    });

    function updateCharacterCount(textarea, countDiv) {
        const currentLength = textarea.value.length;
        countDiv.textContent = `${currentLength}/${maxLength}`;
    }
});


document.addEventListener('DOMContentLoaded', function () {
    const textareas = document.querySelectorAll('.create-text');

    // Function to adjust textarea height
    function adjustTextareaHeight(textarea) {
        textarea.style.height = 'auto';  // Reset the height
        textarea.style.height = textarea.scrollHeight + 'px';  // Set the height to scroll height
    }

    // Apply initial height adjustments and add event listeners
    textareas.forEach(textarea => {
        adjustTextareaHeight(textarea);  // Adjust initially
        textarea.addEventListener('input', () => adjustTextareaHeight(textarea));
    });

    // Adjust height on window resize
    window.addEventListener('resize', () => {
        textareas.forEach(adjustTextareaHeight);
    });
});

