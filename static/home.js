document.querySelectorAll('.post-toggle-reply').forEach(function (button) {
    button.addEventListener('click', function () {
        // Find the nearest sibling '.replies' div relative to the clicked button
        var repliesDiv = button.nextElementSibling;
        repliesDiv.classList.toggle('hidden');
    });
});

