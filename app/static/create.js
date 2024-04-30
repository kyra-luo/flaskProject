
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
